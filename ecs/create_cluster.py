import boto3

# Create ECS client
try:
  ecs_client = boto3.client('ecs')
  
  response = ecs_client.create_cluster(
    clusterName='CLUSTER_NAME'
  )
  print(response)

except BaseException as exe:
    print(exe)