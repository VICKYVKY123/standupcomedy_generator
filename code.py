# Stand-up Comedy Generator using GPT-2
# Compatible with Google Colab

# Step 1: Install dependencies
!pip install transformers --quiet
!pip install torch --quiet

# Step 2: Import libraries
from transformers import pipeline, set_seed
import random

# Step 3: Load text generation pipeline with GPT-2
generator = pipeline('text-generation', model='gpt2')
set_seed(42)

# Step 4: Define comedy prompt templates
comedy_prompts = [
    "So I was at the grocery store the other day, and",
    "Have you ever noticed how",
    "Dating in the 21st century is like",
    "Airports are the only place where",
    "I tried online dating and let me tell you,",
    "I have a friend who's way too into yoga, and",
    "Why do dogs always act like",
]

# Step 5: Comedy generator function
def generate_comedy(prompt=None, max_length=100, num_return_sequences=1):
    if prompt is None:
        prompt = random.choice(comedy_prompts)
    results = generator(prompt, max_length=max_length, num_return_sequences=num_return_sequences, do_sample=True, temperature=0.9)
    return [res['generated_text'] for res in results]

# Step 6: Interactive generation
prompt = input("Enter your comedy prompt (or press Enter for a random one): ").strip()
if prompt == "":
    prompt = random.choice(comedy_prompts)

print("\n🎤 Stand-Up Comedy Set:\n")
jokes = generate_comedy(prompt=prompt, max_length=120, num_return_sequences=1)
print(jokes[0])
