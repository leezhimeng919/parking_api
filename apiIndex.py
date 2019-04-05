#_*_ coding:utf-8_*_ 
#没错，这是中文注释
#就像这样随便写
from getSignToken import getToken
import constant,statusCode
import requests, time, json


stationId = []

plate = []
# hash:use plate to find stationId 
plate_stationId = {}

code_askopen = {}

publicUrl = constant.getConstant()['publicUrl']

clientId = constant.getConstant()['clientId']

timeStamp = str(int(time.time()))

accessToken = str(getToken())


# this is common api
def EP_API_Base(methodArg, bizContentArg):
	if type(methodArg) != str:
		return statusCode.checkCode('F','methodArg is not str ')
	if type(bizContentArg) != dict:
		return statusCode.checkCode('F','bizeContent is not dict ')
	requestParameters = {
	'app_id': clientId, 'method': methodArg, 
	'format': "json", 'charset': "utf-8", 
	'timestamp': timeStamp, 'token': accessToken, 
	'biz_content': json.dumps(bizContentArg) }
	r = requests.post(publicUrl, data=requestParameters)
	return statusCode.checkCode('T',r.json())
	
# get StationList
def EP_getStationList(pageArg = '1', pagesizeArg = '20'):
	method = 'et_common.station.lists'
	bizContent = {
	'appid': clientId, 'page': pageArg, 
	'pagesize': pagesizeArg }
	dataContent = EP_API_Base(method,bizContent)
	if dataContent["statusCode"] == 0:
		return statusCode.checkCode('T',dataContent)
	return statusCode.checkCode('F','parameter error')

# get GateList by station_id
def EP_getGateList(stationIdArg, directionArg = 'in'):
	method = 'et_common.device.lists'
	if directionArg not in ['in','out']:
		return statusCode.checkCode('F','directionArg error')
	bizContent = {
	'appid': clientId, 'station_id': stationIdArg, 
	'dicretion': directionArg }
	dataContent = EP_API_Base(method,bizContent)
	if dataContent["statusCode"] == 0:
		return statusCode.checkCode('T',dataContent)
	return statusCode.checkCode('F','parameter error')



# get ContractList by station_id
def EP_getContractList(
	stationIdArg, plateArg = '#', 
	pageArg = '1', pagesizeArg = '20' ):
	method = 'et_common.contract.lists'
	bizContent = {
		'appid': clientId, 'station_id': stationIdArg, 
		'page': pageArg, 'pagesize': pagesizeArg }
	if plateArg != '#':
		bizContent['palte'] = plateArg
	dataContent = EP_API_Base(method,bizContent)
	if dataContent["statusCode"] == 0:
		return statusCode.checkCode('T',dataContent)
	return statusCode.checkCode('F','parameter error')
	


# del ContractPlate by plate
def EP_delContractPlate(stationIdArg, plateArg):
	method = 'et_common.contract.del'
	bizContent = {
	"appid": clientId, "station_id": stationIdArg, 
	"plate": plateArg }
	dataContent = EP_API_Base(method,bizContent)
	if dataContent["statusCode"] == 0:
		return statusCode.checkCode('T',dataContent)
	return statusCode.checkCode('F','parameter error')
	

# recover ContractPlate by plate
def EP_recoverContractPlate(stationIdArg, plateArg):
	method = 'et_common.contract.recover'
	bizContent = {
	"appid": clientId, "station_id": stationIdArg, 
	"plate": plateArg }
	dataContent = EP_API_Base(method,bizContent)
	if dataContent["statusCode"] == 0:
		return statusCode.checkCode('T',dataContent)
	return statusCode.checkCode('F','parameter error')


# ask GateOpen
def EP_askGateOpen(stationIdArg, plateArg, typeArg = 'in'):
	method = 'et_common.car.askopen'
	if typeArg not in ['in','out']:
		return statusCode.checkCode('F','typeArg error')
	bizContent = {
	"appid": clientId, "station_id": stationIdArg, 
	"plate": plateArg, "type": typeArg }
	dataContent =  EP_API_Base(method,bizContent)
	if dataContent["statusCode"] == 0:
		return statusCode.checkCode('T',dataContent)
	return statusCode.checkCode('F','parameter error')

# set GateOpen
def EP_setGateOpen(stationIdArg, plateArg, code):
	method = 'et_common.car.open'
	bizContent = {
	"appid": clientId, "station_id": stationIdArg, 
	"plate": plate_num, "code": code }
	dataContent =  EP_API_Base(method,bizContent)
	if dataContent["statusCode"] == 0:
		return statusCode.checkCode('T',dataContent)
	return statusCode.checkCode('F','parameter error')


