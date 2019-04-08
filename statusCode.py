# Copyright 2016-2019 Smart Gateway Pte. Ltd. All Rights Reserved.
#
# EP parking signature and token retrieving
# This file is given as an example to calculate the signature and retrieve access token
# from EP cloud server

# Author: Jimmy Li (2019, 4, 4)

__all__ = ['checkCode']


statusTable = {
	'T' : 0,
	'F' : 1
}


def checkCode(bool,content = ""):
	if type(bool) == str:
		if statusTable[bool]:
			return {'statusCode' : statusTable[bool], 'statusMessage' : 'error', 'statusContent' : content }
		return {'statusCode' : statusTable[bool], 'statusMessage' : 'success', 'statusContent' : content }
	else:
		raise ValueError,'you should input type str : "T" or "F"'
		

if __name__ == '__main__':
	print checkCode('T')