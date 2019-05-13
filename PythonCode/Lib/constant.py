# Copyright 2016-2019 Smart Gateway Pte. Ltd. All Rights Reserved.
#
# EP parking signature and token retrieving
# This file is given as an example to calculate the signature and retrieve access token
# from EP cloud server

# Author: Jimmy Li (2019, 4, 4)

__all__ = ['getConstant']

def getConstant():
	constants = {

	'clientId' : '4QFsuiiL3kIVc2OH',

	'clientSecret' : 'hWSWLQ3Fwv1T19pac8z7RxzZxbiAffNrbGBn',

	'baseUrl' : 'https://oauth.eptingche.cn',

	'urlGetCode' : '/silent/auth/get_code',

	'urlGetToken' : '/silent/auth/access_token',

	'publicUrl' : 'https://api.eptingche.cn/v2/gateway'

	}

	return constants
 


if __name__ == '__main__':
	print getConstant()

