#_*_ coding:utf-8_*_ 
# Copyright 2016-2019 Smart Gateway Pte. Ltd. All Rights Reserved.
#
# EP parking signature and token retrieving
# This file is given as an example to calculate the signature and retrieve access token
# from EP cloud server

# Author: Jimmy Li (2019, 4, 8)
# mender: Jimmy Li (2018, 4, 10)

import EP_coreAPILib
import constant,statusCode
import requests, time, json


def checkOutWorkingStatus(stationIdArg, pageArg = '1', pagesizeArg = '20'):
	# call EP_coreAPILib.EP_getStationList to get station Info
	data = EP_coreAPILib.EP_getStationList(pageArg = '1', pagesizeArg = '20')
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

def getContractPlateList(stationIdArg, pageArg = '1', pagesizeArg = '20' ):
	data = EP_coreAPILib.EP_getContractList(stationIdArg, pageArg = '1', pagesizeArg = '20')
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
	preDelList = getContractPlateList(stationIdArg)
	if plateArg in preDelList:
		return False
	EP_coreAPILib.EP_recoverContractPlate(stationIdArg, plateArg)
	postDelList = getContractPlateList(stationIdArg)
	print preDelList
	print postDelList
	if plateArg in postDelList:
		return True
	return False



