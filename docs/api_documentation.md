# API Documentation

## scaleTo.api

This is a animation api.

The type is in parentheses, and the default value is in square brackets.

- `duration`: The duration of the animation. (`number`)
- `by`: The timing function. (`(t: number) => number`) [t => t]
- `fromX`: The start scale on x-coordinate. (`number`)
- `fromY`: The start scale on y-coordinate. (`number`)
- `toX`: The end scale on x-coordinate. (`number`)
- `toY`: The end scale on y-coordinate. (`number`)

## Arc.api

This is a widget from package `@vue-motion/lib`.

The type is in parentheses, and the default value is in square brackets.

- `x`: The position on x-coordinate, the origin is at the center of video. (`number`) [0]
- `y`: The position on y-coordinate, the origin is at the center of video. (`number`) [0]
- `scale-x`: The scale value on x-coordinate. (`number`) [1]
- `scale-y`: The scale value on y-coordinate. (`number`) [1]
- `rotation`: The rotation angle. (`number` ranges [0, 360]) [0]
- `opacity`: The opacity value. (`number` ranges [0, 1]) [1]
- `fill-color`: The fill color. (`string`) ["rgba(135,206,250,0.5)"]
- `border-color`: The stroke color. (`string`) ["rgba(135,206,250,1)"]
- `border-width`: The stroke width. (`number`) [5]
- `border-offset`: The stroke offset. (`number`) [0]
- `border-interval`: The dash of border line. (`[number, number]`) [[1, 0]]
- `radius`: The radius of the circle. (`number`)
- `from`: The start angle. (`number` ranges [0, 360]) [0]
- `to`: The end angle. (`number` ranges [0, 360]) [360]

## discolorateBorderTo.api

This is a animation api. The animation is used to change the border color of the widget.

The type is in parentheses, and the default value is in square brackets.

- `duration`: The duration of the animation. (`number`)
- `by`: The timing function. (`(t: number) => number`) [t => t]
- `to`: The last value of the color, it can be RGB, RGBA, HSL, HSLA, and CSS color string. (`string`)

## NumberAxis.api

This is a widget from package `@vue-motion/extension-math` api.

The type is in parentheses, and the default value is in square brackets.

- `x`: The position on x-coordinate, the origin is at the center of video. (`number`) [0]
- `y`: The position on y-coordinate, the origin is at the center of video. (`number`) [0]
- `scale-x`: The scale value on x-coordinate. (`number`) [1]
- `scale-y`: The scale value on y-coordinate. (`number`) [1]
- `rotation`: The rotation angle. (`number` ranges [0, 360]) [0]
- `opacity`: The opacity value. (`number` ranges [0, 1]) [1]
- `base-unit`: The unit of a coordinate axis. (`'number' | 'radian' | 'degree'`)
- `interval`: Spacing of axes. (`number`) [100]
- `trend`: Trend function to customize the text of the tag. (`(count: number) => string`) [(count) => count.toString()]
- `font-size`: Font size. (`number`) 
- `font-color`: Font color. (`string`) ['white']
- `domain`: Axis range. (`[number, number]`)
- `tip`: Arrow color. (`string`) ["white"]
- `trim`: Arrow border color . (`string`) ["white"]
## grow.api

This is a animation api.

The type is in parentheses, and the default value is in square brackets.

This animation will gradually create the element from 0 to 1.

- `duration`: The duration of the animation. (`number`)
- `by`: The timing function. (`(t: number) => number`) [t => t]
## Image.api

This is a widget from package `@vue-motion/lib`.

The type is in parentheses, and the default value is in square brackets.

- `x`: The position on x-coordinate, the origin is at the center of video. (`number`) [0]
- `y`: The position on y-coordinate, the origin is at the center of video. (`number`) [0]
- `scale-x`: The scale value on x-coordinate. (`number`) [1]
- `scale-y`: The scale value on y-coordinate. (`number`) [1]
- `rotation`: The rotation angle. (`number` ranges [0, 360]) [0]
- `opacity`: The opacity value. (`number` ranges [0, 1]) [1]
- `width`: The width of the rectangle. (`number`)
- `height`: The height of the rectangle. (`number`)
- `href`: The url of image. (`string`)
## destory.api

This is a animation api.

The type is in parentheses, and the default value is in square brackets.

This animation will gradually destroy the element.

- `duration`: The duration of the animation. (`number`)
- `by`: The timing function. (`(t: number) => number`) [t => t]

