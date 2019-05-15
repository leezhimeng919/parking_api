package com.eclab.eparking.models;

import lombok.Data;

/**
 * Author: Marin Cheng
 * Date: 2019/5/8 20:10
 * Content:支付回调参数对象
 */
@Data
public class PaySuccessParam {
    private String amount;
    private String trade_no;
    private String pay_status;
    private String paytime;
    private String client_id;
    private String auth_app_id;
    private String ts;
    private String third_tnum;
    private String secret;
    public PaySuccessParam(){}
    public PaySuccessParam(String amount,String trade_no,String pay_status,String paytime,String client_id,String auth_app_id,String ts,String third_tnum,String secret){
        this.amount = amount;
        this.trade_no = trade_no;
        this.pay_status = pay_status;
        this.paytime = paytime;
        this.client_id = client_id;
        this.auth_app_id = auth_app_id;
        this.ts = ts;
        this.third_tnum = third_tnum;
        this.secret = secret;
    }
}
