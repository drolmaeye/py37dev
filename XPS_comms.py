__author__ = 'jssmith'

'''
Work out a way forward using XPS and Python3
'''

from newportxps import NewportXPS
from newportxps import XPS_C8_drivers
import time
import socket

# xps = NewportXPS('164.54.105.46')
#
# print(xps.status_report())
#
# xps.move_stage('M.X', 0.00)
#
# err, val1, val2 = xps._xps.GroupPositionCurrentGet(xps._sid, 'M', 2)
#
# print(err, val1, val2)
#
myxps = XPS_C8_drivers.XPS()

socketId = myxps.TCP_ConnectToServer('164.54.105.46', 5001, 10)
print(socketId)
myxps.GroupMoveAbsolute(socketId, 'M', [0.5, 1.2])
err, val = myxps.GroupPositionCurrentGet(socketId, 'M.X', 1)
print(val)
# myxps.TCP_CloseSocket(socketId)

