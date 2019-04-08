# Copyright 2016-2019 Smart Gateway Pte. Ltd. All Rights Reserved.
#
# EP parking signature and token retrieving
# This file is given as an example to calculate the signature and retrieve access token
# from EP cloud server

# Author: Jimmy Li (2019, 4, 4)

__all__ = ['checkBaseCode' , 'checkSubCode']


statusTable = {
	'T' : 0,
	'F' : 1
}


def checkBaseCode(bool,content = ""):
	if type(bool) == str:
		if statusTable[bool]:
			if type(content) == dict:
				content = {'errorBaseCode': content['code'] , 'errorBaseMessage':content['message'] }
			return {'statusBaseCode' : statusTable[bool], 'statusBaseMessage' : 'error', 'statusBaseContent' : content }
		return {'statusBaseCode' : statusTable[bool], 'statusBaseMessage' : 'success', 'statusBaseContent' : content }
	else:
		raise ValueError,'you should input type str : "T" or "F"'
		
def checkSubCode(bool,content = ""):
	if type(bool) == str:
		if statusTable[bool]:
			return {'statusSubCode' : statusTable[bool], 'statusSubMessage' : 'error', 'statusSubContent' : content }
		return {'statusSubCode' : statusTable[bool], 'statusSubMessage' : 'success', 'statusSubContent' : content }
	else:
		raise ValueError,'you should input type str : "T" or "F"'


if __name__ == '__main__':
	print checkSubCode('F', {'code':9000 , 'message': 'asdas', 'casd': 'dasdsa'})