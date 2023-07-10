import openai
import os
from dotenv import load_dotenv

load_dotenv(".env")
openai.api_key = os.environ["OPENAI_API_KEY"]

res = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{
        "role": "user",
        "content": "Which model are you?"
    }]
)


with open("./out.txt", "w+") as f:
    f.write(res)
