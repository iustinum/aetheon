import os
import utils
import pickle
from dotenv import load_dotenv
import openai
from llama_index import download_loader, GPTVectorStoreIndex, Document
download_loader("GithubRepositoryReader")
from llama_hub.github_repo import GithubClient, GithubRepositoryReader
import nest_asyncio

load_dotenv()
nest_asyncio.apply()

storeFileName = "data.pkl"


def generateDataFile(username : str, repo : str, branch : str = "main") -> None:

    """
    A function to generate a list of document objects from a github repository. 
    Writes the list of Document objects as a .pkl in data.pkl
    """

    github_client = GithubClient(os.getenv("GITHUB_TOKEN"))
    
    print(f"INFO: {utils.getCurrentTime()} [*] Loading Github repository...")
    loader = GithubRepositoryReader(
    github_client,
    owner =                  username,
    repo =                   repo,
    verbose =                False,
    concurrent_requests =    10)

    data = loader.load_data(branch=branch)  

    print(f"INFO: {utils.getCurrentTime()} [*] Storing data...")
    with open(storeFileName, "wb") as f:
        pickle.dump(data, f)
    
def generateQuery(query :str) -> str:

    """
    A function to generate a query response from the given data. 
    
    """
    
    if not os.path.exists("data.pkl"):
        raise Exception("INFO: [*] Data file does not exist!")
    
    print(f"INFO: {utils.getCurrentTime()} [*] Unpacking data...")
    # Unpackage our documents object
    with open(storeFileName, "rb") as f:
        data = pickle.load(f)

    print(f"INFO: {utils.getCurrentTime()} [*] Generating index...")   
    index = GPTVectorStoreIndex.from_documents(data)

    # Turns index into a query engine to feed questions into.
    print(f"INFO: {utils.getCurrentTime()} [*] Generating query engine...")
    query_engine = index.as_query_engine()
    print(f"INFO: {utils.getCurrentTime()} [*] Generating repsonse...")
    response = query_engine.query(query)

    return response

def generateFileNames() -> set:

    """
    A function to generate file locations from our data. Returns a set of file names, starting from the github repo.
    """

    print(f"INFO: {utils.getCurrentTime()} [*] Generating file names...")
    data = getDataPKL()
    locations = set() 
    for document in data:
        locations.add(document.extra_info)
    return locations

def generateResponseFromFile(fileName : str) -> str:

    """
    A function to generate a detailed description for a certain file.
    This is mainly used to produce descripts for the wikipedia page.
    """

    return generateQuery(f"Write me a detailed description of the following file or class: {fileName}. The response should include a detailed list of variables and functions.")

def getDataPKL() -> list[Document]:

    """
    A function that generates a list of Document objects. Serves as data for later parsing.
    """

    # Error checking to see if our data file exists
    if not os.path.exists(storeFileName):
        raise Exception("Data file not generated!")
    
    with open(storeFileName, "rb") as f:
        data = pickle.load(f)
        return data


# (DEBUGGING)
if __name__ == "__main__":
    print(os.getenv("GITHUB_TOKEN"))
    print(os.getenv("OPENAI_API_KEY"))
    openai.api_key=os.environ["OPENAI_API_KEY"]
    #paste url:
    author, repo_name = utils.get_repo_info("https://github.com/ziyicui2022/cs61b-enigma") #"https://github.com/chiyeon/tmf-beat")
    print(author, repo_name)
    generateDataFile(author, repo_name, branch="master")
    print(generateQuery("Tell me what is inside the Permutation.java file, including a description for what every function is doing."))
    os.remove(storeFileName)
