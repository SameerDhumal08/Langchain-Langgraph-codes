#This code is a LangChain application that takes your personal information, sends it to an OpenAI LLM, and generates a professional summary in 50 words or less.'''
from dotenv import load_dotenv #help to load environment variables from .env file
from langchain_core.prompts import PromptTemplate #help to translate user input to instructions langchain model
from langchain_openai import ChatOpenAI #LLM use ChatOpenAI to generate responses

load_dotenv() #load invironment variables from .env file


def main():
    print("Hello from langchain-course!")
    information = """
    My Name is Sameer I am working as a Software Developer at TCS. About my skills i have done post graduate in advance computing about my skill python , fastapi , langchain , RAG , postgresql"""

    summary_template = """
        Given the information {information} about me,
        write a summary about me in 50 words or less.
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"],
        template=summary_template
    )

    llm = ChatOpenAI(temperature=0, model="gpt-5")
    chain = summary_prompt_template | llm

    response = chain.invoke(input={"information": information})
    print(response.content)

if __name__ == "__main__":
    main()
