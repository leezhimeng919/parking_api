package com.eclab.eparking.models;

/**
 * Author: Marin Cheng
 * Date: 2019/5/7 10:05
 * Content:IO异常处理对象
 */
import java.io.Serializable;

public class ErrorBody implements Serializable {
    private Integer code;
    private String message;
    private long timestamp = System.currentTimeMillis();

    // get set
    @Override
    public String toString() {
        return "ErrorBody{" +
                "code=" + code +
                ", message='" + message + '\'' +
                ", timestamp=" + timestamp +
                '}';
    }
}