# set InviteCar
def EP_setInviteCar(
	stationIdArg, starttimeArg, 
	stoptimeArg, clientIdArg, plateArg):
	method = 'et_common.authorize.bespeak'
	# 这里少了时间格式验证，以后补上
	bizContent = {
	"appid": clientId, "station_id": stationIdArg, 
	"plate": plateArg, "starttime": starttimeArg , 
	"stoptime": stoptimeArg, "clientId": clientIdArg }
	dataContent =  EP_API_Base(method,bizContent)
	if dataContent["statusCode"] == 0:
		return statusCode.checkCode('T',dataContent)
	return statusCode.checkCode('F','parameter error')

# del InviteCar
def EP_delInviteCar(stationIdArg, authorizeIdArg):
	method = 'et_common.authorize.del'
	bizContent = {"appid": clientId,"station_id": stationIdArg,"authorize_id": authorizeIdArg}
	dataContent =  EP_API_Base(method,bizContent)
	if dataContent["statusCode"] == 0:
		return statusCode.checkCode('T',dataContent)
	return statusCode.checkCode('F','parameter error')

# get the list for Invite Car 
def EP_getInviteCarList(
	stationIdArg, plateArg = '#', 
	pageArg = '1', pagesizeArg = '20' ):
	method = 'et_common.authorize.lists'
	bizContent = {
		'appid': clientId, 'station_id': stationIdArg, 
		'page': pageArg, 'pagesize': pagesizeArg }
	if plateArg != '#':
		bizContent['palte'] = plateArg
	dataContent = EP_API_Base(method,bizContent)
	if dataContent["statusCode"] == 0:
		return statusCode.checkCode('T',dataContent)
	return statusCode.checkCode('F','parameter error')

# get Car Image for arrived id and department id
def EP_getCarImage(stationIdArg, typeArg, idArg, 
	dateArg = str(time.strftime('%Y%m',time.localtime(time.time()))) ):
	method = 'et_common.inout.images'
	if typeArg not in ['in','out']:
		return statusCode.checkCode('F','typeArg error')
	if type(dateArg) != str and len(dateArg) != 6:
		return statusCode.checkCode('F','dateArg error')
	bizContent = {
	"appid": clientId, "station_id": stationIdArg,
	'type': typeArg, "id": idArg, 'date': dateArg }
	dataContent =  EP_API_Base(method,bizContent)
	if dataContent["statusCode"] == 0:
		return statusCode.checkCode('T',dataContent)
	return statusCode.checkCode('F','parameter error')

# get the admin_auth to Open Gate
def EP_adminOpenGate(deviceIdArg, cmdArg):
	method = 'et_common.device.openAndClose'
	if cmdArg not in ['open','close']:
		return statusCode.checkCode('F','cmdArg error')
	bizContent = {"appid": clientId,"cmd": cmdArg ,"device_id": deviceIdArg}
	dataContent =  EP_API_Base(method,bizContent)
	if dataContent["statusCode"] == 0:
		return statusCode.checkCode('T',dataContent)
	return statusCode.checkCode('F','parameter error')

# gateContent = EP_API_Base('et_common.device.lists',{'appid': clientId,'station_id': str(2642)})
# print(len(gateContent["content"]["lists"]))

if __name__ == '__main__':

	print("getStationList Return JSON Format Data:\n")
	print EP_getStationList()
	print('\n+++++++++++++++\n')


	print("getAllGateList no Return:\n")
	EP_getGateList()

	print('\n+++++++++++++++\n')

	print("getAllContractList no Return:\n")
	EP_getContractList()

	print('\n+++++++++++++++\n')

	# print('\n+++++++++++++++\n')

	#print(plate[0].encode('utf-8'))

	print('\n+++++++++++++++\n')

	print("the dict for plate : stationId:\n")
	print(plate_stationId)

	print('\n+++++++++++++++\n')

	print("askGateOpen:\n")
	EP_askGateOpen('粤V12345')


	print('\n+++++++++++++++\n')

	print("setGateOpen:\n")
	EP_setGateOpen('粤V12345')

	print('\n+++++++++++++++\n')

	print("getInviteCarList:\n")
	print EP_getInviteCarList('2642')

	print('\n+++++++++++++++\n')

	print("setInviteCar:\n")
	EP_setInviteCar('粤V12345','1',"2019-04-02 14:00:00","2019-04-20 14:00:00")

	print('\n+++++++++++++++\n')

	print("delInviteCar\n")
	EP_delInviteCar('2642','127')

	print('\n+++++++++++++++\n')

	print("getCarImage:\n")

	EP_getCarImage('2642','1','in')

	print('\n+++++++++++++++\n')

	print("adminOpenGate:\n")
	EP_adminOpenGate('3157','open')