A = 48271
M = 2147483647    #必须是质数
Q = M // A
R = M % A

import time
import sys
def randomInt(state=(int)(time.time() % sys.maxsize)):
    tmpState = A * (state % Q) - R * (state // Q)
    if tmpState >= 0:
        state = tmpState
    else:
        state = tmpState + M
    return state

print(randomInt())