## Group.api

This is a widget from package `@vue-motion/lib`.

The type is in parentheses, and the default value is in square brackets.

- `x`: The position on x-coordinate, the origin is at the center of video. (`number`) [0]
- `y`: The position on y-coordinate, the origin is at the center of video. (`number`) [0]
- `scale-x`: The scale value on x-coordinate. (`number`) [1]
- `scale-y`: The scale value on y-coordinate. (`number`) [1]
- `rotation`: The rotation angle. (`number` ranges [0, 360]) [0]
- `opacity`: The opacity value. (`number` ranges [0, 1]) [1]
## moveTo.api

This is a animation api.

The type is in parentheses, and the default value is in square brackets.

- `duration`: The duration of the animation. (`number`)
- `by`: The timing function. (`(t: number) => number`) [t => t]
- `fromX`: The start x-coordinate. (`number`)
- `fromY`: The start y-coordinate. (`number`)
- `toX`: The end x-coordinate. (`number`)
- `toY`: The end y-coordinate. (`number`)

## MathFunction.api

This is a widget from package `@vue-motion/extension-math` api.

The type is in parentheses, and the default value is in square brackets.

- `x`: The position on x-coordinate, the origin is at the center of video. (`number`) [0]
- `y`: The position on y-coordinate, the origin is at the center of video. (`number`) [0]
- `scale-x`: The scale value on x-coordinate. (`number`) [1]
- `scale-y`: The scale value on y-coordinate. (`number`) [1]
- `rotation`: The rotation angle. (`number` ranges [0, 360]) [0]
- `opacity`: The opacity value. (`number` ranges [0, 1]) [1]
- `fn`: Mathematical function. (`(x: number) => number`)
- `domain`: The domain of the function, that is, the range of x. (`[number, number]`)
- `ranges`: An optional y range that controls the upper and lower limits of the drawing. (`[number, number]`) [[0,0]]
- `division-x`: Calculate the X-axis step size. (`number`) [100]
- `division-y`: Calculate the Y-axis step size. (`number`) [100]
- `color`: Control the color of the graphics. (`string`) ['white']
- `width`: Control the line width of the graph. (`number`) 
- `fill-color`: Controls the fill color of the graph. (`string`) ["none"]

Notice:

- `fill-color` is not be suggested to set, because it is a function image.
- property `domain` has a division effect on the graph, the default value of `division-x` is 100, which means the concrete length of a unit of `domain` is 100. for example if you want to draw a function that's domain is [0, 10], the concrete length will be 10 * 100 = 1000. Don't set the value overloaded otherwise it will render slowly.

## Text.api

This is a widget from package `@vue-motion/lib`.

The type is in parentheses, and the default value is in square brackets.

- `x`: The position on x-coordinate, the origin is at the center of video. (`number`) [0]
- `y`: The position on y-coordinate, the origin is at the center of video. (`number`) [0]
- `scale-x`: The scale value on x-coordinate. (`number`) [1]
- `scale-y`: The scale value on y-coordinate. (`number`) [1]
- `rotation`: The rotation angle. (`number` ranges [0, 360]) [0]
- `opacity`: The opacity value. (`number` ranges [0, 1]) [1]
- `fill-color`: The fill color. (`string`) ["rgba(135,206,250,0.5)"]
- `border-color`: The stroke color. (`string`) ["rgba(135,206,250,1)"]
- `border-width`: The stroke width. (`number`) [5]
- `border-offset`: The stroke offset. (`number`) [0]
- `border-interval`: The dash of border line. (`[number, number]`) [[1, 0]]- `font_family`: The font family of the text. (`string`) [""]
- `font-size`: The font size of the text. (`'xx-small' | 'x-small' | 'small' | 'medium' | 'large' | 'x-large' | 'xx-large' | 'xxx-large' | 'larger' | 'smaller' | string | number`) [""]
- `font-weight`: The weight of the font. (`number | 'normal' | 'bold' | 'bolder' | 'lighter'`) ['normal']
- `font-style`: The style of the font. (`'normal' | 'italic' | 'oblique'`) ['normal']
- `align`: The horizontal alignment of the text. (`'start' | 'middle' | 'end'`) ['start']
- `baseline`: The vertical alignment of the text. (`'top' | 'middle' | 'bottom'`) ['middle']
- `decoration`: The decoration applied to the text. (`'none' | 'underline' | 'overline' | 'line-through' | 'blink'`) ['none']
- `word-spacing`: The space between words. (`number`) [0]
- `letter-spacing`: The space between letters. (`number`) [0]
## rotate.api

