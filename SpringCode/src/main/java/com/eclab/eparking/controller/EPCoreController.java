package com.eclab.eparking.controller;
import com.alibaba.fastjson.JSON;
import com.alibaba.fastjson.JSONArray;
import com.alibaba.fastjson.JSONException;
import com.alibaba.fastjson.JSONObject;

import com.eclab.eparking.models.*;
import com.eclab.eparking.service.EParkingService;
import com.eclab.eparking.utils.GetSignToken;
import com.fasterxml.jackson.databind.ObjectMapper;
import io.swagger.annotations.Api;
import io.swagger.annotations.ApiOperation;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.*;
import org.springframework.util.LinkedMultiValueMap;
import org.springframework.util.MultiValueMap;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.client.HttpClientErrorException;
import org.springframework.web.client.RestClientResponseException;
import org.springframework.web.client.RestTemplate;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;


/**
 * Author: Marin Cheng
 * Date: 2019/5/7 9:58
 * Content:
 */
@Api(value = "/eparking", tags = "EParking停车")
@Slf4j
@RestController
@RequestMapping("/eparking")
public class EPCoreController {

    @Autowired
    private EParkingService eParkingService;

    @Autowired
    private RestTemplate restTemplate;

    @ApiOperation(value = "请求AppId接口", notes = "请求AppId接口")
    @RequestMapping(value = "/getCode", method = RequestMethod.POST)
    public ResponseData getCode() {
        ResponseData responseData = eParkingService.getCode();
        return responseData;
    }


    @ApiOperation(value = "请求秘钥", notes = "请求秘钥")
    @RequestMapping(value = "/getAccessToken", method = RequestMethod.POST)
    public ResponseData getAccessToken(){
        ResponseData responseData = eParkingService.getAccessToken();
        return responseData;
    }


    @ApiOperation(value = "传参获取秘钥", notes = "传参获取秘钥")
    @RequestMapping(value = "/getToken", method = RequestMethod.POST)
    public ResponseData getToken(String code,String scope,String appId){
        ResponseData responseData = eParkingService.getAccessToken();
        return responseData;
    }


    @ApiOperation(value = "通用接口", notes = "通用接口")
    @RequestMapping(value = "/baseApi", method = RequestMethod.POST)
    public ResponseData baseApi(String methodArg,String bizContent){
        ResponseData responseData = eParkingService.baseApi(methodArg,bizContent);
        return responseData;
    }


    @ApiOperation(value = "停车场信息查询接口", notes = "停车场信息查询接口")
    @RequestMapping(value = "/getStationLists", method = RequestMethod.POST)
    public ResponseData getStationLists(String appId,String page,String pageSize){
        ResponseData responseData = eParkingService.getStationLists(appId,page,pageSize);
        return responseData;
    }


    @ApiOperation(value = "道闸信息查询", notes = "道闸信息查询")
    @RequestMapping(value = "/getGateList", method = RequestMethod.POST)
    public ResponseData getGateList(String appId,String station_id,String direction){
        ResponseData responseData = eParkingService.getGateList(appId,station_id,direction);
        return responseData;
    }

    @ApiOperation(value = "月卡信息查询", notes = "月卡信息查询")
    @RequestMapping(value = "/getContractList", method = RequestMethod.POST)
    public ResponseData getContractList(String appId,String station_id,String plate,String page,String pageSize){
        ResponseData responseData = eParkingService.getContractList(appId,station_id,plate,page,pageSize);
        return responseData;
    }

    @ApiOperation(value = "月卡删除", notes = "月卡删除")
    @RequestMapping(value = "/delContractPlate", method = RequestMethod.POST)
    public ResponseData delContractPlate(String appId,String station_id,String plate){
        ResponseData responseData = eParkingService.delContractPlate(appId,station_id,plate);
        return responseData;
    }

    @ApiOperation(value = "月卡启用", notes = "月卡启用")
    @RequestMapping(value = "/recoverContractPlate", method = RequestMethod.POST)
    public ResponseData recoverContractPlate(String appId,String station_id,String plate){
        ResponseData responseData = eParkingService.recoverContractPlate(appId,station_id,plate);
        return responseData;
    }

    @ApiOperation(value = "下发道闸码", notes = "下发道闸码")
    @RequestMapping(value = "/askGateOpen", method = RequestMethod.POST)
    public ResponseData askGateOpen(String appId,String station_id,String plate,String type){
        ResponseData responseData = eParkingService.askGateOpen(appId,station_id,plate,type);
        return responseData;
    }

    @ApiOperation(value = "紧急开闸", notes = "紧急开闸")
    @RequestMapping(value = "/setGateOpen", method = RequestMethod.POST)
    public ResponseData setGateOpen(String appId,String station_id,String plate,String code){
        ResponseData responseData = eParkingService.setGateOpen(appId,station_id,plate,code);
        return responseData;
    }

