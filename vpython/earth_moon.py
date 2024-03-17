"""
黑洞不會動
恆星的小球被黑洞拉走
pip3 install vpython
"""
from vpython import *
import math 
import random
"""
 1. 參數設定, 設定變數及初始值
"""
t = 0                # 時間
dt = 0.001            # 時間間隔, 取 0.0001 以降低誤差
# draw_rate = 1/dt
draw_rate = 5000
G=6.67e-11



"""
 2. 畫面設定
"""
scene = canvas(title="Vertical Circle", width=600, height=600, x=0, y=0, background=color.black)

camera_to_earth = True
def clickButton(b):
    global camera_to_earth, earth_sphere
    camera_to_earth = not camera_to_earth
    if camera_to_earth:
        scene.camera.follow(earth_sphere)
    
b1 = button(text="switch camera", pos=scene.title_anchor, bind=clickButton)

moon ={
    'name':'Moon',
    #'mass':3.7620224e+22,    #kg  73477000000000000000000×(0.8^3)  扣掉表層後的質量 
    'mass':7.3477e+22,
    'R':384399,              #km  跟地球的距離
    #'core_radius':540,      #km
    # 'radius':1389.68,        #km  扣掉表層後的半徑  1737.1*0.8
    'radius':1737.1,
    'texture':textures.metal,
}

push_moon_force_on = False  # 給月球往地球的外力
push_moon_force = moon['mass']*1000    #kg/dt
def clickForceButton(b):
    global push_moon_force_on
    push_moon_force_on = not push_moon_force_on
    if push_moon_force_on:
        b.text = "Force on"
    else:
        b.text = "Force off"
    
b2 = button(text="Force off", pos=scene.title_anchor, bind=clickForceButton)


moon_external_ball_num = 36
moon_external_ball ={
    'name':'moon_external_ball',
    # 'mass':(7.3477e+22-moon['mass'])/moon_external_ball_num,   #kg  每一顆月球表層小球的質量
    # 'radius':(1737.1-moon['radius'])/2,        #km  扣掉表層後的半徑  1737*0.8
    'radius':100,
    'texture':textures.rock,
}

earth ={
       'name':'Earth',
       'mass':5.972e+24,   #kg  
       'radius':6371,        #km  
       'texture':textures.earth,
}

earth_sphere = sphere(
    pos=vec(0, 0, 0), 
    #axis=vec(0, 0, 2*size), 
    radius=earth['radius'], 
    texture = earth['texture'], 
    emissive=False, 
    M = earth['mass'])

balls_list = []   #月球表層小球
# https://zh.wikipedia.org/wiki/%E7%90%83%E5%BA%A7%E6%A8%99%E7%B3%BB#%E7%9B%B4%E8%A7%92%E5%BA%A7%E6%A8%99%E7%B3%BB
R = moon['R']
g = G*earth['mass']/(R**2) #m/s^2
pos = vec(R, 0, 0)
v0=vec(0, sqrt(g*R), 0)
moon_sphere = sphere(
    pos=pos, 
    radius=moon['radius'], 
    make_trail=True, 
    #trail_color = planet['color'], 
    #interval = 10, 
    retain=100000, 
    v=v0, 
    texture = moon['texture'], 
    emissive = False)
#print(ball.trail_radius)
balls_list.append(moon_sphere)

for theta in range(0, 360, 60):
    for phi in range(0, 360, 60):
        R = moon['radius']+moon_external_ball['radius']
        pos = vec(
            R*math.sin(theta)*math.cos(phi), 
            R*math.sin(theta)*math.sin(phi), 
            R*math.cos(theta))
        pos+=moon_sphere.pos
        ball = sphere(
            pos=pos, 
            radius=moon_external_ball['radius'], 
            make_trail=True, 
            trail_color = color.yellow, 
            # interval = 10, 
            # retain=100000, 
            v=moon_sphere.v, 
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
        #月球的萬有引力
        if ball is not moon_sphere:
            dis_vec = ball.pos - moon_sphere.pos
            if dis_vec.mag > moon['radius'] + moon_external_ball['radius']:
                moon_a = -G * moon['mass'] / dis_vec.mag2 * dis_vec.norm()
                a+=moon_a
        # 地球的萬有引力
        earth_a = -G*earth_sphere.M/(ball.pos.mag2)*ball.pos.norm()   # pos.norm() 是 pos 的單位向量
        a += earth_a
        # 給月球往地球的外力
        if ball is moon_sphere and push_moon_force_on:
            #a+=-push_moon_force/moon['mass']*ball.pos.norm()
            a+=earth_a
        #print(ball.pos, ball.pos.norm())
        ball.a = a
        ball.v += ball.a*dt
        ball.pos += ball.v*dt
        #若穿越月球核心內，強迫移動到月球表面
        # if ball is not moon_sphere:
        #     dis_vec = ball.pos-moon_sphere.pos
        #     if dis_vec.mag<moon['radius']+moon_external_ball['radius']:
        #         ball.pos = moon_sphere.pos+(moon['radius']+moon_external_ball['radius'])*dis_vec.norm()
    if not camera_to_earth:
        scene.camera.follow(moon_sphere)
    # 更新時間
    t += dt