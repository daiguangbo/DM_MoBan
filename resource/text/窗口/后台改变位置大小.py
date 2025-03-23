import win32gui
import win32con

def 移动窗口(窗口标题, x, y, 宽度=None, 高度=None):
    """
    移动窗口到指定位置，并可选地调整窗口大小。
    :param 窗口标题: 窗口的标题
    :param x: 新位置的 x 坐标
    :param y: 新位置的 y 坐标
    :param 宽度: 可选，新窗口的宽度
    :param 高度: 可选，新窗口的高度
    :return: None
    """
    # 查找窗口句柄
    hwnd = win32gui.FindWindow(None, 窗口标题)
    print(hwnd)
    if not hwnd:
        print(f"未找到窗口 '{窗口标题}'。")
        return

    # 获取当前窗口的状态
    窗口状态 = win32gui.GetWindowPlacement(hwnd)
    if 窗口状态[1] == win32con.SW_SHOWMINIMIZED:
        # 如果窗口被最小化，先将其恢复到正常状态
        win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)

    # 获取当前窗口的位置和大小
    左, 上, 右, 下 = win32gui.GetWindowRect(hwnd)
    当前宽度 = 右 - 左
    当前高度 = 下 - 上

    # 如果未指定宽度和高度，则使用当前窗口的宽度和高度
    if 宽度 is None:
        宽度 = 当前宽度
    if 高度 is None:
        高度 = 当前高度

    # 移动窗口到指定位置并调整大小
    win32gui.MoveWindow(hwnd, x, y, 宽度, 高度, True)
    print(f"窗口 '{窗口标题}' 已移动到 ({x}, {y})，大小为 {宽度}x{高度}。")
    return hwnd
if __name__ == '__main__':
    # 替换为你要移动的窗口标题
    窗口标题 = "大漠插件接口说明v7.2450"
    # 指定新位置和大小
    x = 100
    y = 100
    宽度 = 800
    高度 = 600
    hwnd = 移动窗口(窗口标题, x, y, 宽度, 高度)
    
    # 运行hwnd模块后窗口状态
    (0,1,(-32000,-32000),(-1,-1),(346,186,1626,906))
    # 运行hwnd模块前窗口状态
    (0,1,(-32000,-32000),(-1,-1),(100,100,900,700))
