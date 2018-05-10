import turtle

def draw_olympic_symbol():
	positions = [[0,0,"green"], [-120,0,"yellow"], [60,60,"red"], [-60,60,"black"], [-180,60,"blue"]]
	t.pensize(8)
	for x,y,c in positions:
		t.penup()
		t.goto(x,y)
		t.pendown()
		t.color(c,c)
		t.circle(55)

t = turtle.Turlte()
draw_olympic_symbol()
