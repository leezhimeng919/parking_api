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
def EP_API_Base(
	method = None, 
	bizContent = None, 
	url = publicUrl, 
	timestamp = timeStamp, 
	token = accessToken, 
	apiId = clientId, 
	format = "json", 
	charset = "utf-8" 
	):
	if method == None or bizContent == None:
		return statusCode.checkCode('F','method or bizContent is None ')
	if type(bizContent) != dict:
		return statusCode.checkCode('F','bizeContent is not dict ')
	requestParameters = {
	'app_id': apiId, 
	'method': str(method), 
	'format': format, 
	'charset': charset, 
	'timestamp': timestamp, 
	'token': token, 
	'biz_content': json.dumps(bizContent)
	}

	r = requests.post(url, data=requestParameters)
	return statusCode.checkCode('T',r.json())
	
# get StationList
def EP_getStationList():
	method = 'et_common.station.lists'
	bizContent = {'appid': clientId}
	dataContent = EP_API_Base(method,bizContent)
	if type(dataContent) != dict and dataContent["statusCode"] != 0:
		return statusCode.checkCode('F')
	else:
		dataLists = (dataContent["statusContent"]["content"]["lists"])
		# get station id
		for i in dataLists:
			if "station_id" in i.keys():
				global stationId	
				stationId.append(str(i["station_id"]))
			else:
				return statusCode.checkCode('F')
		return dataContent

# get GateList by station_id
def EP_getOneGateList(station_id):
	method = 'et_common.device.lists'
	if stationId == []:
		return statusCode.checkCode('F')
	if station_id in stationId:
		bizContent = {'appid': clientId,'station_id': station_id}
		dataContent = EP_API_Base(method,bizContent)
		if type(dataContent) != dict and dataContent["statusCode"] != 0:
			return statusCode.checkCode('F')
		else:
			return dataContent
	else:
		return statusCode.checkCode('F')

# get all GateList
def EP_getGateList():
	if stationId == []:
		return statusCode.checkCode('F')
	else:
		for i in stationId:
			EP_getOneGateList(i)

# get ContractList by station_id
def EP_getOneContractList(station_id):
	method = 'et_common.contract.lists'
	if stationId == []:
		return statusCode.checkCode('F')
	if station_id in stationId:
		bizContent = {'appid': clientId,'station_id': station_id}
		dataContent = EP_API_Base(method,bizContent)
		if type(dataContent) != dict and dataContent["statusCode"] != 0:
			return statusCode.checkCode('F')
		else:
			dataLists = dataContent["statusContent"]["content"]["lists"]
			for i in dataLists:
				if "plate" in i.keys():
					global plate	
					plate.append(i["plate"])
					global plate_stationId
					plate_stationId[i["plate"]] = str(i["station_id"])
				else:
					return statusCode.checkCode('F')
			return dataContent
	else:
		return statusCode.checkCode('F')

# get all ContractList
def EP_getContractList():
	if stationId == []:
		return statusCode.checkCode('F')
	else:
		for i in stationId:
			EP_getOneContractList(i)


# del ContractPlate by plate
def EP_delOneContractPlate(plate_num):
	method = 'et_common.contract.del'
	if plate == [] or plate_stationId == {}:
		return statusCode.checkCode('F')
	if plate_num in plate:
		bizContent = {"appid": clientId,"station_id": plate_stationId[plate_num], "plate": plate_num}
		EP_API_Base(method,bizContent)
		return statusCode.checkCode('T')
	else:
		return statusCode.checkCode('F')

# if necessary
# del all ContractPlate
# def Ep_delContractPlate():

# recover ContractPlate by plate
def EP_recoverOneContractPlate(plate_num):
	method = 'et_common.contract.recover'
	if plate == [] or plate_stationId == {}:
		return statusCode.checkCode('F')
	if plate_num in plate:
		bizContent = {"appid": clientId,"station_id": plate_stationId[plate_num], "plate": plate_num}
		EP_API_Base(method,bizContent)
		return statusCode.checkCode('T')
	else:
		return statusCode.checkCode('F')

# ask GateOpen
def EP_askGateOpen(plate_num):
	method = 'et_common.car.askopen'
	if plate == [] or plate_stationId == {}:
		return statusCode.checkCode('F')
	if plate_num in plate:
		bizContent = {"appid": clientId,"station_id": plate_stationId[plate_num], "plate": plate_num}
		dataContent =  EP_API_Base(method,bizContent)
		if type(dataContent["statusContent"]["content"]) == list:
			dataLists = dataContent["statusContent"]["content"]
			global code_askopen
			code_askopen[plate_stationId[plate_num]] = dataLists[0]["code"]
		else:
			code_askopen[plate_stationId[plate_num]] = "12345"
			print(dataContent["statusContent"]["message"].encode('utf-8'))
		return dataContent
	else:
		return statusCode.checkCode('F')

