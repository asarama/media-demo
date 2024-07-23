
from helpers import query
from definitions import PROMPT
# facebook/musicgen-small


API_URL_SUFFIX = "facebook/musicgen-small"


def main():

    output = query(
        {"inputs": PROMPT},
        API_URL_SUFFIX
    )
    with open("output/facebook.flac", "wb") as f:
        f.write(output.content)
