import textwrap
import config
import google.generativeai as genai
import google.api_core.exceptions
from IPython.display import Markdown

#GEMINI_API
GEMINI_API_KEY = config.GEMINI_API_KEY
GEMINI_PROMPT = config.GEMINI_PROMPT
GEMINI_15_FLASH = 'gemini-1.5-flash'
GEMINI_TRANSLATE_TO_ENGLISH_PROMPT = 'Translate the following text to English:'
GEMINI_TRANSLATE_TO_JAPANESE_PROMPT = 'Translate the following text to Japanese:'

def gemini_onetimetext_api(prompt, model_name):
    genai.configure(api_key=GEMINI_API_KEY) 
    model = genai.GenerativeModel(model_name)
    try:
        response = model.generate_content(GEMINI_PROMPT + "\n" + prompt)
        return to_markdown(response.text)
    except google.api_core.exceptions.InternalServerError as e:
        return "内部サーバーエラーが発生しました。後でもう一度お試しください。"
    except Exception as e:
        return "予期しないエラーが発生しました。"

def get_gemini_models():
    genai.configure(api_key=GEMINI_API_KEY)
    return [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]

def translate_to_english(prompt):
    genai.configure(api_key=GEMINI_API_KEY) 
    model = genai.GenerativeModel(GEMINI_15_FLASH)
    response = model.generate_content(GEMINI_TRANSLATE_TO_ENGLISH_PROMPT + prompt)
    return to_markdown(response.text)

def translate_to_japanese(prompt):
    genai.configure(api_key=GEMINI_API_KEY) 
    model = genai.GenerativeModel(GEMINI_15_FLASH)
    response = model.generate_content(GEMINI_TRANSLATE_TO_JAPANESE_PROMPT + prompt)
    return to_markdown(response.text)

def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))