
from helpers import query
from definitions import PROMPT


API_URL_SUFFIX = "microsoft/speecht5_tts"


def main():

    output = query(
        {"inputs": PROMPT},
        API_URL_SUFFIX
    )
    with open("output/microsoft.flac", "wb") as f:
        f.write(output.content)
