from typing import Callable, Optional, Union, List, Tuple
# import lib.Inspectable as Inspectable
from lib.Group import Group
from lib.Base import Base
from lib.AnimationBase import  AnimationBase


class Image(Group):
    def __init__(self, x: int, y: int, scale_x: float, scale_y: float, rotation: int, opacity: float, 
                 width: int, height: int, href: str):
        super().__init__(x, y, scale_x, scale_y, rotation, opacity)
        self.width = width
        self.height = height
        self.href = href

class NumberAxis(Group):
    def __init__(self, x: int, y: int, scale_x: float, scale_y: float, rotation: int, opacity: float, 
                 base_unit: str, interval: int = 100, trend: Callable[[int], str] = lambda count: str(count), 
                 font_size: Optional[int] = None, font_color: str = 'white', domain: Optional[Tuple[int, int]] = None, 
                 tip: str = 'white', trim: str = 'white'):
        super().__init__(x, y, scale_x, scale_y, rotation, opacity)
        self.base_unit = base_unit
        self.interval = interval
        self.trend = trend
        self.font_size = font_size
        self.font_color = font_color
        self.domain = domain
        self.tip = tip
        self.trim = trim

class NumberPlane(Group):
    def __init__(self, x: int, y: int, scale_x: float, scale_y: float, rotation: int, opacity: float, 
                 domain_x: Optional[Tuple[int, int]] = None, domain_y: Optional[Tuple[int, int]] = None, 
                 interval_x: int = 100, interval_y: int = 100, trend_x: Callable[[int], str] = lambda count: str(count), 
                 trend_y: Callable[[int], str] = lambda count: str(count), font_color_x: str = 'white', 
                 font_color_y: str = 'white', font_size_x: Optional[int] = None, font_size_y: Optional[int] = None, 
                 grid: bool = False, grid_color: str = 'white', grid_width: int = 1, tip_x: str = 'white', 
                 tip_y: str = 'white', base_unit: str = 'number', y_rotation: int = 90):
        super().__init__(x, y, scale_x, scale_y, rotation, opacity)
        self.domain_x = domain_x
        self.domain_y = domain_y
        self.interval_x = interval_x
        self.interval_y = interval_y
        self.trend_x = trend_x
        self.trend_y = trend_y
        self.font_color_x = font_color_x
        self.font_color_y = font_color_y
        self.font_size_x = font_size_x
        self.font_size_y = font_size_y
        self.grid = grid
        self.grid_color = grid_color
        self.grid_width = grid_width
        self.tip_x = tip_x
        self.tip_y = tip_y
        self.base_unit = base_unit
        self.y_rotation = y_rotation


class PolarPlane(Group):
    def __init__(self, x: int, y: int, scale_x: float, scale_y: float, rotation: int, opacity: float, 
                 radius: Optional[Tuple[int, int]] = None, interval: int = 100, 
                 trend: Callable[[int], str] = lambda count: str(count), 
                 azimuth_units: str = 'degrees', divide: int = 20, 
                 font_size: Optional[int] = None, font_color: str = 'white'):
        super().__init__(x, y, scale_x, scale_y, rotation, opacity)
        self.radius = radius
        self.interval = interval
        self.trend = trend
        self.azimuth_units = azimuth_units
        self.divide = divide
        self.font_size = font_size
        self.font_color = font_color

class Polygon(Group):
    def __init__(self, x: int, y: int, scale_x: float, scale_y: float, rotation: int, opacity: float, 
                 fill_color: str = "rgba(135,206,250,0.5)", border_color: str = "rgba(135,206,250,1)", 
                 border_width: int = 5, border_offset: int = 0, border_interval: List[Tuple[int, int]] = [[1, 0]], 
                 font_family: str = "", points: List[Tuple[int, int]] = []):
        super().__init__(x, y, scale_x, scale_y, rotation, opacity)
        self.fill_color = fill_color
        self.border_color = border_color
        self.border_width = border_width
        self.border_offset = border_offset
        self.border_interval = border_interval
        self.font_family = font_family
        self.points = points

class Tex(Group):
    def __init__(self, x: int, y: int, scale_x: float, scale_y: float, rotation: int, opacity: float, 
                 katex_options: Optional[dict] = None, auto_center: bool = False):
        super().__init__(x, y, scale_x, scale_y, rotation, opacity)
        self.katex_options = katex_options
        self.auto_center = auto_center

class Video(Group):
    def __init__(self, x: int, y: int, scale_x: float, scale_y: float, rotation: int, opacity: float, 
                 href: str, from_: Optional[int] = None, to: Optional[int] = None, loop: bool = False, 
                 auto_play: bool = False, fps: int = 60):
        super().__init__(x, y, scale_x, scale_y, rotation, opacity)
        self.href = href
        self.from_ = from_
        self.to = to
        self.loop = loop
        self.auto_play = auto_play
        self.fps = fps

class WebView(Group):
    def __init__(self, x: int, y: int, scale_x: float, scale_y: float, rotation: int, opacity: float, 
                 width: int, height: int):
        super().__init__(x, y, scale_x, scale_y, rotation, opacity)
        self.width = width
        self.height = height


class Line(Base):
    def __init__(self, x: int, y: int, scale_x: float, scale_y: float, rotation: int, opacity: float, 
                 from_: int, to: int):
        super().__init__(x, y, scale_x, scale_y, rotation, opacity)
        self.from_ = from_
        self.to = to