    @ApiOperation(value = "预约进场", notes = "预约进场")
    @RequestMapping(value = "/setInviteCar", method = RequestMethod.POST)
    public ResponseData setInviteCar(String appId,String station_id,String starttime,String stoptime,String client_id, String plate){
        ResponseData responseData = eParkingService.setInviteCar(appId,station_id,starttime,stoptime,client_id,plate);
        return responseData;
    }

    @ApiOperation(value = "删除预约进场", notes = "删除预约进场")
    @RequestMapping(value = "/delInviteCar", method = RequestMethod.POST)
    public ResponseData delInviteCar(String appId,String station_id,String authorize_id){
        ResponseData responseData = eParkingService.delInviteCar(appId,station_id,authorize_id);
        return responseData;
    }

    @ApiOperation(value = "预约进场查看", notes = "预约进场查看")
    @RequestMapping(value = "/getInviteCarList", method = RequestMethod.POST)
    public ResponseData getInviteCarList(String appId,String station_id,String plate,String page,String pageSize){
        ResponseData responseData = eParkingService.getInviteCarList(appId,station_id,plate,page,pageSize);
        return responseData;
    }

    @ApiOperation(value = "查询进出场图片", notes = "查询进出场图片")
    @RequestMapping(value = "/getCarImage", method = RequestMethod.POST)
    public ResponseData getCarImage(String appId,String station_id,String type,String date,String id){
        ResponseData responseData = eParkingService.getCarImage(appId,station_id,type,date,id);
        return responseData;
    }

    @ApiOperation(value = "管理员开闸", notes = "管理员开闸")
    @RequestMapping(value = "/adminOpenGate", method = RequestMethod.POST)
    public ResponseData adminOpenGate(String appId,String cmd,String device_id){
        ResponseData responseData = eParkingService.adminOpenGate(appId,cmd,device_id);
        return responseData;
    }

    @ApiOperation(value = "月卡申请接口", notes = "月卡申请接口")
    @RequestMapping(value = "/getContractPlate", method = RequestMethod.POST)
    public ResponseData getContractPlate(ContractApplyParam contractApplyParam){
        ResponseData responseData = eParkingService.getContractPlate(contractApplyParam);
        return responseData;
    }


    @ApiOperation(value = "停车场月卡规则查看接口", notes = "停车场月卡规则查看接口")
    @RequestMapping(value = "/getContractRule", method = RequestMethod.POST)
    public ResponseData getContractRule(ContractRuleParam contractRuleParam){
        ResponseData responseData = eParkingService.getContractRule(contractRuleParam);
        return responseData;
    }


    @ApiOperation(value = "月卡申请同意接口", notes = "月卡申请同意接口")
    @RequestMapping(value = "/getContractAgree", method = RequestMethod.POST)
    public ResponseData getContractAgree(ContractAgreeParam contractAgreeParam){
        ResponseData responseData = eParkingService.getContractAgree(contractAgreeParam);
        return responseData;
    }


    @ApiOperation(value = "月卡计费接口", notes = "月卡计费接口")
    @RequestMapping(value = "/getCostMonth", method = RequestMethod.POST)
    public ResponseData getCostMonth(CostMonthParam costMonthParam){
        ResponseData responseData = eParkingService.getCostMonth(costMonthParam);
        return responseData;
    }


    @ApiOperation(value = "月卡缴费下单接口", notes = "月卡缴费下单接口")
    @RequestMapping(value = "/getMonthorderThird", method = RequestMethod.POST)
    public ResponseData getMonthorderThird(MonthorderThird monthorderThird){
        ResponseData responseData = eParkingService.getMonthorderThird(monthorderThird);
        return responseData;
    }

    @ApiOperation(value = "支付回调通知接口", notes = "支付回调通知接口")
    @RequestMapping(value = "/getPaySuccess", method = RequestMethod.POST)
    public ResponseData getPaySuccess(PaySuccessParam paySuccessParam){
        ResponseData responseData = eParkingService.getPaySuccess(paySuccessParam);
        return responseData;
    }


    @ApiOperation(value = "根据stationId获取月卡接口", notes = "根据stationId获取月卡接口")
    @RequestMapping(value = "/getContractByStationid", method = RequestMethod.POST)
    public ResponseData getContractByStationid(GetContractByStationid getContractByStationid){
        ResponseData responseData = eParkingService.getContractByStationid(getContractByStationid);
        return responseData;
    }

    @ApiOperation(value = "三步添加月卡接口", notes = "三步添加月卡接口")
    @RequestMapping(value = "/addContract", method = RequestMethod.POST)
    public ResponseData addContract(AddContractParam addContractParam){
        ResponseData responseData = eParkingService.addContract(addContractParam);
        return responseData;
    }

    @ApiOperation(value = "六步添加月卡接口", notes = "六步添加月卡接口")
    @RequestMapping(value = "/residentCarRegist", method = RequestMethod.POST)
    public ResponseData residentCarRegist(AddContractParam addContractParam){
        ResponseData responseData = eParkingService.residentCarRegist(addContractParam);
        return responseData;
    }


}