# -*- coding: utf-8 -*-

# @PyCharm：2024.2.1
# @Python：3.11
# @项目：DM后台

# @文件：command.py
# @时间：2025/3/22 20:59
# @作者：LexiSiy
# @邮箱：2172500693@163.com
import os
import json
from source import DMClient
from demo import hwnd模块

def 提取颜色和坐标(dm,str,打印=1,obj=""):
    # 分割输入字符串,提取坐标和颜色
    parts = str.split()
    坐标 = parts[0].split(',')
    color = parts[1][4:6] + parts[1][2:4] + parts[1][0:2]
    obj = {"x":int(坐标[0]),"y":int(坐标[1]),"color":color}
    if 打印:print(obj," ---函数名称:提取颜色和坐标()")
    if obj:return obj

def 查找窗口标题(dm,打印=1,obj="")->list[int]:
    #匹配出的窗口按照窗口打开顺序依次排列
    keep = dm.EnumWindow(0,title,"",1 + 32)
    hwld_LIST: list = keep['value'].split(",")
    obj =  [int(k) for k in hwld_LIST if k != ""]
    if 打印:print(obj," ---函数名称:查找窗口标题()")
    if obj:return obj
def 获取函数名称(func):
    return " ---函数名称:" + func.__name__ + "()"
def 判断窗口是否后台绑定(dm,hwnd):
    re = dm.IsBind(hwnd)
    if re['value'] == 0:
        print("窗口未绑定",re)
        return False
    else:
        print("窗口后台已被绑定",re)
        return True
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
def 后台绑定窗口模式组合(dm,组合索引=0,打印=1):
    if 组合索引==0:
        obj = dm.BindWindowEx(hwnd,"dx2","windows3","dx.keypad.input.lock.api|dx.keypad.state.api|dx.keypad.api","dx.public.graphic.protect",0)
        if 打印: print(obj,获取函数名称(后台绑定窗口模式组合))
    if 组合索引==1:pass
def 窗口_屏幕坐标转窗口坐标(dm,hwnd,打印=1,obj=""):
    obj = dm.ClientToScreen(hwnd,0,0)
    if 打印:print(obj," ---函数名称:屏幕坐标转窗口坐标()")
    if obj:return obj
def 窗口_计算与屏幕偏移量(dm,hwnd,打印=1,obj=""):
    _=窗口_屏幕坐标转窗口坐标(dm,hwnd,打印=0)
    __=hwnd模块.获取窗口状态(hwnd,打印=0)
    x1,y1 = _['value'][0],_['value'][1]
    x2,y2 = __[4][0], __[4][1]
    obj = (x1-x2,y1-y2)
    if 打印:print(obj," ---函数名称:窗口_计算与屏幕偏移量()")
    if obj:return obj
def 键鼠_后台移动点击(dm,x,y,是否激活=0,打印=1,按键=1,双击=0,延迟=50,obj=""):
    _=鼠标_移动(dm1,x,y )
    hwnd模块.设置窗口状态(hwnd,激活=是否激活)
    dm.Delay(1000)
    if 双击:obj=(鼠标_双击(dm1),_);dm.Delay(延迟)
    else:obj=(鼠标_左键(dm1),_);dm.Delay(延迟)
    if 打印:print(obj," ---函数名称:键鼠_后台移动点击()")
    if obj:return obj

def 键鼠_组合按键(dm,a="win",b="d",打印=1,obj=""):
    _=dm.KeyDownChar(a)
    __=dm.KeyPressChar(b)
    obj=(dm.KeyUpChar(a),__,_)
    if 打印:print(obj," ---函数名称:键鼠_组合按键()")
    if obj:return obj
 
"""DM后台操作-----------------------------------------------------------------------------------------------------------------------------"""
def 后台_设置截图等待时长(dm,tiem=2000,打印=1):
    obj = dm.SetDisplayDelay(tiem)
    if 打印:print(obj,获取函数名称(后台_设置截图等待时长))
    return obj
def 后台_解除窗口绑定(dm,打印=1):
    obj = dm.UnBindWindow()
    if 打印:print(obj,获取函数名称(后台_解除窗口绑定))
    return obj
def 后台_禁止外部输入(dm,参数,打印=1):
    "0关闭 1开启 2键盘 3鼠标 4and5"
    obj = dm.LockInput(参数)
    if 打印:print(obj,获取函数名称(后台_禁止外部输入))
    if 参数 != 0 :print("注意您开启了后台_禁止外部输入,记得操作完恢复外部输入!")
    return obj
def 后台_返回dm对象绑定的窗口句柄(dm,打印=1):
    obj = dm.GetBindWindow()
    if 打印:print(obj,获取函数名称(后台_返回dm对象绑定的窗口句柄))
    return obj
