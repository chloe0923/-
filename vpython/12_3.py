"""
 VPython教學: 12-3.行星運動, 用 dictionary 儲存星球資料, 用 for 迴圈產生行星
 Ver. 1: 2018/2/26
 Ver. 2: 2019/9/8
 作者: 王一哲
"""
from vpython import *

"""
 1. 參數設定, 設定變數及初始值, 太陽及行星半徑、質量、遠日距、遠日點速率, 資料來源
"""
# 用 dictionary 儲存星球資料, 半徑 radius, 質量 mass, 遠日距 d_at_aphelion, 於遠日點的速率 v_at_aphelion
radius = {"Mercury": 2439700, "Venus": 6051800, "Earth": 6371000, "Mars": 3389500, "Sun": 696392000}
mass = {"Mercury": 0.33011E24, "Venus": 4.8675E24, "Earth": 5.9723E24, "Mars": 0.64171E24, "Sun": 1988500E24}
material = {"Mercury": color.cyan, "Venus": color.yellow, "Earth": color.blue, "Mars": color.red, "Sun": color.orange}
d_at_aphelion = {"Mercury": 6982E7, "Venus": 10894E7, "Earth": 15210E7, "Mars": 24923E7}
v_at_aphelion = {"Mercury": 38860, "Venus": 34790, "Earth": 29290, "Mars": 21970}
G = 6.67408E-11       # 重力常數
eps = 10000           # 精準度
t = 0                 # 時間
dt = 60*60            # 時間間隔

"""
 2. 畫面設定
"""
scene = canvas(title="Planetary Motion", width=600, height=600, x=0, y=0, background=color.black)
# 產生太陽 sun
sun = sphere(pos=vec(0,0,0), radius=radius["Sun"]*20, m=mass["Sun"], color=color.orange, emissive=True)
# 用 for 迴圈產生水星、金星、地球、火星
names = ["Mercury", "Venus", "Earth", "Mars"]
planets = []

for name in names:
    planets.append(sphere(pos=vec(d_at_aphelion[name], 0, 0), radius=radius[name]*2E3, m=mass[name], 
                          color=material[name], make_trail=True, retain = 365, v=vec(0, v_at_aphelion[name], 0)))

lamp = local_light(pos=vec(0,0,0), color=color.white)

"""
 3. 星球運動部分
"""
while(True):
    rate(60*24)
# 用 for 迴圈自動跑完所有行星的資料
    for planet in planets:
        planet.a = -G*sun.m / planet.pos.mag2 * planet.pos.norm()
        planet.v += planet.a*dt
        planet.pos += planet.v*dt
# 更新時間
    t += dt