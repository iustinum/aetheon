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
    print(chat_model)

    prompt_template_string = """
    Your task is to write accurate docstrings for python functions. You will be provided with python code delimited by triple quotes. Generate docstrings for each function that you find in the python code. Each docstring should consist of the following information:

    description: What is the function's use case?

    arguments: What arguments does the function have? And for each argument, what is its use case?

    return_value: What is the significance of the return value of the function? If the return value is None, simply write \"None\", else write the significance.

    side_effects: What are some side effects caused by calling the function? In Python, a side effect is any change that a function makes to its state or the global program state, besides its return value.

    python code: \"\"\"{input_code}\"\"\"

    {format_instructions}
    """
    print(prompt_template_string)
