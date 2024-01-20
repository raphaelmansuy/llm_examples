from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

prompt = ChatPromptTemplate.from_template("tell me a short joke about {topic}, more than 400 words")
model = ChatOpenAI(openai_api_base="http://localhost:1234/v1")
output_parser = StrOutputParser()

chain = prompt | model | output_parser

res = chain.invoke({"topic": "ice cream"})

print(res)