from __future__ import print_function
import urllib2
import json
import datetime
import csv
from data.urls import woodRiverAtHailey, redirectUrl


def lambda_handler(event, context):
    f = urllib2.urlopen(woodRiverAtHailey)

    reader = csv.reader(f)

    s = [row for row in reader]

    if s[-2][1] is None:
        last_val = s[-2][2]
    else:
        last_val = s[-2][1]

    if s[-1][2] is None:
        lastYear_val = s[-1][1]
    else:
        lastYear_val = s[-1][2]

    # print(last_val)
    # print(lastYear_val)

    slastVal = str(int(float(last_val) + .5))
    slastYear_val = str(int(float(lastYear_val) + .5))
    return_payload = {
        'statusCode': '200',
        'body': json.dumps([
            {
                'uid': str(datetime.datetime.now()),
                'mainText': 'The Wood River in Hailey is flowing at ' + slastVal + ' cubic feet per second.  Last year today it was at ' + slastYear_val + '.',
                'redirectionUrl': redirectUrl,
                'updateDate': datetime.datetime.utcnow().replace(microsecond=0).isoformat() + '.0Z',
                'titleText': 'Today = ' + slastVal + ' cfs.  Last Year = ' + slastYear_val + ' '
            }
        ]),
        'headers': {'Content-Type': "application/json"},
    }
    return return_payload


if __name__ == '__main__':
    incoming = {
        "body": "{\"test\":\"body\"}",
        "resource": "/{proxy+}",
        "requestContext": {
            "resourceId": "123456",
            "apiId": "1234567890",
            "resourcePath": "/{proxy+}",
            "httpMethod": "POST",
            "requestId": "c6af9ac6-7b61-11e6-9a41-93e8deadbeef",
            "accountId": "123456789012",
            "identity": {
                "apiKey": None,
                "userArn": None,
                "cognitoAuthenticationType": None,
                "caller": None,
                "userAgent": "Custom User Agent String",
                "user": None,
                "cognitoIdentityPoolId": None,
                "cognitoIdentityId": None,
                "cognitoAuthenticationProvider": None,
                "sourceIp": "127.0.0.1",
                "accountId": None
            },
            "stage": "prod"
        },
        "queryStringParameters": {
            "foo": "bar"
        },
        "headers": {
            "Via": "1.1 08f323deadbeefa7af34d5feb414ce27.cloudfront.net (CloudFront)",
            "Accept-Language": "en-US,en;q=0.8",
            "CloudFront-Is-Desktop-Viewer": "true",
            "CloudFront-Is-SmartTV-Viewer": "false",
            "CloudFront-Is-Mobile-Viewer": "false",
            "X-Forwarded-For": "127.0.0.1, 127.0.0.2",
            "CloudFront-Viewer-Country": "US",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Upgrade-Insecure-Requests": "1",
            "X-Forwarded-Port": "443",
            "Host": "1234567890.execute-api.us-east-1.amazonaws.com",
            "X-Forwarded-Proto": "https",
            "X-Amz-Cf-Id": "cDehVQoZnx43VYQb9j2-nvCh-9z396Uhbp027Y2JvkCPNLmGJHqlaA==",
            "CloudFront-Is-Tablet-Viewer": "false",
            "Cache-Control": "max-age=0",
            "User-Agent": "Custom User Agent String",
            "CloudFront-Forwarded-Proto": "https",
            "Accept-Encoding": "gzip, deflate, sdch"
        },
        "pathParameters": {
            "proxy": "path/to/resource"
        },
        "httpMethod": "POST",
        "stageVariables": {
            "baz": "qux"
        },
        "path": "/path/to/resource"
    }
    print(lambda_handler(incoming, {}))
