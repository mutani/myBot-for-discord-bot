from dotenv import load_dotenv
load_dotenv()

import os
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
GEMINI_PROMPT = os.getenv('GEMINI_PROMPT')
SDXL_TURBO_STATE = os.getenv('SDXL_TURBO_STATE')
SDXL_TURBO_TEMPORALY_STORAGE = os.getenv('SDXL_TURBO_TEMPORALY_STORAGE')