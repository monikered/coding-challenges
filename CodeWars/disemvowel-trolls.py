# Your task is to write a function that takes a string and return a new string with all vowels removed.

import re

def disemvowel(string):
    return re.sub('[aeiouAEIOU]', '', string)
