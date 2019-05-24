package com.eclab.eparking.service;

import com.alibaba.fastjson.JSON;
import com.alibaba.fastjson.JSONArray;
import com.alibaba.fastjson.JSONObject;
import com.eclab.eparking.models.*;
import com.eclab.eparking.utils.GetSignToken;
import com.fasterxml.jackson.databind.ObjectMapper;
import io.swagger.annotations.ApiOperation;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpEntity;
import org.springframework.http.HttpHeaders;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Service;
import org.springframework.util.LinkedMultiValueMap;
import org.springframework.util.MultiValueMap;
import org.springframework.web.bind.annotation.ExceptionHandler;
import org.springframework.web.client.HttpClientErrorException;
import org.springframework.web.client.RestClientResponseException;
import org.springframework.web.client.RestTemplate;

import java.io.IOException;
import java.util.List;

@Service
@Slf4j
public class EParkingService {

    @Autowired
    private RestTemplate restTemplate;

    public ResponseData getCode(){
        String clientId = Contants.clientId;
        String signature = GetSignToken.getToken();
        String apiURL = Contants.baseUrl + Contants.urlGetCode;

        //创建请求头
        HttpHeaders headers = new HttpHeaders();
        MultiValueMap<String, String> map= new LinkedMultiValueMap<>();
        headers.setContentType(MediaType.APPLICATION_FORM_URLENCODED);
        map.add("client_id", clientId);
        map.add("signature",signature);
        map.add("ts",Contants.timeStamp);
        HttpEntity<MultiValueMap<String, String>> requestParams = new HttpEntity<>(map, headers);
        ResponseEntity<String> response = restTemplate.postForEntity(apiURL,requestParams,String.class);
        String result =response.getBody();
        JSONObject jsStr = JSONObject.parseObject(result);
        String code = jsStr.getString("code");
        log.info("jsStr:{}",jsStr.getString("code"));

        if(Integer.parseInt(code)!= 0){
            ResponseData responseData = new ResponseData(false,"error",result);
            return responseData;
        }
        ResponseData responseData = new ResponseData(true,"success",result);
        log.info(responseData.getContent());
        return responseData;
    }

    public ResponseData getAccessToken(){
        ResponseData rd = getCode();
        if(rd.getCode() != true){
            ResponseData responseData = new ResponseData(false,"error in getCode",rd.getContent());
            return responseData;
        }
        JSONObject content = JSONObject.parseObject(rd.getContent());
        JSONObject params = JSONObject.parseObject(content.getString("content"));
        log.info("content:{}",params);
        String code = params.getString("code");
        String scope = params.getString("scope");
        String appId = params.getString("app_id");
        return getToken(code,scope,appId);
    }


    public ResponseData getToken(String code,String scope,String appId){
        String apiUrl = Contants.baseUrl + Contants.urlGetToken;
        HttpHeaders headers = new HttpHeaders();
        MultiValueMap<String, String> map= new LinkedMultiValueMap<>();
        headers.setContentType(MediaType.APPLICATION_FORM_URLENCODED);
        map.add("client_id", Contants.clientId);
        map.add("code",code);
        map.add("scope",scope);
        map.add("app_id",appId);
        HttpEntity<MultiValueMap<String, String>> requestParams = new HttpEntity<>(map, headers);
        ResponseEntity<String> response = restTemplate.postForEntity(apiUrl,requestParams,String.class);
        String result =response.getBody();
        JSONObject jsStr = JSONObject.parseObject(result);
        String resultCode = jsStr.getString("code");

        if(Integer.parseInt(resultCode)!= 0){
            ResponseData responseData = new ResponseData(false,"error",result);
            return responseData;
        }

        ResponseData responseData = new ResponseData(true,"success",result);
        log.info(responseData.getContent());
        Contants.accessToken=saveTokenParam(responseData);
        log.info("accessToken:{}",Contants.accessToken);
        return responseData;
    }

    public String saveTokenParam(ResponseData responseData){
        String result = responseData.getContent();
        JSONObject epContent = JSONObject.parseObject(result);
        JSONObject content = JSONObject.parseObject(epContent.getString("content"));
        String accessToken = content.getString("access_token");
        return accessToken;
    }

