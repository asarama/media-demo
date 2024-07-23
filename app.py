import requests
from transformers import pipeline
import scipy

from definitions import HF_API_TOKEN

API_URL = "https://api-inference.huggingface.co/models/facebook/musicgen-small"
headers = {"Authorization": f"Bearer {HF_API_TOKEN}"}


def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response


# # data = query({"inputs": "The answer to the universe is [MASK]."})
# # print(data)

output = query({"inputs": "Dogs playing a piano"})
# Save the audio content as a FLAC file
with open("output.flac", "wb") as f:
    f.write(output.content)

print("done")



# synthesiser = pipeline("text-to-audio", "facebook/musicgen-small")

# music = synthesiser("dog playing a piano", forward_params={"do_sample": True})

# scipy.io.wavfile.write("musicgen_out.wav", rate=music["sampling_rate"], data=music["audio"])

# print("done")
