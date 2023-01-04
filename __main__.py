"""A Python Pulumi program"""

import pulumi
from pulumi_docker import *

jenkins_image = Image(
    name="jenkins",
    image_name="jenkins",
    build=DockerBuild(context="./jenkins"),
    skip_push=True,
)