    public ResponseData baseApi(String methodArg,String bizContent){
        if(methodArg == null || methodArg.equals("")){
            ResponseData responseData = new ResponseData(false,"the param methodArg is null","");
            return responseData;
        }
        if(bizContent == null || bizContent.equals("")){
            ResponseData responseData = new ResponseData(false,"the param bizContent is null","");
            return responseData;
        }
        String apiUrl = Contants.publicUrl  +"/"+ methodArg;
        HttpHeaders headers = new HttpHeaders();
        MultiValueMap<String, String> map= new LinkedMultiValueMap<>();
        headers.setContentType(MediaType.APPLICATION_FORM_URLENCODED);
        map.add("app_id", Contants.clientId);
        map.add("method",methodArg);
        map.add("format","json");
        map.add("charset","utf-8");
        map.add("timestamp",Contants.timeStamp);
        map.add("token",Contants.accessToken);
        map.add("biz_content",bizContent);
        HttpEntity<MultiValueMap<String, String>> requestParams = new HttpEntity<>(map, headers);
        ResponseEntity<String> response = restTemplate.postForEntity(apiUrl,requestParams,String.class);
        String result =response.getBody();
        JSONObject jsStr = JSONObject.parseObject(result);
        String resultCode = jsStr.getString("code");

        if(Integer.parseInt(resultCode)!= 0){
            ResponseData responseData = new ResponseData(false,"error",result);
            return responseData;
        }

        ResponseData responseData = new ResponseData(true,"success",result);
        return responseData;
    }

    public ResponseData getStationLists(String appId,String page,String pageSize){
        if(appId == null || appId.equals("")){
            ResponseData responseData = new ResponseData(false,"the param appId is null","");
            return responseData;
        }
        String method = "et_common.station.lists";
        StationListsParam stationListsParam = new StationListsParam(appId,page,pageSize);
        String bizContent = JSON.toJSONString(stationListsParam);
        log.info("bizContent:{}",bizContent);
        ResponseData result = baseApi(method,bizContent);
        if (result.getCode() != true){
            ResponseData responseData = new ResponseData(false,"error",result.getContent());
            return responseData;
        }
        ResponseData responseData = new ResponseData(true,"success",result.getContent());
        return responseData;
    }

    public ResponseData getGateList(String appId,String station_id,String direction){
        if(appId == null || appId.equals("")){
            ResponseData responseData = new ResponseData(false,"the param appId is null","");
            return responseData;
        }
        String method = "et_common.device.lists";
        GateListParam gateListParam = new GateListParam(appId,station_id,direction);
        String bizContent = JSON.toJSONString(gateListParam);
        log.info("bizContent:{}",bizContent);
        ResponseData result = baseApi(method,bizContent);
        if (result.getCode() != true){
            ResponseData responseData = new ResponseData(false,"error",result.getContent());
            return responseData;
        }
        ResponseData responseData = new ResponseData(true,"success",result.getContent());
        return responseData;
    }

    public ResponseData getContractList(String appId,String station_id,String plate,String page,String pageSize){
        if(appId == null || appId.equals("")){
            ResponseData responseData = new ResponseData(false,"the param appId is null","");
            return responseData;
        }
        String method = "et_common.contract.lists";
        ContractListParam contractListParam = new ContractListParam(appId,station_id,plate,page,pageSize);
        String bizContent = JSON.toJSONString(contractListParam);
        log.info("bizContent:{}",bizContent);
        ResponseData result = baseApi(method,bizContent);
        if (result.getCode() != true){
            ResponseData responseData = new ResponseData(false,"error",result.getContent());
            return responseData;
        }
        ResponseData responseData = new ResponseData(true,"success",result.getContent());
        return responseData;
    }

    public ResponseData delContractPlate(String appId,String station_id,String plate){
        if(appId == null || appId.equals("")){
            ResponseData responseData = new ResponseData(false,"the param appId is null","");
            return responseData;
        }
        String method = "et_common.contract.del";
        DelContractPlateParam delContractPlateParam = new DelContractPlateParam(appId,station_id,plate);
        String bizContent = JSON.toJSONString(delContractPlateParam);
        log.info("bizContent:{}",bizContent);
        ResponseData result = baseApi(method,bizContent);
        if (result.getCode() != true){
            ResponseData responseData = new ResponseData(false,"error",result.getContent());
            return responseData;
        }
        ResponseData responseData = new ResponseData(true,"success",result.getContent());
        return responseData;
    }

