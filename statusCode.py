__all__ = ['checkCode']

statusTable = {
	0 : '成功'
	10001 : '参数缺失说明'
}




def checkCode(request):
	if type(request) != dict:
		return 'fasle'
	if "code" in request.keys():
		code = request["code"]
		return status[code]


		

if __name__ == '__main__':
	checkCode({1:2})