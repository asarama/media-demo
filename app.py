
from models.text_2_audio.facebook import main as fb_main
from models.text_2_audio.riffusion import main as riff_main
from models.text_2_audio.mustango import main as must_main

from models.text_2_speech.melo import main as melo_main
from models.text_2_speech.barks import main as barks_main
from models.text_2_speech.microsoft import main as ms_main

from definitions import MODEL_SET

if MODEL_SET == "text_2_speech":
    melo_main()
    barks_main()
    ms_main()
elif MODEL_SET == "text_2_audio":
    fb_main()
    riff_main()
    must_main()

print("done")
