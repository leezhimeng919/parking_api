package com.eclab.eparking.models;

import lombok.Data;

/**
 * Author: Marin Cheng
 * Date: 2019/5/8 11:15
 * Content:月卡申请同意接口参数对象
 */
@Data
public class ContractAgreeParam {
    private String appid;
    private String station_id;
    private String apply_id;
    private String rule_id;
    private String begin_time;

    public ContractAgreeParam(){}
    public ContractAgreeParam(String appId,String stationId,String applyId,String ruleId,String beginTime){
        this.appid = appId;
        this.apply_id = applyId;
        this.station_id = stationId;
        this.rule_id = ruleId;
        this.begin_time = beginTime;
    }
}
