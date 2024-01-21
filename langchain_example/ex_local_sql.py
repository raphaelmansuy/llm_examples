from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_community.utilities import SQLDatabase
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough


template = """Based on the table schema below, write a SQL query that would answer the user's question:
{schema}

Question: {question}
SQL Query:"""
prompt = ChatPromptTemplate.from_template(template)


## Open sql lite database 


db = SQLDatabase.from_uri("sqlite:///./Chinook.db")

table_info = db.get_table_info()

#print(table_info)



def get_schema(_):
    return db.get_table_info()

def run_query(query):
    return db.run(query)




model = ChatOpenAI(model="gpt-3.5-turbo")

sql_response = (
    RunnablePassthrough.assign(schema=get_schema)
    | prompt
    | model.bind(stop=["\nSQLResult:"])
    | StrOutputParser()
)



template = """Based on the table schema below, question, sql query, and sql response, write a natural language response:
{schema}

Question: {question}
SQL Query: {query}
SQL Response: {response}"""
prompt_response = ChatPromptTemplate.from_template(template)


full_chain = (
  RunnablePassthrough.assign(query=sql_response).assign(
    schema=get_schema,
    response=lambda x: db.run(x["query"]),
  )
  | prompt_response
  | model
  | StrOutputParser()
)

res = full_chain.invoke({"question": "What is the name of the last employed person in the company? What is the birth date of the last employed person in the company?"})

print(res)

res = full_chain.invoke({"question": "Display the names of employees that are older than Laura Callahan display their birth date and the age of each ?"})

print(res)