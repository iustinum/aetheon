import openai
import utils
import repo_reader

utils.setup()



class GPT():

    systemContent = "Your are an assistant analyzing a codebase."
    query = "Produce a wikipedia style page for this codebase in markdown syntax, empahsizing functions with headers"
    contextPrefix = "Here is the context for the codebase I want you to analyze:" 

    def __init__(self, model): 
        self.model = model
        self.context = ""

    def giveContext(self, text : str) -> None:

        """
        Gives GPT the context necessary before our query.
        """

        self.context = text

    def createMDText(self, query : str = query) -> str:

        """
        Generates a string, in markdown syntax, from the context (codebase).
        """
        messages = [
                    {"role" : "user", "content": f"{GPT.contextPrefix} {self.context}. {query}"}]
        res = openai.ChatCompletion.create(model=self.model, messages=messages)

        return res["choices"][0]["message"]["content"]
    


if __name__ == "__main__":
    GPTObject = GPT(model="gpt-4")
    author, repo_name = utils.get_repo_info("https://github.com/Jingzhi-Su/PokerBot") #"https://github.com/chiyeon/tmf-beat")
    print(author, repo_name)
    repo_reader.generateDataFile(author, repo_name, branch="main")
    allNames = repo_reader.generateFileNames()
    desc = repo_reader.generateDescriptions(allNames)
    GPTObject.giveContext(desc)
    print(GPTObject.createMDText(GPT.query))
