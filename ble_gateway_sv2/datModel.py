# -*- coding: utf-8 -*- 
# クラス
import appConst

#define
mMaxdevice=10
mBleDat=[]  # List
mRow = {
 "adv_name": ""
, "pubAddr": ""
, "val_1" : ""
, "val_2" : ""
, "val_3" : ""
, "val_4" : ""
, "val_5" : ""
} #dict
mNG_CODE=0
mOK_CODE=1

#datModel
class datModelClass:
    # mMax_GapLength=15
    
    #
    def __init__(self):
        print ""
        
    def init_proc(self):
    	for i in range(0 ,mMaxdevice  ):
    		mBleDat.append(mRow.copy() )
    
    def clear_List(self):
    	for i in range(0 ,mMaxdevice  ):
    		mBleDat[i]["val_1"]=""
    		mBleDat[i]["val_2"]=""
    		mBleDat[i]["val_3"]=""
    		mBleDat[i]["val_4"]=""
    		mBleDat[i]["val_5"]=""
    
    def set_addr(self,  iNum,  addr):
    	mBleDat[iNum]["pubAddr"]= addr
    
    #
    def set_device(self,  iNum,  addr, name):
    	mBleDat[iNum]["pubAddr"]= addr
    	mBleDat[iNum]["adv_name"]= name
    	
    def debug_printDat(self):
    	#print mBleDat
    	for i in range(0 ,mMaxdevice  ):
    		sVal_1=",val_1=" + mBleDat[i]["val_1"]
    		sVal_2=",val_2=" + mBleDat[i]["val_2"]
    		sVal_3=",val_3=" + mBleDat[i]["val_3"]
    		sVal_4=",val_4=" + mBleDat[i]["val_4"]
    		sVal_5=",val_5=" + mBleDat[i]["val_5"]
    		
#    		print ( "i="+str(i)+ ", name=" + mBleDat[i]["adv_name"] +",val_1=" + mBleDat[i]["val_1"] +",val_2=" + mBleDat[i]["val_2"]+",val_3=" + mBleDat[i]["val_3"]  )
    		print ( "i="+str(i)+ ", name=" + mBleDat[i]["adv_name"]  +", addr=" + mBleDat[i]["pubAddr"] +sVal_1 + sVal_2+ sVal_3 +sVal_4 +sVal_5 )
    #
#    def get_addrByName(self ,name  ):
#   	sRet=""
#   	for i in range(0 ,mMaxdevice  ):
#   		if ( mBleDat[i]["adv_name"]== name ):
#   			sRet=mBleDat[i]["pubAddr"]
#   	return sRet
    #
    def get_datByName(self ,name , field ):
    	sRet=""
    	for i in range(0 ,mMaxdevice  ):
#    		if ( mBleDat[i]["pubAddr"]== addr ):
    		if ( mBleDat[i]["adv_name"]== name ):
    			if( field== 1):
    				sRet=mBleDat[i]["val_1"]
    			if( field== 2):
    				sRet=mBleDat[i]["val_2"]
    			if( field== 3):
    				sRet=mBleDat[i]["val_3"]
    			if( field== 4 ):
    				sRet=mBleDat[i]["val_4"]
    			if( field== 5 ):
    				sRet=mBleDat[i]["val_5"]
    	return sRet
    #
    def recvCount(self):
    	ret= mNG_CODE
    	iCount =0
    	iCount2=0
    	for i in range(0 ,mMaxdevice  ):
    		#if (len(mBleDat[i]["adv_name"] ) > 0):
    		if (len(mBleDat[i]["pubAddr"] ) > 0):
    			iCount= iCount+1
    	
    	if (iCount < 1):
    		return ret
    		
    	for ii in range(0 , iCount ):
    		if(len(mBleDat[ii]["pubAddr"] ) > 0 ):
    			if(len(mBleDat[ii]["val_1"] ) > 0 ):
    				iCount2= iCount2 +1
    	print("iCount2=" +  str(iCount2 ) )
    	
    	if(iCount2 > 0):
    		ret=mOK_CODE
    	
    	return ret
    	
    def valid_addr(self, addr ):
    	ret=mNG_CODE
    	for i in range(0 ,mMaxdevice  ):
    		if(mBleDat[i ]["pubAddr"]==addr ):
    			ret= mOK_CODE
    			return ret
    	return ret

    #def set_advValues(self, name , sBuff ):	
    def set_advValues(self, addr , sBuff ):
    	clsConst=appConst.appConstClass()
    	sV1=""
    	sV2=""
    	sV3=""
    	sV4=""
    	sV5=""
    	#for j in range(3 ,8 ):
    	for j in range(0 ,5 ):
    		sV1 += sBuff[j]
    	for j1 in range(5 ,10 ):
    		sV2 += sBuff[j1 ]
    	if (len(sBuff) >= clsConst.mMax_GapLength_25 ):
    		for j2 in range(10 ,15 ):
    			sV3 += sBuff[j2 ]
    		for j3 in range(15 ,20 ):
    			sV4 += sBuff[j3 ]
    		for j4 in range(20 , 25 ):
    			sV5 += sBuff[j4 ]
    		
    	for i in range(0 ,mMaxdevice  ):
    		if(mBleDat[i ]["pubAddr"]==addr ):
    			mBleDat[i ]["val_1"]=sV1
    			mBleDat[i ]["val_2"]=sV2
    			mBleDat[i ]["val_3"]=sV3
    			mBleDat[i ]["val_4"]=sV4
    			mBleDat[i ]["val_5"]=sV5

    	
#    def test(self, sId):
#   	print "test"