# set GateOpen
def EP_setGateOpen(plate_num):
	method = 'et_common.car.open'
	if plate == [] or plate_stationId == {} or code_askopen == {}:
		return statusCode.checkCode('F')
	if plate_num in plate:
		bizContent = {"appid": clientId,"station_id": plate_stationId[plate_num], "plate": plate_num, "code": code_askopen[plate_stationId[plate_num]]}
		dataContent =  EP_API_Base(method,bizContent)
		print(dataContent["statusContent"]["message"].encode('utf-8'))
		return dataContent
	else:
		return statusCode.checkCode('F')

# set InviteCar
def EP_setInviteCar(plate_num,clientId,starttime="2019-04-02 14:00:00",stoptime="2019-04-20 14:00:00"):
	method = 'et_common.authorize.bespeak'
	bizContent = {"appid": clientId,"station_id": plate_stationId[plate_num], "plate": plate_num, "starttime": starttime, "stoptime": stoptime, "clientId": clientId}
	dataContent =  EP_API_Base(method,bizContent)
	print dataContent["statusContent"]["message"].encode('utf-8')
	return dataContent

# del InviteCar
def EP_delInviteCar(station_id,authorize_id = '1'):
	method = 'et_common.authorize.del'
	bizContent = {"appid": clientId,"station_id": station_id,"authorize_id": authorize_id}
	dataContent =  EP_API_Base(method,bizContent)
	print dataContent["statusContent"]["message"].encode('utf-8')
	return dataContent

# get the list for Invite Car 
def EP_getInviteCarList(station_id):
	method = 'et_common.authorize.lists'
	if stationId == []:
		return statusCode.checkCode('F')
	if station_id in stationId:
		bizContent = {'appid': clientId,'station_id': station_id}
		dataContent = EP_API_Base(method,bizContent)
		if type(dataContent) != dict and dataContent["statusCode"] != 0:
			return statusCode.checkCode('F')
		else:
			return dataContent
	else:
		return statusCode.checkCode('F')

# get Car Image for arrived id and department id
def EP_getCarImage(station_id,id = '1',type = 'in'):
	method = 'et_common.inout.images'
	bizContent = {"appid": clientId,"station_id": station_id,'type': type ,"id": id}
	dataContent =  EP_API_Base(method,bizContent)
	print dataContent["statusContent"]["message"].encode('utf-8')
	return dataContent

# get the admin_auth to Open Gate
def EP_adminOpenGate(device_id,cmd = 'open'):
	method = 'et_common.device.openAndClose'
	bizContent = {"appid": clientId,"cmd": cmd ,"device_id": device_id}
	dataContent =  EP_API_Base(method,bizContent)
	print dataContent["statusContent"]["message"].encode('utf-8')
	return dataContent

# gateContent = EP_API_Base('et_common.device.lists',{'appid': clientId,'station_id': str(2642)})
# print(len(gateContent["content"]["lists"]))

if __name__ == '__main__':
	print("getStationList Return JSON Format Data:\n")
	print EP_getStationList()

	print('\n+++++++++++++++\n')

	print("the list for stationId:\n")
	print(stationId)

	print('\n+++++++++++++++\n')

	print("getAllGateList no Return:\n")
	print EP_getOneGateList('2642')

	print('\n+++++++++++++++\n')

	print("getAllContractList no Return:\n")
	print EP_getOneContractList('2642','粤V12345')

	print('\n+++++++++++++++\n')

	print("the list for plate:\n")
	print(plate[0].encode('utf-8'))

	# print('\n+++++++++++++++\n')

	#print(plate[0].encode('utf-8'))

	print('\n+++++++++++++++\n')

	print("the dict for plate : stationId:\n")
	print(plate_stationId)

	print('\n+++++++++++++++\n')

	print("askGateOpen:\n")
	#EP_askGateOpen(plate[0].encode('utf-8'))


	print('\n+++++++++++++++\n')

	print("setGateOpen:\n")
	#EP_setGateOpen(plate[7])

	print('\n+++++++++++++++\n')

	print("getInviteCarList:\n")
	print EP_getInviteCarList('2642')

	print('\n+++++++++++++++\n')

	print("setInviteCar:\n")
	EP_setInviteCar(plate[7],'1',"2019-04-02 14:00:00","2019-04-20 14:00:00")

	print('\n+++++++++++++++\n')

	print("delInviteCar\n")
	EP_delInviteCar('2642','127')

	print('\n+++++++++++++++\n')

	print("getCarImage:\n")

	EP_getCarImage('2642','1','in')

	print('\n+++++++++++++++\n')

	print("adminOpenGate:\n")
	EP_adminOpenGate('3157','open')