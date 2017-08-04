#
# raspberryPi, BLE Gateway server.
#
from bluepy.btle import Scanner, DefaultDelegate
from bluepy import btle
import datetime
import threading
import time
import sys
import traceback
import appConst
import datModel
import http_func
import decode

#define
mTimeMax=30
mPubAddr01=""
mPubAddr02=""
mPubAddr03=""

mNG_CODE=0
mOK_CODE=1

class ScanDelegate(DefaultDelegate):
    def __init__(self):
        DefaultDelegate.__init__(self)

    def handleDiscovery(self, dev, isNewDev, isNewData):
        if isNewDev:
            print "Discovered device", dev.addr
        elif isNewData:
            print "Received new data from", dev.addr

def init_param(clsDat ):
#	clsDat= datModel.datModelClass()
	clsDat.init_proc()
	clsDat.set_addr(0,  mPubAddr01)
	clsDat.set_addr(1,  mPubAddr02)
	
	#clsDat.debug_printDat()
	
#def set_advManufact(clsDat ,value ):
def set_advManufact(clsDat ,value ,addr ):
	clsDec= decode.decodeClass()
	sValue = clsDec.convert_hexToString(value)
	print("sValue="+ sValue)
	if ( clsDat.valid_addr(addr )==0 ):
		print ("Error, invalid addr="+ addr )
		return
	else:
		clsDat.set_advValues( addr , sValue )

#
#def set_advData(clsDat ,value ):
def set_advData(clsDat ,value ,addr ):
#	clsDat= datModel.datModelClass()
	if ( clsDat.valid_addr(addr )==0 ):
		print ("Error, invalid addr="+ addr )
		return
	else:
		clsDat.set_advValues(addr , value )
	
def execute_httpSend(sReq):
	cHttp = http_func.http_funcClass()
	cHttp.send_push(sReq )

def send_http(clsDat):
	clsDat= datModel.datModelClass()
	if(  clsDat.recvCount() ==0):
		print("# Nothing, data")
		return
	#else:
	#debug
	clsDat.debug_printDat()
	print("# http-start")
	sReq=""
	sV1=clsDat.get_datByAddr(mPubAddr01 , 1)
	if (len(sV1 ) > 0 ):
		sReq +="&field1=" + str(sV1)
	sV2=clsDat.get_datByAddr(mPubAddr02 , 1)
	if (len(sV2 ) > 0 ):
		sReq +="&field2=" + str(sV2)
	th=threading.Thread(target=execute_httpSend ,args=(sReq, ) )
	th.start()

def Is_valid_desc(desc):
	ret=mNG_CODE
	clsConst=appConst.appConstClass()
	if (desc==clsConst.mDesc_Localname):
		ret=mOK_CODE
	if (desc==clsConst.mDesc_mafact ):
		ret=mOK_CODE
	return ret

if __name__ == "__main__":
	clsDat= datModel.datModelClass()
	clsConst=appConst.appConstClass()
	init_param(clsDat )
	scanner = Scanner().withDelegate(ScanDelegate())
	from datetime import datetime
	tmBef = datetime.now()
	while True:
		tmNow = datetime.now()
		tmSpan = tmNow - tmBef
		iSpan = tmSpan.total_seconds()
		sTime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
		print("time=" +sTime)
		# BLE
		devices = scanner.scan( 2.0)
		for dev in devices:
			for (adtype, desc, value) in dev.getScanData():
				#if(desc==  clsConst.mDesc_Localname ):
				if (dev.addrType != btle.ADDR_TYPE_PUBLIC):
					print("Error, addType=" + str( dev.addrType ))
					continue
				# print "Device=%s(%s), RSSI=%d dB" % (dev.addr, dev.addrType, dev.rssi)
				if (Is_valid_desc(desc )== mOK_CODE):
					print "  %s=%s" % (desc, value)
					if(desc== clsConst.mDesc_mafact):
						if ( len(value ) >= (clsConst.mMax_GapLength_25 * 2) ):
							set_advManufact(clsDat , value, dev.addr)
							#clsDat.debug_printDat()
						else:
							print ("Error ,manufact Length =" + str(len(value ) ) )
		#http
		if iSpan > mTimeMax:
			tmBef = datetime.now()
			try:
				send_http(clsDat )
				clsDat.clear_List()
			except:
				print "--------------------------------------------"
				print traceback.format_exc(sys.exc_info()[2])
				print "--------------------------------------------"
		

					

