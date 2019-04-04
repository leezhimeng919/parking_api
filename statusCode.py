__all__ = ['checkCode']

statusTable = {
	'T' : 0,
	'F' : 1
}




def checkCode(bool):
	if type(bool) == str:
		if statusTable[bool]:
			return {'statusCode' : statusTable[bool], 'statusMessage' : 'error'}
		return {'statusCode' : statusTable[bool], 'statusMessage' : 'success'}
	else:
		raise ValueError,'you should input type str : "T" or "F"'
		

if __name__ == '__main__':
	print checkCode(1)