from source import DMClient

dm = DMClient.dm_client("127.0.0.1","9000",0)

def 左键点击(x=0,y=0,延迟=200):
    """依赖dm插件"""
    dm.Delay(延迟)
    if x != 0 and y != 0:
        dm.MoveTo(x,y)
    dm.LeftClick()

def 提取颜色和坐标坐标(str):
    """
    :param str:
    :return: [x,y,color]
    """
    # 分割输入字符串,提取坐标和颜色
    parts = str.split()
    坐标 = parts[0].split(',')
    x,y = int(坐标[0]),int(坐标[1])
    
    # 调整顺序为 RGB
    color = parts[1]
    color = color[4:6] + color[2:4] + color[0:2]
    return {
        "x":x,
        "y":y,
        "color":color
    }

def 单点找色(arr: dict,相似度=0.9):
    """
        :param arr=提取颜色和坐标坐标(str)
        :param arr: {"x":x,"y":y,"color":color}
        :return: Bool
    """
    # 调用dm.CmpColor函数
    result = dm.CmpColor(arr["x"],arr["y"],arr["color"],相似度)
    if result['value']:
        print("未找到")
        return False
    else:
        print("找到!",end="")
        return True

def 找色循环(text,回调函数=0,是否移动鼠标=0,单次找色=0):
    arr = 提取颜色和坐标坐标(text)
    if 是否移动鼠标: dm.MoveTo(arr["x"],arr["y"])
    if 单次找色:return 单点找色(arr)
    while True:
        if 单点找色(arr): break
        else: dm.Delay(200)
    
    if 回调函数 != 0 and 回调函数 != 1:
        dm.Delay(400)
        print(回调函数())
    elif 回调函数 == 1:
        左键点击(延迟=200,x=arr["x"],y=arr['y'])
        
def 查找窗口标题(title=r"C:\Users\ADMINI~1\Desktop\python\DM-server\.venv\Scripts\python.exe")->list[int]:
    keep = dm.EnumWindow(0,title,"",1 + 32)
    hwld_LIST: list = keep['value'].split(",")
    return [int(k) for k in hwld_LIST if k != ""]

def 组合按键(a="win",b="d"):
    dm.KeyDownChar(a)
    dm.KeyPressChar(b)
    dm.KeyUpChar(a)



def 确认点击完毕(text):
    arr = 提取颜色和坐标坐标(text)
    while True:
        if 单点找色(arr):
            return
        else:左键点击(arr['x'],arr['y'],400)

def 最大化窗口(hwld):
    dm.SetWindowState(hwld,1)
    dm.SetWindowState(hwld,4)
        

if __name__ == '__main__':
    a=找色循环("904,406  F8F8F8",单次找色=1)
    print(a)
    