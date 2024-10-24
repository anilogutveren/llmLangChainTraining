from dotenv import load_dotenv, dotenv_values

load_dotenv()

if __name__ == '__main__':
    print("hello world")
    print(dotenv_values(".env").get("OPENAI_API_KEY"))
