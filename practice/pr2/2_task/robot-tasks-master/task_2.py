#!/usr/bin/python3

from pyrob.api import *


@task
def task_1_2():
    p = 0
    for i in range(3):
        p +=1
        move_right()
        move_down()
        if p ==2:
            fill_cell()
            move_right()



if __name__ == '__main__':
    run_tasks()
