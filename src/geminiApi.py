import os
from dotenv import load_dotenv
import textwrap
import google.generativeai as genai
from IPython.display import Markdown

load_dotenv()
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
GEMINI_PROMPT = os.getenv('GEMINI_PROMPT')
def gemini_onetimetext_api(prompt, model_name='gemini-1.5-flash'):
    genai.configure(api_key=GEMINI_API_KEY) 
    # モデル設定
    model = genai.GenerativeModel(model_name)
    response = model.generate_content(GEMINI_PROMPT + "\n" + prompt)
    return to_markdown(response.text)

def get_gemini_models():
    genai.configure(api_key=GEMINI_API_KEY)
    return [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]

def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))