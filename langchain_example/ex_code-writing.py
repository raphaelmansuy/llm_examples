import os
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_experimental.utilities import PythonREPL


def _sanitize_output(text: str):
    _, after = text.split("```python")
    return after.split("```")[0]


os.environ["LANGCHAIN_API_KEY"] = "ls__32c9fe60089743128b34df6c064cf7ba"
os.environ["LANGCHAIN_TRACING_V2"] = "true"

template = """Write some python code to solve the user's problem. 

Return only python code in Markdown format, e.g.:

```python
....
```"""
prompt = ChatPromptTemplate.from_messages(
    [("system", template), ("human", "{input}")])


model = ChatOpenAI(openai_api_base="http://localhost:1234/v1")
output_parser = StrOutputParser()

chain = prompt | model | StrOutputParser() | _sanitize_output | PythonREPL().run

res = chain.invoke(
    {"input": "Calculate the surface of a cone with a radius of 3 and a height of 5.8"})

print(res)
