import openai
from dotenv import load_dotenv
import os
import argparse
import nest_asyncio

load_dotenv(".env")
openai.api_key=os.environ["OPENAI_API_KEY"]


def generateParser() -> argparse.ArgumentParser:

    """
    A function that creates a parser for our script.
    """

    # Creates the parser, also gives the parser a description
    parser = argparse.ArgumentParser(description="A utility for generating wiki pages for a code base.")

    # Adds arguments to the parser, may add more in the future.
    parser.add_argument("-l", "--link", help="A github repo link to analyze", required=True)

    return parser

if __name__ == "__main__":
    parser = generateParser()
    inputs = vars(parser.parse_args())
    link = inputs["link"]
    print("INFO: [*] Here is the link")
    print(link)