    public ResponseData recoverContractPlate(String appId,String station_id,String plate){
        if(appId == null || appId.equals("")){
            ResponseData responseData = new ResponseData(false,"the param appId is null","");
            return responseData;
        }
        String method = "et_common.contract.recover";
        RecoverContractPlateParam recoverContractPlateParam = new RecoverContractPlateParam(appId,station_id,plate);
        String bizContent = JSON.toJSONString(recoverContractPlateParam);
        log.info("bizContent:{}",bizContent);
        ResponseData result = baseApi(method,bizContent);
        if (result.getCode() != true){
            ResponseData responseData = new ResponseData(false,"error",result.getContent());
            return responseData;
        }
        ResponseData responseData = new ResponseData(true,"success",result.getContent());
        return responseData;
    }

    public ResponseData askGateOpen(String appId,String station_id,String plate,String type){
        if(appId == null || appId.equals("")){
            ResponseData responseData = new ResponseData(false,"the param appId is null","");
            return responseData;
        }
        String method = "et_common.car_askopen";
        AskGateOpenParam askGateOpenParam = new AskGateOpenParam(appId,station_id,plate,type);
        String bizContent = JSON.toJSONString(askGateOpenParam);
        log.info("bizContent:{}",bizContent);
        ResponseData result = baseApi(method,bizContent);
        if (result.getCode() != true){
            ResponseData responseData = new ResponseData(false,"error",result.getContent());
            return responseData;
        }
        ResponseData responseData = new ResponseData(true,"success",result.getContent());
        return responseData;
    }

    public ResponseData setGateOpen(String appId,String station_id,String plate,String code){
        if(appId == null || appId.equals("")){
            ResponseData responseData = new ResponseData(false,"the param appId is null","");
            return responseData;
        }
        String method = "et_common.car_open";
        SetGateOpenParam setGateOpenParam = new SetGateOpenParam(appId,station_id,plate,code);
        String bizContent = JSON.toJSONString(setGateOpenParam);
        log.info("bizContent:{}",bizContent);
        ResponseData result = baseApi(method,bizContent);
        if (result.getCode() != true){
            ResponseData responseData = new ResponseData(false,"error",result.getContent());
            return responseData;
        }
        ResponseData responseData = new ResponseData(true,"success",result.getContent());
        return responseData;
    }

    public ResponseData setInviteCar(String appId,String station_id,String starttime,String stoptime,String client_id, String plate){
        if(appId == null || appId.equals("")){
            ResponseData responseData = new ResponseData(false,"the param appId is null","");
            return responseData;
        }
        String method = "et_common.authorize.bespeak";
        SetInviteCarParam setInviteCarParam = new SetInviteCarParam(appId,station_id,starttime,stoptime,client_id,plate);
        String bizContent = JSON.toJSONString(setInviteCarParam);
        log.info("bizContent:{}",bizContent);
        ResponseData result = baseApi(method,bizContent);
        if (result.getCode() != true){
            ResponseData responseData = new ResponseData(false,"error",result.getContent());
            return responseData;
        }
        ResponseData responseData = new ResponseData(true,"success",result.getContent());
        return responseData;
    }

    public ResponseData delInviteCar(String appId,String station_id,String authorize_id){
        if(appId == null || appId.equals("")){
            ResponseData responseData = new ResponseData(false,"the param appId is null","");
            return responseData;
        }
        String method = "et_common.authorize.del";
        DelInviteCarParam delInviteCarParam = new DelInviteCarParam(appId,station_id,authorize_id);
        String bizContent = JSON.toJSONString(delInviteCarParam);
        log.info("bizContent:{}",bizContent);
        ResponseData result = baseApi(method,bizContent);
        if (result.getCode() != true){
            ResponseData responseData = new ResponseData(false,"error",result.getContent());
            return responseData;
        }
        ResponseData responseData = new ResponseData(true,"success",result.getContent());
        return responseData;
    }

