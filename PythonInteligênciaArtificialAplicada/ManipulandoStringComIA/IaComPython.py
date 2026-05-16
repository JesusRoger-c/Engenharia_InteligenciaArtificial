#Rodando IA com python

#Realizando os imports
from dotenv import load_dotenv
from google import genai
import os

#Puxando a chave
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY", "Não encontrado...")



client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)



try:
    def perguntar_ia(pergunta):
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=pergunta
        )

        return response.text

except Exception as erro:
    print(f"Erro: {erro}")
