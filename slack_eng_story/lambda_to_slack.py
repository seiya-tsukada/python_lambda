# coding: utf-8

import requests
import json
import random
import os
import re
from bs4 import BeautifulSoup  

slack_url = os.environ.get("SLACK_URL")

def lambda_handler(event, context):

    number_list = range(1, 5)
    number = random.choice(number_list)
    english_story(number)

    return {
        "statusCode": 200,
        "body": json.dumps("OK")
    }

def english_story(story_number):

    site_url_base = "http://readpoopfiction.com/story.php"
    site_url = "{0}?length={1}".format(site_url_base, story_number)

    print(site_url)

    r = requests.get(site_url)
    soup = BeautifulSoup(r.text, "html.parser")

    content_class = soup.find(class_="content")

    content_class_body = content_class("p")

    content_title = content_class("h1")
    content_sub_title = content_class("h2")

    content_title_re = tag_extraction(str(content_title[0]))
    content_sub_title_re = tag_extraction(str(content_sub_title[0]))

    content = ""
    for i in content_class_body:
        content = content + str(i)

    print(content)

    ret = post_slack(site_url, content, content_title_re, content_sub_title_re)

    return ret


def tag_extraction(text):

    pattern = r"<[^>]*?>"
    p = re.compile(pattern)
    return p.sub("", text)

def post_slack(site_url, content, content_title, content_sub_title):

    slack_url = "https://hooks.slack.com/services/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"

    ret = ""
    text = content
    title = content_title
    title_link = site_url
    pretext = content_sub_title

    # post to slack
    ret = requests.post(slack_url, data = json.dumps({
        "channel": "#memo",
        "username": "my_bot",
        "icon_emoji": ":ghost:",
        "link_names": 1,
        "attachments": [{
            "title": title,
            "title_link": title_link,
            "pretext": pretext,
            "text": text,
        }]
    }))

    return ret

lambda_handler("", "")
