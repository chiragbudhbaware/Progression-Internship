from prompt_utils import clean_text, is_long_prompt

text = "   Hello, World!"

cleaned_text = clean_text(text)

long_prompt = is_long_prompt(cleaned_text)

print(f"Cleaned Text: '{cleaned_text}")
print(f"Is the prompt long? {long_prompt}")