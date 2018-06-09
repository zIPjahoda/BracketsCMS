import unicodedata
import re


def generate_url(input_string):
    result = ''.join(c for c in unicodedata.normalize("NFD", input_string) if unicodedata.category(c) != "Mn")
    result = result.replace(" ", "-").lower()
    result = re.sub("[^0-9a-zA-Z\-]", "", result)
    return result
