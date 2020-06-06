import turtle
import winsound

wn = turtle.Screen()
wn.title("Jogo de Pong ")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Placar

score_a = 0
score_b = 0

# Barra do jogador 1

paddle_a =  turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0) # (eixo x, eixo y)

# Barra do jogador 2

paddle_b =  turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white") 
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)

# Bola

ball =  turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white") 
ball.penup()
ball.goto(0,0)
ball.dx = -0.2
ball.dy = -0.2

# Placar_Inicial

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
scoreSentence = "Jogador A: {} Jogador B: {}"
pen.write(scoreSentence.format(score_a,score_b)  ,align="center",font=("Arial",24,"normal"))


# Funções

def paddle_a_up():
	y = paddle_a.ycor()
	y += 20
	paddle_a.sety(y)

def paddle_a_down():
	y = paddle_a.ycor()
	y -= 20
	paddle_a.sety(y)	

def paddle_b_up():
	y = paddle_b.ycor()
	y += 20
	paddle_b.sety(y)

def paddle_b_down():
	y = paddle_b.ycor()
	y -= 20
	paddle_b.sety(y)



# Atrelar eventos do teclado

wn.listen()
wn.onkeypress(paddle_a_up, "w")	
wn.onkeypress(paddle_a_down,"s")

wn.onkeypress(paddle_b_up, "Up")	
wn.onkeypress(paddle_b_down,"Down")

#Loop principal do jogo
while True:
	wn.update()

	# Movimento da bola

	ball.setx(ball.xcor()+ball.dx)
	ball.sety(ball.ycor()+ball.dy)

	# conferir se enconstou na borda superior
	if ball.ycor() > 290:
		ball.sety(290)
		# se tiver enconstado, o indice dy ficará negativo o que mudará o a direção do movimento para baixo
		ball.dy *= -1
		winsound.PlaySound("bounceBorder.wav", winsound.SND_ASYNC)

	# conferir se enconstou na borda inferior
	if ball.ycor() < -290:
		ball.sety(-290)
		# se tiver enconstado, o indice dy ficará positivo o que mudará o a direção do movimento para cima
		ball.dy *= -1
		winsound.PlaySound("bounceBorder.wav", winsound.SND_ASYNC)	

	# conferir se enconstou na lateral direita
	if ball.xcor() > 390:
		ball.goto(0,0)
		ball.dx *= -1	
		# Se enconstou na lateral direita, aumenta a pontuação do jogador A
		score_a += 1
		pen.clear() 
		pen.write(scoreSentence.format(score_a,score_b)  ,align="center",font=("Arial",24,"normal"))

	# conferir se enconstou na lateral esquerda
	if ball.xcor() < -390:
		ball.goto(0,0)
		ball.dx *= -1	
		# Se enconstou na lateral esquerda, aumenta a pontuação do jogador B
		score_b += 1
		pen.clear()
		pen.write(scoreSentence.format(score_a,score_b)  ,align="center",font=("Arial",24,"normal"))

	#colisão entre a barra direita e a bola
	if (ball.xcor() > 340 and ball.xcor()< 350)  and (ball.ycor()< paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() -50):
		ball.setx(340)
		ball.dx *= -1
		winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)	

	#colisão entre a barra esquerda e a bola
	if (ball.xcor() < -340 and ball.xcor() > -350)  and (ball.ycor()< paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() -50):
		ball.setx(-340)
		ball.dx *= -1
		winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)	

	