    public ResponseData getInviteCarList(String appId,String station_id,String plate,String page,String pageSize){
        if(appId == null || appId.equals("")){
            ResponseData responseData = new ResponseData(false,"the param appId is null","");
            return responseData;
        }
        String method = "et_common.authorize.lists";
        GetInviteCarListParam getInviteCarListParam = new GetInviteCarListParam(appId,station_id,plate,page,pageSize);
        String bizContent = JSON.toJSONString(getInviteCarListParam);
        log.info("bizContent:{}",bizContent);
        ResponseData result = baseApi(method,bizContent);
        if (result.getCode() != true){
            ResponseData responseData = new ResponseData(false,"error",result.getContent());
            return responseData;
        }
        ResponseData responseData = new ResponseData(true,"success",result.getContent());
        return responseData;
    }

    public ResponseData getCarImage(String appId,String station_id,String type,String date,String id){
        if(appId == null || appId.equals("")){
            ResponseData responseData = new ResponseData(false,"the param appId is null","");
            return responseData;
        }
        String method = "et_common.inout.images";
        GetCarImageParam getCarImageParam = new GetCarImageParam(appId,station_id,type,date,id);
        String bizContent = JSON.toJSONString(getCarImageParam);
        log.info("bizContent:{}",bizContent);
        ResponseData result = baseApi(method,bizContent);
        if (result.getCode() != true){
            ResponseData responseData = new ResponseData(false,"error",result.getContent());
            return responseData;
        }
        ResponseData responseData = new ResponseData(true,"success",result.getContent());
        return responseData;
    }

    public ResponseData adminOpenGate(String appId,String cmd,String device_id){
        if(appId == null || appId.equals("")){
            ResponseData responseData = new ResponseData(false,"the param appId is null","");
            return responseData;
        }
        String method = "et_common.device.openAndClose";
        AdminOpenGateParam adminOpenGateParam = new AdminOpenGateParam(appId,cmd,device_id);
        String bizContent = JSON.toJSONString(adminOpenGateParam);
        log.info("bizContent:{}",bizContent);
        ResponseData result = baseApi(method,bizContent);
        if (result.getCode() != true){
            ResponseData responseData = new ResponseData(false,"error",result.getContent());
            return responseData;
        }
        ResponseData responseData = new ResponseData(true,"success",result.getContent());
        return responseData;
    }

    public ResponseData getContractPlate(ContractApplyParam contractApplyParam){
        String appId = contractApplyParam.getAppid();
        String stationId = contractApplyParam.getStation_id();
        String plate = contractApplyParam.getPlate();

        if (appId == null || appId.equals("")){
            ResponseData responseData = new ResponseData(false,"the param appId is null","");
            return responseData;
        }
        if(stationId == null || stationId.equals("")){
            ResponseData responseData = new ResponseData(false,"the param stationId is null","");
            return responseData;
        }
        if(plate == null || plate.equals("")){
            ResponseData responseData = new ResponseData(false,"the param plate is null","");
            return responseData;
        }

        String method = "et_common.contract.apply";
        String bizContent = JSON.toJSONString(contractApplyParam);
        ResponseData result = baseApi(method,bizContent);
        if (result.getCode() != true){
            ResponseData responseData = new ResponseData(false,"error",result.getContent());
            return responseData;
        }
        ResponseData responseData = new ResponseData(true,"success",result.getContent());
        return responseData;
    }


    public ResponseData getContractRule(ContractRuleParam contractRuleParam){
        String appId = contractRuleParam.getAppid();
        String stationId = contractRuleParam.getStation_id();

        if (appId == null || appId.equals("")){
            ResponseData responseData = new ResponseData(false,"the param appId is null","");
            return responseData;
        }
        if(stationId == null || stationId.equals("")){
            ResponseData responseData = new ResponseData(false,"the param stationId is null","");
            return responseData;
        }

        String method = "et_common.contract.rule";
        String bizContent = JSON.toJSONString(contractRuleParam);
        ResponseData result = baseApi(method,bizContent);
        if (result.getCode() != true){
            ResponseData responseData = new ResponseData(false,"error",result.getContent());
            return responseData;
        }
        ResponseData responseData = new ResponseData(true,"success",result.getContent());
        return responseData;
    }

