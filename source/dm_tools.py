# -*- coding: utf-8 -*-

# @PyCharm：2024.2.1
# @Python：3.11
# @项目：dm插件模板

# @文件：dm_tools.py
# @时间：2025/3/20 19:11
# @作者：LexiSiy
# @邮箱：2172500693@163.com

import time
from source import DMClient

dm = DMClient.dm_client("127.0.0.1", "9000", 0)

    
def 提取颜色和坐标(str):
    # 分割输入字符串,提取坐标和颜色
    parts = str.split()
    坐标 = parts[0].split(',')
    color = parts[1][4:6] + parts[1][2:4] + parts[1][0:2]
    return {"x":int(坐标[0]),"y":int(坐标[1]),"color":color}

def 单点找色(arr: dict,相似度=0.9,备注="",是否打印=1):
    result = dm.CmpColor(arr["x"],arr["y"],arr["color"],相似度)
    if result['value']:
        if 是否打印:print("未找到:",备注)
        return False
    else:
        print("找到!",备注,end="")
        return True

def 找色循环(text,回调函数=None,是否移动鼠标=False,单次找色=False,点击并移动=False,查找时长=10,备注=""):
    arr = 提取颜色和坐标(text)
    
    if 点击并移动:
        是否移动鼠标,回调函数 = True,lambda:左键点击(arr['x'],arr['y'],200)
    if 是否移动鼠标:dm.MoveTo(arr["x"],arr["y"])
    if 单次找色:return 单点找色(arr,备注=备注)
    
    time_找色时长 = time.time()
    time_打印频率 = time.time()
    
    while True:
        time_new = time.time()
        if time_new - time_找色时长 > 查找时长:return
        if time_new - time_打印频率 >= 1:
            if 单点找色(arr,备注=备注,是否打印=True):break
            time_打印频率 = time.time()
        else:
            if 单点找色(arr,备注=备注,是否打印=False):break
    
    if 回调函数 == 1:左键点击(arr['x'],arr['y'],200)
    elif 回调函数:回调函数()
    
def 枚举窗口_程序标题_子类名(标题,类名)->list:
    hwnds = dm.EnumWindowSuper(标题,8,1,类名,2,1,0)
    if hwnds['value']:
        print("找到句柄:",hwnds['value'],获取函数名称(枚举窗口_程序标题_子类名))
        return hwnds['value'].split(',')
    else:
        print("未找到句柄: ",获取函数名称(枚举窗口_程序标题_子类名))
        return []
    
def 枚举窗口_父句柄_子类名(句柄,类名)->list:
    hwnds = dm.EnumWindowSuper(句柄,4,1,类名,2,1,0)
    if hwnds['value']:
        print("找到句柄:",hwnds['value'],获取函数名称(枚举窗口_父句柄_子类名))
        return hwnds['value'].split(',')
    else:
        print("未找到句柄: ",获取函数名称(枚举窗口_父句柄_子类名))
        return []
    
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