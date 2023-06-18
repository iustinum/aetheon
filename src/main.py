import argparse
import sys
from dotenv import load_dotenv
import os

import openai
# import nest_asyncio

import utils
from repo_reader import generateFileNames, generateQuery 


def generateParser() -> argparse.ArgumentParser:

    """
    A function that creates a parser for our script.
    """

    # Creates the parser, also gives the parser a description
    parser = argparse.ArgumentParser(description="A utility for generating wiki pages for a code base.")

    # Adds arguments to the parser, may add more in the future.
    parser.add_argument("-l", "--link", help="A github repo link to analyze", required=True)
    parser.add_argument("-b", "--branch", help="The branch of the repo that you want to analyze. Default is set to 'main'.", required=False, default="main")

    return parser

def setup():
    # keys
    load_dotenv(".env")
    openai.api_key=os.environ["OPENAI_API_KEY"]

    # async stuff ??
    nest_asyncio.apply()

    storeFileName = "data.pkl"


if __name__ == "__main__":
    parser = generateParser()
    inputs = vars(parser.parse_args())

    link = inputs["link"]
    branch = inputs["branch"]


    # Prompt link
    

    # Parse link
    print(f"Using the repository ${link}")
    author, repo_name = utils.get_repo_info(link)
    if (not author) or (not repo_name):
        sys.exit("Please provide a valid repository!")
    print(f"Author: \t{author}\nRepo Name: \t{repo_name}")

    # generateDataFile(author, repo_name, branch="master")
    # query = generateQuery("Tell me what is inside the Permutation.java file, including a description for what every function is doing.")
    # print(query)
    # os.remove(storeFileName)


