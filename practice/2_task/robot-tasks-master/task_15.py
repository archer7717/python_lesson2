#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_21():
    if wall_is_on_the_right() and wall_is_above():
        for i in range(9):
            move_left(1)
            move_down(1)
    elif wall_is_above() and wall_is_on_the_left():
        for i in range(9):
            move_right(1)
            move_down(1)
    elif wall_is_on_the_left() and wall_is_beneath():
        for i in range(9):
            move_right(1)
            move_up(1)

    elif wall_is_beneath() and wall_is_on_the_left():
        for i in range(9):
            move_left(1)
            move_up(1)

    elif wall_is_beneath() and wall_is_on_the_right():
        for i in range(9):
            move_left(1)
            move_up(1)



if __name__ == '__main__':
    run_tasks()
