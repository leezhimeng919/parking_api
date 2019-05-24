package com.eclab.eparking.models;

import lombok.Data;

/**
 * Author: li zhi meng
 * Date: 2019/5/14 19:57
 * Content:删除预约进场查询接口参数对象
 */

@Data
public class DelInviteCarParam {
    private String appid;
    private String station_id;
    private String authorize_id;

    public DelInviteCarParam(){}

    public DelInviteCarParam(String appid,String station_id,String authorize_id){
        this.appid = appid;
        this.station_id = station_id;
        this.authorize_id = authorize_id;
    }
}