This is a animation api.

The type is in parentheses, and the default value is in square brackets.

- `duration`: The duration of the animation. (`number`)
- `by`: The timing function. (`(t: number) => number`) [t => t]
- `offset`: The offset angle. (`number`)
## Line.api

This is a widget from package `@vue-motion/lib`.

The type is in parentheses, and the default value is in square brackets.

- `x`: The position on x-coordinate, the origin is at the center of video. (`number`) [0]
- `y`: The position on y-coordinate, the origin is at the center of video. (`number`) [0]
- `scale-x`: The scale value on x-coordinate. (`number`) [1]
- `scale-y`: The scale value on y-coordinate. (`number`) [1]
- `rotation`: The rotation angle. (`number` ranges [0, 360]) [0]
- `opacity`: The opacity value. (`number` ranges [0, 1]) [1]
- `fill-color`: The fill color. (`string`) ["rgba(135,206,250,0.5)"]
- `border-color`: The stroke color. (`string`) ["rgba(135,206,250,1)"]
- `border-width`: The stroke width. (`number`) [5]
- `border-offset`: The stroke offset. (`number`) [0]
- `border-interval`: The dash of border line. (`[number, number]`) [[1, 0]]
- `from`: The start point of the line. (`[number, number]`)
- `to`: The end point of the line. (`[number, number]`)
## rotateTo.api

This is a animation api.

The type is in parentheses, and the default value is in square brackets.

- `duration`: The duration of the animation. (`number`)
- `by`: The timing function. (`(t: number) => number`) [t => t]
- `from`: The start angle. (`number`)
- `to`: The end angle. (`number`)

## Polygon.api

This is a widget from package `@vue-motion/lib`.

The type is in parentheses, and the default value is in square brackets.

- `x`: The position on x-coordinate, the origin is at the center of video. (`number`) [0]
- `y`: The position on y-coordinate, the origin is at the center of video. (`number`) [0]
- `scale-x`: The scale value on x-coordinate. (`number`) [1]
- `scale-y`: The scale value on y-coordinate. (`number`) [1]
- `rotation`: The rotation angle. (`number` ranges [0, 360]) [0]
- `opacity`: The opacity value. (`number` ranges [0, 1]) [1]
- `fill-color`: The fill color. (`string`) ["rgba(135,206,250,0.5)"]
- `border-color`: The stroke color. (`string`) ["rgba(135,206,250,1)"]
- `border-width`: The stroke width. (`number`) [5]
- `border-offset`: The stroke offset. (`number`) [0]
- `border-interval`: The dash of border line. (`[number, number]`) [[1, 0]]
- `font_family`: The font family of the text. (`string`) [""]
- `points`: The points composing the polygon. (`Array<[number, number]>`)
## Webview.api

This is a widget from package `@vue-motion/lib`.

The type is in parentheses, and the default value is in square brackets.

- `x`: The position on x-coordinate, the origin is at the center of video. (`number`) [0]
- `y`: The position on y-coordinate, the origin is at the center of video. (`number`) [0]
- `scale-x`: The scale value on x-coordinate. (`number`) [1]
- `scale-y`: The scale value on y-coordinate. (`number`) [1]
- `rotation`: The rotation angle. (`number` ranges [0, 360]) [0]
- `opacity`: The opacity value. (`number` ranges [0, 1]) [1]
- `width`: The width of the rectangle. (`number`)
- `height`: The height of the rectangle. (`number`)
## NumberPlane.api

This is a widget from package `@vue-motion/extension-math` api.

The type is in parentheses, and the default value is in square brackets.