    public ResponseData getContractAgree(ContractAgreeParam contractAgreeParam){
        String appId = contractAgreeParam.getAppid();
        String stationId = contractAgreeParam.getStation_id();
        String applyId = contractAgreeParam.getApply_id();
        String ruleId = contractAgreeParam.getRule_id();
        String beginTime = contractAgreeParam.getBegin_time();
        if (appId == null || appId.equals("")){
            ResponseData responseData = new ResponseData(false,"the param appId is null","");
            return responseData;
        }
        if(stationId == null || stationId.equals("")){
            ResponseData responseData = new ResponseData(false,"the param stationId is null","");
            return responseData;
        }
        if(applyId == null || applyId.equals("")){
            ResponseData responseData = new ResponseData(false,"the param applyId is null","");
            return responseData;
        }
        if(ruleId == null || ruleId.equals("")){
            ResponseData responseData = new ResponseData(false,"the param ruleId is null","");
            return responseData;
        }
        if(beginTime == null || beginTime.equals("")){
            ResponseData responseData = new ResponseData(false,"the param beginTime is null","");
            return responseData;
        }

        String method = "et_common.contract.applyagree";
        String bizContent = JSON.toJSONString(contractAgreeParam);
        ResponseData result = baseApi(method,bizContent);
        if (result.getCode() != true){
            ResponseData responseData = new ResponseData(false,"error",result.getContent());
            return responseData;
        }
        ResponseData responseData = new ResponseData(true,"success",result.getContent());
        return responseData;
    }

    public ResponseData getCostMonth(CostMonthParam costMonthParam){
        String contractId = costMonthParam.getContract_id();
        String monthTotal = costMonthParam.getMonth_total();
        if (contractId == null || contractId.equals("")){
            ResponseData responseData = new ResponseData(false,"the param contractId is null","");
            return responseData;
        }
        if(monthTotal == null || monthTotal.equals("")){
            ResponseData responseData = new ResponseData(false,"the param monthTotal is null","");
            return responseData;
        }
        String method = "et_client.cost.month";
        String bizContent = JSON.toJSONString(costMonthParam);
        ResponseData result = baseApi(method,bizContent);
        if (result.getCode() != true){
            ResponseData responseData = new ResponseData(false,"error",result.getContent());
            return responseData;
        }
        ResponseData responseData = new ResponseData(true,"success",result.getContent());
        return responseData;
    }

    public ResponseData getMonthorderThird(MonthorderThird monthorderThird){
        String contractId = monthorderThird.getContract_id();
        String monthTotal = monthorderThird.getMonth_total();
        String amount = monthorderThird.getAmount();
        String mobile = monthorderThird.getMobile();
        String source = monthorderThird.getSource();
        String appId = monthorderThird.getAppid();

        if (appId == null || appId.equals("")){
            ResponseData responseData = new ResponseData(false,"the param appId is null","");
            return responseData;
        }
        if (contractId == null || contractId.equals("")){
            ResponseData responseData = new ResponseData(false,"the param contractId is null","");
            return responseData;
        }
        if(monthTotal == null || monthTotal.equals("")){
            ResponseData responseData = new ResponseData(false,"the param monthTotal is null","");
            return responseData;
        }
        if(amount == null || amount.equals("")){
            ResponseData responseData = new ResponseData(false,"the param amount is null","");
            return responseData;
        }
        if(mobile == null || mobile.equals("")){
            ResponseData responseData = new ResponseData(false,"the param mobile is null","");
            return responseData;
        }
        if(source == null || source.equals("")){
            ResponseData responseData = new ResponseData(false,"the param source is null","");
            return responseData;
        }

        String method = "et_client.pay.monthorder.third_party";
        String bizContent = JSON.toJSONString(monthorderThird);
        ResponseData result = baseApi(method,bizContent);
        if (result.getCode() != true){
            ResponseData responseData = new ResponseData(false,"error",result.getContent());
            return responseData;
        }
        ResponseData responseData = new ResponseData(true,"success",result.getContent());
        return responseData;
    }

