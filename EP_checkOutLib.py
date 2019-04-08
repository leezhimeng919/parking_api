#_*_ coding:utf-8_*_ 
# Copyright 2016-2019 Smart Gateway Pte. Ltd. All Rights Reserved.
#
# EP parking signature and token retrieving
# This file is given as an example to calculate the signature and retrieve access token
# from EP cloud server

# Author: Jimmy Li (2019, 4, 8)
import EP_coreAPILib
import constant,statusCode
import requests, time, json


# 需求：LifeUp 停车场工作状态监控，报警

# 目标：将停车场ID和对应的alive参数传给上层

# 实现： 1.调用EP_coreAPILib模块的EP_getStationList接口，获取停车场信息
#		2.遍历接口信息中的Lists以获取station_id和alive的哈希表
#		3.将上述哈希表当做statusSubContent返回



def checkOutWorkStatus(pageArg = '1', pagesizeArg = '20'):
	# 调用EP_coreAPILib模块的EP_getStationList接口，获取停车场信息
	data = EP_coreAPILib.EP_getStationList(pageArg = '1', pagesizeArg = '20')
	if data['statusSubContent']['content'] == '':
		return statusCode.checkSubCode('F','api is error')
	stationLists = data['statusSubContent']['content']['lists']

	if stationLists == []:
		return statusCode.checkSubCode('F','the list of station is empty')
	for i in stationLists:
		if 'alive' in stationLists.keys() and 'station_id' in stationLists.keys():
			# 创建一个station_id和alive的哈希表
			dataContent = {}
			dataContent[i['station_id']] = i['alive']
	# 将上述哈希表当做statusSubContent返回
	return  statusCode.checkSubCode('F',dataContent)


print checkOutWorkStatus()
# 输出结果
# {
# 	'statusBaseMessage': 'success', 
# 	'statusBaseCode': 0,
# 	'statusBaseContent': 
# 		{
# 			10:'false',
# 			11:'false'
# 		}
# }
	

