from gtts import gTTS
from pathlib import Path
import time





for i in range(20):
    tts_fr = gTTS(f'Bravo, tu as {i} points!', lang='fr')
    with open(Path(f'../sounds/quizz_des_enfants/points/{i}_points.mp3'), 'wb') as p:
        tts_fr.write_to_fp(p)
    time.sleep(1)