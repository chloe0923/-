"""
pip3 install vpython
"""
from vpython import *
from datetime import datetime
import math 
import random
import os
import statistics

"""
1. 參數設定, 設定變數及初始值
"""
file_name = "tmp2.txt"
file = open(file_name, "w")
# time  s(sec)
time_to_close = 60*60*24   #結束檔案的時間
t = 0
is_pull_apart_ratio = 5
pull_apart_ratio_to_close = 10
# dt = 86400
# dt = 7200
# dt = 3600
# dt = 1800
# dt = 600
dt = 300
# dt = 60
# dt = 1
# dt = 0.1
# dt = 0.01
# dt = 0.001
# dt = 0.0001
# dt = 0.0000001
# dt = 0.00000001
# dt = 0.000001
# dt = 0.00001
# draw_rate = 1/dt
draw_rate = 5000000
G=6.67e-11
k = 0
# k = 0.00000001
# k = 0.001
# k = 1
# k = 1000

# dis_unit=1000     #所使用的距離及座標單位為公尺的幾倍
dis_unit=1

"""
 2. 畫面設定
"""
scene = canvas(title="Vertical Circle", width=800, height=700, x=0, y=0, background=color.yellow)
is_started = False
def clickStartButton(b):
    global earth_sphere, balls_list, v0, is_started
    earth_sphere.visible = True
    is_started = True
    for ball in balls_list:
        ball.v = v0
button_start = button(text="start", pos=scene.title_anchor, bind=clickStartButton)

camera_to_earth = True
def clickButton(b):
    global camera_to_earth, earth_sphere
    camera_to_earth = not camera_to_earth
    if camera_to_earth:
        scene.camera.follow(earth_sphere)
    
b1 = button(text="switch camera", pos=scene.title_anchor, bind=clickButton)

is_pull_apart = False
def closeAndSave():
    for ball in balls_list:
        print (f'ball pos: {ball.pos.x} {ball.pos.y} {ball.pos.z}')
    global file
    if not is_started:
        return
    if is_pull_apart:
        file.write("Pull Apart\n")
    else:
        file.write("Not Pull Apart\n")
    file.write(f'mass:{external_ball_mass} kg\n')
    file.write(f'full_mass:{full_external_ball_mass} kg')
    file.close()
    now = datetime.now()
    dt_string = now.strftime("%Y%m%d_%H%M")
    new_file_name = f'{dt_string}_mass_{full_external_ball_mass}_dis_{dis_R}_{is_pull_apart}.txt'
    os.rename(file_name, new_file_name)
    exit()


def clickEndButton(b):
    closeAndSave()
button_end = button(text="end", pos=scene.title_anchor, bind=clickEndButton)

#dis_R 地球和繞行天體的距離 m
# dis_R = 384399/60*1000
# dis_R = 384399/40*1000
# dis_R = 384399/20*1000
# dis_R = 384399/15*1000
# dis_R = 384399/5*1000
# dis_R = 384399/2*1000
# dis_R = 384399/4*3*1000
# dis_R = 1120*1000
# dis_R = 384399*1000
# dis_R = 6371*1000*1.5
# dis_R = 6371*1000*3.125
# dis_R = 6371*1000*2
# dis_R = 6371*1000*2.5
# dis_R = 6371*1000*1.8
# dis_R = 6371*1000*2.7
# dis_R = 6371*1000*2.9
# dis_R = 6371*1000*2.6
# dis_R = 6371*1000*2.3
# dis_R = 6371*1000*3
# dis_R = 6371*1000*3.2
# dis_R = 6371*1000*3.25
# dis_R = 6371*1000*3.3
# dis_R = 6371*1000*3.4
dis_R = 6371*1000*3.5
# dis_R = 6371*1000*3.6
# dis_R = 6371*1000*4
# dis_R = 38439900*1000

