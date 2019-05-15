package com.eclab.eparking.models;

import lombok.Data;

/**
 * Author: li zhi meng
 * Date: 2019/5/14 19:57
 * Content:下发道闸码接口参数对象
 */

@Data
public class AskGateOpenParam {
    private String appid;
    private String station_id;
    private String plate;
    private String type;

    public AskGateOpenParam(){}

    public AskGateOpenParam(String appid,String station_id,String plate,String type){
        this.appid = appid;
        this.station_id = station_id;
        this.plate = plate;
        this.type = type;
    }
}
