#_*_ coding:utf-8_*_ 
# Copyright 2016-2019 Smart Gateway Pte. Ltd. All Rights Reserved.
#
# EP parking signature and token retrieving
# This file is given as an example to calculate the signature and retrieve access token
# from EP cloud server

# Author: Jimmy Li (2019, 4, 4)
# Mender: Jimmy Li (2019, 4, 5)
#	      Jimmy Li (2019, 4, 8)

from getSignToken import getToken
import constant,statusCode
import requests, time, json


__all__ = ['EP_getStationList' , 'EP_getGateList', 'EP_getContractList', 
'EP_delContractPlate', 'EP_recoverContractPlate', 'EP_askGateOpen',
'EP_setGateOpen', 'EP_setInviteCar', 'EP_delInviteCar', 'EP_getInviteCarList', 
'EP_getCarImage', 'EP_adminOpenGate' ]


publicUrl = constant.getConstant()['publicUrl']

clientId = constant.getConstant()['clientId']

timeStamp = str(int(time.time()))

accessToken = str(getToken())


def judToken(requestParameters):
	if 'token' not in requestParameters.keys():
		return statusCode.checkBaseCode('F','token not in reqestPara')
	requestParameters['token'] = str(getToken())
	r = requests.post(publicUrl, data=requestParameters)
	return statusCode.checkBaseCode('T',r.json())

# this is common api
def EP_API_Base(methodArg, bizContentArg):
	if type(methodArg) != str:
		return statusCode.checkBaseCode('F','methodArg is not str ')
	if type(bizContentArg) != dict:
		return statusCode.checkBaseCode('F','bizeContent is not dict ')
	requestParameters = {
	'app_id': clientId, 'method': methodArg, 
	'format': "json", 'charset': "utf-8", 
	'timestamp': timeStamp, 'token': accessToken, 
	'biz_content': json.dumps(bizContentArg) }
	r = requests.post(publicUrl, data=requestParameters)
	if r.json()['code'] != 0:
		if r.json()['code']  == 90000:
			return judToken(requestParameters)
		return statusCode.checkBaseCode('F',r.json())
	return statusCode.checkBaseCode('T',r.json())
	
# get StationList
def EP_getStationList(pageArg = '1', pagesizeArg = '20'):
	method = 'et_common.station.lists'
	bizContent = {
	'appid': clientId, 'page': pageArg, 
	'pagesize': pagesizeArg }
	data = EP_API_Base(method,bizContent)
	dataContent = data['statusBaseContent']
	if data["statusBaseCode"] == 0:
		return statusCode.checkSubCode('T',dataContent)
	return statusCode.checkSubCode('F',dataContent)

# get GateList by station_id
def EP_getGateList(stationIdArg, directionArg = 'in'):
	method = 'et_common.device.lists'
	if directionArg not in ['in','out']:
		return statusCode.checkSubCode('F','directionArg error')
	bizContent = {
	'appid': clientId, 'station_id': stationIdArg, 
	'dicretion': directionArg }
	data = EP_API_Base(method,bizContent)
	dataContent = data['statusBaseContent']
	if data["statusBaseCode"] == 0:
		return statusCode.checkSubCode('T',dataContent)
	return statusCode.checkSubCode('F',dataContent)

# get ContractList by station_id
def EP_getContractList(
	stationIdArg, plateArg = '#', 
	pageArg = '1', pagesizeArg = '20' ):
	method = 'et_common.contract.lists'
	bizContent = {
		'appid': clientId, 'station_id': stationIdArg, 
		'page': pageArg, 'pagesize': pagesizeArg }
	if plateArg != '#':
		bizContent['plate'] = plateArg
	data = EP_API_Base(method,bizContent)
	dataContent = data['statusBaseContent']
	if data["statusBaseCode"] == 0:
		return statusCode.checkSubCode('T',dataContent)
	return statusCode.checkSubCode('F',dataContent)
	


# del ContractPlate by plate
def EP_delContractPlate(stationIdArg, plateArg):
	method = 'et_common.contract.del'
	bizContent = {
	"appid": clientId, "station_id": stationIdArg, 
	"plate": plateArg }
	data = EP_API_Base(method,bizContent)
	dataContent = data['statusBaseContent']
	if data["statusBaseCode"] == 0:
		return statusCode.checkSubCode('T',dataContent)
	return statusCode.checkSubCode('F',dataContent)
	
# recover ContractPlate by plate
def EP_recoverContractPlate(stationIdArg, plateArg):
	method = 'et_common.contract.recover'
	bizContent = {
	"appid": clientId, "station_id": stationIdArg, 
	"plate": plateArg }
	data = EP_API_Base(method,bizContent)
	dataContent = data['statusBaseContent']
	if data["statusBaseCode"] == 0:
		return statusCode.checkSubCode('T',dataContent)
	return statusCode.checkSubCode('F',dataContent)

# ask GateOpen
def EP_askGateOpen(stationIdArg, plateArg, typeArg = 'in'):
	method = 'et_common.car.askopen'
	if typeArg not in ['in','out']:
		return statusCode.checkSubCode('F','typeArg error')
	bizContent = {
	"appid": clientId, "station_id": stationIdArg, 
	"plate": plateArg, "type": typeArg }
	data = EP_API_Base(method,bizContent)
	dataContent = data['statusBaseContent']
	if data["statusBaseCode"] == 0:
		return statusCode.checkSubCode('T',dataContent)
	return statusCode.checkSubCode('F',dataContent)

# set GateOpen
def EP_setGateOpen(stationIdArg, plateArg, code):
	method = 'et_common.car.open'
	bizContent = {
	"appid": clientId, "station_id": stationIdArg, 
	"plate": plateArg, "code": code }
	data = EP_API_Base(method,bizContent)
	dataContent = data['statusBaseContent']
	if data["statusBaseCode"] == 0:
		return statusCode.checkSubCode('T',dataContent)
	return statusCode.checkSubCode('F',dataContent)

