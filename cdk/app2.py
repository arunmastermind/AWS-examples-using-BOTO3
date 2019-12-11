from aws_cdk import (
    aws_s3 as s3,
    core,
)


class S3Stack(core.Stack):
    def __init__(self, app: core.App, id: str) -> None:
        super().__init__(app, id)

        bucket = s3.Bucket(
            self, "MyBucket",
            versioned=True,
            encryption=aws_s3.BucketEncryption.KMS_MANAGED)

app = core.App()
S3Stack(app, "MyStack")
app.synth()
