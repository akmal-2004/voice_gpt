import openai
import config
import stt
import tts

openai.api_key = config.API_KEY

chat_history = ""

ai_name = "алекс"
human_name = "человек"
ai_mode = f"Притворись что ты ассистент женского пола по имени {ai_name}. Продолжи разговор. Ты очень полезная, творческая, умная, дружелюбная и ты готова на всё что-бы помочь {human_name}."

def get_response(userprompt):
    global chat_history, openai
    if chat_history == "" or len(chat_history) > (4116 - 400): # max 4116
        chat_history = ai_mode

    userprompt = f"{chat_history}\n{human_name}: {userprompt}\n{ai_name}: "
    try:
        response = openai.Completion.create(
            model = "text-davinci-003",
            prompt = userprompt,
            temperature = 0.5,
            max_tokens = 400,
            top_p = 1,
            frequency_penalty = 0.5,
            presence_penalty = 0.0,
            stop = [f"{ai_name}: "]
        )
    except Exception as e:
        print(e)
        tts.va_speak("Ошибка. Перезагружаю подключение.")
        del openai
        import openai
        openai.api_key = config.API_KEY
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
    va_respond(f"{ai_name} представься и попреветсвуй {human_name}. Напиши это очень красиво, оригинально, креативно и коротко")
    main()