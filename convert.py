import boto3

codebuild = boto3.client('codebuild')

response = codebuild.create_project(
    name='SimpleBuildProject',
    source={
        'type': 'GITHUB',
        'location': 'https://github.com/your-username/your-repo',
    },
    artifacts={
        'type': 'NO_ARTIFACTS'
    },
    environment={
        'type': 'LINUX_CONTAINER',
        'image': 'aws/codebuild/standard:5.0',
        'computeType': 'BUILD_GENERAL1_SMALL',
    },
    serviceRole='arn:aws:iam::123456789012:role/codebuild-service-role'
)

print("Project Created:", response['project']['name'])
