#_*_ coding:utf-8_*_ 
# Copyright 2016-2019 Smart Gateway Pte. Ltd. All Rights Reserved.
#
# EP parking signature and token retrieving
# This file is given as an example to calculate the signature and retrieve access token
# from EP cloud server

# Author: Jimmy Li (2019, 4, 8)
# mender: Jimmy Li (2018, 4, 9)
# mender: Jimmy Li (2018, 4, 10)
# mender: Jimmy Li (2018, 4, 11)
# mender: Jimmy Li (2018, 4, 12)

import EP_coreAPILib
import constant,statusCode
import requests, time, json


authorizedIdHash = {}

def checkOutWorkingStatus(stationIdArg):
	# call EP_coreAPILib.EP_getStationList to get station Info
	data = EP_coreAPILib.EP_getStationList()
	if 'content' not in data['statusSubContent']:
		return False
	stationLists = data['statusSubContent']['content']['lists']
	dataContent = {}
	for i in stationLists:
		if 'alive' not in i.keys() or 'station_id' not in i.keys():
			continue
		# create a hashmap with station_id : alive
		dataContent[i['station_id']] = i['alive']
	if stationIdArg not in dataContent.keys():
		return False
	return dataContent[stationIdArg]

def getContractPlateList(stationIdArg):
	data = EP_coreAPILib.EP_getContractList(stationIdArg)
	if 'content' not in data['statusSubContent']:
		return []
	dataLists = data['statusSubContent']['content']['lists']
	plateList = []
	for i in dataLists:
		if 'plate' not in i.keys():
			continue
		plateList.append(i['plate'].encode('utf-8'))
	return plateList

def delOneContractPlate(stationIdArg, plateArg):
	preDelList = getContractPlateList(stationIdArg)
	if plateArg not in preDelList:
		return False
	EP_coreAPILib.EP_delContractPlate(stationIdArg, plateArg)
	postDelList = getContractPlateList(stationIdArg)
	if plateArg not in postDelList:
		return True
	return False

def recoverOneContractPlate(stationIdArg, plateArg):
	preRecoverList = getContractPlateList(stationIdArg)
	if plateArg in preRecoverList:
		return False
	EP_coreAPILib.EP_recoverContractPlate(stationIdArg, plateArg)
	postRecoverList = getContractPlateList(stationIdArg)

	if plateArg in postRecoverList:
		return True
	return False

def getInviteCarPlateList(stationIdArg):
	data = EP_coreAPILib.EP_getInviteCarList(stationIdArg)
	if 'content' not in data['statusSubContent']:
		return []
	dataLists = data['statusSubContent']['content']['lists']
	plateList = []
	for i in dataLists:
		if 'plate' not in i.keys() and 'authorize_id' not in i.keys():
			continue
		plateList.append(i['plate'].encode('utf-8'))
	return plateList

def getAuthorizeIdByPlate(stationIdArg,plateArg):
	data = EP_coreAPILib.EP_getInviteCarList(stationIdArg)
	if 'content' not in data['statusSubContent']:
		return None
	dataLists = data['statusSubContent']['content']['lists']
	plateAuthHash = {}
	for i in dataLists:
		if 'authorize_id' not in i.keys():
			continue
		plateAuthHash[i['plate'].encode('utf-8')] = i['authorize_id']
	plateList = getInviteCarPlateList(stationIdArg)
	if plateArg in plateList:
		return plateAuthHash[plateArg]
	return None

def setInviteCarPlate(
	stationIdArg, starttimeArg, 
	stoptimeArg, clientIdArg, plateArg):
	preSetList = getInviteCarPlateList(stationIdArg)
	if plateArg in preSetList:
		return False
	data = EP_coreAPILib.EP_setInviteCar(stationIdArg, starttimeArg, 
	stoptimeArg, clientIdArg, plateArg)
	postSetList = getInviteCarPlateList(stationIdArg)
	if plateArg in postSetList:
		return True
	return False

def delInviteCarPlate(stationIdArg, plateArg):
	preDelList = getInviteCarPlateList(stationIdArg)
	if plateArg not in preDelList:
		return False
	authorizeIdArg = getAuthorizeIdByPlate(stationIdArg, plateArg)
	data = EP_coreAPILib.EP_delInviteCar(stationIdArg, authorizeIdArg)
	# print data['statusSubContent']['errorBaseMessage'].encode('utf-8')
	postDelList = getInviteCarPlateList(stationIdArg)
	if plateArg not in postDelList:
		return True
	return False

# 目标：紧急道闸开启
# 实现：通过getGateList接口得到的status信息(Y/N)来

# def setGateOpen(stationIdArg, plateArg):
# 	dataGate = EP_coreAPILib.EP_getGateList(stationIdArg)
# 	if 'content' not in dataGate['statusSubContent']:
# 		return False
# 	dataLists = dataGate['statusSubContent']['content']['lists']
# 	gateStatusHash = {}
# 	for i in dataLists:
# 		gateStatusHash[i['station_id']] = [i['direction'], i['status']]
# 	typeArg = gateStatusHash[stationIdArg][0]
# 	print typeArg
# 	print gateStatusHash
# 	data = EP_coreAPILib.EP_askGateOpen(stationIdArg, plateArg, typeArg)
# 	if 'content' not in data['statusSubContent']:
# 		# return data['statusSubContent']['errorBaseMessage'].encode('utf-8')
# 		return False
# 	gateCode = data['statusSubContent']['content']['code']
# 	dataContent = EP_coreAPILib.EP_setGateOpen(stationIdArg, plateArg, gateCode)
# 	if gateStatusHash[stationIdArg][1] != 'Y':
# 		return False
# 	return True

def setGateOpen(stationIdArg, plateArg, typeArg = 'in'):
	data = EP_coreAPILib.EP_askGateOpen(stationIdArg, plateArg, typeArg)
	if 'content' not in data['statusSubContent']:
		# return data['statusSubContent']['errorBaseMessage'].encode('utf-8')
		return False
	gateCode = data['statusSubContent']['content']['code']
	dataContent = EP_coreAPILib.EP_setGateOpen(stationIdArg, plateArg, gateCode)
	if 'errorBaseMessage'  in data['statusSubContent']:
		return False
	return True


def adminOpenGate(deviceIdArg, cmdArg):
	data = EP_coreAPILib.EP_adminOpenGate(deviceIdArg, cmdArg)
	if 'errorBaseMessage' in data['statusSubContent']:
		# return data['statusSubContent']['errorBaseMessage'].encode('utf-8')
		return False
	return True

def TBD(departureIdArg, arrivalIdArg, deviceIdArg,
	timeArg, memberArg, carIdArg, plateArg, eventArg, 
	stationIdArg, stationNameArg):
	data = EP_coreAPILib.EP_TBD(deviceIdArg, cmdArg)
	if 'errorBaseMessage' in data['statusSubContent']:
		# return data['statusSubContent']['errorBaseMessage'].encode('utf-8')
		return False
	return True

def getCarImage(stationIdArg, typeArg, idArg, 
	dateArg = str(time.strftime('%Y%m',time.localtime(time.time()))) ):
	data = EP_coreAPILib.etCarImage(stationIdArg, typeArg, idArg, 
	dateArg = str(time.strftime('%Y%m',time.localtime(time.time()))) )
	if 'errorBaseMessage' in data['statusSubContent']:
		# return data['statusSubContent']['errorBaseMessage'].encode('utf-8')
		return False
	return True