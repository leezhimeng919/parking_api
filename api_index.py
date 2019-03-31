from EParking_signature_token import getToken,endpoint_url,client_id
import json
import requests
import time, datetime, hashlib
import urllib

ts = getToken()["ts"]
stationId = []
plate = []
# hash:use plate to find stationId 
plate_stationId = {}
code_askopen = {}
datat = json.loads(getToken()["content"])

access_token = datat["content"]["access_token"]

falseMessage = {"code": 10001, "message": "False", "content": ""}
successMessage = {"code": 0, "message": "success", "content": ""}
#

# this is common api
def EP_API_Base(method=None,biz_content=None,url=endpoint_url,timestamp=str(ts),token=str(access_token),api_id = client_id ,format="json",charset="utf-8"):
	if type(method) != str:
		return "method format error"
	if type(biz_content) != dict:
		return "biz_content format error"
	if url == None or timestamp == None or token == None or api_id == None:
		return "Parameters are missing"
	request_parameters = {'app_id': api_id, 'method': method, 'format': format, 'charset': charset, 'timestamp': timestamp, 'token': token, 'biz_content': json.dumps((biz_content))}

	r = requests.post(url, data=request_parameters)
	return {"status_code": 0, "return_message": "success", "content": r.json()}
	
	

# get StationList
def EP_getStationList():
	method = 'et_common.station.lists'
	biz_content = {'appid': client_id}
	dataContent = EP_API_Base(method,biz_content)
	if type(dataContent) != dict and dataContent["status_code"] !=0:
		return falseMessage
	else:
		dataLists = (dataContent["content"]["content"]["lists"])
		# get station id
		for i in dataLists:
			if "station_id" in i.keys():
				global stationId	
				stationId.append(str(i["station_id"]))
			else:
				return falseMessage
		return dataContent

# get GateList by station_id
def EP_getOneGateList(station_id):
	method = 'et_common.device.lists'
	if stationId == []:
		return falseMessage
	if station_id in stationId:
		biz_content = {'appid': client_id,'station_id': station_id}
		dataContent = EP_API_Base(method,biz_content)
		if type(dataContent) != dict and dataContent["status_code"] != 0:
			return falseMessage
		else:
			return dataContent
	else:
		return falseMessage

# get all GateList
def EP_getGateList():
	if stationId == []:
		return falseMessage
	else:
		for i in stationId:
			EP_getOneGateList(i)

# get ContractList by station_id
def EP_getOneContractList(station_id):
	method = 'et_common.contract.lists'
	if stationId == []:
		return falseMessage
	if station_id in stationId:
		biz_content = {'appid': client_id,'station_id': station_id}
		dataContent = EP_API_Base(method,biz_content)
		if type(dataContent) != dict and dataContent["status_code"] != 0:
			return falseMessage
		else:
			dataLists = dataContent["content"]["content"]["lists"]
			for i in dataLists:
				if "plate" in i.keys():
					global plate	
					plate.append(i["plate"])
					global plate_stationId
					plate_stationId[i["plate"]] = str(i["station_id"])
				else:
					return falseMessage
			return dataContent
	else:
		return falseMessage

# get all ContractList
def EP_getContractList():
	if stationId == []:
		return falseMessage
	else:
		for i in stationId:
			EP_getOneContractList(i)


# del ContractPlate by plate
def EP_delOneContractPlate(plate_num):
	method = 'et_common.contract.del'
	if plate == [] or plate_stationId == {}:
		return falseMessage
	if plate_num in plate:
		biz_content = {"appid": client_id,"station_id": plate_stationId[plate_num], "plate": plate_num}
		EP_API_Base(method,biz_content)
		return successMessage
	else:
		return falseMessage

# if necessary
# del all ContractPlate
# def Ep_delContractPlate():

# recover ContractPlate by plate
def EP_recoverOneContractPlate(plate_num):
	method = 'et_common.contract.recover'
	if plate == [] or plate_stationId == {}:
		return falseMessage
	if plate_num in plate:
		biz_content = {"appid": client_id,"station_id": plate_stationId[plate_num], "plate": plate_num}
		EP_API_Base(method,biz_content)
		return successMessage
	else:
		return falseMessage

