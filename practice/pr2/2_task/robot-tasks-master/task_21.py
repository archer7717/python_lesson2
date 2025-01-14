#!/usr/bin/python3

from pyrob.api import *

@task(delay=0.5)
def task_4_11():

    for i in range(2):
        move_right()
        g = 14
        g -=1
        for b in range(g):
            move_down()
            fill_cell()




if __name__ == '__main__':
    run_tasks()
