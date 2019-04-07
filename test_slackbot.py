from slackbot import lambda_handler


def test_slackbot_handler_url_verification():
    test_payload = {
        "token": "Jhj5dZrVaK7ZwHHjRyZWjbDl",
        "challenge": "3eZbrw1aBm2rZgRNFdxV2595E9CY3gmdALWMmHkvFXO7tYXAYM8P",
        "type": "url_verification",
    }
    result = lambda_handler(test_payload, None)
    assert result == test_payload["challenge"]


# # for development use only, mute this
# def test_slackbot_handler_chat():
#     test_payload = {"event": {"channel": "TEST_CHANNEL", "text": "test message text"}}
#     result = lambda_handler(test_payload, None)
#     assert result == 200


example_event_data_from_slack = {
    "resource": "/",
    "path": "/",
    "httpMethod": "POST",
    "headers": {
        "Accept": "*/*",
        "Accept-Encoding": "gzip,deflate",
        "CloudFront-Forwarded-Proto": "https",
        "CloudFront-Is-Desktop-Viewer": "true",
        "CloudFront-Is-Mobile-Viewer": "false",
        "CloudFront-Is-SmartTV-Viewer": "false",
        "CloudFront-Is-Tablet-Viewer": "false",
        "CloudFront-Viewer-Country": "US",
        "Content-Type": "application/json",
        "Host": "m2cm42c9fb.execute-api.ap-southeast-2.amazonaws.com",
        "User-Agent": "Slackbot 1.0 (+https://api.slack.com/robots)",
        "Via": "1.1 a20436c6d109fe9002d093f519ad4399.cloudfront.net (CloudFront)",
        "X-Amz-Cf-Id": "4sSTVWFHclSz_qRoVz8_csubM-ZFFzVw3ZRUuI2BKC2LYZGEXOMiJw==",
        "X-Amzn-Trace-Id": "Root=1-5ca98528-0257b7b5ca959cf08385b39c",
        "X-Forwarded-For": "34.207.64.242, 70.132.60.83",
        "X-Forwarded-Port": "443",
        "X-Forwarded-Proto": "https",
        "X-Slack-Request-Timestamp": "1554613543",
        "X-Slack-Signature": "v0=58cb9d61fc44f3dc0733ed3651c1095d7308949c603fc7fd0c3955367f3adba4",
    },
    "multiValueHeaders": {
        "Accept": ["*/*"],
        "Accept-Encoding": ["gzip,deflate"],
        "CloudFront-Forwarded-Proto": ["https"],
        "CloudFront-Is-Desktop-Viewer": ["true"],
        "CloudFront-Is-Mobile-Viewer": ["false"],
        "CloudFront-Is-SmartTV-Viewer": ["false"],
        "CloudFront-Is-Tablet-Viewer": ["false"],
        "CloudFront-Viewer-Country": ["US"],
        "Content-Type": ["application/json"],
        "Host": ["m2cm42c9fb.execute-api.ap-southeast-2.amazonaws.com"],
        "User-Agent": ["Slackbot 1.0 (+https://api.slack.com/robots)"],
        "Via": ["1.1 a20436c6d109fe9002d093f519ad4399.cloudfront.net (CloudFront)"],
        "X-Amz-Cf-Id": ["4sSTVWFHclSz_qRoVz8_csubM-ZFFzVw3ZRUuI2BKC2LYZGEXOMiJw=="],
        "X-Amzn-Trace-Id": ["Root=1-5ca98528-0257b7b5ca959cf08385b39c"],
        "X-Forwarded-For": ["34.207.64.242, 70.132.60.83"],
        "X-Forwarded-Port": ["443"],
        "X-Forwarded-Proto": ["https"],
        "X-Slack-Request-Timestamp": ["1554613543"],
        "X-Slack-Signature": [
            "v0=58cb9d61fc44f3dc0733ed3651c1095d7308949c603fc7fd0c3955367f3adba4"
        ],
    },
    "queryStringParameters": None,
    "multiValueQueryStringParameters": None,
    "pathParameters": None,
    "stageVariables": None,
    "requestContext": {
        "resourceId": "5d12jz2aw9",
        "resourcePath": "/",
        "httpMethod": "POST",
        "extendedRequestId": "XwG-UFD0ywMFuzA=",
        "requestTime": "07/Apr/2019:05:05:44 +0000",
        "path": "/dev",
        "accountId": "432873811268",
        "protocol": "HTTP/1.1",
        "stage": "dev",
        "domainPrefix": "m2cm42c9fb",
        "requestTimeEpoch": 1554613544444,
        "requestId": "cc4cdcb8-58f2-11e9-bd34-fbb177ec25ba",
        "identity": {
            "cognitoIdentityPoolId": None,
            "accountId": None,
            "cognitoIdentityId": None,
            "caller": None,
            "sourceIp": "34.207.64.242",
            "accessKey": None,
            "cognitoAuthenticationType": None,
            "cognitoAuthenticationProvider": None,
            "userArn": None,
            "userAgent": "Slackbot 1.0 (+https://api.slack.com/robots)",
            "user": None,
        },
        "domainName": "m2cm42c9fb.execute-api.ap-southeast-2.amazonaws.com",
        "apiId": "m2cm42c9fb",
    },
    "body": '{"token":"42mQKr5BfzLUvnUdp0itZYmY","challenge":"kIghLNVoSMS9OKEgnV7FxwrYOqfPi2IUl6vi3ORHmR8ZwFuTO0rS","type":"url_verification"}',
    "isBase64Encoded": False,
}
