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
--function-name [function_name] \
--zip-file fileb:///tmp/output.zip \
--publish \
--region ap-northeast-1
```

test

```
aws lambda invoke --invocation-type Event \
--function-name [finction_name] \
--payload '{"key1": "value1"}' \
--region ap-northeast-1
output.txt
```