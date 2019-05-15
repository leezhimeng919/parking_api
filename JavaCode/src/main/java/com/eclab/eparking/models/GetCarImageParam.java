package com.eclab.eparking.models;

import lombok.Data;

/**
 * Author: li zhi meng
 * Date: 2019/5/14 19:57
 * Content:查询进出场图片接口参数对象
 */

@Data
public class GetCarImageParam {
    private String appid;
    private String station_id;
    private String type;
    private String date;
    private String id;

    public GetCarImageParam(){}

    public GetCarImageParam(String appid,String station_id,String type,String date,String id){
        this.appid = appid;
        this.station_id = station_id;
        this.type = type;
        this.date = date;
        this.id = id;
    }
}