    public ResponseData getPaySuccess(PaySuccessParam paySuccessParam){
        String amount = paySuccessParam.getAmount();
        String tradeNo = paySuccessParam.getTrade_no();
        String payStatus = paySuccessParam.getPay_status();
        String payTime = paySuccessParam.getPaytime();
        String authAppId = paySuccessParam.getAuth_app_id();
        String secret = paySuccessParam.getSecret();
        String ts = paySuccessParam.getTs();
        String thirdTnum = paySuccessParam.getThird_tnum();
        if (amount == null || amount.equals("")){
            ResponseData responseData = new ResponseData(false,"the param amount is null","");
            return responseData;
        }
        if (tradeNo == null || tradeNo.equals("")){
            ResponseData responseData = new ResponseData(false,"the param tradeNo is null","");
            return responseData;
        }
        if(payStatus == null || payStatus.equals("")){
            ResponseData responseData = new ResponseData(false,"the param monthTotal is null","");
            return responseData;
        }
        if(payTime == null || payTime.equals("")){
            ResponseData responseData = new ResponseData(false,"the param payTime is null","");
            return responseData;
        }
        if(authAppId == null || authAppId.equals("")){
            ResponseData responseData = new ResponseData(false,"the param authAppId is null","");
            return responseData;
        }
        if(secret == null || secret.equals("")){
            ResponseData responseData = new ResponseData(false,"the param secret is null","");
            return responseData;
        }
        if(ts == null || ts.equals("")){
            ResponseData responseData = new ResponseData(false,"the param ts is null","");
            return responseData;
        }

        String apiUrl = "https://api.eptingche.cn/notify/month/third_party";
        String signature = GetSignToken.getSignature(paySuccessParam);

        HttpHeaders headers = new HttpHeaders();
        MultiValueMap<String, String> map= new LinkedMultiValueMap<>();
        headers.setContentType(MediaType.APPLICATION_FORM_URLENCODED);
        map.add("amount", amount);
        map.add("trade_no",tradeNo);
        map.add("pay_status",payStatus);
        map.add("paytime",payTime);
        map.add("auth_app_id",authAppId);
        map.add("signature",signature);
        map.add("ts",ts);
        map.add("third_tnum",thirdTnum);
        HttpEntity<MultiValueMap<String, String>> requestParams = new HttpEntity<>(map, headers);
        ResponseEntity<String> response = restTemplate.postForEntity(apiUrl,requestParams,String.class);
        String result =response.getBody().toLowerCase();
        if(result.equals("success")){
            ResponseData responseData = new ResponseData(true,"success","you pay successfully");
            return responseData;
        }
        ResponseData responseData = new ResponseData(false,"fail","you pay fail");
        return responseData;
    }

    public ResponseData getContractByStationid(GetContractByStationid getContractByStationid){
        String appId = getContractByStationid.getAppid();
        String stationId = getContractByStationid.getStation_id();
        if (appId == null || appId.equals("")){
            ResponseData responseData = new ResponseData(false,"the param appId is null","");
            return responseData;
        }
        if (stationId == null || stationId.equals("")){
            ResponseData responseData = new ResponseData(false,"the param stationId is null","");
            return responseData;
        }
        String method = "et_common.contract.lists";
        String bizContent = JSON.toJSONString(getContractByStationid);
        ResponseData result = baseApi(method,bizContent);
        if (result.getCode() != true){
            ResponseData responseData = new ResponseData(false,"error",result.getContent());
            return responseData;
        }
        ResponseData responseData = new ResponseData(true,"success",result.getContent());
        return responseData;
    }

