from aws_cdk import (
    aws_s3 as s3,
    aws_cloudfront as cloudfront
)
from constructs import Construct

class StaticSite(Construct):
    def __init__(self):
    
        self.bucket = s3.Bucket(self, "MyBucket",
                           access_control=s3.BucketAccessControl.PUBLIC_READ,
                           website_index_document="index.html"
                           )
        bucket.grant_public_access()
        
        self.distribution = cloudfront.Distribution(
            self,
            "cloudfront_distribution",
            default_behavior=cloudfront.BehaviorOptions(
                origin=origins.S3Origin(self.bucket),
                viewer_protocol_policy=cloudfront.ViewerProtocolPolicy.REDIRECT_TO_HTTPS,
            ),
            default_root_object="index.html",
        )
        app.synth()
        