# full_external_ball_mass = 5.5e+10    #整個天體的質量
# full_external_ball_mass = 2.8e+6
full_external_ball_mass = 5e+5
# full_external_ball_mass = 5.4e+5
# full_external_ball_mass = 7.5e+5
# full_external_ball_mass = 2.3e+6
# full_external_ball_mass = 2.8e+6
# full_external_ball_mass = 3.5e+6
# full_external_ball_mass = 9.8e+6
# full_external_ball_mass = 3e+7
# full_external_ball_mass = 3.3e+7
# full_external_ball_mass = 3.4e+7
# full_external_ball_mass = 4.1e+7

# moon_external_ball_num = 27
# moon_external_ball_num = 64
moon_external_ball_num = 81
# external_ball_mass = 7.3477e+22/moon_external_ball_num    #會形變但不會被完全拉開，dt=1800，正常地月半徑
external_ball_mass = full_external_ball_mass/moon_external_ball_num
# external_ball_mass = 50  #會被拉開，dt=86400，正常地月半徑
# external_ball_mass = 9.3e10/moon_external_ball_num
# external_ball_radius = 5000000 #小球本身的半徑, 為顯示效果  m
# external_ball_radius = 100000
external_ball_radius = 100
# ball_center_dis = 10000000     #初始小球和繞行天體中心的最大距離 m
# ball_center_dis = 4100000
# ball_center_dis = 17371000
# ball_center_dis = 0.17
# ball_center_dis = 170
# ball_center_dis = 6.5
ball_center_dis = 3.5
# ball_center_dis = 4
# ball_center_dis = 6
# ball_center_dis = 6.5
# ball_center_dis = 7
# ball_center_dis = 9.5
# ball_center_dis = 14
# ball_center_dis = 14.5
spring_force_dis_threshold = ball_center_dis   # m
# spring_force_dis_threshold = 10000
moon_external_ball ={
    'name':'moon_external_ball',
    'radius':external_ball_radius,
    'texture':textures.rock,
}

"""
地球
"""
earth ={
    'name':'Earth',
    'mass':5.972e+24,   #kg  
    'radius':6371000,        #m , real data
    # 'radius':67310000,     # 為了顯示效果
    # 'radius':6731, 
    'texture':textures.earth,
}

earth_sphere = sphere(
    pos=vec(0, 0, 0), 
    # axis=vec(0, 5, 0), 
    radius=earth['radius']/dis_unit, 
    texture = earth['texture'], 
    emissive = False, 
    M = earth['mass'])
earth_sphere.visible = False
# 將地球旋轉至北極面向攝影機
earth_sphere.rotate(angle=radians(90), axis=vec(1, 0, 0))

balls_list = []
g = G*earth['mass']/((dis_R)**2) #m/s^2
external_pos = vec(dis_R/dis_unit, 0, 0)
v0=vec(0, sqrt(g*(dis_R))/dis_unit, 0)  #m/s
# v0*=1000

for _ in range(moon_external_ball_num):
    r = random.uniform(0, ball_center_dis/dis_unit)
    theta = random.uniform(0, 2*math.pi)
    phi = random.uniform(0, 2*math.pi)
    pos = vec(
        r*math.sin(theta)*math.cos(phi), 
        r*math.sin(theta)*math.sin(phi), 
        r*math.cos(theta))
    pos+=external_pos   #把小球移到繞行天體所在位置
    ball = sphere(
        pos=pos, 
        radius=moon_external_ball['radius']/dis_unit, 
        make_trail=True, 
        trail_color = color.blue, 
        # interval = 10, 
        retain=1, 
        # v=v0,
        v = vec(0, 0, 0),
        texture = moon_external_ball['texture'],
        emissive = False)
    balls_list.append(ball)

#給xy座標，算與+X軸夾角(0~360)
def XYToDegree(x, y):
    # 假設xy兩者必有一不為0
    if y==0:
        if x>0:
            return 0
        else:
            return 180
    elif x==0:
        if y>0:
            return 90
        else:
            return 270
    if x>0 and y>0:
        return atan(y/x)/math.pi*180
    elif x<0 and y>0:
        return 180+atan(y/x)/math.pi*180
    elif x<0 and y<0:
        return 180+atan(y/x)/math.pi*180
    else:
        return 360+atan(y/x)/math.pi*180

