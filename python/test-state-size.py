#!/usr/bin/env python
import hubo_ach
import ach
import sys
from ctypes import *

ha = hubo_ach



s = ach.Channel(ha.HUBO_CHAN_STATE_NAME)
r = ach.Channel(ha.HUBO_CHAN_REF_NAME)
s.flush()
r.flush()
state = ha.HUBO_STATE()
ref = ha.HUBO_REF()


flag = 1
while(flag<3):
    [statusr, framesizer] = r.get(ref, wait=True, last=False)
    [statuss, framesizes] = s.get(state, wait=False, last=False)
#    for i in range(0,ha.HUBO_JOINT_COUNT):
#        print ref.ref[i]
    print "ref : ", framesizer, " : ", sizeof(ref)
    print "stat: ", framesizes, " : ", sizeof(state)
    flag = flag+1
r.close()
s.close()
