import os
from dotenv import load_dotenv

def env_using_os():
    # Set an environment variable programmatically
    os.environ['MY_ENV_VAR'] = 'Hello from os.environ'
    # Access the environment variable using os.environ
    value = os.environ.get('MY_ENV_VAR')
    print(f"Value from os.environ: {value}")
    # Delete the environment variable
    del os.environ['MY_ENV_VAR']
    print("Environment variable deleted.")

def env_using_dotenv():
    # Load environment variables from a .env file
    load_dotenv()
    # We can also load environment variables from a specific file
    # dotenv.load_dotenv(dotenv_path='path/to/your/.env')

    # Access the environment variable using os.environ after loading .env
    name = os.environ.get('NAME')
    city = os.environ.get('CITY')
    print(f"Name from dotenv: {name}")
    print(f"City from dotenv: {city}")

if __name__ == "__main__":
    # env_using_os()
    env_using_dotenv()