
from helpers import query
from definitions import PROMPT


API_URL_SUFFIX = "prompthero/openjourney-v4"


def main():

    output = query(
        {"inputs": PROMPT},
        API_URL_SUFFIX
    )

    if output:
        with open("output/oj.jpeg", "wb") as f:
            f.write(output.content)
