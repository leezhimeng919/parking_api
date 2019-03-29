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
datat = json.loads(getToken()["content"])

access_token = datat["content"]["access_token"]



# this is common api
def EP_API_Base(method=None,biz_content=None,url=endpoint_url,timestamp=str(ts),token=str(access_token),api_id = client_id ,format="json",charset="utf-8"):

	request_parameters = {'app_id': api_id, 'method': method, 'format': format, 'charset': charset, 'timestamp': timestamp, 'token': token, 'biz_content': json.dumps((biz_content))}

	r = requests.post(url, data=request_parameters)
	try:
		return r.json()
	except:
		return {"code": 10001, "message": "False"}

# get StationList
def EP_getStationList():
	method = 'et_common.station.lists'
	biz_content = {'appid': client_id}
	dataContent = EP_API_Base(method,biz_content)
	dataLists = (dataContent["content"]["lists"])
	# get station id
	for i in dataLists:
		if "station_id" in i.keys():
			global stationId	
			stationId.append(i["station_id"])
		else:
			print('no station_id in dataLists')	
	print(json.dumps(dataContent))
	return dataContent

# get GateList by station_id
def EP_getOneGateList(station_id):
	method = 'et_common.device.lists'
	if station_id in stationId:
		biz_content = {'appid': client_id,'station_id': str(station_id)}
		dataContent = EP_API_Base(method,biz_content)
		print(json.dumps(dataContent))
		return(dataContent)
	else:
		print('input station_id not exist')

# get all GateList
def EP_getGateList():
	if len(stationId) > 1: 
		for i in stationId:
			EP_getOneGateList(i)
	else:
		print('no station ID')

# get ContractList by station_id
def EP_getOneContractList(station_id):
	method = 'et_common.contract.lists'
	if station_id in stationId:
		biz_content = {'appid': client_id,'station_id': str(station_id)}
		dataContent = EP_API_Base(method,biz_content)
		dataLists = dataContent["content"]["lists"]
		for i in dataLists:
			if "plate" in i.keys():
				global plate	
				plate.append(i["plate"])
				global plate_stationId
				plate_stationId[i["plate"]] = str(i["station_id"])
			else:
				print('no plate in dataLists')	
		print(dataContent["content"]["lists"])
		return(dataContent)
	else:
		print('input station_id not exist')

# get all ContractList
def EP_getContractList():
	if len(stationId) > 1: 
		for i in stationId:
			EP_getOneContractList(i)
	else:
		print('no station ID')

# del ContractPlate by plate
def EP_delOneContractPlate(plate_num):
	method = 'et_common.contract.del'
	if plate_num in plate:
		biz_content = {"appid": client_id,"station_id": plate_stationId[plate_num], "plate": plate_num}
		EP_API_Base(method,biz_content)
		print('successfully delete!!')
	else:
		print('input plate_num not exist')

# if necessary
# del all ContractPlate
# def Ep_delContractPlate():

# recover ContractPlate by plate
def EP_recoverOneContractPlate(plate_num):
	method = 'et_common.contract.recover'
	if plate_num in plate:
		biz_content = {"appid": client_id,"station_id": plate_stationId[plate_num], "plate": plate_num}
		EP_API_Base(method,biz_content)
		print('successfully delete!!')
	else:
		print('input plate_num not exist')



# gateContent = EP_API_Base('et_common.device.lists',{'appid': client_id,'station_id': str(2642)})
# print(len(gateContent["content"]["lists"]))


print("getStationList Return JSON Format Data:\n")
EP_getStationList()

print('\n+++++++++++++++\n')

print("the list for stationId:\n")
print(stationId)

print('\n+++++++++++++++\n')

print("getAllGateList Return JSON Format Data:\n")
EP_getGateList()

print('\n+++++++++++++++\n')

print("getAllGateList Return JSON Format Data:\n")
EP_getContractList()

print('\n+++++++++++++++\n')

print("the list for plate:\n")
print(plate)

print('\n+++++++++++++++\n')

print(plate[0].encode('utf-8'))

print('\n+++++++++++++++\n')

print("the dict for plate : stationId:\n")
print(plate_stationId)