    public ResponseData addContract(AddContractParam addContractParam){
        String appid = addContractParam.getAppid();
        String stationId = addContractParam.getStation_id();
        String plate = addContractParam.getPlate();
        if(appid == null || appid.equals("")){
            ResponseData responseData = new ResponseData(false,"the param appid is null","");
            return responseData;
        }
        if(stationId == null || stationId.equals("")){
            ResponseData responseData = new ResponseData(false,"the param bizContent is null","");
            return responseData;
        }
        if(plate == null || plate.equals("")){
            ResponseData responseData = new ResponseData(false,"the param plate is null","");
            return responseData;
        }
        ContractApplyParam cap = new ContractApplyParam(appid,stationId,plate);
        ResponseData result1 = getContractPlate(cap);
        log.info("result1:{}",result1);
        if(result1.getCode() != true){
            ResponseData responseData = new ResponseData(false,"fail",result1.getContent());
            return responseData;
        }
        JSONObject jsStr = JSONObject.parseObject(result1.getContent());
        JSONObject content = JSONObject.parseObject(jsStr.getString("content"));
        String applyId = content.getString("apply_id");
        ContractRuleParam contractRuleParam = new ContractRuleParam(appid,stationId);
        ResponseData result2 = getContractRule(contractRuleParam);
        log.info("result2:{}",result2);
        if(result2.getCode() != true){
            ResponseData responseData = new ResponseData(false,"fail",result2.getContent());
            return responseData;
        }
        JSONObject jsStr1 = JSONObject.parseObject(result2.getContent());
        JSONArray jsonArray = JSONArray.parseArray(jsStr1.getString("content"));
        String ruleIdArray = jsonArray.getString(0);
        JSONObject jsStr2 = JSONObject.parseObject(ruleIdArray);
        String ruleId = jsStr2.getString("rule_id");
        log.info("ruleId:{}",ruleId);
        if(ruleId == null || ruleId.equals("")){
            ResponseData responseData = new ResponseData(false,"ruleId is null","");
            return responseData;
        }
        String beginTime = GetSignToken.getTime();
        ContractAgreeParam contractAgreeParam = new ContractAgreeParam(appid,stationId,applyId,ruleId,beginTime);
        ResponseData result3 = getContractAgree(contractAgreeParam);
        log.info("result3:{}",result3);
        if(result3.getCode() != true){
            ResponseData responseData = new ResponseData(false,"fail",result3.getContent());
            return responseData;
        }
        JSONObject jsStr3 = JSONObject.parseObject(result3.getContent());
        log.info("jsStr3:{}",jsStr3);
        JSONObject jsonstr = JSONObject.parseObject(jsStr3.getString("content"));
        String contractId = jsonstr.getString("contract_id");
        log.info("contractId:{}",contractId);
        GetContractByStationid getContractByStationid = new GetContractByStationid(appid,stationId);
        ResponseData result4 = getContractByStationid(getContractByStationid);
        if(result4.getCode() != true){
            ResponseData responseData = new ResponseData(false,"fail",result4.getContent());
            return responseData;
        }
        JSONObject jsStr4 = JSONObject.parseObject(result4.getContent());
        String jsStr4Lists = jsStr4.getString("content");
        JSONObject jsStr5 = JSONObject.parseObject(jsStr4Lists);

        String lists = jsStr5.getString("lists");
        List<JSONObject> jsonObjectList = JSON.parseArray(lists, JSONObject.class);
        log.info("lists:{}",lists);
        for(JSONObject jsonObject2 : jsonObjectList){
            String contractid = jsonObject2.getString("contract_id");
            log.info("contractid:{}",contractid);
            if(contractid.equals(contractId)){
                ResponseData responseData = new ResponseData(true,"add contract successfully",result4.getContent());
                return responseData;
            }
        }
        ResponseData responseData = new ResponseData(false,"add contract fail",result4.getContent());
        return responseData;
    }

