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