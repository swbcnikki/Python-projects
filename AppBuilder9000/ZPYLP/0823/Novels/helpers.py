import requests
import json
from django.shortcuts import render, get_object_or_404, redirect


# parse JSON response from defineWord() - JSON response stored in variable 'define'
# helper for defineWord()
def parseDefine(define):
    all_definitions = []
    definitions = define[0]['meaning']
    for word_type in definitions:
        for word_def in definitions[word_type]:
            print(word_def['definition'])
            # makes response as 'word type': 'definition' for each iteration
            all_definitions.append(f"{word_type}: {word_def['definition']}")
    return all_definitions


# parse through HTML for paragraph elements
# helper for soupRead()
def parseSoup(body):
    content = []
    for paragraph in body.find_all('p'):
        print(paragraph.text)
        content.append(paragraph.text)
    return content
