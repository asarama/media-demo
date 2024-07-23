
from models.text_2_speech.melo import main as melo_main
from models.text_2_speech.barks import main as barks_main
from models.text_2_speech.microsoft import main as ms_main

from definitions import MODEL_SET

if MODEL_SET == "text_2_speech":
    melo_main()
    barks_main()
    ms_main()

print("done")


# from transformers import pipeline
# import scipy

# synthesiser = pipeline("text-to-audio", "facebook/musicgen-small")

# music = synthesiser("dog playing a piano", forward_params={"do_sample": True})

# scipy.io.wavfile.write("musicgen_out.wav", rate=music["sampling_rate"], data=music["audio"])

# print("done")