# set InviteCar
def EP_setInviteCar(
	stationIdArg, starttimeArg, 
	stoptimeArg, clientIdArg, plateArg):
	method = 'et_common.authorize.bespeak'
	# 这里少了时间格式验证，以后补上
	bizContent = {
	"appid": clientId, "station_id": stationIdArg, 
	"plate": plateArg, "starttime": starttimeArg , 
	"stoptime": stoptimeArg, "client_id": clientIdArg }
	data = EP_API_Base(method,bizContent)
	dataContent = data['statusBaseContent']
	if data["statusBaseCode"] == 0:
		return statusCode.checkSubCode('T',dataContent)
	return statusCode.checkSubCode('F',dataContent)

# del InviteCar
def EP_delInviteCar(stationIdArg, authorizeIdArg):
	method = 'et_common.authorize.del'
	bizContent = {"appid": clientId,"station_id": stationIdArg,"authorize_id": authorizeIdArg}
	data = EP_API_Base(method, bizContent)
	dataContent = data['statusBaseContent']
	if data["statusBaseCode"] == 0:
		return statusCode.checkSubCode('T',dataContent)
	return statusCode.checkSubCode('F',dataContent)

# get the list for Invite Car 
def EP_getInviteCarList(
	stationIdArg, plateArg = '#', 
	pageArg = '1', pagesizeArg = '20' ):
	method = 'et_common.authorize.lists'
	bizContent = {
		'appid': clientId, 'station_id': stationIdArg, 
		'page': pageArg, 'pagesize': pagesizeArg }
	if plateArg != '#':
		bizContent['plate'] = plateArg
	data = EP_API_Base(method,bizContent)
	dataContent = data['statusBaseContent']
	if data["statusBaseCode"] == 0:
		return statusCode.checkSubCode('T',dataContent)
	return statusCode.checkSubCode('F',dataContent)
	return statusCode.checkSubCode('F',dataContent['statusBaseContent'])

# get Car Image for arrived id and department id
def EP_getCarImage(stationIdArg, typeArg, idArg, 
	dateArg = str(time.strftime('%Y%m',time.localtime(time.time()))) ):
	method = 'et_common.inout.images'
	if typeArg not in ['in','out']:
		return statusCode.checkSubCode('F','typeArg error')
	if type(dateArg) != str and len(dateArg) != 6:
		return statusCode.checkSubCode('F','dateArg error')
	bizContent = {
	"appid": clientId, "station_id": stationIdArg,
	'type': typeArg, "id": idArg, 'date': dateArg }
	data = EP_API_Base(method,bizContent)
	dataContent = data['statusBaseContent']
	if data["statusBaseCode"] == 0:
		return statusCode.checkSubCode('T',dataContent)
	return statusCode.checkSubCode('F',dataContent)

# get the admin_auth to Open Gate
def EP_adminOpenGate(deviceIdArg, cmdArg):
	method = 'et_common.device.openAndClose'
	if cmdArg not in ['open','close']:
		return statusCode.checkSubCode('F','cmdArg error')
	bizContent = {"appid": clientId,"cmd": cmdArg ,"device_id": deviceIdArg}
	data = EP_API_Base(method,bizContent)
	dataContent = data['statusBaseContent']
	if data["statusBaseCode"] == 0:
		return statusCode.checkSubCode('T',dataContent)
	return statusCode.checkSubCode('F',dataContent)

def EP_TBD(departureIdArg, arrivalIdArg, deviceIdArg,
	timeArg, memberArg, carIdArg, plateArg, eventArg, 
	stationIdArg, stationNameArg):
	method = '#'
	bizContent = {
	'departure_id': departureIdArg, 'arrival_id':arrivalIdArg,
	'device_id': deviceIdArg, 'time': timeArg, 'member': memberArg,
	'car_id': carIdArg, 'plate': plateArg, 'event': eventArg,
	'station_id': stationIdArg, 'station_name': stationNameArg
	}
	data = EP_API_Base(method,bizContent)
	dataContent = data['statusBaseContent']
	if data["statusBaseCode"] == 0:
		return statusCode.checkSubCode('T',dataContent)
	return statusCode.checkSubCode('F',dataContent)

	
def selfPrint():
	print("getStationList:\n")
	print EP_getStationList()
	print('\n+++++++++++++++\n')
	print("getGateList:\n")
	print EP_getGateList('2642')
	print('\n+++++++++++++++\n')
	print("getContractList:\n")
	print EP_getContractList('2642','粤B10007')
	print('\n+++++++++++++++\n')
	# print EP_delContractPlate('2642', '粤B9999X')['statusSubContent']
	print("askGateOpen:\n")
	print EP_askGateOpen('2642','粤V12345')
	print('\n+++++++++++++++\n')
	print("setGateOpen:\n")
	print EP_setGateOpen('2642','粤V12345','12345')
	print('\n+++++++++++++++\n')
	print("getInviteCarList:\n")
	print EP_getInviteCarList('2642')
	print('\n+++++++++++++++\n')
	print("setInviteCar:\n")
	print EP_setInviteCar('2642',"2019-04-11 14:00:00","2019-04-16 14:00:00",'1','粤V12352')
	print('\n+++++++++++++++\n')
	print("delInviteCar\n")
	print EP_delInviteCar(264,141)
	print('\n+++++++++++++++\n')
	print("getCarImage:\n")
	print EP_getCarImage('2642','in','1')
	print('\n+++++++++++++++\n')
	print("adminOpenGate:\n")
	print EP_adminOpenGate('3157','open')

if __name__ == '__main__':
	selfPrint()
	