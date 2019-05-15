package com.eclab.eparking.models;

import lombok.Data;

/**
 * Author: li zhi meng
 * Date: 2019/5/14 19:57
 * Content:紧急开闸接口参数对象
 */

@Data
public class SetGateOpenParam {
    private String appid;
    private String station_id;
    private String plate;
    private String code;

    public SetGateOpenParam(){}

    public SetGateOpenParam(String appid,String station_id,String plate,String code){
        this.appid = appid;
        this.station_id = station_id;
        this.plate = plate;
        this.code = code;
    }
}