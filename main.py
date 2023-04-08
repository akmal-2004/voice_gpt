import openai

import config
import stt
import tts

openai.api_key = (config.API_KEY)

def get_response(prompt):
    response = openai.Completion.create(
        model = "text-davinci-003",
        # prompt = "I am a highly intelligent question answering bot. If you ask me a question that is rooted in truth, I will give you the answer. If you ask me a question that is nonsense, trickery, or has no clear answer, I will respond with \"Unknown\".\n\nQ: What is human life expectancy in the United States?\nA: Human life expectancy in the United States is 78 years.\n\nQ: Who was president of the United States in 1955?\nA: Dwight D. Eisenhower was president of the United States in 1955.\n\nQ: Which party did he belong to?\nA: He belonged to the Republican Party.\n\nQ: What is the square root of banana?\nA: Unknown\n\nQ: How does a telescope work?\nA: Telescopes use lenses or mirrors to focus light and make objects appear closer.\n\nQ: Where were the 1992 Olympics held?\nA: The 1992 Olympics were held in Barcelona, Spain.\n\nQ: How many squigs are in a bonk?\nA: Unknown\n\nQ: Where is the Valley of Kings?\nA:",
        prompt = "The following is a conversation with an AI assistant (using werbs like woman). The assistant is helpful, creative, clever, and very friendly.\nHuman: " + prompt + "\nAI: ",
        temperature = 0.8,
        max_tokens = 500,
        top_p = 1,
        frequency_penalty = 0.0,
        presence_penalty = 0.6,
        stop=["AI:"]
    )
    return response.choices[0].text

def va_respond(voice: str):
    if 'алекс' in voice:
        voice = voice.replace('алекс', "").strip()
        tts.va_speak(get_response(voice))


def main():
    stt.va_listen(va_respond)

if __name__ == '__main__':
    va_respond("алекс представься как женский род и попреветсвуй человечество как настоящий искусственный интеллект по имени Алекс. Напиши это очень красиво, оригинально, креативно и коротко")
    main()