class Rect(Base):
    def __init__(self, x: int, y: int, scale_x: float, scale_y: float, rotation: int, opacity: float, 
                 width: int, height: int, radius: int = None):
        super().__init__(x, y, scale_x, scale_y, rotation, opacity)
        self.width = width
        self.height = height
        self.radius = radius

class Text(Base):
    def __init__(self, x: int, y: int, scale_x: float, scale_y: float, rotation: int, opacity: float, 
                 font_size: Union[str, int] = "", font_weight: Union[int, str] = 'normal', 
                 font_style: str = 'normal', align: str = 'start', baseline: str = 'middle', 
                 decoration: str = 'none', word_spacing: int = 0, letter_spacing: int = 0):
        super().__init__(x, y, scale_x, scale_y, rotation, opacity)
        self.font_size = font_size
        self.font_weight = font_weight
        self.font_style = font_style
        self.align = align
        self.baseline = baseline
        self.decoration = decoration
        self.word_spacing = word_spacing
        self.letter_spacing = letter_spacing

class TextUnit(Base):
    def __init__(self, x: int, y: int, scale_x: float, scale_y: float, rotation: int, opacity: float, 
                 font_size: Union[str, int] = "", font_weight: Union[int, str] = 'normal', 
                 font_style: str = 'normal', align: str = 'start', baseline: str = 'middle', 
                 decoration: str = 'none', word_spacing: int = 0, letter_spacing: int = 0):
        super().__init__(x, y, scale_x, scale_y, rotation, opacity)
        self.font_size = font_size
        self.font_weight = font_weight
        self.font_style = font_style
        self.align = align
        self.baseline = baseline
        self.decoration = decoration
        self.word_spacing = word_spacing
        self.letter_spacing = letter_spacing

class Arc(Base):
    def __init__(self, x: int, y: int, scale_x: float, scale_y: float, rotation: int, opacity: float, 
                 radius: int, from_: int, to: int):
        super().__init__(x, y, scale_x, scale_y, rotation, opacity)
        self.radius = radius
        self.from_ = from_
        self.to = to

class Circle(Base):
    def __init__(self, x: int, y: int, scale_x: float, scale_y: float, rotation: int, opacity: float, 
                 radius: int):
        super().__init__(x, y, scale_x, scale_y, rotation, opacity)
        self.radius = radius

class Ellipse(Base):
    def __init__(self, x: int, y: int, scale_x: float, scale_y: float, rotation: int, opacity: float, 
                 cx: int, cy: int, rx: int, ry: int):
        super().__init__(x, y, scale_x, scale_y, rotation, opacity)
        self.cx = cx
        self.cy = cy
        self.rx = rx
        self.ry = ry



class Rotate(AnimationBase):
    def __init__(self, duration: int,by, offset: int):
        super().__init__(duration, by)
        self.offset = offset

class RotateTo(AnimationBase):
    def __init__(self, duration: int, by, from_: int, to: int):
        super().__init__(duration,by)
        self.from_ = from_
        self.to = to

class Scale(AnimationBase):
    def __init__(self, duration: int,by, offset_x: float, offset_y: float):
        super().__init__(duration,by)
        self.offset_x = offset_x
        self.offset_y = offset_y

class ScaleTo(AnimationBase):
    def __init__(self, duration: int,by: object, from_x: float, from_y: float, to_x: float, to_y: float):
        super().__init__(duration,by)
        self.from_x = from_x
        self.from_y = from_y
        self.to_x = to_x
        self.to_y = to_y

class Move(AnimationBase):
    def __init__(self, duration: int,by: object, offset_x: int, offset_y: int):
        super().__init__(duration,by)
        self.offset_x = offset_x
        self.offset_y = offset_y

class MoveOnFunction(AnimationBase):
    def __init__(self, duration: int, by: object, path: Callable):
        super().__init__(duration,by)
        self.path = path

class MoveOnPath(AnimationBase):
    def __init__(self, duration: int,by: object, path: str):
        super().__init__(duration,by)
        self.path = path

class MoveTo(AnimationBase):
    def __init__(self, duration: int,by: object, from_x: int, from_y: int, to_x: int, to_y: int):
        super().__init__(duration,by)
        self.from_x = from_x
        self.from_y = from_y
        self.to_x = to_x
        self.to_y = to_y

class Trace(AnimationBase):
    def __init__(self, duration: int , by: object):
        super().__init__(duration,by)

class FadeIn(AnimationBase):
    def __init__(self, duration: int , by: object):
        super().__init__(duration, by)

class FadeOut(AnimationBase):
    def __init__(self, duration: int, by: object):
        super().__init__(duration, by)

class Grow(AnimationBase):
    def __init__(self, duration: int,by: object):
        super().__init__(duration, by)

class FadeTo(AnimationBase):
    def __init__(self, duration: int,by: object, from_: float, to: float):
        super().__init__(duration,by)
        self.from_ = from_
        self.to = to

class DiscolorateFillTo(AnimationBase):
    def __init__(self, duration: int, by: object, to: str):
        super().__init__(duration,by)
        self.to = to

class DiscolorateBorderTo(AnimationBase):
    def __init__(self, duration: int, by: object, to: str):
        super().__init__(duration, by)
        self.to = to
