#
# raspberryPi, BLE Gateway server2.
# version : 0.9.3
# date : 2017/09/06
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
import config
import timeZone

#define
mTimeMax    =30
mTimeMaxScan=5

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
	clsConst=appConst.appConstClass()
	cls= config.configClass()
	clsDat.init_proc()
	cls.load_config(clsConst.mDeviceFile )
#	clsDat.set_addr(0,  mPubAddr01)
#	clsDat.set_addr(1,  mPubAddr02)
#	clsDat.set_addr(2,  mPubAddr03)
	
	clsDat.debug_printDat()
	
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
	sV1=clsDat.get_datByName("device1" , 1)
	if (len(sV1 ) > 0 ):
		sReq +="&field1=" + str(sV1)
	sV2=clsDat.get_datByName("device2" , 1)
	if (len(sV2 ) > 0 ):
		sReq +="&field2=" + str(sV2)
	sV2b=clsDat.get_datByName("device2" , 2 )
	if (len(sV2b ) > 0 ):
		sReq +="&field3=" + str(sV2b )
	sV3=clsDat.get_datByName("device3" , 1 )
	if (len(sV3 ) > 0 ):
		sReq +="&field4=" + str(sV3 )
	sV4=clsDat.get_datByName("device4" , 1 )
	if (len(sV4 ) > 0 ):
		sReq +="&field5=" + str(sV4 )
		
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

def proc_scan():
	print("#scan")
	devices = scanner.scan(2.0)
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

if __name__ == "__main__":
	clsDat= datModel.datModelClass()
	clsConst=appConst.appConstClass()
	init_param(clsDat )
	scanner = Scanner().withDelegate(ScanDelegate())
	from datetime import datetime
	clsJST= timeZone.timeZoneClass()
	nowJST = datetime.now(tz=clsJST )
	print(nowJST )
	tmBef     = nowJST
	tmBefScan = nowJST
	while True:
		time.sleep(1.0)
		#from datetime import datetime
		#
		tmNow = datetime.now(tz=clsJST )
#		tmNow = datetime.now()
		tmSpan = tmNow - tmBef
		tmSpanScan = tmNow - tmBefScan
		iSpan     = tmSpan.total_seconds()
		iSpanScan = tmSpanScan.total_seconds()
#		sTime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
		sTime = tmNow.strftime("%Y-%m-%d %H:%M:%S")
		print("time=" +sTime)
		sHH   = tmNow.strftime("%H")
		iHH = int(sHH)
#		print("iHH=" + str(iHH) )
		# BLE# Is_validActive
		if clsConst.mTimeAct==mOK_CODE:
			if clsJST.Is_validActive(iHH )==mNG_CODE:
				continue
		#
		if iSpanScan > mTimeMaxScan:
			tmBefScan = datetime.now(tz=clsJST )
			proc_scan()
		#http
		if iSpan > mTimeMax:
			tmBef = datetime.now(tz=clsJST )
			try:
				send_http(clsDat )
				clsDat.clear_List()
			except:
				print "--------------------------------------------"
				print traceback.format_exc(sys.exc_info()[2])
				print "--------------------------------------------"
		

					

