package com.eclab.eparking.models;

import lombok.Data;

/**
 * Author: Marin Cheng
 * Date: 2019/5/9 15:09
 * Content:三步添加月卡接口参数对象
 */
@Data
public class AddContractParam {
    private String appid;
    private String station_id;
    private String plate;
}
