
from helpers import query
from definitions import PROMPT

# Backup: https://huggingface.co/spaces/mrfakename/MeloTTS

API_URL_SUFFIX = "myshell-ai/MeloTTS-English"


def main():

    output = query(
        {"inputs": PROMPT},
        API_URL_SUFFIX
    )
    with open("output/melo.flac", "wb") as f:
        f.write(output.content)
