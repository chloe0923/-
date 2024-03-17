"""
 VPython進階教學: 按鈕
 日期: 2018/7/23
 作者: 王一哲
"""
from vpython import *

"""
 1. 參數設定, 設定變數及初始值
"""
size = 0.1        # 木塊邊長
L = 1             # 地板長度
v = 0.03          # 木塊速度
t = 0             # 時間
dt = 0.01         # 時間間隔
re = False        # 重置狀態
running = False   # 物體運動狀態
end = False       # 程式是否結束

"""
 2. 函式設定
"""
# 建立動畫視窗, 建立按鈕時才不會另外開啟一個黑底、無物件的動畫視窗
scene = canvas(title="1D Motion\n\n", width=800, height=400, x=0, y=0,
               center=vec(0, 0.1, 0), background=vec(0, 0.6, 0.6))

# 初始畫面設定
def setup():
    global floor, cube, gd, gd2, xt, vt
    floor = box(pos=vec(0, 0, 0), size=vec(L, 0.1*size, 0.5*L), color=color.blue)
    cube = box(pos=vec(-0.5*L + 0.5*size, 0.55*size, 0), size=vec(size, size, size),
               color=color.red, v=vec(v, 0, 0))
    gd = graph(title="<i>x</i>-<i>t</i> plot", width=600, height=450, x=0, y=400,
               xtitle="<i>t</i> (s)", ytitle="<i>x</i> (m)")
    gd2 = graph(title="<i>v</i>-<i>t</i> plot", width=600, height=450, x=0, y=850,
                xtitle="<i>t</i> (s)", ytitle="<i>v</i> (m/s)")
    xt = gcurve(graph=gd, color=color.red)
    vt = gcurve(graph=gd2, color=color.red)

# 執行按鈕
def run(b1):
    global running
    running = not running
    
b1 = button(text="Run", pos=scene.title_anchor, bind=run)

# 物體運動
def motion(t, dt):
    global running
    while(cube.pos.x <= L*0.5 - size*0.5):
        rate(1000)
        cube.pos += cube.v*dt
        xt.plot(pos=(t, cube.pos.x))
        vt.plot(pos=(t, cube.v.x))
        t += dt
    print("t = ", t)
    running = False

# 重置按鈕
def reset(b2):
    global re
    re = not re
    
b2 = button(text="Reset", pos=scene.title_anchor, bind=reset)

# 重置用, 初始化
def init():
    global re, running
    cube.pos = vec(-L*0.5 + size*0.5, size*0.55, 0)
    cube.v = vec(v, 0, 0)
    t = 0
    xt.delete()
    vt.delete()
    re = False
    running = False

# 停止按鈕
def stop(b3):
    global end
    end = not end
    
b3 = button(text="Stop", pos=scene.title_anchor, bind=stop)

"""
 3. 主程式
"""
setup()
while not end:
    if running:
        print("Run")
        motion(t, dt)
    if re:
        print("Reset")
        init()

print("Stop")