- `x`: The position on x-coordinate, the origin is at the center of video. (`number`) [0]
- `y`: The position on y-coordinate, the origin is at the center of video. (`number`) [0]
- `scale-x`: The scale value on x-coordinate. (`number`) [1]
- `scale-y`: The scale value on y-coordinate. (`number`) [1]
- `rotation`: The rotation angle. (`number` ranges [0, 360]) [0]
- `opacity`: The opacity value. (`number` ranges [0, 1]) [1]
- `domain-x`: X axis range. (`[number, number]`)
- `domain-y`: Y axis range. (`[number, number]`)
- `interval-x`: X axis interval. (`number`) [100]
- `intervalY`: Y axis interval. (`number`) [100]
- `trend-x`: X axis label trend function. (`(count: number) => string`) [(count) => count.toString()]
- `trend-y`: Y axis label trend function. (`(count: number) => string`) [(count) => count.toString()]
- `font-color-x`: X axis font color. (`string`) ["white"]
- `font-color-y`: Y axis font color. (`string`) ["white"]
- `font-size-x`: X axis font size. (`number`) 
- `font-size-y`: Y axis font size. (`number`) 
- `grid`: Show grid. (`boolean`) [false]
- `grid-color`: Grid color. (`string`) ["white"]
- `grid-width`: Grid line width. (`number`) [1]
- `tip-x`: X axis arrow color. (`string`) ["white"]
- `tip-y`: Y axis arrow color. (`string`) ["white"]
- `base-unit`: The unit of a coordinate axis. (`'number' | 'radian' | 'degree'`)
- `y-rotation`: Control the rotation Angle of Y-axis text. (`number` ranges [0, 360]) [90]

Notice:

- property `domain-x` and `domain-y` has a division effect on the graph, the default value of `interval-x` and `interval-y` is 100, which means the concrete length of a unit of `domain` is 100. for example if you want to draw a function that's domain is [0, 10], the concrete length will be 10 * 100 = 1000. Don't set the value overloaded otherwise it will render slowly.

## move.api

This is a animation api.

The type is in parentheses, and the default value is in square brackets.

- `duration`: The duration of the animation. (`number`)
- `by`: The timing function. (`(t: number) => number`) [t => t]
- `offsetX`: The offset on x-coordinate. (`number`)
- `offsetY`: The offset on y-coordinate. (`number`)

## discolorateFillTo.api

This is a animation api. The animation is used to change the fill color of the widget.

The type is in parentheses, and the default value is in square brackets.

- `duration`: The duration of the animation. (`number`)
- `by`: The timing function. (`(t: number) => number`) [t => t]
- `to`: The last value of the color, it can be RGB, RGBA, HSL, HSLA, and CSS color string. (`string`)

## PolarPlane.api

This is a widget from package `@vue-motion/extension-math` api.

The type is in parentheses, and the default value is in square brackets.

- `x`: The position on x-coordinate, the origin is at the center of video. (`number`) [0]
- `y`: The position on y-coordinate, the origin is at the center of video. (`number`) [0]
- `scale-x`: The scale value on x-coordinate. (`number`) [1]
- `scale-y`: The scale value on y-coordinate. (`number`) [1]
- `rotation`: The rotation angle. (`number` ranges [0, 360]) [0]
- `opacity`: The opacity value. (`number` ranges [0, 1]) [1]
- `radius`: The radius of the polar coordinate system. (`[number, number]`)
- `interval`: Angular intervals, used to draw arcs.. (`number`) [100]
- `trend`: Trend function to calculate the Angle trend function. (`(count: number) => string`) [(count) => count.toString()]
- `azimuth-units`: Angular unit. (`'PI radians' | 'TAU radians' | 'degrees' | 'gradians'`) 
- `divide`: Controls how many parts of the polar coordinate plane are divided. (`number`) [20]
- `font-size`: Font size. (`number`) 
- `font-color`: Font color. (`string`) ['white']
## Video.api

This is a widget from package `@vue-motion/lib`.

The type is in parentheses, and the default value is in square brackets.

- `x`: The position on x-coordinate, the origin is at the center of video. (`number`) [0]
- `y`: The position on y-coordinate, the origin is at the center of video. (`number`) [0]
- `scale-x`: The scale value on x-coordinate. (`number`) [1]
- `scale-y`: The scale value on y-coordinate. (`number`) [1]
- `rotation`: The rotation angle. (`number` ranges [0, 360]) [0]
- `opacity`: The opacity value. (`number` ranges [0, 1]) [1]
- `href`: The URL of the video. (`string`)
- `from`: The start time of the video. (`number`)
- `to`: The end time of the video. (`number`)
- `loop`: Whether the video is looped. (`boolean`) [false]
- `auto-play`: Whether the video is autoplayed. (`boolean`) [false]
- `fps`: The frame rate of the video. (`number`) [60]

## Tex.api

This is a widget from package `@vue-motion/extension-math` api.

The type is in parentheses, and the default value is in square brackets.

