import math
import matplotlib.pyplot as plt
import tkinter
import time

PI = math.pi
g = 9.8067
Patm = 101325 # атмосферное давление
Row = 1000 # плотность воды
x=[]
y=[]
Pin = 15000 # давление внутри резервуара

# По основному уравнению гидростатики, при которой происходит баланс системы
h = (Patm-Pin)/(Row * g)

Vs = 600.0 # объем резервуара
Dotv = 0.12 # d отверстия
Sotv = PI*(Dotv/2)**2
rshar = (3.0 * Vs / (4.0 * PI))**(1/3) # Радиус шара

hout = 2*rshar - h # незаполненной части шара

Vout = (PI * hout**2 ) * (rshar - (1/3) *hout)

    # x.append(Pin)
    # y.append(Vout)
# print(Vout)
#
# plt.plot(x,y)
# plt.xlabel("Давление внутри сосуда")
# plt.ylabel("Объем вытекшей жидкости")
# plt.show()



Window_Width = 800
Window_Height = 600
tank_x = 400
tank_y = 300
Tank_Radius = 100

otv_x = tank_x
otv_y = tank_y + Tank_Radius
otv_R = Dotv/2/rshar*Tank_Radius
Tank_h = 200
Tank_point_h = h/(2*rshar)*Tank_h
print(Tank_point_h)
pointline_r = math.sqrt(Tank_Radius**2 - abs(Tank_point_h - Tank_Radius)**2)
pointline_y = tank_y + Tank_Radius - Tank_point_h


Ball_min_movement = 5

Refresh_Sec = 0.01


def create_animation_window():
    Window = tkinter.Tk()
    Window.title("Ball Tank")

    Window.geometry(f'{Window_Width}x{Window_Height}')
    return Window


def create_animation_canvas(Window):
    canvas = tkinter.Canvas(Window)
    canvas.configure(bg="White")
    canvas.pack(fill="both", expand=True)
    return canvas


def animate_ball(Window, canvas, xinc, yinc):
    line = canvas.create_line(tank_x - pointline_r,
                              pointline_y,
                              tank_x + Tank_Radius + 130,
                                pointline_y)
    text = canvas.create_text(tank_x + Tank_Radius + 130,
                              pointline_y+10, text="Уровень воды в резервуаре",
          font="Verdana 12",fill="black")
    ball = canvas.create_oval(tank_x - Tank_Radius,
                              tank_y - Tank_Radius,
                              tank_x + Tank_Radius,
                              tank_y + Tank_Radius,
                              fill="White", outline="Black", width=2)
    otv = canvas.create_oval(otv_x - otv_R,
                              otv_y - otv_R/2,
                              otv_x + otv_R,
                              otv_y + otv_R/2,
                              fill="Blue", outline="Black", width=1)

    point_line = canvas.create_oval(tank_x - pointline_r,
                              pointline_y - pointline_r/4,
                              tank_x +  pointline_r,
                              pointline_y +  pointline_r/4,
                              fill="Blue", outline="Black", width=1)
    while True:
        canvas.coords(text)
        canvas.coords(ball)
        canvas.coords(otv)
        canvas.coords(point_line)
        canvas.coords(line)
        Window.update()
        time.sleep(Refresh_Sec)
        ball_pos = canvas.coords(ball)




Animation_Window = create_animation_window()
Animation_canvas = create_animation_canvas(Animation_Window)
animate_ball(Animation_Window, Animation_canvas, Ball_min_movement, Ball_min_movement)