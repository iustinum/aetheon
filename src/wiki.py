import openai 
import os

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

    os.remove("test.md")
    test = "## Hello World"
    generateMarkDown(test, "test.md")