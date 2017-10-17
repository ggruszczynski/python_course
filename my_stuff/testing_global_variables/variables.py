
P2P_PROTOCOL_ID = 14
TASK_PROTOCOL_ID = 15


mylist = {"item1"}
x = 0

class CLASS_PROTOCOL_ID(object):
    """
    https://docs.python.org/2/faq/programming.html#how-do-i-share-global-variables-across-modules
    https://bytes.com/topic/python/answers/19859-accessing-updating-global-variables-among-several-modules
    """
    P2P_ID = 14
    TASK_ID = 15

def monkey_patch_global(ctx, param, value):
    """
    Used at golem startup
    """
    # del ctx, param
    if value:
        # from golem.core.variables import P2P_PROTOCOL_ID, TASK_PROTOCOL_ID
        print("patching \n")
        global P2P_PROTOCOL_ID, TASK_PROTOCOL_ID
        P2P_PROTOCOL_ID = value
        TASK_PROTOCOL_ID = value
        mylist.add(value)
        x = value
        CLASS_PROTOCOL_ID.P2P_ID = value
        CLASS_PROTOCOL_ID.TASK_ID = value