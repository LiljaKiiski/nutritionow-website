from transformers import pipeline
from pprint import pprint

#generator = pipeline('text-generation', model='EleutherAI/gpt-neo-1.3B')
generator = pipeline('text-generation', model='gpt2-large')

prompt = "Nutrition is important because "

output = generator(prompt, min_length=30, max_length=60)
print(output[0])