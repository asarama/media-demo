
from helpers import query
from definitions import PROMPT

# Backup: https://huggingface.co/spaces/fffiloni/spectrogram-to-music

API_URL_SUFFIX = "riffusion/riffusion-model-v1"


def main():

    output = query(
        {"inputs": PROMPT},
        API_URL_SUFFIX
    )

    if output:
        with open("output/riff.flac", "wb") as f:
            f.write(output.content)
