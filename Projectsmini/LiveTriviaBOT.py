# -*- coding: utf-8 -*-

# A Python bot which fetch questions from live trivia and tries to find answer on a quick google search
# Technology Used: Python, Pytesseract, google search api

from googleapiclient.discovery import build
import pprint
import json
from PIL import Image
import pytesseract 
import pprint

col = Image.open("########3")
gray = col.convert('L')
bw = gray.point(lambda x: 0 if x<128 else 255, '1')
bw.save("result_bw.png")
im = Image.open("result_bw.png")
text = pytesseract.image_to_string(im)
# Here text is a string
print (text)
parts = text.split("\n\n")
question = parts.pop(0).replace("\n", " ")
#parts = "\n".join(parts)
#parts = parts.split("\n")
print question
print parts
#answers = list(filter(lambda p: len(p) > 0, parts))

my_api_key = "##############################" 
my_cse_id =  "##############################"


def google_search(search_term, api_key, cse_id, **kwargs):
    service = build("customsearch", "v1", developerKey=api_key)
    res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
    return res['items']

results = google_search(
    question, my_api_key, my_cse_id, num=9)
#print results

count = [0,0,0]
output_res = " "
for i in range(0,5):
	output_res = output_res+" "+results[i]['snippet']

print output_res
for i in range(0,3):
	count[i] = output_res.count(parts[i])
	print count[i]

