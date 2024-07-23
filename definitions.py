import os

from dotenv import load_dotenv

# Check if .env file is present
if not os.path.isfile(".env"):
    raise Exception("App setup error: Missing .env file.")

# Load variables from .env file
load_dotenv()


try:
    HF_API_TOKEN = os.environ["HF_API_TOKEN"]
    MODEL_SET = os.environ["MODEL_SET"]
    PROMPT = os.environ["PROMPT"]

except KeyError as err:
    raise Exception(f"Missing ENV variable. {err}")
