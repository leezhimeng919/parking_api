# Copyright 2016-2019 Smart Gateway Pte. Ltd. All Rights Reserved.
#
# EP parking signature and token retrieving
# This file is given as an example to calculate the signature and retrieve access token
# from EP cloud server

# Author: Wilson Wang (2019, 3, 25)

# Mender: Jimmy Li (2019, 4, 3)

# Imported headers for libraries


import time, hashlib, urllib, requests
# a private module
import constant,statusCode

# ************* REQUEST VALUES *************


clientId = constant.getConstant()['clientId']

clientSecret = constant.getConstant()['clientSecret']

baseUrl = constant.getConstant()['baseUrl']

urlGetCode = constant.getConstant()['urlGetCode']

urlGetToken = constant.getConstant()['urlGetToken']

# the content is JSON.

# First step is to get code for access token retrieving

# get timestamp
timeStamp = str(int(time.time()))

# urlencode
signStr = "client_id=" + clientId + "&ts=" + timeStamp + "&secret=" + clientSecret
signStrEncode = urllib.quote(signStr)

# get signature use md5
signature = hashlib.md5()
signature.update(signStrEncode)
signature = signature.hexdigest()



# Request parameters for CreateTable--passed in a JSON block.
requestParameters =  {'client_id': clientId, 'ts' : timeStamp, 'signature' : signature}

endPoint = baseUrl + urlGetCode

r = requests.post(endPoint, data=requestParameters)

data = r.json()

# The Second step is to get access token
def getToken():
    if data["code"] != 0:
        return statusCode.checkBaseCode('F', data)
    if "content" not in data.keys():
        return statusCode.checkBaseCode('F', data)
    content = data["content"]
    if "code" not in content or "app_id" not in content or "scope" not in content:
        return statusCode.checkBaseCode('F', data)
    code = content["code"]
    app_id= content["app_id"]
    scope = content["scope"]
    #print "return code and app_id are: " + str(code)+ "," + str(app_id)
    # Request parameters for access token retrieving in a JSON block.
    requestParameters = {'client_id': clientId, 'scope': scope, 'code': code, 'app_id': app_id}
   
    endPoint = baseUrl + urlGetToken

    r = requests.post(endPoint, data=requestParameters)

    try:
        return r.json()["content"]["access_token"]
    except ValueError:
        return statusCode.checkBaseCode('F', data)
  

  

if __name__ == '__main__':
    print getToken()
