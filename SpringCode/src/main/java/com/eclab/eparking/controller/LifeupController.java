package com.eclab.eparking.controller;

import com.alibaba.fastjson.JSONObject;
import com.eclab.eparking.models.ResponseData;
import com.eclab.eparking.models.StationListsParam;
import com.eclab.eparking.service.EParkingService;
import io.swagger.annotations.Api;
import io.swagger.annotations.ApiOperation;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RestController;

/**
 * Author: Marin Cheng
 * Date: 2019/5/16 9:15
 * Content:
 */
@Api(value = "/lifeup", tags = "LifeUp接口")
@Slf4j
@RestController
@RequestMapping("/lifeup")
public class LifeupController {

    @Autowired
    private EParkingService eParkingService;

    @ApiOperation(value = "请求AppId接口", notes = "请求AppId接口")
    @RequestMapping(value = "/getCode", method = RequestMethod.POST)
    public Boolean getWorkingStatus(String appId, String page, String pageSize) {
//        ResponseData responseData = eParkingService.baseApi(appId,page,pageSize);
        return true;
    }
}
