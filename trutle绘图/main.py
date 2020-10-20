import turtle as tt

t=tt.Pen()
t.color(1,0,0)
t.up()      # 不画
t.backward(280)     # 后退
t.left(90)      # 左转 90°
t.forward(100)
t.right(90)
t.down()
for i in range(4):
    t.forward(150)
    t.left(90)

t.color(0,0,0)
t.up()
t.forward(200)