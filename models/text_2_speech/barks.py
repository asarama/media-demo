
from helpers import query
from definitions import PROMPT


API_URL_SUFFIX = "suno/bark"


def main():

    output = query(
        {"inputs": PROMPT},
        API_URL_SUFFIX
    )
    with open("output/barks.flac", "wb") as f:
        f.write(output.content)
