# -*- coding: utf-8 -*- 
import os
import json
import appConst
import datModel

#
class configClass:
	#
	def load_config(self,  fname ):
		clsDat= datModel.datModelClass()
		sDir =os.path.dirname(os.path.abspath(__file__))
		sPath =sDir +"/"+ fname
		print( "sPath=" +sPath)
		file=open(sPath  ,'r')
		json_dict = json.load(file)
		iCt=0
		for item in json_dict:
#			print (item)
			print json_dict[item ]
#			clsDat.set_addr(iCt,  json_dict[item ] )
			clsDat.set_device(iCt,  json_dict[item ] ,item)
			iCt =iCt+1
		


