# python ,BLE gateway server2 (BETA)

 Version: 0.9.1

 Author  : Kouji Nakashima / kuc-arc-f.com

 date    : 2017/08/05

***

## Summary
* scan to Bluetooth device address version (public address )
* BLE gateway server (BLE Central device), http send possible
* running for nano Pi NEO ,raspberry Pi 
* Peripheral device -- RN4020 BLE + atmega328P ,Low power version.


<img src="https://github.com/kuc-arc-f/screen-img/blob/master/python/ss-rPI-gateway.png?raw=true" style="max-width : 100%; max-height: 600px;">

***

### thanks

* bluepy
https://github.com/IanHarvey/bluepy


***
### Usage
* ble_gateway_sv.py /public address setting (48 bit)
 
 ex: mPubAddr01="00:00:00:00:00:00" and add to init_param()
* http_func.py -- http send URL, setting 
* ble_gateway_sv.py send_http() -- request param setting
* sudo python ble_gateway_sv.py

***

### update
* v0.9,1  new

 related (old) version: 

https://github.com/kuc-arc-f/ble_gateway_sv

***

### blog

http://knaka0209.blogspot.jp/2017/08/nanoPi-4.html

(related blog )

rasPi BLE server:

http://knaka0209.blogspot.jp/2017/07/raspi-5-BLE.html

peripheral device:

http://knaka0209.blogspot.jp/2017/07/esp32-21.html


***



