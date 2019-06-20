import os
import json
import requests
from requests.exceptions import HTTPError
# Get api access to NobelPrize data
# Use requests.get
# 200 is OK
# action determined by get and post
# get is to retrieve
response = requests.get("http://api.nobelprize.org/v1/prize.json")

# store response and use it to retrieve info
response.status_code
# returns 200, implying success.
# test if the response was successful:


def test_response(response):
    if response.status_code == 200:
        print("Successs")
    elif response.status_code == 404:
        print("Not found!")




test_response(response)
# Convert text to dict with json loads
json.loads(response.text)
# Better way is to use .json
res_dict = response.json()

type(res_dict)

# get each author and year
import re

authors = []

[type(i) for i in res_dict["prizes"]]

# All dictionaries
# Get each unqiue dictionary
# Append to a table or some other format, perhaps print
# Check length of this result
import itertools

len(res_dict["prizes"])

res = res_dict["prizes"]


nobels = []

for val in res:
    for key, value in val.items():
        if re.match("lau+", key):
            nobels.append((key, value))

def extract_data(match):
    for nobel in nobels:
        if isinstance(nobel, tuple):
            for key, value in nobel[1][0].items():
                if re.match(eval(repr(match)), key):
                    print(value)


# Extract the nobel's first names
extract_data("first+")

# Extract their surnames

extract_data("sur+")

# Extract their motivation

extract_data("mot+")

# Extract how many shared the prize

extract_data("shar+")


























