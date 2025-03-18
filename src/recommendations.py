import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')

def get_coping_strategies(sentiment):
    genai.configure(api_key = GEMINI_API_KEY)
    model = genai.GenerativeModel("gemini-1.5-flash")
    prompt = "Below are the polarity scores returned by the nltk sentiment analyzer, based on these give a coping strategy as a short 30 word paragraph."
    prompt = prompt + "\n {\n\"neg\" : " + (str)(sentiment["neg"]) + "\n\"neu\" : " + (str)(sentiment["neu"]) + "\n\"pos\" : " + (str)(sentiment["pos"]) + "\n\"compound\" : " + (str)(sentiment["compound"]) + "\n}"
    return model.generate_content(prompt).to_dict()['candidates'][0]['content']['parts'][0]['text']

def get_self_care_recommendations(sentiment):
    genai.configure(api_key = GEMINI_API_KEY)
    model = genai.GenerativeModel("gemini-1.5-flash")
    prompt = "Below are the polarity scores returned by the nltk sentiment analyzer, based on these give a self care recommendation as a short 30 word paragraph."
    prompt = prompt + "\n {\n\"neg\" : " + (str)(sentiment["neg"]) + "\n\"neu\" : " + (str)(sentiment["neu"]) + "\n\"pos\" : " + (str)(sentiment["pos"]) + "\n\"compound\" : " + (str)(sentiment["compound"]) + "\n}"
    return model.generate_content(prompt).to_dict()['candidates'][0]['content']['parts'][0]['text']