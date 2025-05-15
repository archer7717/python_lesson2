import graphics as gr
from practice.pr_4.graphics import Polygon


window = gr.GraphWin("Jenkslex and Ganzz project", 1000, 800)

def sky(x):
    sky = gr.Line(gr.Point(0, 0), gr.Point(1000, 0))

    sky.setOutline('blue')

    sky.setWidth(x)

    sky.draw(window)

def clouds(x, y, size):
    #default x=150 y=100 radius=25
    cloud1 = gr.Circle(gr.Point(x,y), size)
    cloud2 = gr.Circle(gr.Point(x-40, y), size)
    cloud3 = gr.Circle(gr.Point(x+20, y+10), size)
    cloud4 = gr.Circle(gr.Point(x-20, y+10), size)
    cloud5 = gr.Circle(gr.Point(x-60, y+10), size)

    cloud1.setFill('white')
    cloud2.setFill('white')
    cloud3.setFill('white')
    cloud4.setFill('white')
    cloud5.setFill('white')

    cloud1.draw(window)
    cloud2.draw(window)
    cloud3.draw(window)
    cloud4.draw(window)
    cloud5.draw(window)


def sun(x,y,size):
    #deafault x=700 y=150 radius=70
    sun = gr.Circle(gr.Point(x, y), size)

    sun.setFill('yellow')

    sun.draw(window)

def house(x,y):
    #default x=250 y=300
    my_rectangle = gr.Rectangle(gr.Point(x, y), gr.Point(x+250, y+300))
    centerPoint = my_rectangle.getCenter()

    # window_1 =  gr.Line(gr.Point(325, 450), gr.Point(425, 450))
    window_2 = gr.Rectangle(gr.Point(x+75, y+100), gr.Point(x+175, y+200))
    window_2_line_1 = gr.Line(gr.Point(x+75, y+150), (gr.Point(x+175, y+150)))
    window_2_line_2 = gr.Line(gr.Point(x+125, y+100), (gr.Point(x+125, y+200)))

    roof = Polygon(gr.Point(x, y), gr.Point(x+250, y), gr.Point(x+125, y-165))
    roof_line_1 = gr.Line(gr.Point(x, y), (gr.Point(x+250, y)))
    roof_line_2 = gr.Line(gr.Point(x+250, y), (gr.Point(x+125, y-165)))
    roof_line_3 = gr.Line(gr.Point(x, y), (gr.Point(x+125, y-165)))

    house_line_1 = gr.Line(gr.Point(x, y), (gr.Point(x, y+300)))
    house_line_2 = gr.Line(gr.Point(x, y+300), (gr.Point(x+250, y+300)))
    house_line_3 = gr.Line(gr.Point(x+250, y+300), (gr.Point(x+250, y)))
    house_line_4 = gr.Line(gr.Point(x, y), (gr.Point(x+125, y-165)))

    my_rectangle.setFill('grey')
    roof.setFill('brown')
    roof_line_1.setFill('black')
    roof_line_2.setFill('black')
    roof_line_3.setFill('black')
    house_line_1.setFill('black')
    house_line_2.setFill('black')
    house_line_3.setFill('black')
    house_line_4.setFill('black')
    window_2.setFill('yellow')

    roof_line_1.setWidth(5)
    roof_line_2.setWidth(5)
    roof_line_3.setWidth(5)
    house_line_1.setWidth(5)
    house_line_2.setWidth(5)
    house_line_3.setWidth(5)
    house_line_4.setWidth(5)
    window_2.setWidth(5)
    window_2_line_1.setWidth(5)
    window_2_line_2.setWidth(5)

    my_rectangle.draw(window)
    # window_1.draw(window)
    roof.draw(window)
    roof_line_1.draw(window)
    roof_line_2.draw(window)
    roof_line_3.draw(window)
    house_line_1.draw(window)
    house_line_2.draw(window)
    house_line_3.draw(window)
    house_line_4.draw(window)
    window_2.draw(window)
    window_2_line_1.draw(window)
    window_2_line_2.draw(window)

def tree(x,y):
    # deafult x=800 y=630
    wood = gr.Rectangle(gr.Point(x, y), gr.Point(x+10, y+70))
    fir_tree_1 = Polygon(gr.Point(x-100, y), gr.Point(x+100, y), gr.Point(x, y-130))
    fir_tree_2 = Polygon(gr.Point(x-100, y-80), gr.Point(x+100, y-80), gr.Point(x, y-230))
    fir_tree_3 = Polygon(gr.Point(x-100, y-160), gr.Point(x+100, y-160), gr.Point(x,y-330))
    wood = gr.Rectangle(gr.Point(x, y), gr.Point(x+10, y+70))
    # fir_tree_1 = Polygon(gr.Point(700, 630), gr.Point(900, 630), gr.Point(800, 500))
    # fir_tree_2 = Polygon(gr.Point(700, 550), gr.Point(900, 550), gr.Point(800, 400))
    # fir_tree_3 = Polygon(gr.Point(700, 470), gr.Point(900, 470), gr.Point(800, 300))


    wood.setOutline('black')
    # window_1.setOutline('yellow')
    fir_tree_1.setOutline('black')
    fir_tree_2.setOutline('black')
    fir_tree_3.setOutline('black')

    wood.setFill('brown')
    fir_tree_1.setFill('green')
    fir_tree_2.setFill('green')
    fir_tree_3.setFill('green')

    wood.setWidth(5)
    fir_tree_1.setWidth(5)
    fir_tree_2.setWidth(5)
    fir_tree_3.setWidth(5)

    wood.draw(window)
    fir_tree_1.draw(window)
    fir_tree_2.draw(window)
    fir_tree_3.draw(window)

def scenery():
    sky(800)
    clouds(150,100,25)
    clouds(400,50,25)
    clouds(900, 200, 25)
    clouds(840, 70, 25)
    sun(650,150,70)
    house(250,300)
    tree(800,630)

scenery()

window.getMouse()

window.close()


