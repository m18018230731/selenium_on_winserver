#!/usr/bin/env python
# -*- coding:UTF-8 -*-
#
# @AUTHOR: Rabbir
# @FILE: E:\Github\chrome_stapi\main.py
# @DATE: 2020/12/19 周六
# @TIME: 12:13:16
#
# @DESCRIPTION: chrome.stapi.cn 远程页面访问和 JS 执行


import time
import urllib
import platform
import selenium
from fastapi import FastAPI, HTTPException
from rab_python_packages import rab_chrome
from rab_python_packages import rab_logging


# FastAPI 初始化
app = FastAPI()
# 日志记录
chrome_logger = rab_logging.build_rab_logger()


"""
@url: /execute_script
@method: POST
-------
@description: 在指定端口的浏览器上执行 JS 脚本
-------
@param: port_num<int>, js<str>
-------
@return: <json>
"""
@app.post("/execute_script")
async def execute_script(port_num,
                         web_url,
                         js,
                         build_wait_time=3,
                         get_wait_time=3):
    print(port_num, web_url, js, build_wait_time, get_wait_time)
    # 判断当前操作系统是　Windows 还是 Linux
    if ("Windows" in str(platform.platform())):
        headless = False
    else:
        headless = True
    # 尝试执行 JS
    try:
        result = rab_chrome.build_chrome_and_execute_script(port_num,
                                                            web_url,
                                                            js,
                                                            build_wait_time,
                                                            get_wait_time,
                                                            headless=headless)
        if (result):
            return result
        else:
            raise HTTPException(status_code=500, detail="JS 执行返回值为空！")
    except Exception as e:
        err_msg = "JS 执行出错！" + str(e)
        raise HTTPException(status_code=500, detail=err_msg)



