# coding: utf-8

import requests
import json
import random

year_list = ["28", "29", "30"]
half_list = ["1", "2"]
question_list = list()
slack_url = ""

# site_url_base = "https://www.nw-siken.com/kakomon/30_aki/am1_2.html"

site_url_base = "https://www.nw-siken.com/kakomon/"
year = random.choice(year_list)
half = random.choice(half_list)

if half == "1":
    question_list = range(1, 31)
    question = random.choice(question_list)
elif half == "2":
    question_list = range(1, 26)
    question = random.choice(question_list)

suffix_url = "{0}_aki/am{1}_{2}.html".format(year, half, question)

site_url = site_url_base + suffix_url

print site_url

# create content
content = """

今日の問題はこれです

{0}

""".format(site_url)

# post to slack
requests.post(slack_url, data = json.dumps({
    "text": content,
    "username": "my_bot",
    "icon_emoji": ":ghost:",
    "link_names": 1,
}))