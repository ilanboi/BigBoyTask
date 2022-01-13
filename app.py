#!/usr/bin/env python3

#from aws_cdk import core

from static_web.static_web import StaticExampleStack

#app = core.App()
app = App()
StaticExampleStack(app, "static-web")

app.synth()
