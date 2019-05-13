package com.eclab.eparking.models;

import lombok.Data;

/**
 * Author: Marin Cheng
 * Date: 2019/5/7 19:57
 * Content:停车场信息查询接口参数对象
 */

@Data
public class StationListsParam {
    private String appid;
    private String page;
    private String pagesize;

   public StationListsParam(){}

    public StationListsParam(String appid,String page,String pagesize){
        this.appid = appid;
        this.page = page;
        this.pagesize = pagesize;
    }
}
