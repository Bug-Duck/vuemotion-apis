import random
from color import get_random_color_name, Color
from class_define import *
from options_map import options_map,timingsFuctions_map,animation_map
from random_generate import *

variables_ranges_rect = {
    'x':range(100, 1600,100),  # 离散数值区间
    'y':range(100, 900,100),  # 离散数值区间
    'rotate': range(0, 360,30),  # 离散数值区间
    'scale-x': (0,1),
    'scale-y': (0,1),
    'opacity': (0,1),
    'fill-color':  Color,
    'border-color': Color,
    'border-width': range(0, 10,1),  # 离散数值区间
    'border-offset': range(0, 10,1),  # 离散数值区间
    'border-interval': [range(0, 10), range(0, 10) ],  # 离散数值区间的列表
    'width': range(50, 800,50),  # 离散数值区间
    'height': range(50, 800,50),  # 离散数值区间
    'radius': range(0,50,5),
}



def get_instance_variable_names(instance):
    # 获取实例的属性名称
    variable_names = [attr for attr in dir(instance) if not attr.startswith('__')]
    for attr in variable_names:
        if instance.__getattribute__(attr) is None:
            variable_names.remove(attr)

    return variable_names

# 定义生成随机值的函数
def generate_random_values_rect(variables_ranges):
    random_values = {}
    for var_name, values_range in variables_ranges.items():
        if var_name == 'border-interval':
            # 如果是border-interval，需要生成两个随机数
            random_value = [random.choice(list(values_range[0])), random.choice(list(values_range[1]))]
            random_values[var_name] = random_value
            continue

        if isinstance(values_range, range):
            # 如果是range类型，使用random.choice或random.randint
            random_value = random.choice(list(values_range))

        elif isinstance(values_range, list):
            # 如果是list类型，使用random.choice
            random_value = random.choice(values_range)
        elif isinstance(values_range, tuple):
            # 如果是tuple类型，表示连续区间，使用random.uniform
            # print(var_name, values_range)

            random_value = random.uniform(values_range[0], values_range[1])
            random_value = round(random_value, 2)
        elif var_name == 'fill-color' or var_name == 'border-color':
            # 如果是Color类型，使用get_random_color_name
            random_value = get_random_color_name()
        else:
            raise ValueError(f"Unsupported range type for {var_name}")
        random_values.update({var_name: random_value})
    
    return random_values





def import_state(*args):
    # 定义导入库的函数
    import_statement = ','.join(args)
    return import_statement

def import_vue_from_lib(*args):
    import_statement = ','.join(args)
    statements = f"import {{ {import_statement} }} from '@vue-motion/lib'\n"
    return statements

def import_vue_from_core(*args):
    import_statement = ','.join(args)
    statements = f"import {{ {import_statement} }} from '@vue-motion/core'\n"
    return statements

def generate_animation_params(animation, animation_params:dict):
    # 定义生成动画参数的函数
    animation_params_str = ''
    if 'duration' in animation_params:
        animation_params_str += f"duration: {animation_params['duration']},\n "
    if 'timingFunction' in animation_params:
        animation_params_str += f"by: {animation_params['timingFunction']}, \n"
    if 'duration' in animation_params or 'timingFunction' in animation_params:
        animation_params_str = f"{{ \n {animation_params_str} }},\n"
    for key,value in animation_params.items():
        if key=='duration' or key=='timingFunction':
            continue
        elif animation == 'discolorate' or animation == 'discolorateBorder' or animation == 'discolorateFill' or animation == 'discolorateTo' or animation == 'discolorateBorderTo' or animation == 'discolorateFillTo':
            animation_params_str = f" \"{value}\"," + animation_params_str
        else:
            animation_params_str = f"{value}," + animation_params_str
    

    return animation_params_str

def generate_animation_script(instance_name:str,animation_name:str, animation_params:str):
    # 定义生成动画脚本的函数
    animation_script = f"{instance_name}.{animation_name}({animation_params})\n"
    return animation_script