- `x`: The position on x-coordinate, the origin is at the center of video. (`number`) [0]
- `y`: The position on y-coordinate, the origin is at the center of video. (`number`) [0]
- `scale-x`: The scale value on x-coordinate. (`number`) [1]
- `scale-y`: The scale value on y-coordinate. (`number`) [1]
- `rotation`: The rotation angle. (`number` ranges [0, 360]) [0]
- `opacity`: The opacity value. (`number` ranges [0, 1]) [1]
- `katex-options`: Configuration options to pass to katex rendering. (`katex.KatexOptions`)
- `auto-center`: Whether the formula is automatically centered to render. (`boolean`)

## Circle.api

This is a widget from package `@vue-motion/lib`.

The type is in parentheses, and the default value is in square brackets.

- `x`: The position on x-coordinate, the origin is at the center of video. (`number`) [0]
- `y`: The position on y-coordinate, the origin is at the center of video. (`number`) [0]
- `scale-x`: The scale value on x-coordinate. (`number`) [1]
- `scale-y`: The scale value on y-coordinate. (`number`) [1]
- `rotation`: The rotation angle. (`number` ranges [0, 360]) [0]
- `opacity`: The opacity value. (`number` ranges [0, 1]) [1]
- `fill-color`: The fill color. (`string`) ["rgba(135,206,250,0.5)"]
- `border-color`: The stroke color. (`string`) ["rgba(135,206,250,1)"]
- `border-width`: The stroke width. (`number`) [5]
- `border-offset`: The stroke offset. (`number`) [0]
- `border-interval`: The dash of border line. (`[number, number]`) [[1, 0]]
- `radius`: The radius of the circle. (`number`)
## discolorateFill.api

This is a animation api. The animation is used to change the fill color of the widget.

The type is in parentheses, and the default value is in square brackets.

- `duration`: The duration of the animation. (`number`)
- `by`: The timing function. (`(t: number) => number`) [t => t]
- `offset`: The offset value of the color, it can be RGB, RGBA, HSL, HSLA, and CSS color string. (`string`)

## fadeIn.api

This is a animation api.

The type is in parentheses, and the default value is in square brackets.

- `duration`: The duration of the animation. (`number`)
- `by`: The timing function. (`(t: number) => number`) [t => t]

## TextUnit.api

This is a widget from package `@vue-motion/lib`.

The type is in parentheses, and the default value is in square brackets.

- `x`: The position on x-coordinate, the origin is at the center of video. (`number`) [0]
- `y`: The position on y-coordinate, the origin is at the center of video. (`number`) [0]
- `scale-x`: The scale value on x-coordinate. (`number`) [1]
- `scale-y`: The scale value on y-coordinate. (`number`) [1]
- `rotation`: The rotation angle. (`number` ranges [0, 360]) [0]
- `opacity`: The opacity value. (`number` ranges [0, 1]) [1]
- `fill-color`: The fill color. (`string`) ["rgba(135,206,250,0.5)"]
- `border-color`: The stroke color. (`string`) ["rgba(135,206,250,1)"]
- `border-width`: The stroke width. (`number`) [5]
- `border-offset`: The stroke offset. (`number`) [0]
- `border-interval`: The dash of border line. (`[number, number]`) [[1, 0]]- `font_family`: The font family of the text. (`string`) [""]
- `font-size`: The font size of the text. (`'xx-small' | 'x-small' | 'small' | 'medium' | 'large' | 'x-large' | 'xx-large' | 'xxx-large' | 'larger' | 'smaller' | string | number`) [""]
- `font-weight`: The weight of the font. (`number | 'normal' | 'bold' | 'bolder' | 'lighter'`) ['normal']
- `font-style`: The style of the font. (`'normal' | 'italic' | 'oblique'`) ['normal']
- `align`: The horizontal alignment of the text. (`'start' | 'middle' | 'end'`) ['start']
- `baseline`: The vertical alignment of the text. (`'top' | 'middle' | 'bottom'`) ['middle']
- `decoration`: The decoration applied to the text. (`'none' | 'underline' | 'overline' | 'line-through' | 'blink'`) ['none']
- `word-spacing`: The space between words. (`number`) [0]
- `letter-spacing`: The space between letters. (`number`) [0]
## fadeOut.api

This is a animation api.

The type is in parentheses, and the default value is in square brackets.

- `duration`: The duration of the animation. (`number`)
- `by`: The timing function. (`(t: number) => number`) [t => t]

## fadeTo.api

