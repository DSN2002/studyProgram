# -*- coding: utf-8 -*-
# Author: DSN2002
# Date: 2021-11-12 16:41
# LastEditTime: 2021-11-12 17:25
# LastEditors: DSN2002
# Description:
# 仅供研究使用，请勿用于其他活动

from ctypes import *
import os
import easygui as g
relativepath = os.getcwd()
relativepath = relativepath + "\\dll"
print("%s"%relativepath)
os.add_dll_directory("%s"%relativepath)
relativepath = relativepath + "\\lazycode.dll"
i = 1
q = 1
result = 0
while i > 0:
    while q > 0:
        URL = g.enterbox(msg='请输入URL', title='懒人脚本',strip=True)
        if len(URL) ==0:  ## 判断URL是否为空
            g.msgbox(msg='请输入正确的URL', title='错误', ok_button='OK', image=None, root=None)
        else:
            break
    num = ['用mpv观看','显示视频真url','下载视频','查看该url下视频信息']
    mode = g.buttonbox(msg='请选择解析方式', title='懒人脚本', choices=num)

## 用mpv观看 模式一

    if mode == "用mpv观看":
        choices1 = ['youtube-dl','youget']
        msg_txt1 = '选择解析模式，bilbil用youtube-dl，腾讯视频用youget,其他随意'
        n = g.buttonbox(msg=msg_txt1, title='用mpv观看', choices=choices1)
        if n == "youtube-dl":
            result = cdll.LoadLibrary(relativepath)
            result.ytb_w(URL)
            print(result)
            cmd  = "mpv " + URL
            info = cmd
            os.system(cmd)
        else:
            cmd  = "you-get -p mpv " + URL
            info = cmd
            os.system(info)

## 显示视频真url 模式二

    elif mode == "显示视频真url":
            cmd  = 'you-get -u ' + URL
            info = cmd
            os.system(info)

## 下载视频 模式三

    elif mode == "下载视频":
        choices2 = ['单集下载','全集下载']
        msg_txt2 = '请选择下载方式'
        n = g.buttonbox(msg=msg_txt2, title='下载视频', choices=choices2)
        ## 单集下载
        if n == "单集下载":
            choices3 = ['是','否']
            msg_txt3 = '该模式会自动下载最高画质,该视频是否需要VIP?'
            VIP = g.buttonbox(msg=msg_txt3, title='下载视频', choices=choices3)
            if VIP == "否":
                cmd  = 'you-get -o ' + 'D:\Videos ' + URL
                info = cmd
                print("自动下载开启中，去活动一下吧！")
                os.system(info)
            else:
                cookie = g.enterbox('请输存放该视频VIP信息cookie的路径','cookie的路径')
                cmd    = 'you-get -c ' + cookie + ' -o ' + 'D:\Videos ' + URL
                print("自动下载开启中，去活动一下吧！")
                info   = cmd
                os.system(info)
        ## 全集下载
        else:
            choices3 = ['是','否']
            msg_txt3 = '该模式会自动下载最高画质,该视频是否需要VIP?'
            VIP = g.buttonbox(msg=msg_txt3, title='下载全集视频', choices=choices3)
            fold = g.enterbox('请为存放视频的文件夹命名','文件夹命名')
            if VIP == "否":
                cmd  = 'you-get -o ' + 'D:\Videos\\' + fold + ' --playlist '+ URL
                info = cmd
                print("自动下载开启中，去活动一下吧！")
                os.system(info)
            else:
                cookie = g.enterbox('请输存放该视频VIP信息cookie的路径','cookie的路径')
                cmd    = 'you-get -c ' + cookie + ' -o ' + 'D:\Videos\\' + fold + ' --playlist ' + URL
                info   = cmd
                print("自动下载开启中，去活动一下吧！")
                os.system(info)

##查看该url下视频信息

    elif mode == "查看该url下视频信息":
        cmd  = 'you-get -i ' + URL
        info = cmd
        os.system(info)
    else:
        break
##  继续运行程序
    i = g.ccbox(msg='要继续吗?', title='懒人脚本', choices=('继续', '不了'), image=None)
