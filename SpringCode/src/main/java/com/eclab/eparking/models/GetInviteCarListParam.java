package com.eclab.eparking.models;

import lombok.Data;

/**
 * Author: li zhi meng
 * Date: 2019/5/14 19:57
 * Content:预约进场查看查询接口参数对象
 */

@Data
public class GetInviteCarListParam {
    private String appid;
    private String station_id;
    private String plate;
    private String page;
    private String pagesize;

    public GetInviteCarListParam(){}

    public GetInviteCarListParam(String appid,String station_id,String plate,String page,String pageSize){
        this.appid = appid;
        this.station_id = station_id;
        this.plate = plate;
        this.page = page;
        this.pagesize = pagesize;
    }
}