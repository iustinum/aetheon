import openai

openai.api_key = "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"

if __name__ == "__main__":
    print("INFO: [*] GENERATING MESSAGE...")
    res = openai.ChatCompletion.create(
    model = "gpt-4",
    messages = [{"role":"user", "content":"tell me more about the ja morant gun controversy."}]
    )
    print(res)




