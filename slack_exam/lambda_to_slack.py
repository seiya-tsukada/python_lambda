# coding: utf-8

import requests
import json
import random
import os

slack_url = os.environ.get("SLACK_URL")

def lambda_handler(event, context):

    # for i in range(1, 3):
    #    network_exam(i)

    part_list = [2, 2, 2]
    for i in part_list:
        network_exam(i)

    toeix_exam_alc()

    return {
        "statusCode": 200,
        "body": json.dumps("OK")
    }

def network_exam(part_num):

    ret = ""

    # site_url_base = "https://www.nw-siken.com/kakomon/30_aki/am1_2.html"
    site_url_base = "https://www.nw-siken.com/kakomon/"

    year_list = ["27", "28", "29", "30"]
    year = random.choice(year_list)

    question_list = list()
    question = ""
    if part_num == 1:
        question_list = range(1, 31)
        question = random.choice(question_list)
    elif part_num == 2:
        question_list = range(1, 26)
        question = random.choice(question_list)

    suffix_url = "{0}_aki/am{1}_{2}.html".format(year, part_num, question)

    site_url = site_url_base + suffix_url

    print(site_url)
    ret = post_slack(site_url)

    return ret

def toeix_exam_alc():

    ret = ""
    site_url = "https://www.alc.co.jp/toeic/article/daily/"

    print(site_url)
    ret = post_slack(site_url)

    return ret

def post_slack(text):

    ret = ""
    pretext = "今日の問題です"


    # post to slack
    ret = requests.post(slack_url, data = json.dumps({
        "channel": "#memo",
        "username": "my_bot",
        "icon_emoji": ":ghost:",
        "link_names": 1,
        "attachments": [{
            "text": text,
            "pretext": pretext,
        }]
    }))

    return ret