# -*- coding: utf-8 -*-
#import os
import time
from datetime import timedelta, tzinfo
import appConst

mTZnum=9
mTZname="JST"

# timeZone
class timeZoneClass(tzinfo):
    def utcoffset(self, dt):
#        return timedelta(hours=9)
        return timedelta(hours=mTZnum )

    def dst(self, dt):
        return timedelta(0)

    def tzname(self, dt):
#        return 'JST'
        return mTZname
        
    def Is_validActive(self, iNum):
    	ret=0;
    	clsConst=appConst.appConstClass()
    	if clsConst.mActStart <= iNum:
    		if clsConst.mActEnd > iNum:
    			ret=1
#return ret
#return ret
#ret=1
    	return ret 






