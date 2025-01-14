#!/usr/bin/python3

from pyrob.api import *


@task
def task_5_2():
    while True:
        if wall_is_beneath()==True:
            move_right()
        elif wall_is_beneath()==False:
            return  False



if __name__ == '__main__':
    run_tasks()
