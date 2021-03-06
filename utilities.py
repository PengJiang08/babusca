from __future__ import print_function, division
import numpy as np


# Kronecker's
#
#           $$\           $$\   $$\
#           $$ |          $$ |  $$ |
#      $$$$$$$ | $$$$$$\  $$ |$$$$$$\    $$$$$$\
#     $$  __$$ |$$  __$$\ $$ |\_$$  _|   \____$$\
#     $$ /  $$ |$$$$$$$$ |$$ |  $$ |     $$$$$$$ |
#     $$ |  $$ |$$   ____|$$ |  $$ |$$\ $$  __$$ |
#     \$$$$$$$ |\$$$$$$$\ $$ |  \$$$$  |\$$$$$$$ |
#      \_______| \_______|\__|   \____/  \_______|

def delta(a, b):
    """
    Kronecker delta function
    """
    return 1 if a == b else 0


#     $$\
#     \__|
#     $$\  $$$$$$$\  $$$$$$\   $$$$$$\   $$$$$$\  $$$$$$\  $$\   $$\
#     $$ |$$  _____| \____$$\ $$  __$$\ $$  __$$\ \____$$\ $$ |  $$ |
#     $$ |\$$$$$$\   $$$$$$$ |$$ |  \__|$$ |  \__|$$$$$$$ |$$ |  $$ |
#     $$ | \____$$\ $$  __$$ |$$ |      $$ |     $$  __$$ |$$ |  $$ |
#     $$ |$$$$$$$  |\$$$$$$$ |$$ |      $$ |     \$$$$$$$ |\$$$$$$$ |
#     \__|\_______/  \_______|\__|      \__|      \_______| \____$$ |
#                                                          $$\   $$ |
#                                                          \$$$$$$  |
#                                                           \______/

def isarray(A):
    """
    returns True if A is an array
    """
    try:
        if A.shape:
            return True
        else:
            return False
    except:
        return False
