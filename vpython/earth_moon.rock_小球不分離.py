"""
pip3 install vpython
"""
from vpython import *
import math
"""
 1. 參數設定, 設定變數及初始值
"""
t = 0                # 時間
dt = 0.0001            # 時間間隔, 取 0.0001 以降低誤差
# dt = 0.01
# dt = 0.0000001
# draw_rate = 1/dt
draw_rate = 5000
G=6.67e-11
# k = 0.00000001
# k = 0.001
k = 1


"""
 2. 畫面設定
"""
scene = canvas(title="Vertical Circle", width=600, height=600, x=0, y=0, background=color.black)

def clickStartButton(b):
    global earth_sphere, balls_list, v0
    earth_sphere.visible = True
    for ball in balls_list:
        ball.v = v0
button_start = button(text="start", pos=scene.title_anchor, bind=clickStartButton)

camera_to_earth = True
def clickButton(b):
    global camera_to_earth, earth_sphere, balls_list
    camera_to_earth = not camera_to_earth
    if camera_to_earth:
        scene.camera.follow(earth_sphere)
    else:
        scene.camera.follow(balls_list[0])

button_switch_camera = button(text="switch camera", pos=scene.title_anchor, bind=clickButton)

dis_R = 384399/40
# dis_R = 384399/20
# dis_R = 384399/15
# dis_R = 384399/10
# dis_R = 384399
# dis_R = 38439900

moon_external_ball_num = 36
# moon_external_ball_num = 144
# moon_external_ball_num = 225
# moon_external_ball_num = 400
# external_ball_mass = 7.3477e+22/moon_external_ball_num
external_ball_mass = 1e+17
external_ball_radius = 10
big_ball_radius = external_ball_radius * 3
# k_limit_dis = external_ball_radius * 80
k_limit_dis = external_ball_radius * 3
# k_limit_dis = external_ball_radius * 0.5
angle = 360/sqrt(moon_external_ball_num)
moon_external_ball ={
    'name':'moon_external_ball',
    # 'mass':(7.3477e+22-moon['mass'])/moon_external_ball_num,   #kg  每一顆月球表層小球的質量
    # 'radius':(1737.1-moon['radius'])/2,        #km  扣掉表層後的半徑  1737*0.8
    'radius':external_ball_radius,
    'texture':textures.rock,
}

earth ={
       'name':'Earth',
       'mass':5.972e+24,   #kg  
    #    'mass':2e+39,
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
earth_sphere.visible = False

balls_list = []   #月球表層小球
# https://zh.wikipedia.org/wiki/%E7%90%83%E5%BA%A7%E6%A8%99%E7%B3%BB#%E7%9B%B4%E8%A7%92%E5%BA%A7%E6%A8%99%E7%B3%BB
g = G*earth['mass']/(dis_R**2) #m/s^2
external_pos = vec(dis_R, 0, 0)
v0=vec(0, sqrt(g*dis_R), 0)

theta = 0
while theta<360:
    phi=0
    while phi<360:
        R = big_ball_radius
        pos = vec(
            R*math.sin(theta)*math.cos(phi), 
            R*math.sin(theta)*math.sin(phi), 
            R*math.cos(theta))
        pos+=external_pos
        ball = sphere(
            pos=pos, 
            radius=moon_external_ball['radius'], 
            make_trail=True, 
            trail_color = color.yellow, 
            # interval = 10, 
            retain=5, 
            # v=v0,
            v = vec(0, 0, 0),
            texture = moon_external_ball['texture'],
            emissive = False)
        balls_list.append(ball)
        phi+=angle
    theta+=angle


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
            earth_a = -G*earth_sphere.M/(ball.pos.mag2)*ball.pos.norm()   # pos.norm() 是 pos 的單位向量
            a += earth_a
        #小球間的萬有引力
        for ball2 in balls_list:
            if ball is ball2:
                continue
            dis_vec = ball.pos - ball2.pos
            if dis_vec.mag < k_limit_dis:
                ball2_a = -k*dis_vec.mag/external_ball_mass*dis_vec.norm()
            else:
                ball2_a = -G*external_ball_mass/(dis_vec.mag2)*dis_vec.norm()
            a += ball2_a
            # print(ball2_a)
        # print(ball.pos, ball.pos.norm())
        ball.a = a
        ball.v += ball.a*dt
        ball.pos += ball.v*dt
    # 更新時間
    t += dt