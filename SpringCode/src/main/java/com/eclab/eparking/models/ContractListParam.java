package com.eclab.eparking.models;

import lombok.Data;

/**
 * Author: li zhi meng
 * Date: 2019/5/14 19:57
 * Content:月卡信息查询接口参数对象
 */

@Data
public class ContractListParam {
    private String appid;
    private String station_id;
    private String plate;
    private String page;
    private String pagesize;

    public ContractListParam(){}

    public ContractListParam(String appid,String station_id,String plate,String page,String pagesize){
        this.appid = appid;
        this.station_id = station_id;
        this.plate = plate;
        this.page = page;
        this.pagesize = pagesize;
    }
}