# ask GateOpen
def EP_askGateOpen(plate_num):
	method = 'et_common.car.askopen'
	if plate == [] or plate_stationId == {}:
		return falseMessage
	if plate_num in plate:
		biz_content = {"appid": client_id,"station_id": plate_stationId[plate_num], "plate": plate_num}
		dataContent =  EP_API_Base(method,biz_content)
		if type(dataContent["content"]["content"]) == list:
			dataLists = dataContent["content"]["content"]
			global code_askopen
			code_askopen[plate_stationId[plate_num]] = dataLists[0]["code"]
		else:
			code_askopen[plate_stationId[plate_num]] = "12345"
			print(dataContent["content"]["message"].encode('utf-8'))
		return dataContent
	else:
		return falseMessage

# set GateOpen
def EP_setGateOpen(plate_num):
	method = 'et_common.car.open'
	if plate == [] or plate_stationId == {} or code_askopen == {}:
		return falseMessage
	if plate_num in plate:
		biz_content = {"appid": client_id,"station_id": plate_stationId[plate_num], "plate": plate_num, "code": code_askopen[plate_stationId[plate_num]]}
		dataContent =  EP_API_Base(method,biz_content)
		print(dataContent["content"]["message"].encode('utf-8'))
		return dataContent
	else:
		return falseMessage

# set InviteCar
def EP_setInviteCar(plate_num,clientId,starttime="2019-04-02 14:00:00",stoptime="2019-04-20 14:00:00"):
	method = 'et_common.authorize.bespeak'
	biz_content = {"appid": client_id,"station_id": plate_stationId[plate_num], "plate": plate_num, "starttime": starttime, "stoptime": stoptime, "client_id": clientId}
	dataContent =  EP_API_Base(method,biz_content)
	print dataContent["content"]["message"].encode('utf-8')
	return dataContent

# del InviteCar
def EP_delInviteCar(station_id,authorize_id = '1'):
	method = 'et_common.authorize.del'
	biz_content = {"appid": client_id,"station_id": station_id,"authorize_id": authorize_id}
	dataContent =  EP_API_Base(method,biz_content)
	print dataContent["content"]["message"].encode('utf-8')
	return dataContent

# get the list for Invite Car 
def EP_getInviteCarList(station_id):
	method = 'et_common.authorize.lists'
	if stationId == []:
		return falseMessage
	if station_id in stationId:
		biz_content = {'appid': client_id,'station_id': station_id}
		dataContent = EP_API_Base(method,biz_content)
		if type(dataContent) != dict and dataContent["status_code"] != 0:
			return falseMessage
		else:
			return dataContent
	else:
		return falseMessage

# get Car Image for arrived id and department id
def EP_getCarImage(station_id,id = '12',type = 'in'):
	method = 'et_common.input.images'
	biz_content = {"appid": client_id,"station_id": station_id,'type': type ,"id": id}
	dataContent =  EP_API_Base(method,biz_content)
	print dataContent["content"]["message"].encode('utf-8')
	return dataContent

# get the admin_auth to Open Gate
def EP_adminOpenGate(device_id,cmd = 'open'):
	method = 'et_common.device.openAndClose'
	biz_content = {"appid": client_id,"cmd": cmd ,"device_id": device_id}
	dataContent =  EP_API_Base(method,biz_content)
	print dataContent["content"]["message"].encode('utf-8')
	return dataContent

# gateContent = EP_API_Base('et_common.device.lists',{'appid': client_id,'station_id': str(2642)})
# print(len(gateContent["content"]["lists"]))

print("getStationList Return JSON Format Data:\n")
print EP_getStationList()

print('\n+++++++++++++++\n')

print("the list for stationId:\n")
print(stationId)

print('\n+++++++++++++++\n')

print("getAllGateList no Return:\n")
EP_getGateList()

print('\n+++++++++++++++\n')

print("getAllContractList no Return:\n")
EP_getContractList()

print('\n+++++++++++++++\n')

print("the list for plate:\n")
print(plate)

# print('\n+++++++++++++++\n')

#print(plate[0].encode('utf-8'))

print('\n+++++++++++++++\n')

print("the dict for plate : stationId:\n")
print(plate_stationId)

print('\n+++++++++++++++\n')

print("askGateOpen:\n")
EP_askGateOpen(plate[7])


print('\n+++++++++++++++\n')

print("setGateOpen:\n")
EP_setGateOpen(plate[7])

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