import time
from attr.filters import exclude
from aws_cdk import (
    aws_s3 as s3,
    aws_s3_deployment as s3deploy,
    aws_cloudfront as cf,
    core
)

class StaticExampleStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)
        
        bucket = s3.Bucket(self, "ilanbucket12345666",
                           public_read_access=True,
                           website_index_document="index.html"
                           )
        s3deploy.BucketDeployment(self, "DeployWebsite",
                           sources=[s3deploy.Source.asset("./website")],
                           destination_bucket=bucket
                           )

        cloudfront = cf.CloudFrontWebDistribution(self, "ilanCDN12345666",
                                     origin_configs=[
                                         cf.SourceConfiguration(
                                             behaviors=[
                                                 cf.Behavior(
                                                     is_default_behavior=True)
                                             ],
                                             s3_origin_source=cf.S3OriginConfig(
                                                 s3_bucket_source=bucket
                                             )
                                         )
                                     ]
                                     )
        print(cloudfront.distribution_domain_name)
