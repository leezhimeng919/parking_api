package com.eclab.eparking.models;

import lombok.Data;

/**
 * Author: Marin Cheng
 * Date: 2019/5/8 14:58
 * Content:月卡计费接口参数对象
 */
@Data
public class CostMonthParam {
    private String contract_id;
    private String month_total;
    public CostMonthParam(){}
    public CostMonthParam(String contractId,String monthTotal){
        this.contract_id = contractId;
        this.month_total = monthTotal;
    }
}
