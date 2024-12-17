import random
from class_define import *
from color import *
def random_base() -> Base:
    """随机生成一个 Base 类的实例"""
    x = random.randint(0, 100)  # 随机生成 x 坐标
    y = random.randint(0, 100)  # 随机生成 y 坐标
    scale_x = random.uniform(0.5, 2.0)  # 随机生成 x 方向缩放比例
    scale_y = random.uniform(0.5, 2.0)  # 随机生成 y 方向缩放比例
    rotation = random.randint(0, 360)  # 随机生成旋转角度
    opacity = random.uniform(0.0, 1.0)  # 随机生成透明度
    fill_color =  get_random_color_name()  # 生成随机填充颜色
    border_color = get_random_color_name()  # 生成随机边框颜色
    border_width = random.randint(1, 10)  # 随机生成边框宽度
    border_offset = random.randint(0, 10)  # 随机生成边框偏移
    border_interval = (random.randint(0, 5), random.randint(0, 5))  # 随机生成边框间隔

    # 创建并返回 Base 类的实例
    return Base(x, y, scale_x, scale_y, rotation, opacity,
                fill_color, border_color, border_width,
                border_offset, border_interval)

def random_group() -> Group:
    """随机生成一个 Group 类的实例"""
    x = random.randint(0, 100)  # 随机生成 x 坐标
    y = random.randint(0, 100)  # 随机生成 y 坐标
    scale_x = random.uniform(0.5, 2.0)  # 随机生成 x 方向缩放比例
    scale_y = random.uniform(0.5, 2.0)  # 随机生成 y 方向缩放比例
    rotation = random.randint(0, 360)  # 随机生成旋转角度
    opacity = random.uniform(0.0, 1.0)  # 随机生成透明度
    

    # 创建并返回 Group 类的实例
    return Group(x, y, scale_x, scale_y, rotation, opacity)

def random_line() -> Line:
    """随机生成一个 Line 类的实例"""
    x = random.randint(0, 100)  # 随机生成 x 坐标
    y = random.randint(0, 100)  # 随机生成 y 坐标
    scale_x = random.uniform(0.5, 2.0)  # 随机生成 x 方向缩放比例
    scale_y = random.uniform(0.5, 2.0)  # 随机生成 y 方向缩放比例
    rotation = random.randint(0, 360)  # 随机生成旋转角度
    opacity = random.uniform(0.0, 1.0)  # 随机生成透明度
    fill_color =  get_random_color_name()  # 生成随机填充颜色
    border_color = get_random_color_name()  # 生成随机边框颜色
    border_width = random.randint(1, 10)  # 随机生成边框宽度
    border_offset = random.randint(0, 10)  # 随机生成边框偏移
    border_interval = (random.randint(0, 5), random.randint(0, 5))  # 随机生成边框间隔

    # 创建并返回 Line 类的实例
    return Line(x, y, scale_x, scale_y, rotation, opacity,
                fill_color, border_color, border_width,
                border_offset, border_interval)

def random_rect() -> Rect:
    """随机生成一个 Rect 类的实例"""
    x = random.randint(0, 100)  # 随机生成 x 坐标
    y = random.randint(0, 100)  # 随机生成 y 坐标
    scale_x = random.uniform(0.5, 2.0)  # 随机生成 x 方向缩放比例
    scale_y = random.uniform(0.5, 2.0)  # 随机生成 y 方向缩放比例
    rotation = random.randint(0, 360)  # 随机生成旋转角度
    opacity = random.uniform(0.0, 1.0)  # 随机生成透明度
    # fill_color =  get_random_color_name()  # 生成随机填充颜色
    # border_color = get_random_color_name()  # 生成随机边框颜色
    # border_width = random.randint(1, 10)  # 随机生成边框宽度
    # border_offset = random.randint(0, 10)  # 随机生成边框偏移
    # border_interval = (random.randint(0, 5), random.randint(0, 5))  # 随机生成边框间隔
    width = random.randint(50, 500)  # 随机生成宽度
    height = random.randint(50, 500)  # 随机生成高度
    radius = random.randint(0, 20)  # 随机生成圆角半径
    # 创建并返回 Rect 类的实例
    return Rect(x, y, scale_x, scale_y, rotation, opacity,width, height, radius)

def random_text() -> Text:
    """随机生成一个 Text 类的实例"""
    x = random.randint(0, 100)  # 随机生成 x 坐标
    y = random.randint(0, 100)  # 随机生成 y 坐标
    scale_x = random.uniform(0.5, 2.0)  # 随机生成 x 方向缩放比例
    scale_y = random.uniform(0.5, 2.0)  # 随机生成 y 方向缩放比例
    rotation = random.randint(0, 360)  # 随机生成旋转角度
    opacity = random.uniform(0.0, 1.0)  # 随机生成透明度
    fill_color =  get_random_color_name()  # 生成随机填充颜色
    border_color = get_random_color_name()  # 生成随机边框颜色
    border_width = random.randint(1, 10)  # 随机生成边框宽度
    border_offset = random.randint(0, 10)  # 随机生成边框偏移
    border_interval = (random.randint(0, 5), random.randint(0, 5))  # 随机生成边框间隔

    # 创建并返回 Text 类的实例
    return Text(x, y, scale_x, scale_y, rotation, opacity,
                fill_color, border_color, border_width,
                border_offset, border_interval)
