
from helpers import query
from definitions import PROMPT

# Backup: https://huggingface.co/spaces/Zhenhong/text-to-speech-SpeechT5-demo

API_URL_SUFFIX = "microsoft/speecht5_tts"


def main():

    output = query(
        {"inputs": PROMPT},
        API_URL_SUFFIX
    )

    if output:
        with open("output/microsoft.flac", "wb") as f:
            f.write(output.content)
