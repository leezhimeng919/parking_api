# Copyright 2016-2019 Smart Gateway Pte. Ltd. All Rights Reserved.
#
# EP parking signature and token retrieving
# This file is given as an example to calculate the signature and retrieve access token
# from EP cloud server

# Author: Wilson Wang (2019, 3, 25)
# Mender: Jimmy Li (2019, 3, 28)
# Imported headers for libraries
import json
import requests
import time, datetime, hashlib
import urllib

# ************* REQUEST VALUES *************
method = 'POST'

client_id ='4QFsuiiL3kIVc2OH'

secret = 'hWSWLQ3Fwv1T19pac8z7RxzZxbiAffNrbGBn'

endpoint_base = 'https://oauth.eptingche.cn'
# get code
endpoint_get='/silent/auth/get_code'
# use code to get access_token
endpoint_token='/silent/auth/access_token'

endpoint_url = 'https://api.eptingche.cn/v2/gateway'
# the content is JSON.
content_type = 'application/x-www-form-urlencoded'

# First step is to get code for access token retrieving
if type(client_id) != str:
    client_id = str(client_id)

dt = datetime.datetime.now()
ts = int(time.mktime(dt.timetuple()))
# ts = '1553505653'
#print "Current timestamp is: " + str(ts)

signStr="client_id="+client_id+"&"+"ts="+str(ts)+"&"+"secret="+secret
signStr_encode=signStr.replace("=", "%3D").replace("&", "%26").strip()
#print "The signStr is: "+ str(signStr)
#print "The encoded signStr is: " + str(signStr_encode)

m = hashlib.md5(str(signStr_encode))
signature = m.hexdigest()

#print "The signature is: " + signature

# Request parameters for CreateTable--passed in a JSON block.
request_parameters =  {'client_id': client_id, 'ts' : str(ts), 'signature' : signature}
#
endpoint = endpoint_base+endpoint_get
#print('Request URL = ' + endpoint)
#print('Request parameters is: ' + str(request_parameters))
#print(request_parameters["signature"])


r = requests.post(endpoint, data=request_parameters)

#print('\nRESPONSE++++++++++++++++++++++++++++++++++++')
#print('Response code: %d\n' % r.status_code)
#print(r.text)

data = json.loads(r.text)
#print "json data is: " + str(data)
# The Second step is to get access token
def getToken():
    if "content" in data:
        content=data["content"]
        #print "return content is: " + str(content)
        if "code" in content and "app_id" in content and "scope" in content:
            code = content["code"]
            app_id= content["app_id"]
            scope = content["scope"]

            #print "return code and app_id are: " + str(code)+ "," + str(app_id)
            # Request parameters for access token retrieving in a JSON block.
            request_parameters = {'client_id': client_id, 'scope': str(scope), 'code': str(code), 'app_id': str(app_id)}
            endpoint = endpoint_base + endpoint_token
            r = requests.post(endpoint, data=request_parameters)
            #print('\nRESPONSE++++++++++++++++++++++++++++++++++++')
            #print('Response code: %d\n' % r.status_code)
            #print(request_parameters)
            #print(r.text)
            try:
                return {"content": r.text, "ts": str(ts)}
            except ValueError:
                print('Error: In return access_token process error')
    #Here is the new code
            # datat = json.loads(r.text)
            # access_token = datat["content"]["access_token"]
            # endpoint = endpoint_url
            # method = 'et_common.station.lists'
            # biz_content = {'appid': str(client_id)}
            # request_parameters = {'app_id': str(client_id), 'method': method, 'format': 'json', 'charset': 'utf-8', 'timestamp': str(ts), 'token': str(access_token), 'biz_content': json.dumps((biz_content))}
            # #request_parameters = json.dumps(request_parameters)
            # r = requests.post(endpoint, data=request_parameters)
            # print('\nRESPONSE++++++++++++++++++++++++++++++++++++\n')
            # print('request param:\n')
            # print(request_parameters)
            # print('\nresponse param:\n')
            # print(r.content)
            # datatt = json.loads(r.content)
            # print(datatt["content"]["lists"])
            # print(r.json())
            # print(r.url)


        else:
            print "error here."
    else:
        print "error here."