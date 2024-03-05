from googletrans import Translator, LANGUAGES
import re
from tqdm import tqdm
import time

# ⲯ﹍︿﹍︿﹍ 𝙲𝚘𝚍𝚎 𝙱𝚢 𝚃𝚑𝚊𝚛𝚒𝚗𝚍𝚞 𝙼𝚊𝚍𝚞𝚜𝚑𝚊𝚗 ﹍ⲯ﹍ⲯ﹍︿﹍☼

# Initialize the translator
translator = Translator()

def safe_translate(text, dest='si', retries=3, delay=2):
    for attempt in range(retries):
        try:
            return translator.translate(text, dest=dest).text
        except Exception as e:
            print(f"Translation attempt {attempt+1}/{retries} failed: {e}")
            time.sleep(delay)  # Wait before retrying
    return text  # Return the original text if all retries fail

def translate_subtitle(input_file_path, output_file_path):
    with open(input_file_path, 'r', encoding='utf-8') as file:
        subtitles = file.readlines()
    
    with open(output_file_path, 'w', encoding='utf-8') as file:
        for line in tqdm(subtitles, desc="Translating"):
            if re.match(r'^\d+$', line) or re.match(r'^\d{2}:\d{2}:\d{2},\d{3} --> \d{2}:\d{2}:\d{2},\d{3}$', line):
                file.write(line)
            elif line.strip():
                translated = safe_translate(line, dest='si')
                file.write(translated + '\n')
            else:
                file.write('\n')

# Example usage
input_file_path = '1.en.srt'
output_file_path = 'translated_subtitle_file.srt'

translate_subtitle(input_file_path, output_file_path)


Code By Tharindu