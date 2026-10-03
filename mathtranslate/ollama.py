from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


class Translator:
    def __init__(self):
        # Load model
        self.llm = ChatOllama(model="llama3", temperature=0)
        self.prompt = ChatPromptTemplate.from_messages([
            ("system", "Übersetze den folgenden Text von Deutsch nach Englisch. Antworte nur mit der Übersetzung."),
            ("human", "{text}")
        ])

        self.chain = self.prompt | self.llm | StrOutputParser()

    def is_error_request_frequency(self, e: exception.TencentCloudSDKException):        
            return False

    def translate(self, text, language_to, language_from):        
        return self.chain.invoke({"text": config.math_code })
