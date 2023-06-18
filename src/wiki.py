import os
import repo_reader
import gpt
import utils


def generateNewMD(outputFile : str) -> None:

    """
    A function to generate a new wiki.md file.
    """

    if os.path.exists(outputFile):
        raise Exception("File already exists!")
    
    open(outputFile, "x")


def generateMarkDown(textInMDFormat : str, outputFile : str) -> None:

    """
    A function to generate a markdown file from the given input text. Creates the file in the given output file.
    Note that the input text should be in markdown code format (ie. Titles have # before it, etc.)
    """

    generateNewMD(outputFile)

    with open(outputFile, "w") as f:
        f.write(textInMDFormat)
        f.close()

if __name__ == "__main__":

    utils.setup()

    testFile = "test2.md"
    GPTObject = gpt.GPT(model="gpt-4")
    author, repo_name = utils.get_repo_info("https://github.com/Jingzhi-Su/PokerBot") #"https://github.com/chiyeon/tmf-beat")
    print(author, repo_name)
    repo_reader.generateDataFile(author, repo_name, branch="main")
    print("INFO: [*] Generated file data")
    allNames = repo_reader.generateFileNames()
    desc = repo_reader.generateDescriptions(allNames)
    print("INFO: [*] Generated descriptions")
    GPTObject.giveContext(desc)
    print("INFO: [*] Generating Text")
    text = GPTObject.createMDText(gpt.GPT.query)
    print(text)
    generateMarkDown(text, testFile)
    print("INFO: [*] DONE!")