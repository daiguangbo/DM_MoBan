# -*- coding: utf-8 -*-

# @PyCharm：2024.2.1
# @Python：3.11
# @项目：dm插件

# @文件：单例模式.py
# @时间：2025/3/21 14:39
# @作者：LexiSiy
# @邮箱：2172500693@163.com

import json
import sys
import requests
import os
import json


class 测试类:
    实例字典 = {}
    
    def __init__(self,ip,prot,index=0,单例类=None):
        self.ip = ip
        self.prot = prot
        self.index = index
        self.单练类 = 单例类
    def __new__(cls,ip,prot,index=0,单例类=None):
        key = (ip,prot,index)
        if key not in cls.实例字典:
            实例 = super(单例类,cls).__new__(cls)
            print(f'测试对象{index}创建成功!!!')
            cls.实例字典[key] = 实例
        else:
            print(f'测试对象{index}返回成功')
        return cls.实例字典[key]
    
    # noinspection PyMethodParameters
    def 测试方法(cls,参数):
        print(cls.实例字典[参数])


    
if __name__ == '__main__':
    # 不同参数的单例创建测试
    text1 = 测试类("127.0.0.1", "9000", 1,单例类=测试类) #测试对象1创建成功!!!
    text2 = 测试类("127.0.0.1", "9000", 2,单例类=测试类) #测试对象2创建成功!!!
    text3 = 测试类("127.0.0.1", "9000", 3,单例类=测试类)#测试对象3创建成功!!!
    print(text1 == text2,"and",text2 == text3) #False and False
    
    text1.测试方法(("127.0.0.1", "9000", 1)) #<__main__.测试类 object at 0x000002476C7E0310>
    text2.测试方法(("127.0.0.1", "9000", 2)) #<__main__.测试类 object at 0x000002476C92EE50>
    text3.测试方法(("127.0.0.1", "9000", 3)) #<__main__.测试类 object at 0x000002476C92EE90>
    
    # 不同参数的单练返回测试
    text1x = 测试类("127.0.0.1", "9000", 1) #测试对象1返回成功
    text2x = 测试类("127.0.0.1", "9000", 2) #测试对象2返回成功
    text3x = 测试类("127.0.0.1", "9000", 3) #测试对象3返回成功
    print(text1 == text1x,"and",text2 == text2x)  #True and True
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    