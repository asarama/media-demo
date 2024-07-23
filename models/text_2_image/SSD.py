
from helpers import query
from definitions import PROMPT


API_URL_SUFFIX = "segmind/SSD-1B"


def main():

    output = query(
        {"inputs": PROMPT},
        API_URL_SUFFIX
    )

    if output:
        with open("output/ssd.jpeg", "wb") as f:
            f.write(output.content)
