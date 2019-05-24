package com.eclab.eparking.utils;

import com.eclab.eparking.models.Contants;
import com.eclab.eparking.models.PaySuccessParam;

import java.io.IOException;
import java.io.UnsupportedEncodingException;
import java.net.URLEncoder;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.text.SimpleDateFormat;
import java.util.Date;

import static org.reflections.Reflections.log;

/**
 * Author: Marin Cheng
 * Date: 2019/5/7 9:16
 * Content: 获取加密签名的对象及方法
 */
public class GetSignToken {


    //获取当前时间
    public static String getTime(){
        Date d = new Date();
        SimpleDateFormat sdf = new SimpleDateFormat("yyyy-MM-dd kk:mm:ss");
        return sdf.format(d);
    }

    //MD5加密
    public static String encodeByMd5(String value){
        String result = null;
        MessageDigest md5 = null;
        try{
            md5 = MessageDigest.getInstance("MD5");
            md5.update((value).getBytes("UTF-8"));
        }catch (NoSuchAlgorithmException error){
            error.printStackTrace();
        }catch (UnsupportedEncodingException e){
            e.printStackTrace();
        }
        byte b[] = md5.digest();
        int i;
        StringBuffer buf = new StringBuffer("");
        for(int offset=0; offset<b.length; offset++){
            i = b[offset];
            if(i<0){
                i+=256;
            }
            if(i<16){
                buf.append("0");
            }
            buf.append(Integer.toHexString(i));
        }

        result = buf.toString();
        return result;
    }

    //url编码
    public static String getUrlCode(String str) throws IOException {
        String encode = URLEncoder.encode(str, "UTF-8");
        return encode;
    }

    //获取token秘钥
    public static String getToken(){
        String encodeStr = "";
        String signature="";
        String clientId = Contants.clientId;
        Contants.timeStamp = Long.toString((System.currentTimeMillis()/1000));
        String signStr = "client_id=" + clientId + "&ts="+Contants.timeStamp+ "&secret=" + Contants.clientSecret;
        System.out.println("signstr:"+signStr);
        try{
            encodeStr = getUrlCode(signStr);
            log.info("encodeStr:{}",encodeStr);
        }catch (IOException e){
            e.printStackTrace();
        }
        try{
            signature = encodeByMd5(encodeStr);
            log.info("signature:{}",signature);
        }catch(Exception e){
            e.printStackTrace();
        }

        return signature;
    }


    //获取支付回调签名
    public static String getSignature(PaySuccessParam paySuccessParam){
        String thirdSignature = "";
        String encodeStr = "";
        String amount = paySuccessParam.getAmount();
        String tradeNo = paySuccessParam.getTrade_no();
        String payStatus = paySuccessParam.getPay_status();
        String payTime = paySuccessParam.getPaytime();
        String authAppId = paySuccessParam.getAuth_app_id();
        String secret = paySuccessParam.getSecret();
        String ts = paySuccessParam.getTs();
        String thirdTnum = paySuccessParam.getThird_tnum();

        String signStr = "amount=" + amount + "&auth_app_id="+authAppId+ "&pay_status=" + payStatus +
                "&paytime="+payTime+"&third_tnum="+thirdTnum+"&trade_no="+tradeNo+"&ts="+ts+"&secret="+secret;
        System.out.println("signstr:"+signStr);
        try{
            encodeStr = getUrlCode(signStr);
            log.info("encodeStr:{}",encodeStr);
        }catch (IOException e){
            e.printStackTrace();
        }
        try{
            thirdSignature = encodeByMd5(encodeStr);
            log.info("signature:{}",thirdSignature);
        }catch(Exception e){
            e.printStackTrace();
        }

        return thirdSignature;
    }


    public static void main(String [] args){
        System.out.println(getTime());
        long timeStap = (System.currentTimeMillis()/1000);
        String token = getToken();
        System.out.println(timeStap);
        System.out.println(token);
    }
}