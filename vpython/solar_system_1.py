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
size = 5             # 小球半徑
R = 20*size          # 圓周運動半徑
#g = 9.8             # 重力加速度 9.8 m/s^2
ratio = 0.1          # 速度, 加速度箭頭長度與實際的比例
t = 0                # 時間
dt = 0.01           # 時間間隔, 取 0.0001 以降低誤差
starM = 1.98855e+30  #kg
G=6.67e-11



"""
 2. 畫面設定
"""
scene = canvas(title="Vertical Circle", width=600, height=600, x=0, y=0, background=color.black)
planets = [
    {
       'name':'Mercury',
       'mass':3.3022e+23,   #kg
       'R':57909100,        #km
       'radius':2439.7,      #km
       'color':color.blue,
    },
    {
       'name':'Venus',
       'mass':4.8676e+24,    #kg
       'R':108208000,        #km
       'radius':6051.8,       #km
       'color':color.yellow,
    },
    {
       'name':'Earth',
       'mass':5.972e+24,     #kg
       'R':149598023,        #km
       'radius':6371,         #km
       'color':color.green
    },
]

balls_list = []
for planet in planets:
    # https://zh.wikipedia.org/wiki/%E7%90%83%E5%BA%A7%E6%A8%99%E7%B3%BB#%E7%9B%B4%E8%A7%92%E5%BA%A7%E6%A8%99%E7%B3%BB
    print(planet['name'])
    R = planet['R']
    g = G*starM/(R**2) #m/s^2
    theta = random.random()*2*math.pi
    phi = random.random()*2*math.pi
    pos = vec(R*math.sin(theta)*math.cos(phi), R*math.sin(theta)*math.sin(phi), R*math.cos(theta))
    plane_pos = vec(random.random(), random.random(), 0)
    d = pos.x**2+pos.y**2+pos.z**2
    plane_pos.z = (d-plane_pos.x*pos.x-plane_pos.y*pos.y)/pos.z
    v0=(plane_pos-pos)
    v0=v0/v0.mag*sqrt(g*R)
    ball = sphere(
        pos=pos, 
        radius=planet['radius'], 
        make_trail=True, 
        trail_color = planet['color'], 
        interval = 10, 
        retain=100000, 
        v=v0, 
        texture = textures.wood_old, 
        R = R, 
        emissive = True)
    print(ball.trail_radius)
    balls_list.append(ball)

center = sphere(pos=vec(0, 0, 0), axis=vec(0, 0, 2*size), radius=696340, texture = textures.metal, emissive=True, M = starM)

"""
 4. 物體運動部分, 小球回到出發點 5 次停止運作
"""

i = 0                 # 小球回到出發點的次數
while(i < 5):
    # 由於 dt 較小，每秒計算 5000 次使動畫速度加快
    rate(5000)    
    # 計算小球 an 更新加速度, 速度, 位置
    for ball in balls_list:
        star_a = -G*center.M/(ball.pos.mag2)*ball.pos.norm() 
        ball.a = star_a
        ball.v += ball.a*dt
        ball.pos += ball.v*dt
        
        
    # 更新時間
    t += dt