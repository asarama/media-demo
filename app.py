
from models.text_2_speech.facebook import main

main()

print("done")


# from transformers import pipeline
# import scipy

# synthesiser = pipeline("text-to-audio", "facebook/musicgen-small")

# music = synthesiser("dog playing a piano", forward_params={"do_sample": True})

# scipy.io.wavfile.write("musicgen_out.wav", rate=music["sampling_rate"], data=music["audio"])

# print("done")
