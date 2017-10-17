import click

from my_stuff.testing_global_variables.variables import monkey_patch_global

from my_stuff.testing_global_variables.variables import \
    P2P_PROTOCOL_ID, TASK_PROTOCOL_ID, mylist, CLASS_PROTOCOL_ID

import my_stuff.testing_global_variables.variables as v
import my_stuff.testing_global_variables.config as config

@click.command()

@click.option('--global_var', type=click.INT,
              callback=monkey_patch_global,
              help='changes the global variable')
def hello(global_var):
    print("the global variables are:")
    print(P2P_PROTOCOL_ID, TASK_PROTOCOL_ID, config.v.x,
          CLASS_PROTOCOL_ID.P2P_ID, CLASS_PROTOCOL_ID.TASK_ID)

    global P2P_PROTOCOL_ID
    a = P2P_PROTOCOL_ID

    for i in v.mylist:
        print(i)


    fun()



def fun():
    from my_stuff.testing_global_variables.variables import P2P_PROTOCOL_ID, TASK_PROTOCOL_ID

    print("inside fun", P2P_PROTOCOL_ID, TASK_PROTOCOL_ID)

if __name__ == '__main__':

    P2P_PROTOCOL_ID = 1000500100900
    print("First", P2P_PROTOCOL_ID, TASK_PROTOCOL_ID)
    hello()

    print("exiting", P2P_PROTOCOL_ID, TASK_PROTOCOL_ID)

