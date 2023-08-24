import aetheon

# TEST CONFIG:
GH_LINK = "https://github.com/Jingzhi-Su/PokerBot"
AUTHOR = "Jingzhi-Su"
REPO_NAME = "PokerBot"
BRANCH = "main"

if __name__ == "__main__":
    ae = aetheon.Aetheon(model_name="gpt-3.5-turbo")
    ae.run(repo_name=REPO_NAME, author=AUTHOR, branch=BRANCH)
