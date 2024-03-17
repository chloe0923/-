"""
pip3 install vpython
"""
from vpython import *
import math 
import random

"""
1. 參數設定, 設定變數及初始值
"""
# time  s(sec)
t = 0
# dt = 3600
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
# k = 0.00000001
# k = 0.001
k = 1
# k = 1000

dis_unit=1000     #所使用的距離及座標單位為公尺的幾倍

"""
 2. 畫面設定
"""
scene = canvas(title="Vertical Circle", width=800, height=700, x=0, y=0, background=color.yellow)
def clickStartButton(b):
    global earth_sphere, balls_list, v0
    earth_sphere.visible = True
    for ball in balls_list:
        ball.v = v0
button_start = button(text="start", pos=scene.title_anchor, bind=clickStartButton)

#dis_R 地球和繞行天體的距離 m
# dis_R = 384399/60*1000
# dis_R = 384399/40*1000
# dis_R = 384399/20*1000
# dis_R = 384399/15*1000
# dis_R = 384399/5*1000
dis_R = 384399*1000
# dis_R = 38439900*1000

# moon_external_ball_num = 27
moon_external_ball_num = 64
external_ball_mass = 7.3477e+22/moon_external_ball_num
external_ball_radius = 5000000 #小球本身的半徑, 為顯示效果  m
ball_center_dis = 10000000     #初始小球和繞行天體中心的最大距離 m
angle = 360/sqrt(moon_external_ball_num)
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
    # 'radius':6371000,        #m , real data
    'radius':67310000,     # 為了顯示效果
    'texture':textures.earth,
}

earth_sphere = sphere(
    pos=vec(0, 0, 0), 
    #axis=vec(0, 0, 2*size), 
    radius=earth['radius']/dis_unit, 
    texture = earth['texture'], 
    emissive = False, 
    M = earth['mass'])
earth_sphere.visible = False

balls_list = []
g = G*earth['mass']/(dis_R**2) #m/s^2
external_pos = vec(dis_R/dis_unit, 0, 0)
v0=vec(0, sqrt(g*dis_R)/dis_unit, 0)  #m/s
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

"""
 4. 物體運動部分, 小球回到出發點 5 次停止運作
"""
while True:
    # 由於 dt 較小，每秒計算 5000 次使動畫速度加快
    rate(draw_rate)    
    # 計算小球 an 更新加速度, 速度, 位置
    for ball in balls_list:
        a=vec(0, 0, 0)
        # 地球的萬有引力
        if earth_sphere.visible:
            earth_a = -G*earth_sphere.M/(ball.pos.mag2*(dis_unit**2))*ball.pos.norm()   # pos.norm() 是 pos 的單位向量
            a += earth_a
        #小球間的萬有引力
        # for ball2 in balls_list:
        #     if ball is ball2:
        #         continue
        #     dis_vec = ball.pos-ball2.pos
        #     if dis_vec.mag <800:
        #         ball2_a = -k*dis_vec.mag/external_ball_mass*dis_vec.norm()
        #     else:
        #         ball2_a = -G*external_ball_mass/(dis_vec.mag2)*dis_vec.norm()
        #     a+=ball2_a
            # print(ball2_a)
        # print(ball.pos, ball.pos.norm())
        ball.a = a/dis_unit
        ball.v += ball.a*dt
        # ball.v*=1000
        ball.pos += ball.v*dt
    # if not camera_to_earth:
    #     scene.camera.follow(moon_sphere)
    # 更新時間
    t += dt
