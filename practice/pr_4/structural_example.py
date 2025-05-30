import graphics as gr

window = gr.GraphWin("Jenkslex and Ganzz project", 400, 400)

def draw_eye(x, y, size):
    eye = gr.Circle(gr.Point(x, y), size)
    pupil = gr.Circle(gr.Point(x, y), size/2)

    eye.setFill('red')
    pupil.setFill('black')

    eye.draw(window)
    pupil.draw(window)

def draw_eyebrows():
    eyebrow1 = gr.Line(gr.Point(100, 120), gr.Point(180, 170))
    eyebrow2 = gr.Line(gr.Point(220, 170), gr.Point(300, 120))

    eyebrow1.setWidth(10)
    eyebrow2.setWidth(10)

    eyebrow1.setOutline('black')
    eyebrow2.setOutline('black')

    eyebrow1.draw(window)
    eyebrow2.draw(window)

def draw_face():
    face = gr.Circle(gr.Point(200, 200), 100)
    face.setFill('yellow')

    face.draw(window)

def draw_mouth():
    mouth = gr.Line(gr.Point(150, 260), gr.Point(250, 260))
    mouth.setWidth(20)
    mouth.setOutline('black')

    mouth.draw(window)

def draw_angry_lecturer():
    draw_face()
    draw_eye(150,180,20)
    draw_eye(250, 180, 14)
    draw_eyebrows()
    draw_mouth()


draw_angry_lecturer()

window.getMouse()

window.close()