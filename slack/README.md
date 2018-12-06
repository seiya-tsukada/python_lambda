# python_lambda

## Post Slack

pip install

```
pip install -r requirements.txt -t .
```

to zip

```
zip -r /tmp/output.zip ./*
```

zip upload to lambda

```
aws lambda \
update-function-code \
--profile <aws_profile> \
--function-name <function_name> \
--zip-file fileb:///tmp/output.zip \
--publish
```