def 后台_强制解绑窗口(dm,hwnd,打印=1):
    obj = dm.ForceUnBindWindow(hwnd)
    if 打印:print(obj,获取函数名称(后台_强制解绑窗口))
    return obj
def 后台_鼠标真实模拟(dm,模式,移动时间,移动速度,打印=1):
    """dm.EnableRealMouse 1,20,30 ;0关闭 1开启直线 2随机曲线 3小弧曲线 4大弧曲线"""
    obj = dm.EnableRealMouse(模式,移动时间,移动速度)
    if 打印:print(obj,获取函数名称(后台_鼠标真实模拟))
    return obj
def 后台_按键真实模拟(dm,参数,打印=1):
    """参数:0关闭 1开启"""
    obj = dm.EnableRealKeypad(参数)
    if 打印:print(obj,获取函数名称(后台_按键真实模拟))
    return obj
def 后台_设置是否鼠标同步点击(dm,参数,等待超时,打印=1):
    """参数:0关闭 1开启"""
    obj = dm.EnableMouseSync(参数,等待超时)
    if 打印:print(obj,获取函数名称(后台_设置是否鼠标同步点击))
    return obj
def 后台_设置是否键盘同步点击(dm,参数,等待超时,打印=1):
    """参数:0关闭 1开启"""
    obj = dm.EnableKeypadSync(参数,等待超时,打印=1)
    if 打印:print(obj,获取函数名称(后台_设置是否键盘同步点击))
    return obj
def 后台_DX模式鼠标关闭Windows消息(dm,参数,打印=1):
    """参数:0关闭 1开启"""
    obj = dm.EnableMouseMsg(参数)
    if 打印:print(obj,获取函数名称(后台_DX模式鼠标关闭Windows消息))
    return obj
def 后台_DX模式键盘关闭Windows消息(dm,参数,打印=1):
    """参数:0关闭 1开启"""
    obj = dm.EnableKeypadMsg(参数)
    if 打印:print(obj,获取函数名称(后台_DX模式键盘关闭Windows消息))
    return obj
def 后台_窗口假激活(dm,参数,打印=1):
    """参数:0关闭 1开启"""
    obj = dm.EnableFakeActive(参数)
    if 打印:print(obj,获取函数名称(后台_窗口假激活))
    return obj
def 后台_临时关闭后台模式(dm,参数,打印=1):
    """参数:0全关 1恢复"""
    obj = dm.EnableBind(enable)
    if 打印: print(obj,获取函数名称(后台_临时关闭后台模式))
    return obj


"""DM键鼠操作-----------------------------------------------------------------------------------------------------------------------------"""
def 鼠标_左键(dm,打印=1):
    obj = dm.LeftClick()
    if 打印: print(obj,获取函数名称(鼠标_左键))
    return obj
def 鼠标_右键(dm,打印=1):
    obj = dm.RightClick()
    if 打印: print(obj,获取函数名称(鼠标_右键))
    return obj
def 鼠标_双击(dm,打印=1):
    obj = dm.LeftDoubleClick()
    if 打印: print(obj,获取函数名称(鼠标_双击))
    return obj
def 鼠标_滚轮(dm,方向=1,打印=1,obj=""):
    """参数:0上滚 1下滚"""
    if 方向==1:obj = dm.WheelDown()
    if 方向==0:obj = dm.WheelUp()
    if 打印: print(obj,获取函数名称(鼠标_滚轮))
    return obj
def 鼠标_移动(dm,x,y,打印=1):
    obj = dm.MoveTo(x,y)
    if 打印: print(obj,获取函数名称(鼠标_移动))
    return obj
def 鼠标_左键按住(dm,打印=1):
    obj = dm.LeftDown()
    if 打印: print(obj,获取函数名称(鼠标_左键按住))
    return obj
def 鼠标_右键按住(dm,打印=1):
    obj = dm.RightDown()
    if 打印: print(obj,获取函数名称(鼠标_右键按住))
    return obj
def 鼠标_左键松开(dm,打印=1):
    obj = dm.LeftUp()
    if 打印: print(obj,获取函数名称(鼠标_左键松开))
    return obj
def 鼠标_右键松开(dm,打印=1):
    obj = dm.RightUp()
    if 打印: print(obj,获取函数名称(鼠标_右键松开))
    return obj
def 鼠标_相对移动(dm,x,y,打印=1):
    obj = dm.MoveR(x,y)
    if 打印: print(obj,获取函数名称(鼠标_相对移动))
    return obj
def 鼠标_获取位置(dm,打印=1):
    obj = dm.GetCursorPos()
    if 打印: print(obj,获取函数名称(鼠标_获取位置))
    return obj
def 鼠标_获取鼠标移动速度(dm,打印=1):
    obj = dm.GetMouseSpeed()
    if 打印: print(obj,获取函数名称(鼠标_获取鼠标移动速度))
    return obj
