const AWS = require('aws-sdk');

const ddb = new AWS.DynamoDB.DocumentClient({ apiVersion: '2012-08-10' });

const { TableName } = process.env;

exports.lambda_handler = async (event, context) => {
  // console.log(`Environment Variables:\n` + JSON.stringify(process.env, null, 2));
  // console.log(`WebSocket sendmsg: DynamoDB Table: ${TableName}`);
  console.log(`WebSocket sendmsg: event argument:\n` + JSON.stringify(event,null,2));

  // Retrieve all current connections
  let connectionData;
  try {
    connectionData = await ddb.scan({ TableName: TableName,
                                      ProjectionExpression: 'connectionId' }).promise();
  } catch (e) {
    console.log(e.stack);
    return { statusCode: 500, body: e.stack };
  }

  // Create management object for posting the message to each connection
  const apigwManagementApi = new AWS.ApiGatewayManagementApi({
    apiVersion: '2018-11-29',
    endpoint: event.requestContext.domainName + '/' + event.requestContext.stage
  });

  // Retrieve the message
  const message = JSON.parse(event.body).msg;
  console.log(`WebSocket sendmsg: Received message "${message}"`);

  // Send the message to each connection
  const postCalls = connectionData.Items.map(async ({ connectionId }) => {
    try {
      await apigwManagementApi.postToConnection({ ConnectionId: connectionId, Data: message }).promise();
    } catch (e) {
      if (e.statusCode === 410) {
        console.log(`Found stale connection, deleting ${connectionId}`);
        await ddb.delete({ TableName: TableName, Key: { connectionId } }).promise();
      } else {
        throw e;
      }
    }
  });

  try {
    await Promise.all(postCalls);
  } catch (e) {
    return { statusCode: 500, body: e.stack };
  }

  return { statusCode: 200, body: 'Data sent.' };
};