import torch
import sounddevice as sd
import time
from num2words import num2words

language = 'ru'
model_id = 'v3_1_ru' # ru_v3
sample_rate = 48000 # 8000, 24000, 48000
speaker = 'xenia' # aidar, eugene, baya, kseniya, xenia, random
put_accent = True
put_yo = True
device = torch.device('cpu') # cpu или gpu
text = "Привет, мир!"

model, _ = torch.hub.load(repo_or_dir='snakers4/silero-models',
                          model='silero_tts',
                          language=language,
                          speaker=model_id)
model.to(device)



def va_speak(what: str):
    print(what)

    whatlist = what.replace(':', ' ').replace(',', ' ').replace('-', ' ').replace('.', ' ').split()
    for i in whatlist:
        if i.isdigit():
            what = what.replace(i, num2words(int(i), lang='ru'))

    audio = model.apply_tts(text=what+"..",
                            speaker=speaker,
                            sample_rate=sample_rate,
                            put_accent=put_accent,
                            put_yo=put_yo)

    sd.play(audio, sample_rate * 1.05)
    time.sleep((len(audio) / sample_rate) + 0.5)
    sd.stop()

# sd.play(audio, sample_rate)
# time.sleep(len(audio) / sample_rate)
# sd.stop()

# va_speak("привет Акмаль! Это я. Программа, голосовой ассистент! Звучу очень реалистично, не так ли?")