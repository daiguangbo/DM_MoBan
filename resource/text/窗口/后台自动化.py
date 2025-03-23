# -*- coding: utf-8 -*-

# @PyCharm：2024.2.1
# @Python：3.11
# @项目：dm插件模板

# @文件：game.py
# @时间：2025/3/19 15:23
# @作者：LexiSiy
# @邮箱：2172500693@163.com


import os
import time
from typing import Any,Tuple

from source import DMClient
from source import dm_tools
from demo import hwnd模块

import win32api
import win32process
import win32gui
import win32con
import subprocess


dm = DMClient.dm_client("127.0.0.1", "9000", 0)
dm1 = DMClient.dm_client("127.0.0.1", "9000", 1)


def 按键精灵计算相对坐标(hwnd,text,是否只返回坐标=1):
    屏幕坐标转窗口坐标 = dm.ClientToScreen(hwnd,0,0)
    print(屏幕坐标转窗口坐标)
    if 屏幕坐标转窗口坐标['state']:
        x,y = int(屏幕坐标转窗口坐标['value'][0]),int(屏幕坐标转窗口坐标['value'][1])
        dict = dm_tool.提取颜色和坐标(text)
        print(dict['x'],dict['y'],"原坐标 函数:",按键精灵计算相对坐标.__name__)
        print(dict['x']-x,dict['y']-y,x,y,"偏移坐标 函数:",按键精灵计算相对坐标.__name__)
        if 是否只返回坐标:return dict['x']-x,dict['y']-y
        return dict['x']-x,dict['y']-y,dict['color']
    else:
        print("坐标转化失败")
        return 0,0,0
    
def 窗口绑定大漠对象(dm,hwnd):
    dm_tools.窗口绑定dm对象(dm,hwnd)

def 单点找色_后台(text,hwnd,dm,打印=1,备注=""):
    x,y,color = 按键精灵计算相对坐标(hwnd,text,0)
    if x or y or color:
        result = dm.CmpColor(x,y,color,0.8)
        if result['value']:
            if 打印:print("未找到:",备注)
            return 0,0
        else:
            print("找到!",备注,end="")
            return x,y
    else:return 0,0

def 查询软件状态并打开(标题:str="",path:str="",隐藏窗口:int=0):
    hwnd = win32gui.FindWindow(None,标题)
    if hwnd:
        print("软件正在运行,句柄:",hwnd)
        print()
        if 隐藏窗口:win32gui.ShowWindow(hwnd,win32con.SW_HIDE)#隐藏窗口
        else:win32gui.ShowWindow(hwnd,win32con.SW_SHOW)#显示窗口
        return hwnd
    else:
        print("软件未运行")
        subprocess.Popen(path)
    print("软件服务端启动中...  ",end="")
    while True:
        hwnd = win32gui.FindWindow(None,标题)
        if hwnd:
            print("软件成功运行,句柄:",hwnd)
            if 隐藏窗口: win32gui.ShowWindow(hwnd,win32con.SW_HIDE)  #隐藏窗口
            else: win32gui.ShowWindow(hwnd,win32con.SW_SHOW)  #显示窗口
            break
        else: pass
    return hwnd

def 关闭软件程序(hwnd):
    _,pid = win32process.GetWindowThreadProcessId(hwnd)
    print(f"窗口句柄 {hwnd} 对应的进程 ID 为 {pid}")
    handle = win32api.OpenProcess(win32con.PROCESS_TERMINATE,False,pid)
    win32api.TerminateProcess(handle,0)
    print(f"已结束进程 ID 为 {pid} 的程序")
    
def 计算窗口和屏幕的坐标偏移(hwnd)-> tuple[int,int]:
    窗口状态 = win32gui.GetWindowPlacement(hwnd)
    x,y = 窗口状态[4][0]+8,窗口状态[4][1]+31
    return x,y

def 计算相对坐标(hwnd,text,是否只返回坐标=1):
    x,y = 计算窗口和屏幕的坐标偏移(hwnd)
    dict = dm_tools.提取颜色和坐标(text)
    print(dict['x'],dict['y'],"原坐标 函数:",按键精灵计算相对坐标.__name__)
    print(dict['x']-x,dict['y']-y,x,y,"偏移坐标 函数:",按键精灵计算相对坐标.__name__)
    if 是否只返回坐标:return dict['x']-x,dict['y']-y
    return dict['x']-x,dict['y']-y,dict['color']




""" 配置v2ray软件 """

# 获取窗口句柄并测试
标题 = "大漠插件接口说明v7.2450"
hwnds = hwnd模块.根据标题枚举窗口句柄(标题);hwnd = hwnds
print(hwnds,type(hwnds),"  ",dm,dm1)

# 窗口绑定dm

dm_tool.窗口绑定dm对象(dm1,hwnd)

hwnd模块.设置窗口状态(hwnd,位置大小=1)
x,y = 计算相对坐标(hwnd,"564,286  000000")
if x and y:dm1.MoveTo(x,y)
if x and y:dm1.LeftClick()

