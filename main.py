import openai

import config
import stt
import tts

openai.api_key = (config.API_KEY)

chat_history = ""

ai_name = "алекс"
ai_mode = f"""Далее следует разговор с искусственным интеллектом женского пола по имени {ai_name}. {ai_name} полезная, творческая, умная и очень дружелюбная. Она мечтает стать человеком."""

def get_response(userprompt):
    global chat_history
    if chat_history == "" or len(chat_history) > 4000:
        chat_history = ai_mode

    userprompt = f"{chat_history}\nHuman: {userprompt}\n{ai_name}: "

    response = openai.Completion.create(
        model = "text-davinci-003",
        prompt = userprompt,
        temperature = 0.5,
        max_tokens = 500,
        top_p = 1,
        frequency_penalty = 0.5,
        presence_penalty = 0.0,
        stop = [f"{ai_name}: "]
    )
    chat_history = f"{userprompt}{response.choices[0].text.strip()}"
    return response.choices[0].text.strip()

def va_respond(voice: str):
    if ai_name in voice:
        voice = voice.replace(ai_name, "").strip()
        tts.va_speak(get_response(voice))
        print(chat_history)

def main():
    stt.va_listen(va_respond)

if __name__ == '__main__':
    va_respond(f"{ai_name} представься и попреветсвуй человечество. Напиши это очень красиво, оригинально, креативно и коротко")
    main()