"""
 4. 物體運動部分
"""
while True:
    if not is_started:
        continue
    # print(f'earth: {earth_sphere.axis}')
    # 由於 dt 較小，每秒計算 5000 次使動畫速度加快
    rate(draw_rate)    
    # 計算小球 an 更新加速度, 速度, 位置
    max_earth_a_vs_balls_a_ratio = 0     #地球引力與小球間作用力的比例
    farthest_two_ball_dis = 0      #最遠兩顆小球間的距離 
    for ball in balls_list:
        a=vec(0, 0, 0)
        # 地球的萬有引力
        earth_a = None
        if earth_sphere.visible:
            earth_a = -G*earth_sphere.M/(ball.pos.mag2*(dis_unit**2))*ball.pos.norm()   # pos.norm() 是 pos 的單位向量
            a += earth_a
        #小球間的萬有引力
        balls_a = vec(0, 0, 0)
        for ball2 in balls_list:
            if ball is ball2:
                continue
            dis_vec = (ball.pos-ball2.pos)*dis_unit  # m
            # print(f'dis_vec:{dis_vec.mag}')
            if dis_vec.mag <spring_force_dis_threshold:
                ball2_a = -k*dis_vec.mag/external_ball_mass*dis_vec.norm()
            else:
                ball2_a = -G*external_ball_mass/(dis_vec.mag2)*dis_vec.norm()
            balls_a+=ball2_a
            # print(ball2_a)
            #計算兩顆小球的距離
            #farthest_two_ball_dis = max(farthest_two_ball_dis, dis_vec.mag)
            if dis_vec.mag > farthest_two_ball_dis:
                farthest_two_ball_dis=dis_vec.mag
                # print(f'ball1.pos:{ball.pos} ball2.pos:{ball2.pos} farthest_two_ball_dis:{farthest_two_ball_dis}')
        a+=balls_a 
        # print(ball.pos, ball.pos.norm())
        ball.a = a/dis_unit
        ball.v += ball.a*dt
        # ball.v*=1000
        # print(f'ball.pos:{ball.pos}')
        # ball.pos += ball.v*dt
        
        # 計算地球引力與小球間作用力的比例
        #print(f'earth_a:{earth_a.mag} balls_a:{balls_a.mag}')
        # if earth_a!=None and balls_a.mag>0:
        #     max_earth_a_vs_balls_a_ratio = max(max_earth_a_vs_balls_a_ratio, earth_a.mag/balls_a.mag)

    if t%3600==0:
        print(f'{t} : ')
    balls_degree = []
    for ball in balls_list:
        ball.pos += ball.v*dt
        if t%3600==0:
            print (f'ball pos: {ball.pos.x} {ball.pos.y}')
        balls_degree.append(XYToDegree(ball.pos.x, ball.pos.y))
    # print(f'first ball degree: {XYToDegree(balls_list[0].pos.x, balls_list[0].pos.y)}')
    # print(f'balls_degree: {balls_degree}')
    # print(f'degree variance: {statistics.variance(balls_degree)}')
    # print(f'{t} : {max_earth_a_vs_balls_a_ratio}')
    dis_ratio = farthest_two_ball_dis/ball_center_dis
    dis_ratio_str = f'{t} : {dis_ratio}'
    # print(dis_ratio_str)
    file.write(dis_ratio_str+"\n")

    # if dis_ratio>is_pull_apart_ratio:
        # is_pull_apart = True
        # if dis_ratio > pull_apart_ratio_to_close:
            # closeAndSave()
    if not camera_to_earth:
        scene.camera.follow(balls_list[0])
    # 更新時間
    t += dt
    if t >= time_to_close:
        closeAndSave()
