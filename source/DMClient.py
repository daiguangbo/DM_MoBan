# -*- coding: utf-8 -*-
"""
@Time ： 2023/2/7 0:26
@Auth ： 大雄
@File ：client.py
@IDE ：PyCharm
@Email:3475228828@qq.com
@func:功能
"""

import json
import sys
import requests
import os
import json

class dm_client:
    实例字典 = {}

    def __init__(self, ip, prot, index=0):
        self.ip = ip
        self.prot = prot
        self.index = index

    def __new__(cls, ip, prot, index=0):
        key = (ip, prot, index)
        if key not in cls.实例字典:
            实例 = super(dm_client, cls).__new__(cls)
            # print(f'大漠对象{index}创建成功!!!')
            cls.实例字典[key] = 实例
        else:
            pass
            # print(f'大漠对象{index}返回成功')
        return cls.实例字典[key]
        
    def __getattribute__(self,item):
        ret = super().__getattribute__(item)
        if str(type(ret))=="<class 'function'>" or str(type(ret))=="<class 'method'>":
            global  temp
            temp = ret
            def res(*args):
                data = {
                    "dm_num":self.index,# 如果不写默认使用序号0
                    "func":str(temp.__name__),
                    "args":args,
                }
                return requests.post(f'http://{self.ip}:{self.prot}/login', json=data).json()
            return res
        else:
            return ret
    @staticmethod
    def GetDmCount():
        pass

    @staticmethod
    def Ver():
        """获取版本信息。"""
        pass

    @staticmethod
    def LeftClick():
        """模拟鼠标左键点击"""
        pass

    @staticmethod
    def Delay(num):
        """延时一定时间"""
        pass

    @staticmethod
    def MoveTo(x: int, y: int):
        """模拟鼠标移动到指定位置"""
        pass
    
    @staticmethod
    def RightClick():
        """模拟鼠标右键点击"""
        pass
    
    @staticmethod
    def Ocr(x1, y1, x2, y2, color_format, sim):
        """使用OCR技术识别指定区域内的文本"""
        pass
    
    @staticmethod
    def RunApp(app_path, mode):
        """运行指定的应用程序"""
        pass
    
    @staticmethod
    def GetID():
        pass
    
    @staticmethod
    def LeftDown():
        """模拟按住左键点击"""
        pass
    
    @staticmethod
    def LeftUp():
        """模拟按住左键点击"""
        pass
    
    @staticmethod
    def MoveR(rx,ry):
        """
        移动鼠标
        参数定义:
        rx: 鼠标移动的x轴偏移量
        ry: 鼠标移动的y轴偏移量
        """
    @staticmethod
    def EnableMouseAccuracy(enable):
        """鼠标精准度开关"""
    
    @staticmethod
    def WheelUp():
        """模拟鼠标滚轮向上"""
    
    @staticmethod
    def WheelDown():
        """模拟鼠标滚轮向下"""
        

    """按键操作合集"""
    @staticmethod
    def KeyDownChar(key_str):pass
    @staticmethod
    def KeyPressChar(key_str):pass
    @staticmethod
    def KeyPressStr(key_str,delay):pass
    @staticmethod
    def KeyUpChar(key_str):pass
    @staticmethod
    def GetCursorPos():pass
    
    
    """窗口操作"""
    @staticmethod # 枚举进程,按打开先后排序
    def EnumProcess(name):pass
    
    @staticmethod # 枚举系统中符合条件的窗口
    def EnumWindow(parent,title,class_name,filter):pass
                
    @staticmethod # 枚举指定进程下的窗口
    def EnumWindowByProcess(process_name,title,class_name,filter):
        pass

    @staticmethod # 移动窗口
    def MoveWindow(hwnd,x,y):
        pass
    
    @staticmethod #设置窗口的状态
    def SetWindowState(hwnd, flag):pass

    @staticmethod
    def GetWindowState(hwnd,flag):pass


    """其他函数"""
    @staticmethod #蜂鸣器-频率&时长
    def Beep(f=2500,duration=1000):
        pass
    
    @staticmethod #获取剪贴板内容
    def GetClipboard():
        pass
    
    @staticmethod #获取显卡信息
    def GetDisplayInfo():
        pass
    
    @staticmethod #设置剪贴板内容
    def SetClipboard(value):
        pass
    
    @staticmethod #显示任务栏图标
    def ShowTaskBarIcon(hwnd,is_show):
        """is_show 整形数: 0为隐藏,1为显示"""
        pass
        
    @staticmethod # 获取注册在系统中的dm.dll的路径.
    def GetBasePath():
        pass
    
    """后台设置---------------------------------------------------------------------------------------------------------------------------"""
    @staticmethod
    def BindWindow(hwnd, display, mouse, keypad, mode): pass
    
    @staticmethod
    def BindWindowEx(hwnd, display, mouse, keypad, public, mode): pass
    
    @staticmethod
    def DownCpu(type, rate): pass
    
    @staticmethod
    def EnableBind(enable): pass
    
    @staticmethod
    def EnableFakeActive(enable): pass
    
    @staticmethod
    def EnableIme(enable): pass
    
    @staticmethod
    def EnableKeypadMsg(enable): pass
    
    @staticmethod
    def EnableKeypadPatch(enable): pass
    
    @staticmethod
    def EnableKeypadSync(enable, time_out): pass
    
    @staticmethod
    def EnableMouseMsg(enable): pass
    
    @staticmethod
    def EnableMouseSync(enable, time_out): pass
    
    @staticmethod
    def EnableRealKeypad(enable): pass
    
    @staticmethod
    def EnableRealMouse(enable, mousedelay, mousestep): pass
    
    @staticmethod
    def EnableSpeedDx(enable): pass
    
    @staticmethod
    def ForceUnBindWindow(hwnd): pass
    
    @staticmethod
    def GetBindWindow(): pass
    
    @staticmethod
    def GetFps(): pass
    
    @staticmethod
    def HackSpeed(rate): pass
    
    @staticmethod
    def IsBind(hwnd): pass
    
    @staticmethod
    def LockDisplay(lock): pass
    
    @staticmethod
    def LockInput(lock): pass
    
    @staticmethod
    def LockMouseRect(x1, y1, x2, y2): pass
    
    @staticmethod
    def SetAero(enable): pass
    
    @staticmethod
    def SetDisplayDelay(time): pass
    
    @staticmethod
    def SetDisplayRefreshDelay(time): pass
    
    @staticmethod
    def SetInputDm(dm_id, rx, ry): pass
    
    @staticmethod
    def SwitchBindWindow(hwnd): pass
    
    @staticmethod
    def UnBindWindow(): pass

    @staticmethod # 临时的截图函数
    def FaqCaptureFromFile(x1, y1, x2, y2, file, quality):pass

    @staticmethod
    def ClientToScreen(hwnd,x,y):pass
    
    @staticmethod
    def GetLastError():pass
    
    @staticmethod
    def EnumWindowSuper(spec1,flag1,type1,spec2,flag2,type2,sort):pass

    @staticmethod
    def LeftDoubleClick():pass
    
    """防护盾状态-------------------------------------------------------------------------------------------------------------------------"""
    @staticmethod
    def DmGuard(enable,type):pass
    
    @staticmethod
    def DmGuardExtract(type,path):pass
    
    @staticmethod
    def DmGuardLoadCustom(type,path):pass
    
    @staticmethod
    def DmGuardParams(cmd,subcmd,param):pass
    
    @staticmethod
    def UnLoadDriver():pass
    
    """图色操作---------------------------------------------------------------------------------------------------------------------------"""
    @staticmethod
    def FindPic(x1,y1,x2,y2,pic_name,delta_color,sim,dir):
        """在指定区域内查找图片:dm.FindPic(0,0,200,400,"1.bmp|3.bmp","000000",0.9,0"""
        pass
    @staticmethod
    def Capture(x1,y1,x2,y2,file):
        """抓取位图"""
        pass
    @staticmethod
    def BGR2RGB(bgr_color):
        """把BGR(按键格式)的颜色格式转换为RGB"""
        pass
    @staticmethod
    def FindMultiColor(x1,y1,x2,y2,first_color,offset_color,sim,dir):
        """根据指定的多点查找颜色坐标"""
        pass
    @staticmethod
    def CaptureGif(x1,y1,x2,y2,file,delay,time):
        """捕获屏幕上的指定区域并保存为GIF动画文件"""
        pass
    @staticmethod
    def CmpColor(x,y,color,sim):
        """比较指定坐标的颜色与给定颜色的相似度"""
        pass
    @staticmethod
    def FindStr(x1,y1,x2,y2,string,color_format,sim):
        """在指定区域内查找指定颜色格式的字符串"""
        pass
    @staticmethod
    def ImageToBmp(pic_name,bmp_name):
        """图片转为24为bmp图片"""
        pass
    
    
    
    
    
    @staticmethod
    def SetMouseDelay(type,delay):pass