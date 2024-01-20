import os
import json
import boto3

os.environ["AWS_PROFILE"] = "bedrock"

bedrock_client = boto3.client("bedrock-runtime",region_name="us-west-2")

request_body = {
    "prompt": "Human: Write a haiku poem about nature.\n\nAssistant:",
    "max_tokens_to_sample": 50,
    "stop_sequences": ["\n\nHuman:"],
#    "anthropic_version": "bedrock-2023-05-31"
}

response = bedrock_client.invoke_model(
    modelId="anthropic.claude-v2:1",
    body=json.dumps(request_body)
)

print(json.loads(response["body"].read())["completion"])