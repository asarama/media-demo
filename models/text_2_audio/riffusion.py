
from helpers import query
from definitions import PROMPT


API_URL_SUFFIX = "riffusion/riffusion-model-v1"


def main():

    output = query(
        {"inputs": PROMPT},
        API_URL_SUFFIX
    )
    with open("output/facebook.flac", "wb") as f:
        f.write(output.content)
