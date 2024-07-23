
from helpers import query
from definitions import PROMPT


API_URL_SUFFIX = "stabilityai/stable-diffusion-2-1"


def main():

    output = query(
        {"inputs": PROMPT},
        API_URL_SUFFIX
    )

    if output:
        with open("output/sd.jpeg", "wb") as f:
            f.write(output.content)