def generate_vue_script(name:str, animation,function_name, instance: dict,aniParams: dict):
    # 生成import语句
    arguments = []
    
    arguments = options_map[name].copy()
    if animation == 'scale' or animation == 'scaleTo':
        arguments.append('scale')
        arguments.append('scaleTo')
    functions=timingsFuctions_map[function_name]
    arguments.append('Motion')
    for i in functions:
        arguments.append(i)
    import_vue = f"import {{ { 'onMounted' } }} from 'vue'\n"
    import_lib = import_vue_from_lib(*arguments)
    # print(import_lib)
    import_core = import_vue_from_core("usePlayer","useWidget")
    
    #生成常量声明语句
    constant_declarations = ''
    ins_name = name.lower()
    constant_declarations += f"const {ins_name} = useWidget<{name}Ins>();\n"
    for key,value in instance.items():
        if key=='fill-color' or key=='border-color':
            constant_declarations += f"const {key} = \"{value}\";\n"
        else:
            constant_declarations += f"const {key} = {value};\n"

    constant_declarations += f"const {{ {"play, elapsed , useAnimation,setElapsed,pause,renderOnce"} }} = usePlayer();\n"
    
    # onMounted语句
    # animation_params = ''
    animation_params = generate_animation_params(animation,aniParams)
    animation_script = generate_animation_script(ins_name,animation,animation_params)

    # if animation=='move':
    #     animation_params = f"{aniParams['offsetX']},{aniParams['offsetY']}"
    #     if 'duration' in aniParams:
    #         if 'timingFunction' in aniParams:
    #             animation_params += f",{{ duration: {aniParams['duration']}, by: {aniParams['timingFunction']} }}"
    #         else:
    #             animation_params += f",{{ duration: {aniParams['duration']}, }},"
    #     elif 'timingFunction' in aniParams:
    #         animation_params += f",{{ by: {aniParams['timingFunction']} }},"
            # animation_params += f",{{ duration: 1 }}"
    on_play = f"play()\n"
    on_mounted = f"onMounted(() => {{\n {animation_script}  \n  {on_play}\n}} )\n"
    
    #play()
    
    
    # 生成Vue代码
    vue_script = f"<script setup lang='ts'>\n{import_vue}\n{import_lib}\n{import_core}\n{constant_declarations}\n{on_mounted} </script>\n"
    return vue_script

def generate_vue_template(template_name: str, instance):
    # 定义生成Vue代码的函数
    variables = instance
    vue_template = f"<template>\n  <Motion :width=\"1600\" :height=\"900\"> \n <{template_name} "
    vue_template += f"  :widget=\"{template_name.lower()}\""
    for key,value in variables.items():
        if key=='fill-color' or key=='border-color':
            vue_template += f"  {key}=\"{value}\""
        else:
            vue_template += f"  :{key}=\"{value}\""
    vue_template += f"/> \n"
    vue_template += f" </Motion>\n </template>\n"
    return vue_template

def main():
    number_of_samples = 10  # 定义要生成的样本数量n rang
    # all_samples = [generate_random_values_rect(variables_ranges_rect) for _ ie(number_of_samples)]

    # # 打印结果
    # for i, sample in enumerate(all_samples):
    #     print(f"Sample {i+1}: {sample}")
    num = 0
    for i in range(number_of_samples):
        
        # 生成实例对象

        rect = random_rect()
        for key,value in animation_map.items(): # 遍历动画

            animation_params = value  # 获取动画参数
            params_dict = {}
            for i in animation_params:
                if i == 'offsetX' or i == 'offsetY':
                    params_dict[i] = random.randint(50, 500)
                elif i == 'toX' or i == 'toY':
                    params_dict[i] = random.randint(50, 500)
                elif i == 'offset':
                    if key == 'discolorate' or key == 'discolorateBorder' or key == 'discolorateFill':
                        params_dict[i] = get_random_color_name()
                    else:
                        params_dict[i] = random.randint(0, 360)
                elif i == 'to':
                    if key == 'discolorateTo' or key == 'discolorateBorderTo' or key == 'discolorateFillTo':
                        params_dict[i] = get_random_color_name()
                    else:
                        params_dict[i] = random.randint(0, 360)
                elif i == 'path' and key =='moveOnPath':
                    params_dict[i] = 'M0,0 L100,100 L200,200 L300,300 L400,400 L500,500  L0,0'
                elif i == 'path' and key =='moveOnFunction':
                    continue
                else:
                    continue
                    # 尝试所有的时间函数
            # if 'timingFunction' in params_dict or 'duration' in params_dict:
            for key_func,value in timingsFuctions_map.items(): # 遍历时间函数
                if key != 'discolorate' and key != 'discolorateBorder' and key != 'discolorateFill' and key != 'discolorateTo' and key != 'discolorateBorderTo' and key != 'discolorateFillTo':
                    params_dict['timingFunction'] = value[-1]
                

                vue_script = generate_vue_script('Rect', key,key_func, rect.get_attributes(),params_dict)
                vue_template = generate_vue_template('Rect', rect.get_attributes())
                print(vue_script)
                print(vue_template)
                print()
                num += 1

    print(num)
    # print(rect.get_attributes())
    circle = Circle(x=100, y=100, scale_x=0.5, scale_y=0.5, rotation=0, opacity=1, radius=20)
    # print(circle.get_attributes())
    
    # animation_params = {'offsetX':100, 'offsetY':100,  'timingFunction':'easeInOutBack'}
    # # 生成Vue代码
    # vue_script = generate_vue_script('Rect', 'move','back', rect.get_attributes(),animation_params)
    # vue_template = generate_vue_template('Rect', rect.get_attributes())
    # print(vue_script)
    # print(vue_template)
    # 获取了实例的有效属性名称，下一步进行装填，将对应的属性按照类别生成对应的Vue代码
if __name__ == '__main__':
    main()