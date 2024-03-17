from vpython import *
import math 
import random

"""
 1. 參數設定, 設定變數及初始值
"""
size = 1             # 小球半徑
R = 20*size          # 圓周運動半徑
g = 100                # 重力加速度 9.8 m/s^2
v0 = 1*sqrt(g*R)      # 小球初速, 1 ~ 7 sqrt(g*R)
ratio = 0.1           # 速度, 加速度箭頭長度與實際的比例
i = 0                 # 小球回到出發點的次數
t = 0                 # 時間
dt = 0.0001           # 時間間隔, 取 0.0001 以降低誤差

"""
 2. 畫面設定
"""
scene = canvas(title="Vertical Circle", width=600, height=600, x=0, y=0, background=color.black)
ball1 = sphere(pos=vec(0, R, 0), radius=size, make_trail=True, retain=100000, v=vec(-v0, 0, 0), texture = textures.wood)

ball2 = sphere(pos=vec(R, 0, 0), radius=0.5*size, make_trail=True, retain=100000, v=vec(0, 0, -v0), texture = textures.flower)

ball3 = sphere(pos=vec(0, 0, R), radius=0.5*size, make_trail=True, retain=100000, v=vec(v0*3, -v0, 0), texture = textures.earth)

sqrt2=sqrt(2)

ball4 = sphere(pos=vec(0, R*sqrt2, R*sqrt2), radius=0.5*size, make_trail=True, retain=100000, v=vec(v0*3, -v0, v0), texture = textures.stucco, R = R*2)


ball5_R = 10
theta = random.random()*2*math.pi
phi = random.random()*2*math.pi
ball5_pos = vec(ball5_R*math.sin(theta)*math.cos(phi), ball5_R*math.sin(theta)*math.sin(phi), ball5_R*math.cos(phi))
ball5_plane_pos = vec(random.randrange(0, 100), random.randrange(0, 100), 0)
ball5_d = ball5_pos.x**2+ball5_pos.y**2+ball5_pos.z**2
ball5_plane_pos.z = (ball5_d-ball5_plane_pos.x*ball5_pos.x-ball5_plane_pos.y*ball5_pos.y)/ball5_pos.z
ball5 = sphere(pos=ball5_pos, radius=0.5*size, make_trail=True, retain=100000, v=(ball5_plane_pos-ball5_pos), texture = textures.wood_old, R = ball5_R)

balls_list = []
for _ in range(10):
    theta = random.random()*2*math.pi
    phi = random.random()*2*math.pi
    ball5_pos = vec(ball5_R*math.sin(theta)*math.cos(phi), ball5_R*math.sin(theta)*math.sin(phi), ball5_R*math.cos(phi))
    ball5_plane_pos = vec(random.randrange(0, 100), random.randrange(0, 100), 0)
    ball5_d = ball5_pos.x**2+ball5_pos.y**2+ball5_pos.z**2
    ball5_plane_pos.z = (ball5_d-ball5_plane_pos.x*ball5_pos.x-ball5_plane_pos.y*ball5_pos.y)/ball5_pos.z
    balls_list.append(sphere(pos=ball5_pos, radius=0.5*size, make_trail=False, retain=100000, v=(ball5_plane_pos-ball5_pos), texture = textures.wood_old, R = ball5_R))

center = sphere(pos=vec(0, 0, 0), axis=vec(0, 0, 2*size), radius=3*size, texture = textures.metal, emissive=True )

"""
rope = cylinder(pos=vec(0, 0, 0), axis=ball.pos, radius=0.1*size, color=color.yellow)
"""
b1arrow_v = arrow(pos=ball1.pos, axis=vec(0, 0, 0), radius=0.2*size, shaftwidth=0.4*size, color=color.green)
b1arrow_a = arrow(pos=ball1.pos, axis=vec(0, 0, 0), radius=0.2*size, shaftwidth=0.4*size, color=color.blue)
b1gd = graph(title="plot", width=600, height=450, x=0, y=600, xtitle="<i>t</i>(s)",
           ytitle="green: <i>v</i>(m/s), red: <i>a<sub>t</sub></i>(m/s<sup>2</sup>), blue: <i>a<sub>n</sub></i>(m/s<sup>2</sup>)")
b1_b1vt_plot = gcurve(graph=b1gd, color=color.green)
b1_b1at_plot = gcurve(graph=b1gd, color=color.red)
b1_b1an_plot = gcurve(graph=b1gd, color=color.blue)

b2arrow_v = arrow(pos=ball2.pos, axis=vec(0, 0, 0), radius=0.2*size, shaftwidth=0.4*size, color=color.green)
b2arrow_a = arrow(pos=ball2.pos, axis=vec(0, 0, 0), radius=0.2*size, shaftwidth=0.4*size, color=color.blue)
b2gd = graph(title="plot", width=600, height=450, x=0, y=600, xtitle="<i>t</i>(s)",
           ytitle="green: <i>v</i>(m/s), red: <i>a<sub>t</sub></i>(m/s<sup>2</sup>), blue: <i>a<sub>n</sub></i>(m/s<sup>2</sup>)")
b2_b2vt_plot = gcurve(graph=b2gd, color=color.green)
b2_b2at_plot = gcurve(graph=b2gd, color=color.red)
b2_b2an_plot = gcurve(graph=b2gd, color=color.blue)

"""
axis_size = 60

arrow_x = arrow(pos = vec(0, 0, 0), axis = vec(axis_size, 0, 0), radius = 0.1, color = color.red)

arrow_y = arrow(pos = vec(0, 0, 0), axis = vec(0, axis_size, 0), radius = 0.1, color = color.green)

arrow_z = arrow(pos = vec(0, 0, 0), axis = vec(0, 0, axis_size), radius = 0.1, color = color.blue)
"""

