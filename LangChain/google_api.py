import os
from langchain_google_genai import ChatGoogleGenerativeAI

google_api_key = os.getenv("GOOGLE_API_KEY")
if not google_api_key:
    raise SystemExit("GOOGLE_API_KEY is not set. Set it in this terminal, then rerun.")

llm = ChatGoogleGenerativeAI(
    model="gemini-3.8-flash",
    google_api_key=google_api_key
)

response = llm.invoke("Explain Snowflake architecture in simple terms.")

print(response.content)
