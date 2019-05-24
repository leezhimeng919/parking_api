# LifeUp LPR 与EP 停车API 接口系统集成开发接口说明
- 模块名LifeUpController.py

- LifeUp 停车场工作状态监控，报警
    + 接口名：checkOutWorkingStatus(stationIdArg)
    + 输入：停车场ID(str)
    + 输出
        * True(bool)表示在线
        * False(bool)表示掉线
- 月卡用户车牌列表显示
    + 接口名：getContractPlateList(stationIdArg)
    + 输入：停车场ID(str)
    + 输出：一个存有该停车场所有车牌号列表
- 月卡用户车牌添加，并显示验证
- 月卡用户车牌删除，并显示验证
    + 接口名：delOneContractPlate(stationIdArg, plateArg)
    + 输入：停车场ID(str)，车牌号(str)
    + 输出
        * True(bool)表示删除成功
        * False(bool)表示删除失败
- 月卡用户车牌重新启用，并显示验证
    + 接口名：recoverOneContractPlate(stationIdArg, plateArg)
    + 输入：停车场ID(str)，车牌号(str)
    + 输出：
        * True(bool)表示恢复成功
        * False(bool)表示恢复失败
- 预约访客车牌列表显示
    + 接口名：getInviteCarPlateList(stationIdArg)
    + 输入：停车场ID(str)
    + 输出：一个存有该停车场预约的所有车牌号列表
- 预约访客车牌添加，并显示验证
    + 接口名：setInviteCarPlate(stationIdArg, starttimeArg, stoptimeArg, clientIdArg, plateArg)
    + 输入：停车场ID(str)，开始时间(str)，结束时间(str)，客户ID(str)，车牌号(str)
    + 输出：
        * True(bool)表示添加成功
        * False(bool)表示添加失败
- 预约放开车牌删除，并显示验证
    + 接口名:delInviteCarPlate(stationIdArg, plateArg)
    + 输入：停车场ID(str)，车牌号(str)
    + 输出
        * True(bool)表示删除成功
        * False(bool)表示删除失败
- 紧急道闸开启
    + 接口名：setGateOpen(stationIdArg, plateArg, [typeArg = 'in'])
    + 输入：停车场ID(str)，车牌号(str)，进场出场(str,默认值'in')
    + 输出
        * True(bool)表示开启成功
        * False(bool)表示开启失败
- 管理员开道闸
    + 接口名：adminOpenGate(deviceIdArg, cmdArg)
    + 输入：设备ID(str), 管理员命令(str,['open' or 'close'])
    + 输出：
        * True(bool)表示开启成功
        * False(bool)表示开启失败
- EP推送消息处理
    + 待定
- LifeUp 查询进出场车牌图片（根据推送事件id）
    + 接口名：getCarImage(stationIdArg, typeArg, idArg, dateArg = str(time.strftime('%Y%m',time.localtime(time.time()))) )
    + 输入：停车场ID(str)，进场出场(str)，接口方提供ID(str)，日期(str,'201903',默认值当前年月)
    + 输出：
        * True(bool)表示获取成功
        * False(bool)表示获取失败