"""
b3arrow_v = arrow(pos=ball3.pos, axis=vec(0, 0, 0), radius=0.2*size, shaftwidth=0.4*size, color=color.green)
b3arrow_a = arrow(pos=ball3.pos, axis=vec(0, 0, 0), radius=0.2*size, shaftwidth=0.4*size, color=color.blue)
b3gd = graph(title="plot", width=600, height=450, x=0, y=600, xtitle="<i>t</i>(s)",
           ytitle="green: <i>v</i>(m/s), red: <i>a<sub>t</sub></i>(m/s<sup>2</sup>), blue: <i>a<sub>n</sub></i>(m/s<sup>2</sup>)")
b3_b3vt_plot = gcurve(graph=b3gd, color=color.green)
b3_b3at_plot = gcurve(graph=b3gd, color=color.red)
b3_b3an_plot = gcurve(graph=b3gd, color=color.blue)
"""

"""
 3. 自訂函式, findan 計算法線加速度, findat 計算切線加速度
"""

def findBallAn(ball):
    an = -ball.v.mag2 / ball.R * ball.pos.norm()
    return an

def findan(v, pos, name=''):
    """
    if name: print(name)
    print('  v:',v, -v.mag2)
    print('  pos:', pos, pos.norm())
    """
    an = -v.mag2 / R * pos.norm()
    return an

def findat(pos):
    x = pos.x
    y = pos.y
    z = pos.z
    r = sqrt(x**2 + y**2+z**2)
    sintheta = abs(x)/r
    costheta = abs(y)/r
    absat = g*sintheta
    aty = -absat*sintheta
    if((x <= 0 and y <= 0) or (x >=0 and y>= 0)):
        atx = +absat*costheta
    elif((x <= 0 and y >= 0) or (x >= 0 and y <= 0)):
        atx = -absat*costheta
    at = vec(atx, aty, 0)
    return at

"""
 4. 物體運動部分, 小球回到出發點 5 次停止運作
"""
while(i < 5):
# 由於 dt 較小，每秒計算 5000 次使動畫速度加快
    rate(5000)
# xp 是小球原來的位置, xc 是小球現在的位置, 用來判斷小球是否回到出發點    
# 計算小球 an, at, 更新加速度, 速度, 位置
    b1xp = ball1.pos.x
    b1an = findan(ball1.v, ball1.pos)
    b1at = findat(ball1.pos)
    ball1.a = b1an #+ b1at
    ball1.v += ball1.a*dt
    ball1.pos += ball1.v*dt
    b1xc = ball1.pos.x
    #rope.axis = ball.pos
    
    b2xp = ball2.pos.x
    b2an = findan(ball2.v, ball2.pos)
    #b2at = findat(ball2.pos)
    ball2.a = b2an 
    ball2.v += ball2.a*dt
    ball2.pos += ball2.v*dt
    b2xc = ball2.pos.x
    
    
    b3xp = ball3.pos.x
    b3an = findan(ball3.v, ball3.pos, 'ball3')
    #b3at = findat(ball3.pos)
    ball3.a = b3an
    ball3.v += ball3.a*dt
    ball3.pos += ball3.v*dt
    b3xc = ball3.pos.x
    
    #b4xp = ball4.pos.x
    ball4.a = findBallAn(ball4)
    ball4.v += ball4.a*dt
    ball4.pos += ball4.v*dt
    #b3xc = ball3.pos.x
    
    ball5.a = findBallAn(ball5)
    ball5.v += ball5.a*dt
    ball5.pos += ball5.v*dt
    
    for ball in balls_list:
        ball.a = findBallAn(ball)
        ball.v += ball.a*dt
        ball.pos += ball.v*dt
    
# 若小球回到出發點, 將 i 加 1, 印出時間 t, 由於誤差會累積, 取第一次回到出發點的時間作為週期
    if(b1xp > 0 and b1xc < 0):
        i += 1
        print(i, t)
    
    if(b2xp > 0 and b2xc < 0):
        i += 1
        print(i, t)
    
    """
    if(b3xp > 0 and b3xc < 0):
        i += 1
        print(i, t)
    """
# 更新代表速度, 加速度的箭頭
    b1arrow_v.pos = ball1.pos
    b1arrow_v.axis = ball1.v * ratio
    b1arrow_a.pos = ball1.pos
    b1arrow_a.axis = ball1.a * ratio
    
    b2arrow_v.pos = ball2.pos
    b2arrow_v.axis = ball2.v * ratio
    b2arrow_a.pos = ball2.pos
    b2arrow_a.axis = ball2.a * ratio
    
    """
    b3arrow_v.pos = ball3.pos
    b3arrow_v.axis = ball3.v * ratio
    b3arrow_a.pos = ball3.pos
    b3arrow_a.axis = ball3.a * ratio
    """
# 更新 v-t, at-t, an-t 圖
    b1_b1vt_plot.plot(t, ball1.v.mag)
    b1_b1at_plot.plot(t, b1at.mag)
    b1_b1an_plot.plot(t, b1an.mag)
    
    b2_b2vt_plot.plot(t, ball2.v.mag)
    #b2_b2at_plot.plot(t, b2at.mag)
    b2_b2an_plot.plot(t, b2an.mag)
    
    """
    b3_b3vt_plot.plot(t, ball3.v.mag)
    b3_b3at_plot.plot(t, b3at.mag)
    b3_b3an_plot.plot(t, b3an.mag)
    """
# 更新時間
    t += dt