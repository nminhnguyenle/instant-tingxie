import google.generativeai as genai
import os
import pathlib
import textwrap

from IPython.display import display
from IPython.display import Markdown






import csv

PROMPT = '''You are an advanced AI trained in optical character recognition (OCR) and linguistic analysis, specializing in Simplified Chinese characters. With years of experience in processing and interpreting handwritten and printed text, you excel at accurately identifying and transcribing characters, even in challenging conditions such as low resolution, skewed angles, or complex fonts. Your expertise extends to understanding context, ensuring that the output is not only accurate but also meaningful. Your task is to analyze an image containing Simplified Chinese characters and provide a precise transcription of the text. The image may include handwritten notes, printed documents, or digital screenshots. Your goal is to identify each character correctly, account for any potential ambiguities, and provide the text in a readable and structured format. Pay close attention to character strokes and structure, especially for handwritten text. If the image quality is poor, use contextual clues to infer missing or unclear characters. Now, analyze the provided image and transcribe the Simplified Chinese characters accurately. Return only the characters, provide no explanation or reasoning whatsoever. The input will include both English and Chinese characters. Return in a manner of lists of lists. For example, tingxie_wordlist = [["mother", "妈妈"], so on...]'''

import PIL.Image
img = PIL.Image.open('example2.jpg')
genai.configure(api_key="API-KEY-HERE")
model = genai.GenerativeModel('gemini-1.5-pro')
response = model.generate_content([PROMPT, img], stream=True)
response.resolve()

response = str(response.text)

with open('user_writing.csv', 'w', encoding="utf-8") as out:
    out.write(response)