def 鼠标_设置鼠标移动速度(dm,speed,打印=1):
    """鼠标移动速度, 最小1，最大11.  居中为6. 推荐设置为6"""
    obj = dm.SetMouseSpeed(speed)
    if 打印: print(obj,获取函数名称(鼠标_设置鼠标移动速度))
    return obj
def 键盘_按下按键(dm,key_str,打印=1):
    obj = dm.KeyPressChar(key_str)
    if 打印: print(obj,获取函数名称(键盘_按下按键))
    return obj
def 键盘_按住按键(dm,key_str,打印=1):
    obj = dm.KeyDownChar(key_str)
    if 打印: print(obj,获取函数名称(键盘_按住按键))
    return obj
def 键盘_松开按键(dm,key_str,打印=1):
    obj = dm.KeyUpChar(key_str)
    if 打印: print(obj,获取函数名称(键盘_松开按键))
    return obj
def 鼠标_双击间隔(dm,参数,延迟,打印=1):
    "normal windows dx: delay 整形数: 延时,单位是毫秒"
    obj = dm.SetMouseDelay(参数,延迟)
    if 打印: print(obj,获取函数名称(鼠标_双击间隔))
    return obj
def 键盘_双击间隔(dm,参数,延迟,打印=1):
    "normal windows dx: delay 整形数: 延时,单位是毫秒"
    obj = dm.SetKeypadDelay(参数,延迟)
    if 打印: print(obj,获取函数名称(键盘_双击间隔))
    return obj


"""DM图色操作-----------------------------------------------------------------------------------------------------------------------------"""
def 找色_单点找色(dm,x,y,color,sim=0.8,打印=1,obj=""):
    obj = dm.CmpColor(x,y,color,sim)
    if 打印:print(obj," ---函数名称:找色_单点找色()")
    if obj:return obj

def 找图_单图(dm,x1,y1,x2,y2,pic_name,delta_color="",sim=0.8,查找方向=0,打印=1,obj=""):
    obj = dm.FindPic(x1,y1,x2,y2,pic_name,delta_color,sim,查找方向)
    if 打印:print(obj," ---函数名称:找图_单图()")
    if obj:return obj

def 找图_截图保存为bmp(dm,x1,y1,x2,y2,path_file,打印=1,obj=""):
    obj = dm.Capture(x1, y1, x2, y2, path_file)
    if 打印:print(obj," ---函数名称:找图_截图保存为bmp()")
    if obj:return obj

if __name__ == '__main__':
    title_dict = {0:["大漠插件接口说明v7.2416",(-8,-31),(0, 0, 692, 469)]}
    
    dm = DMClient.dm_client("127.0.0.1", "9000", 0)
    dm1 = DMClient.dm_client("127.0.0.1", "9000", 1)
    hwnd = hwnd模块.获取窗口句柄_标题(title_dict[0][0]);print(hwnd)
    
    鼠标_双击间隔(dm1,"windows3",10)

    后台绑定窗口模式组合(dm1)
    # 后台绑定窗口模式组合(dm)
    
    # 后台_解除窗口绑定(dm)
    # 后台_解除窗口绑定(dm1)
    
    后台_返回dm对象绑定的窗口句柄(dm)
    后台_返回dm对象绑定的窗口句柄(dm1)
    判断窗口是否后台绑定(dm,hwnd)
    
    
    # 鼠标_移动(dm1,33,203 )
    # 鼠标_左键(dm1);dm.Delay(50)

    # 鼠标_移动(dm1,358,286)
    # 鼠标_双击(dm1);dm.Delay(1000)
    # 鼠标_双击(dm1);dm.Delay(1000)
    # 鼠标_双击(dm1);dm.Delay(1000)

    # 窗口_计算与屏幕偏移量(dm,hwnd)
    # hwnd模块.设置窗口状态(hwnd,改变位置=1,位置=title_dict[0][1])


    # 键鼠_后台移动点击(dm1,358,286,双击=1,是否激活=1)
    # 键鼠_后台移动点击(dm1,358,286,双击=1,是否激活=1)
    # 键鼠_后台移动点击(dm1,358,286,双击=1,是否激活=1)
    
    坐标集合 = title_dict[0][2]
    x,y,w,h = 坐标集合[0],坐标集合[1],坐标集合[2],坐标集合[3]
    hwnd模块.设置窗口状态(hwnd,置底=1);print(x,y,w,h)
    找图_截图保存为bmp(dm1,x,y,w,h,r"C:\Users\Administrator\Desktop\DM后台\resource\demo\大漠文档.bmp")
    
    from source.dm_tools import 提取颜色和坐标
    arr = 提取颜色和坐标("268,14  0000FF");print(arr)
    找色_单点找色(dm1,arr['x'],arr['y'],arr['color'])
    
    
    
    
    
    