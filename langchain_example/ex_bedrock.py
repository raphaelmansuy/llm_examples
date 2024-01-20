import os
import boto3

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Bedrock


os.environ["AWS_PROFILE"] = "bedrock"

client = boto3.client("bedrock-runtime",region_name="us-west-2")

model = Bedrock(client=client, model_id="anthropic.claude-v2:1")

prompt = ChatPromptTemplate.from_template("tell me a joke about {foo}")
chain = prompt | model | StrOutputParser()

res = chain.invoke({"foo": "bears"})

print(res)

