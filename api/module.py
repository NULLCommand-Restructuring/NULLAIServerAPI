import os
from g4f.client import Client
from g4f.cookies import set_cookies
from g4f.Provider import RetryProvider, Gemini, FreeGpt, Blackbox, BingCreateImages

def gpt_answer(message):
    try:
        set_cookies(".google.com", {
            "__Secure-1PSID": os.getenv('Secure1PSID')
            "__Secure-1PSIDTS": os.getenv('Secure1PSIDTS')
        })

        response = Client(provider=Gemini).chat.completions.create(
            model="gemini",
            messages=[{"role": "user", "content": message}]
        )
        return response.choices[0].message.content + "\n[Current model: FXT feat Gemini]"

    except Exception as e:
        print(f"An error occurred: {e}")
        response = Client(provider=RetryProvider([Blackbox, FreeGpt])).chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": message}]
        )
        return response.choices[0].message.content + "\n[Current model: FXT feat GPT]"

def bing_image_answer(prompt):
    set_cookies(".bing.com", {"_U": os.getenv('BingCookie')})

    response = Client(image_provider=BingCreateImages).images.generate(
        model="dall-e-3",
        prompt=prompt
    )

    return response.data[0].url
