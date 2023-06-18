import argparse
import sys
from dotenv import load_dotenv
import os

import openai
import nest_asyncio

import utils
from repo_reader import generateFileNames, generateQuery 

# CLI Interface
def generateParser() -> argparse.ArgumentParser:

    """
    A function that creates a parser for our script.
    """

    # Creates the parser, also gives the parser a description
    parser = argparse.ArgumentParser(description="A utility for generating wiki pages for a code base.")

    # Adds arguments to the parser, may add more in the future.
    parser.add_argument("-l", "--link", help="A github repo link to analyze", required=False)
    parser.add_argument("-b", "--branch", help="The branch of the repo that you want to analyze. Default is set to 'main'.", required=False, default="main")
    parser.add_argument("-v", "--verbose", help="Verbose, 1 to display all messages", required=False)

    return parser

def run_gitlance(author, repo_name, branch, save_dest):
    print("Beginning wiki creation.")

    # TODO: Use link and Branch to run the neccessary code

    # generateDataFile(author, repo_name, branch="master")
    # query = generateQuery("Tell me what is inside the Permutation.java file, including a description for what every function is doing.")
    # print(query)
    # os.remove(storeFileName)
    
    return

if __name__ == "__main__":
    parser = generateParser()
    inputs = vars(parser.parse_args())

    # link = inputs["link"]
    # branch = inputs["branch"]


    # Prompt to get link, author, and repo_name

    author = None
    while not author:
        link = input("Please provide a github repository link: ")
        author, repo_name = utils.get_repo_info(link)
        if (not author) or (not repo_name):
            print("Please provide a valid repository!")


    # Prompt to get branch name
    branch = input("Please provide the name of the branch you want to analyze (default: main): ")

    if not branch:
        branch = "main"


    # Prompt to get directory of save destination
    save_dest = None

    while not save_dest:
        save_dest = input("Please provide the folder where you would like the wiki output to be saved: ")
        if not save_dest:
            print("Please provide a file destination!")


    print(f"Using the repository {link} on the branch '{branch}'")
    print(f"Author: \t{author}\nRepo Name: \t{repo_name}")
    print(f"Save Dest: \t{save_dest}")

    cont = input("Is this correct? (Y/n)")

    if cont == None or cont == "Y" or cont == "y":
        run_gitlance(author, repo_name, branch, save_dest)
        sys.exit("Finished wiki creation.")
    else:
        sys.exit("Canceling run ..")


