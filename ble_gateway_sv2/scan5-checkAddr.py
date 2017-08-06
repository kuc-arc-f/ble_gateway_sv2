#
# BT addr check version(peripheral= public addr only)
#

from bluepy.btle import Scanner, DefaultDelegate
from bluepy import btle
import datetime
import time
import sys


class ScanDelegate(DefaultDelegate):
    def __init__(self):
        DefaultDelegate.__init__(self)

    def handleDiscovery(self, dev, isNewDev, isNewData):
        if isNewDev:
            print "Discovered device", dev.addr
        elif isNewData:
            print "Received new data from", dev.addr

if __name__ == "__main__":
	scanner = Scanner().withDelegate(ScanDelegate())
	from datetime import datetime
	while True:
		sTime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
		print("time=" +sTime)
		devices = scanner.scan(3.0)
		#sTime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#		print("time.aft=" +sTime)
		for dev in devices:
			if (dev.addrType != btle.ADDR_TYPE_PUBLIC ):
				print ("Error ,addr=random addr : " + str( dev.addrType ))
				continue
			print "addr=%s (%s)" % (dev.addr , dev.addrType  )
#			print "Device=%s (%s), RSSI=%d dB" % (dev.addr, dev.addrType, dev.rssi)
			#for (adtype, desc, value) in dev.getScanData():
			#	print "  %s=%s" % (desc, value)
        