This is a animation api.

The type is in parentheses, and the default value is in square brackets.

- `duration`: The duration of the animation. (`number`)
- `by`: The timing function. (`(t: number) => number`) [t => t]
- `from`: The start opacity. (`number`)
- `to`: The end opacity. (`number`)

## moveOnFunction.api

This is a animation api. The `moveOnFunction` animation is used to move the widget on the mathematical function.

The type is in parentheses, and the default value is in square brackets.

- `duration`: The duration of the animation. (`number`)
- `by`: The timing function. (`(t: number) => number`) [t => t]
- `path`: The function. (`(progress: number) => { x: number, y: number }`)

## scale.api

This is a animation api.

The type is in parentheses, and the default value is in square brackets.

- `duration`: The duration of the animation. (`number`)
- `by`: The timing function. (`(t: number) => number`) [t => t]
- `offsetX`: The scale value on x-coordinate. (`number`)
- `offsetY`: The scale value on y-coordinate. (`number`)
## discolorateBorder.api

This is a animation api. The animation is used to change the border color of the widget.

The type is in parentheses, and the default value is in square brackets.

- `duration`: The duration of the animation. (`number`)
- `by`: The timing function. (`(t: number) => number`) [t => t]
- `offset`: The offset value of the color, it can be RGB, RGBA, HSL, HSLA, and CSS color string. (`string`)

## moveOnPath.api

This is a animation api. The `moveOnPath` animation is used to move the widget on the SVG path.

The type is in parentheses, and the default value is in square brackets.

- `duration`: The duration of the animation. (`number`)
- `path`: The SVG path. (`string`)

## Ellipse.api

This is a widget from package `@vue-motion/lib`.

The type is in parentheses, and the default value is in square brackets.

- `x`: The position on x-coordinate, the origin is at the center of video. (`number`) [0]
- `y`: The position on y-coordinate, the origin is at the center of video. (`number`) [0]
- `scale-x`: The scale value on x-coordinate. (`number`) [1]
- `scale-y`: The scale value on y-coordinate. (`number`) [1]
- `rotation`: The rotation angle. (`number` ranges [0, 360]) [0]
- `opacity`: The opacity value. (`number` ranges [0, 1]) [1]
- `fill-color`: The fill color. (`string`) ["rgba(135,206,250,0.5)"]
- `border-color`: The stroke color. (`string`) ["rgba(135,206,250,1)"]
- `border-width`: The stroke width. (`number`) [5]
- `border-offset`: The stroke offset. (`number`) [0]
- `border-interval`: The dash of border line. (`[number, number]`) [[1, 0]]
- `radius`: The radius of the circle. (`number`)
- `cx`: The x-coordinate of the center of the ellipse. (`number`)
- `cy`: The y-coordinate of the center of the ellipse. (`number`)
- `rx`: The x-radius of the ellipse. (`number`)
- `ry`: The y-radius of the ellipse. (`number`)
- `width`: The width of the ellipse. (`number`)
- `height`: The height of the ellipse. (`number`)

## trace.api

This is a animation api.

The type is in parentheses, and the default value is in square brackets.

This animation will gradually change the stroke of the element.

- `duration`: The duration of the animation. (`number`)
- `by`: The timing function. (`(t: number) => number`) [t => t]

## Rect.api

This is a widget from package `@vue-motion/lib`.

The type is in parentheses, and the default value is in square brackets.

- `x`: The position on x-coordinate, the origin is at the center of video. (`number`) [0]
- `y`: The position on y-coordinate, the origin is at the center of video. (`number`) [0]
- `scale-x`: The scale value on x-coordinate. (`number`) [1]
- `scale-y`: The scale value on y-coordinate. (`number`) [1]
- `rotation`: The rotation angle. (`number` ranges [0, 360]) [0]
- `opacity`: The opacity value. (`number` ranges [0, 1]) [1]
- `fill-color`: The fill color. (`string`) ["rgba(135,206,250,0.5)"]
- `border-color`: The stroke color. (`string`) ["rgba(135,206,250,1)"]
- `border-width`: The stroke width. (`number`) [5]
- `border-offset`: The stroke offset. (`number`) [0]
- `border-interval`: The dash of border line. (`[number, number]`) [[1, 0]]
- `width`: The width of the rectangle. (`number`)
- `height`: The height of the rectangle. (`number`)
- `radius`: The radius of the rectangle's four summits. (`number`)
