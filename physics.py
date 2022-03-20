import turtle
pen = turtle.Pen()
pen.pencolor('red')
pen.penup()
pen.goto(-250,-250)
pen.down()
ball_x = -250
ball_y = -249
g = 0.98
f = 0.05
act_x = int(input())
act_y = int(input())
while act_y != 0:
	ball_x = ball_x + act_x
	act_y = act_y - g
	ball_y = ball_y + act_y
	pen.goto(ball_x,ball_y)
	a = ball_y + act_y - g
	if a < -250:
		ball_y = ball_y + (act_y-g)*abs((250 - abs(ball_y))/act_y)
		ball_x = ball_x + act_x*abs((250 - abs(ball_y))/act_y)
		pen.goto(ball_x,ball_y)
		if abs(act_y) >= (g/2):
			F = (-act_y) - g/2
			act_y = F
		if abs(act_y) < (g/2):
			act_y = 0
			act_x = 0
	if a > 250:
		ball_y = ball_y + (act_y-g)*abs((250 - abs(ball_y))/act_y)
		ball_x = ball_x + act_x*abs((250 - abs(ball_y))/act_y)
		pen.goto(ball_x,ball_y)
		F = (-act_y) - g/2
		act_y = F
	b = ball_x + act_x
	if b < -250:
		ball_x = -250
		ball_y = ball_y + act_y*abs((250 - abs(ball_x))/act_x)
		pen.goto(ball_x,ball_y)
		F = (-act_x) - g/2
		act_x = F
	if b > 250:
		ball_x = 250
		ball_y = ball_y + act_y*abs((250 - abs(ball_x))/act_x)
		pen.goto(ball_x,ball_y)
		F = (-act_x) + g/2
		act_x = F
	if act_x > 0:
		act_x = act_x - f
	if act_x < 0:
		act_x = act_x + f
	if act_y > 0:
		act_y = act_y - f
	if act_y < 0:
		act_y = act_y + f
	print(ball_y)
turtle.done()