
from helpers import query
from definitions import PROMPT

# Backup: https://huggingface.co/spaces/declare-lab/mustango

API_URL_SUFFIX = "declare-lab/mustango"


def main():

    output = query(
        {"inputs": PROMPT},
        API_URL_SUFFIX
    )

    if output:
        with open("output/mustango.flac", "wb") as f:
            f.write(output.content)
