package com.eclab.eparking.models;

import lombok.Data;

/**
 * Author: li zhi meng
 * Date: 2019/5/14 19:57
 * Content:管理员开闸接口参数对象
 */

@Data
public class AdminOpenGateParam {
    private String appid;
    private String cmd;
    private String device_id;

    public AdminOpenGateParam(){}

    public AdminOpenGateParam(String appid,String cmd,String device_id){
        this.appid = appid;
        this.cmd = cmd;
        this.device_id = device_id;
    }
}