    public ResponseData residentCarRegist(AddContractParam addContractParam){
        String appid = addContractParam.getAppid();
        String stationId = addContractParam.getStation_id();
        String plate = addContractParam.getPlate();
        if(appid == null || appid.equals("")){
            ResponseData responseData = new ResponseData(false,"the param appid is null","");
            return responseData;
        }
        if(stationId == null || stationId.equals("")){
            ResponseData responseData = new ResponseData(false,"the param bizContent is null","");
            return responseData;
        }
        if(plate == null || plate.equals("")){
            ResponseData responseData = new ResponseData(false,"the param plate is null","");
            return responseData;
        }
        ContractApplyParam cap = new ContractApplyParam(appid,stationId,plate);
        ResponseData result1 = getContractPlate(cap);
        log.info("result1:{}",result1);
        if(result1.getCode() != true){
            ResponseData responseData = new ResponseData(false,"fail",result1.getContent());
            return responseData;
        }
        JSONObject jsStr = JSONObject.parseObject(result1.getContent());
        JSONObject content = JSONObject.parseObject(jsStr.getString("content"));
        String applyId = content.getString("apply_id");
        ContractRuleParam contractRuleParam = new ContractRuleParam(appid,stationId);
        ResponseData result2 = getContractRule(contractRuleParam);
        log.info("result2:{}",result2);
        if(result2.getCode() != true){
            ResponseData responseData = new ResponseData(false,"fail",result2.getContent());
            return responseData;
        }
        JSONObject jsStr1 = JSONObject.parseObject(result2.getContent());
        JSONArray jsonArray = JSONArray.parseArray(jsStr1.getString("content"));
        String ruleIdArray = jsonArray.getString(0);
        JSONObject jsStr2 = JSONObject.parseObject(ruleIdArray);
        String ruleId = jsStr2.getString("rule_id");
        log.info("ruleId:{}",ruleId);
        if(ruleId == null || ruleId.equals("")){
            ResponseData responseData = new ResponseData(false,"ruleId is null","");
            return responseData;
        }
        String beginTime = GetSignToken.getTime();
        ContractAgreeParam contractAgreeParam = new ContractAgreeParam(appid,stationId,applyId,ruleId,beginTime);
        ResponseData result3 = getContractAgree(contractAgreeParam);
        log.info("result3:{}",result3);
        if(result3.getCode() != true){
            ResponseData responseData = new ResponseData(false,"fail",result3.getContent());
            return responseData;
        }
        JSONObject jsStr3 = JSONObject.parseObject(result3.getContent());
        log.info("jsStr3:{}",jsStr3);
        JSONObject jsonstr = JSONObject.parseObject(jsStr3.getString("content"));
        String contractId = jsonstr.getString("contract_id");
        log.info("contractId:{}",contractId);
        GetContractByStationid getContractByStationid = new GetContractByStationid(appid,stationId);
        ResponseData result4 = getContractByStationid(getContractByStationid);
        if(result4.getCode() != true){
            ResponseData responseData = new ResponseData(false,"fail",result4.getContent());
            return responseData;
        }
        JSONObject jsStr4 = JSONObject.parseObject(result4.getContent());
        String jsStr4Lists = jsStr4.getString("content");
        JSONObject jsStr5 = JSONObject.parseObject(jsStr4Lists);

        String lists = jsStr5.getString("lists");
        List<JSONObject> jsonObjectList = JSON.parseArray(lists, JSONObject.class);
        log.info("lists:{}",lists);
        for(JSONObject jsonObject2 : jsonObjectList){
            String contractid = jsonObject2.getString("contract_id");
            log.info("contractid:{}",contractid);
            if(contractid.equals(contractId)){
                CostMonthParam costMonthParam = new CostMonthParam("665652","20");
                ResponseData result5 = getCostMonth(costMonthParam);
                if(result5.getCode() != true){
                    ResponseData responseData = new ResponseData(false,"fail",result5.getContent());
                    return responseData;
                }
                JSONObject jsStr6 = JSONObject.parseObject(result5.getContent());
                String totalAmount = jsStr6.getString("total_amount");
                log.info("totalAmount:{}",totalAmount);
                String timeBegin = jsStr6.getString("time_begin");
                log.info("timeBegin:{}",timeBegin);
                String timeEnd = jsStr6.getString("time_end");
                log.info("timeEnd:{}",timeEnd);
                String couponAmount = jsStr6.getString("coupon_amount");
                log.info("couponAmount:{}",couponAmount);
                String couponLists = jsStr6.getString("coupon_lists");
                log.info("couponLists:{}",couponLists);
                MonthorderThird monthorderThird = new MonthorderThird(appid,contractId,"1",totalAmount,"20","17376593658","SINGAPORE",null,null);
                ResponseData result6 = getMonthorderThird(monthorderThird);
                if(result6.getCode() != true){
                    ResponseData responseData = new ResponseData(false,"fail",result6.getContent());
                    return responseData;
                }
                JSONObject jsStr7 = JSONObject.parseObject(result6.getContent());
                String tnum = jsStr7.getString("tnum");
                PaySuccessParam paySuccessParam = new PaySuccessParam("20","1127834846962614272000117001","SUCCESS",null,"1",Contants.clientId,null,tnum,Contants.secret);
                ResponseData result7 = getPaySuccess(paySuccessParam);
                if(result7.getCode() != true){
                    ResponseData responseData = new ResponseData(false,"fail",result7.getContent());
                    return responseData;
                }
                ResponseData responseData = new ResponseData(true,"success",result7.getContent());
                return responseData;
            }
            ResponseData responseData = new ResponseData(false,"fail","there is no contract_id");
            return responseData;
        }
        ResponseData responseData = new ResponseData(false,"fail","there is no lists");
        return responseData;
    }



    @ExceptionHandler(RestClientResponseException.class)
    public ErrorBody exceptionHandler(HttpClientErrorException e) throws IOException {
        return new ObjectMapper().readValue(e.getResponseBodyAsString(), ErrorBody.class);
    }
}

