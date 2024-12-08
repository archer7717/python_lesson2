#!/usr/bin/python3
from cloudinit.config.cc_fan import stop_update_start

from pyrob.api import *
from pyrob.core import step_down


@task
def task_5_4():
    x = 0
    while wall_is_beneath() == False:
        move_down()

    while wall_is_beneath() == True:
        x+=1
        move_right()
    move_down()
    move_left(x)






if __name__ == '__main__':
    run_tasks()
