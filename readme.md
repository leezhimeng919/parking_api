# 返回值说明
- 通用接口返回值
成功
: 
    { 
        'statusBaseCode':'0', 
        'statusBaseMessage':'success', 
        'statusBaseContent':'接收的数据'
    }
失败
:
  
    {
        'statusBaseCode' : 1, 
        'statusBaseMessage' : 'error', 
        'statusBaseContent': 
            {
                'errorBaseCode': content['code'] ,
                'errorBaseMessage':content['message'] 
            }

    }




- 其他子接口返回值
成功
:
     {
        'statusSubCode': '0',
        'statusSubMessage': 'success', 
        'statusSubContent': '接收的数据'
    }

失败
: 
    {
        'statusSubCode':'1', 
        'statusSubMessage':'error', 
        'statusSubContent':
            {
                'errorBaseCode': content['code'] , 
                'errorBaseMessage':content['message'] 
            }
    }


# 接口说明

- 通用EP停车场接口调用 EP_API_Base(methodArg, bizContentArg)
    + 必传的参数
        * 第一个参数 method 
            - 类型 str
        * 第二个参数 bizContentArg 
            - 类型 dict
    + 可选的参数
        * 无

- 停车场信息查询接口 EP_getStationList([pageArg = '1', pagesizeArg = '20'])  
    + 必传的参数
        * 无
    + 可选参数
        * 第一个参数 pageArg 
            - 类型 str
            - 默认值 '1' 
        * 第二个参数 pagesizeArg
            - 类型 str
            - 默认值 '20'

   
- 道闸信息查询 EP_getGateList(stationIdArg [,directionArg = 'in'])
    + 必传的参数
        * 第一个参数 stationIdArg
            - 类型 str
    + 可选参数
        * 第二个参数 directionArg
            - 类型 str
            - 默认值 'in'
            - 可选值 ['in','out']

- 月卡信息查询 EP_getContractList(stationIdArg [, plateArg = '#',pageArg = '1', pagesizeArg = '20']) 
    + 必传的参数
        * 第一个参数 stationIdArg
            - 类型 str
    + 可选参数
        * 第二个参数 plateArg
            - 类型 str
            - 默认值 '#'
        * 第三个参数 pageArg 
            - 类型 str
            - 默认值 '1' 
        * 第四个参数 pagesizeArg
            - 类型 str
            - 默认值 '20'

- 月卡删除 EP_delContractPlate(stationIdArg, plateArg)  
    + 必传的参数
        * 第一个参数 stationIdArg
            - 类型 str
        * 第二个参数 plateArg
            - 类型 str
    + 可选参数
        * 无
- 月卡启用 EP_recoverContractPlate(stationIdArg, plateArg)  
     + 必传的参数
        * 第一个参数 stationIdArg
            - 类型 str
        * 第二个参数 plateArg
            - 类型 str
    + 可选参数
        * 无
- 下发道闸码 EP_askGateOpen(stationIdArg, plateArg [, typeArg = 'in'])  
    + 必传的参数
        * 第一个参数 stationIdArg
            - 类型 str
        * 第二个参数 plateArg
            - 类型 str
    + 可选参数
        * 第三个参数 typeArg
            - 类型 str
            - 默认值 'in'
            - 可选值 ['in','out']

- 紧急开闸 EP_setGateOpen(stationIdArg, plateArg, code)   
    + 必传的参数
        * 第一个参数 stationIdArg
            - 类型 str
        * 第二个参数 plateArg
            - 类型 str
        * 第三个参数 code
            - 类型 str
    + 可选参数
        * 无
- 预约进场 EP_setInviteCar(stationIdArg, starttimeArg, stoptimeArg, clientIdArg, plateArg)  
    + 必传的参数
        * 第一个参数 stationIdArg
            - 类型 str
        * 第二个参数 starttimeArg
            - 类型 str
            - 格式 Y-m-d H:i:s
        * 第三个参数 stoptimeArg
            - 类型 str
            - 格式 Y-m-d H:i:s
        * 第四个参数 clientIdArg
            - 类型 str
        * 第五个参数 plateArg
            - 类型 str
    + 可选参数
        * 无
- 删除预约进场 EP_delInviteCar(stationIdArg, authorizeIdArg)    
    + 必传的参数
        * 第一个参数 stationIdArg
            - 类型 str
        * 第二个参数 authorizeIdArg
            - 类型 str
    + 可选参数
        * 无

- 预约进场查看 EP_getInviteCarList(stationIdArg, [plateArg = '#', pageArg = '1', pagesizeArg = '20' ])   
    + 必传的参数
        * 第一个参数 stationIdArg
            - 类型 str
    + 可选参数
        * 第二个参数 plateArg
            - 类型 str
            - 默认值 '#'
        * 第三个参数 pageArg 
            - 类型 str
            - 默认值 '1' 
        * 第四个参数 pagesizeArg
            - 类型 str
            - 默认值 '20'



