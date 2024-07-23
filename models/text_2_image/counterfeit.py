
from helpers import query
from definitions import PROMPT


API_URL_SUFFIX = "gsdf/Counterfeit-V2.5"


def main():

    output = query(
        {"inputs": PROMPT},
        API_URL_SUFFIX
    )

    if output:
        with open("output/counter.jpeg", "wb") as f:
            f.write(output.content)
