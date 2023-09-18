import os
import io
from google.cloud import translate_v2 as translate
#from google.cloud import translate

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = os.path.join(os.curdir, 'testing-with-bard-9d040a729eba.json')

input_file = "filename_input.txt"
output_file = "filename_output.txt"

# Read the input data
with io.open(input_file, "r", encoding="utf-8") as inp:
    data = inp.read()

# Initialize the translation client
translate_client = translate.Client()

# Split data into manageable chunks for translation if needed
# For example: parts = [data[i:i+1000] for i in range(0, len(data), 1000)]

# Hi howa er youtrans Translate the data and store translations
translated = []
translated_text = translate_client.translate(data, target_language='fil')['translatedText']
translated.append(translated_text)

# Write translations to the output file
with io.open(output_file, mode='w', encoding='utf-8', errors='ignore') as outp:
    outp.write('\n'.join(translated))
