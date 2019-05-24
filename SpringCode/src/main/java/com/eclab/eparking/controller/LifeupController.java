package com.eclab.eparking.controller;

import com.alibaba.fastjson.JSON;
import com.alibaba.fastjson.JSONArray;
import com.alibaba.fastjson.JSONObject;
import com.eclab.eparking.models.ResponseData;
import com.eclab.eparking.models.StationListsParam;
import com.eclab.eparking.service.EParkingService;
import io.swagger.annotations.Api;
import io.swagger.annotations.ApiOperation;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.util.StringUtils;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RestController;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

/**
 * Author: JL
 * Date: 2019/5/10 9:15
 * Content:
 */
@Api(value = "/lifeup", tags = "LifeUp接口")
@Slf4j
@RestController
@RequestMapping("/lifeup")
public class LifeupController {

    @Autowired
    private EParkingService eParkingService;

    @ApiOperation(value = "检查工作状态", notes = "检查工作状态")
    @RequestMapping(value = "/checkOutWorkingStatus", method = RequestMethod.POST)
    public Boolean checkOutWorkingStatus(String appId, String page,String pageSize) {
        ResponseData responseData = eParkingService.getStationLists(appId, page, pageSize);
        JSONObject jsonObject = JSONObject.parseObject(responseData.getContent());
        String jsonCode = jsonObject.getString("code");
        if(jsonCode.equals("0"))
            return true;
        return false;
    }

    @ApiOperation(value = "获取月卡车牌列表", notes = "获取月卡车牌列表")
    @RequestMapping(value = "/getContractPlateList", method = RequestMethod.POST)
    public Set<String> getContractPlateList(String appId,String station_id,String plate,String page,String pageSize) {
        ResponseData responseData = eParkingService.getContractList(appId, station_id, plate, page, pageSize);
        JSONObject jsonObject = JSONObject.parseObject(responseData.getContent());
        String jsonContent = jsonObject.getString("content");
        log.info("jsonContent:{}", jsonContent);
        JSONObject listContent = JSONObject.parseObject(jsonContent);
        log.info("listContent:{}", listContent);
        JSONArray jsonArray2Lists = listContent.getJSONArray("lists");
        log.info("jsonArray2Lists:{}", jsonArray2Lists);
        Set arr = new HashSet();

        jsonArray2Lists.forEach(e-> {
            JSONObject e1 = (JSONObject)e;
            String res = e1.getString("plate");

            arr.add(res);
        });
        return arr;

    }

    @ApiOperation(value = "删除月卡", notes = "删除月卡")
    @RequestMapping(value = "/delOneContractPlate", method = RequestMethod.POST)
    public Boolean delOneContractPlate(String appId,String station_id,String plate,String page,String pageSize) {
        ResponseData responseData = eParkingService.getContractList(appId, station_id, plate, page, pageSize);
        JSONObject jsonObject = JSONObject.parseObject(responseData.getContent());
        String jsonCode = jsonObject.getString("code");
        if(jsonCode.equals("0"))
            return true;
        return false;
    }

    @ApiOperation(value = "恢复月卡", notes = "恢复月卡")
    @RequestMapping(value = "/recoverOneContractPlate", method = RequestMethod.POST)
    public Boolean recoverOneContractPlate(String appId,String station_id,String plate,String page,String pageSize) {
        ResponseData responseData = eParkingService.getContractList(appId, station_id, plate, page, pageSize);
        JSONObject jsonObject = JSONObject.parseObject(responseData.getContent());
        String jsonCode = jsonObject.getString("code");
        if(jsonCode.equals(0))
            return true;
        return false;
    }

    @ApiOperation(value = "获取预约车牌列表", notes = "获取预约车牌列表")
    @RequestMapping(value = "/getInviteCarPlateList", method = RequestMethod.POST)
    public Set<String> getInviteCarPlateList(String appId,String station_id,String plate,String page,String pageSize) {
        ResponseData responseData = eParkingService.getInviteCarList(appId, station_id, plate, page, pageSize);
        JSONObject jsonObject = JSONObject.parseObject(responseData.getContent());
        String jsonContent = jsonObject.getString("content");
        log.info("jsonContent:{}", jsonContent);
        JSONObject listContent = JSONObject.parseObject(jsonContent);
        log.info("listContent:{}", listContent);
        JSONArray jsonArray2Lists = listContent.getJSONArray("lists");
        log.info("jsonArray2Lists:{}", jsonArray2Lists);
        Set arr = new HashSet();

        jsonArray2Lists.forEach(e-> {
            JSONObject e1 = (JSONObject)e;
            String res = e1.getString("plate");

            arr.add(res);
        });
        return arr;
    }


    @ApiOperation(value = "预约访客车牌添加", notes = "预约访客车牌添加")
    @RequestMapping(value = "/setInviteCarPlate", method = RequestMethod.POST)
    public Boolean setInviteCarPlate(String appId,String station_id,String starttime,String stoptime,String client_id, String plate) {
        ResponseData responseData = eParkingService.setInviteCar(appId, station_id, starttime, stoptime, client_id,plate);
        JSONObject jsonObject = JSONObject.parseObject(responseData.getContent());
        String jsonCode = jsonObject.getString("code");
        if(jsonCode.equals(0))
            return true;
        return false;
    }

    @ApiOperation(value = "预约访客车牌删除", notes = "预约访客车牌删除")
    @RequestMapping(value = "/delInviteCarPlate", method = RequestMethod.POST)
    public Boolean delInviteCarPlate(String appId,String station_id,String authorize_id) {
        ResponseData responseData = eParkingService.delInviteCar(appId, station_id, authorize_id);
        JSONObject jsonObject = JSONObject.parseObject(responseData.getContent());
        String jsonCode = jsonObject.getString("code");
        if(jsonCode.equals("0"))
            return true;
        return false;
    }

    @ApiOperation(value = "道闸开启", notes = "道闸开启")
    @RequestMapping(value = "/setGateOpen", method = RequestMethod.POST)
    public Boolean setGateOpen(String appId,String station_id,String plate,String code) {
        ResponseData responseData = eParkingService.setGateOpen(appId, station_id, plate, code);
        JSONObject jsonObject = JSONObject.parseObject(responseData.getContent());
        String jsonCode = jsonObject.getString("code");
        if(jsonCode.equals("0"))
            return true;
        return false;
    }

    @ApiOperation(value = "管理员开闸", notes = "管理员开闸")
    @RequestMapping(value = "/adminOpenGate", method = RequestMethod.POST)
    public Boolean adminOpenGate(String appId,String cmd,String device_id) {
        ResponseData responseData = eParkingService.adminOpenGate(appId, cmd,device_id);
        JSONObject jsonObject = JSONObject.parseObject(responseData.getContent());
        String jsonCode = jsonObject.getString("code");
        if(jsonCode.equals("0"))
            return true;
        return false;
    }

    @ApiOperation(value = "获取车辆图片", notes = "获取车辆图片")
    @RequestMapping(value = "/getCarImage", method = RequestMethod.POST)
    public Boolean getCarImage(String appId,String station_id,String plate,String page,String pageSize) {
        ResponseData responseData = eParkingService.getCarImage(appId, station_id, plate, page, pageSize);
        JSONObject jsonObject = JSONObject.parseObject(responseData.getContent());
        String jsonCode = jsonObject.getString("code");
        if(jsonCode.equals("0"))
            return true;
        return false;
    }
}
