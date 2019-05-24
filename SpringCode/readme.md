
 * Author: Marin Cheng
 * Date: 2019/5/15 9:23
 * Content:接口说明文档
 

# 返回值说明
- 通用接口返回值
成功
```
ResponseData对象
    { 
        'code':true, 
        'message':'success', 
        'content':'从EP端接收回来的数据'
    }
```
失败
```
ResponseData对象
    { 
        'code':false, 
        'message':'fail', 
        'content':'从EP端接收回来的数据'
    }
```
# 接口说明

- 请求appId接口 getCode()
    + 必传的参数
        * 无
    + 可选参数
        * 无    
    + 成功结果
    {
      "code": true,
      "message": "success",
      "content": "{\"code\":0,\"message\":\"success\",\"content\":{\"code\":\"355a02614d81c74dccaad3c2eb165eee7584third\",\"app_id\":\"35cefb37_1a48_6fa4_2688_2577dcbcfb24\",\"scope\":\"third_party\",\"expires\":7200}}"
    }
    
- 请求秘钥接口 getAccessToken()
    + 必传的参数
        * 无
    + 可选参数
        * 无    
    + 成功结果
    {
      "code": true,
      "message": "success",
      "content": "{\"code\":0,\"message\":\"success\",\"content\":{\"code\":\"57a4f7f2a28cd794214e6cce92d48b251407third\",\"app_id\":\"fe594695_7684_9f51_ccd0_d431bb113512\",\"scope\":\"third_party\",\"expires\":7200}}"
    }

- 通用接口 baseApi(String method,String bizContent)
    + 必传的参数
        * method (类型 String)
        * bizContent (类型 String)
    + 可选参数
        * 无    
    + 成功结果
        * 根据method和bizContent参数不同，结果不同
        
- 停车场月卡规则查看接口 getContractRule(ContractRuleParam contractRuleParam)
    + 必传的参数
        ContractRuleParam对象，包含参数：
        * appid (类型 String)
        * station_id (类型 String)
    + 可选参数
        * 无    
    + 成功结果
    {
      "code": true,
      "message": "success",
      "content": "{\"code\":0,\"message\":\"success\",\"content\":[{\"rule_id\":7443,\"N1\":0}]}"
    }
    
- 停车场月卡查看接口 getContractRule(ContractRuleParam contractRuleParam)
    + 必传的参数
        ContractRuleParam对象，包含参数：
        * appid (类型 String)
        * station_id (类型 String)
    + 可选参数
        * 无    
    + 成功结果
    {
      "code": true,
      "message": "success",
      "content": "{\"code\":0,\"message\":\"success\",\"content\":[{\"rule_id\":7443,\"N1\":0}]}"
    }

- 根据stationId获取月卡接口 getContractByStationid(GetContractByStationid getContractByStationid)
    + 必传的参数
        GetContractByStationid对象，包含参数：
        * appid (类型 String)
        * station_id (类型 String)
    + 可选参数
        * 无    
    + 成功结果
    {
      "code": true,
      "message": "success",
      "content": "{\"code\":0,\"message\":\"success\",\"content\":{\"lists\":[{\"contract_id\":665786,\"station_id\":2641,\"station_name\":\"西溪美景\",\"plate\":\"粤B1013\",\"rule_id\":7443,\"rule_name\":\"新加坡月卡收费1\",\"time_begin\":\"2019-05-13 00:00:00\",\"time_end\":\"2019-05-13 00:00:00\"}]}}"
    }
    
- 月卡申请接口 getContractPlate(ContractApplyParam contractApplyParam)
    + 必传的参数
        ContractApplyParam对象，包含参数：
        * appid (类型 String)
        * station_id (类型 String)
        * plate (类型 String)
        
    + 可选参数
       * card_phone (类型 String)
       * apply_phone (类型 String) 
       * image1 (类型 String)
       * image2 (类型 String)
    + 成功结果
      
- 月卡申请同意接口 getContractAgree(ContractAgreeParam contractAgreeParam)
    + 必传的参数
        ContractAgreeParam对象，包含参数：
        * appid (类型 String)
        * station_id (类型 String)
        * apply_id (类型 String)
        * rule_id (类型 String)
        * begin_time (类型 String)
    + 可选参数
        * 无    
    + 成功结果

- 支付回调通知接口 getPaySuccess(PaySuccessParam paySuccessParam)
    + 必传的参数
        PaySuccessParam对象，包含参数：
        * amount (类型 String)
        * trade_no (类型 String)
        * pay_status (类型 String)
        * paytime (类型 String)
        * client_id (类型 String)
        * auth_app_id (类型 String)
        * ts (类型 String)
        * secret (类型 String)
    + 可选参数
        * third_tnum  (类型 String)  
    + 成功结果
    {
      "code": true,
      "message": "success",
      "content": "you pay successfully"
    }

- 月卡计费接口 getCostMonth(CostMonthParam costMonthParam)
    + 必传的参数
        CostMonthParam对象，包含参数：
        * contract_id (类型 String)
        * month_total (类型 String)
    + 可选参数
        * 无  
    + 成功结果
    {
      "code": true,
      "message": "success",
      "content": "{\"code\":0,\"message\":\"success\",\"content\":{\"total_amount\":\"0.2\",\"time_begin\":\"2019-04-01 00:00:00\",\"time_end\":\"2020-11-30 23:59:59\",\"coupon_amount\":0,\"coupon_lists\":[]}}"
    }
    
- 传参获取秘钥 getToken(String code,String scope,String appId)
    + 必传的参数
        * code (类型 String)
        * scope (类型 String)
        * appId (类型 String)
    + 可选参数
        * 无  
    + 成功结果
    {
      "code": true,
      "message": "success",
      "content": "{\"code\":0,\"message\":\"success\",\"content\":{\"access_token\":\"4c19fad15b41d8815c4102ff3c7ed78347456third\",\"expires_in\":7200,\"scope\":\"third_party\",\"token_type\":\"silent_auth\"}}"
    }

- 三步添加月卡接口 addContract(AddContractParam addContractParam)
    + 必传的参数
        AddContractParam对象，包含参数：
        * appid (类型 String)
        * station_id (类型 String)
        * plate (类型 String)
    + 可选参数
        * 无  
    + 成功结果

- 六步添加月卡接口 residentCarRegist(AddContractParam addContractParam)
    + 必传的参数
        AddContractParam，包含参数：
        * appid (类型 String)
        * station_id (类型 String)
        * plate (类型 String)
    + 可选参数
        * 无  
    + 成功结果
    
- 月卡缴费下单接口 getMonthorderThird(MonthorderThird monthorderThird)
    + 必传的参数
        MonthorderThird，包含参数：
        * appid (类型 String)
        * contract_id (类型 String)
        * month_total (类型 String)
        * total_amount (类型 String)
        * amount (类型 String)
        * mobile (类型 String)
    + 可选参数
        * source (类型 String)
        * body (类型 String)
        * attach (类型 String)  
    + 成功结果