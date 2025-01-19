#given: worksheet, characters
import csv
from deep_translator import GoogleTranslator
import pandas as pd

user_input = pd.read_csv('user_writing.csv', header=None)
translated = []
for i in range(0, len(user_input)):
    text_to_translate = user_input.iloc[i, 0]
    translated_text = GoogleTranslator(source='auto', target='zh-CN').translate(text_to_translate)
    translated.append(translated_text)
    print(translated_text)

user_input['translated'] = translated
print(len(user_input))
user_input.to_csv('user_writing_translated.csv', index=False)