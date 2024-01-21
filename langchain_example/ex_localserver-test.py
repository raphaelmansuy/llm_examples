import os 
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI


os.environ["LANGCHAIN_API_KEY"] = "ls__32c9fe60089743128b34df6c064cf7ba"
os.environ["LANGCHAIN_TRACING_V2"] = "true"

prompt = ChatPromptTemplate.from_template("""
    Pourquoi les oeufs des locomotives à vapeur sont plus gros que ceux des locomotives électriques.
""")

model = ChatOpenAI(openai_api_base="http://localhost:1234/v1")
output_parser = StrOutputParser()

chain = prompt | model | output_parser



for chunk in chain.stream({}):
    print(chunk, end="", flush=True)

