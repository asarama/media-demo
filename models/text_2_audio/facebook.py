
from helpers import query
from definitions import PROMPT


API_URL_SUFFIX = "facebook/musicgen-small"


def main():

    output = query(
        {"inputs": PROMPT},
        API_URL_SUFFIX
    )

    if output:
        with open("output/facebook.flac", "wb") as f:
            f.write(output.content)
