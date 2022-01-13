#!/usr/bin/env python3

from aws_cdk import core

from static_web.static_web import StaticExampleStack

app = core.App()
StaticExampleStack(app, "static-web")

app.synth()
=======
from aws_cdk import (
    aws_s3 as s3,
    aws_cloudfront as cloudfront,
    App,
    Stack,
)
import aws_cdk.core as core

app = core.App()

class StaticSite(core.Stack):
    def __init__(self):
    
        self.bucket = s3.Bucket(self, "ilanbucket123456789",
                           access_control=s3.BucketAccessControl.PUBLIC_READ,
                           website_index_document="index.html"
                           )
        bucket.grant_public_access()
        
        self.distribution = cloudfront.Distribution(
            self,
            "ilanfront123456789",
            default_behavior=cloudfront.BehaviorOptions(
                origin=origins.S3Origin(self.bucket),
                viewer_protocol_policy=cloudfront.ViewerProtocolPolicy.REDIRECT_TO_HTTPS,
            ),
            default_root_object="index.html",
        )
app.synth()
        
>>>>>>> 452c880ad62a83b65f43bd847f43e60854f4b9cb
