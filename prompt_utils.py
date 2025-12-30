def clean_text(text):
    cleaned = text.strip().lower()
    return cleaned

def is_long_prompt(text):
    if len(text) > 20:
        return True
    else:
        return False
    