- 查询进出场图片 EP_getCarImage(stationIdArg, typeArg, idArg [, dateArg = str(time.strftime('%Y%m',time.localtime(time.time()))) ])    
    + 必传的参数
        * 第一个参数 stationIdArg
            - 类型 str
        * 第二个参数 typeArg
            - 类型 str
            - 可选值 ['in','out']
        * 第三个参数 idArg
            - 类型 str
    + 可选参数
        * 第四个参数 dateArg
            - 类型 str
            - 格式 如'201903'
            - 默认值 当前年月

- 管理员开闸 EP_adminOpenGate(deviceIdArg, cmdArg)
    + 必传的参数
        * 第一个参数 deviceIdArg
            - 类型 str
        * 第二个参数 cmdArg
            - 类型 str
            - 可选值 ['open','close']
    + 可选参数

- 进出场消息推送接口 EP_TBD(departureIdArg, arrivalIdArg, deviceIdArg,
    timeArg, memberArg, carIdArg, plateArg, eventArg, 
    stationIdArg, stationNameArg)


# 模块说明
- constant.py
    + 说明：存放所有可变参数，如需改动只需修改此模块即可
    + 开放函数：getConstant
    + 使用方式：
    ` from constant import getConstant`

- statusCode.py
    + 说明：接口开发测试所用的添加状态头的模块
    + 开放函数：checkBaseCode、checkSubCode
    + 使用方式：
    `from statusCode import checkCode checkSubCode`

- getSignToken.py
    + 说明：获取access_token的模块
    + 开放函数：getToken
    + 使用方法
    `from getSignToken import getToken`

- EP_coreAPILib.py
    + 说明：主接口通道
    + 开放函数： all

#添加月卡接口说明
- 文件名：EP_addContractPlate.py
- 月卡申请接口EP_applyContractPlate(stationIdArg, plateArg)
     + 必传的参数
        * 第一个参数 stationIdArg
            - 类型 str
        * 第二个参数plateArg
            - 类型 str


- 停车场月卡规则查看EP_checkContractRule(stationIdArg)
    + 必传的参数stationIdArg
        * 参数 stationIdArg
            - 类型str


- 月卡申请同意接口EP_getContractApproval(stationIdArg,applyIdArg,ruleIdArg,beginTimeArg)
    + 必传的参数
        * 第一个参数 stationIdArg
            - 类型str
            - 停车场id
        * 第二个参数 applyIdArg
            - 类型str
            - 月卡申请记录id
        * 第三个参数 ruleIdArg
            - 类型str
            - 月卡收费规则id
        * 第四个参数 beginTimeArg，
            - 类型str
            - 开始时间
            - 格式：2019-03-22 11:52:28
            - 默认值当前时间


- 月卡计费接口EP_monthlyContractCost(contractIdArg,monthTotalArg)
    + 必传的参数
        * 第一个参数为contractIdArg
            - 类型str
            - 月卡申请记录id
        * 第二个参数为monthTotalArg
            - 类型str
            - 月卡缴费月数


- 月卡缴费下单EP_monthlyThridPartyPay(contractIdArg,monthTotalArg,stationIdArg,totalAmountArg,amountArg,mobileArg,sourceArg)
    + 必传的参数
        * 第一个参数 contractIdArg
            - 类型str
            - 月卡申请记录id
        * 第二个参数 monthTotalArg
            - 类型str
            - 月卡缴费月数
        * 第三个参数 stationIdArg
            - 类型str
            - 停车场id
        * 第五个参数 amountArg
            - 类型str
            - 实付金额，单位为分
        * 第六个参数 mobileArg
            - 类型str
            - 缴费用户手机号
        * 第七个参数 sourceArg
            - 类型str
            - 来源：这里填写 SINGAPORE
    + 非必传参数
        * 第四个参数 totalAmountArg
            - 类型str
            - 订单总金额，单位为分，可与实付金额一致


- 支付回调通知EP_paySuccess(amountArg,thirdTnumArg,tradeNoArg,payStatusArg)
    + 必传的参数
        * 第一个参数 amountArg
            - 类型str
            - 订单总金额，单位为元订单总金额，单位为元
        * 第三个参数 tradeNoArg
            - 类型str
            - EP停车订单号
        * 第四个参数 payStatusArg
            - 类型str
            - 支付状态，固定填SUCCESS
    + 非必传的参数
        * 第二个参数 thirdTnumArg
            - 类型str
            - 第三方订单号


- 根据停车场id获取月卡列表EP_getContractByStationid(stationIdArg)
    + 必传的参数
        * 第一个参数 amountArg
            - 类型str
            - 订单总金额，单位为元订单总金额，单位为元


- 添加月卡六个流程接口Lifeup_residentCarRegist(stationIdArg,plateArg)
    + 必传的参数
        * 第一个参数 stationIdArg
            - 类型str
            - 停车场id
        * 第二个参数 plateArg
            - 类型str
            - 车牌号


- 添加月卡三个接口流程EP_addContract(stationIdArg,plateArg)
    + 必传的参数
        * 第一个参数 stationIdArg
            - 类型str
            - 停车场id
        * 第二个参数 plateArg
            - 类型str
            - 车牌号