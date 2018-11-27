# coding: utf-8

import json
import boto3
import datetime

def lambda_handler(event, context):
    
    sns = boto3.client("sns")
    
    date = datetime.datetime.now()
    date_now = "{0}.{1}.{2} {3}:{4}:{5}".format(
        date.year,
        date.month,
        date.day, 
        date.hour,
        date.minute,
        date.second
    )
    
    # print(date_now)
    
    # Get SNS Event
    message_unicode = event["Records"][0]["Sns"]["Message"]
    
    # Convirt
    message_dist = json.loads(message_unicode)
    
    # Get CloudWatchAlarm Name
    event_sorce_alarm_name = message_dist['AlarmName']
 
    # print(event_sorce_alarm_name)
 
    # Get HostName From Alarm Name
    alarm_name = event_sorce_alarm_name.split("-")
    alarm_name_host_name = alarm_name[0]

    # Create Topic ARN
    topic_arn_base = "arn:aws:sns:[region]:[id]:"    
    topic_arn = topic_arn_base + alarm_name_host_name + "-Alert"
    # print(topic_arn)
    
    subject = alarm_name_host_name + "が自動復旧しました"
    
    message = """
    発生時刻(UTC): {0}
    サーバ {1} が自動復旧しました。
    念の為、サーバの動作確認をお願いします
    """.format(date_now, alarm_name_host_name)
    
    # publish
    response = sns.publish(
        TopicArn = topic_arn,
        Subject = subject,
        Message = message,
    )

    return {
        "statusCode": 200,
        "body": json.dumps(response)
    }