from dotenv import load_dotenv

from langchain.chat_models import ChatOpenAI


# TEST CONFIG:
GH_LINK = "https://github.com/Jingzhi-Su/PokerBot"
AUTHOR = "Jingzhi-Su"
REPO_NAME = "PokerBot"
BRANCH = "main"

if __name__ == "__main__":
    load_dotenv(".env")

    chat_model = ChatOpenAI(temperature=0.0)
