#!/usr/bin/python

from Adafruit_CharLCDPlate import Adafruit_CharLCDPlate
from subprocess import *
import urllib2
import time
import json
from math import exp
from operator import mul

delay = 5 # 20 second display cycle with 4 messages
refresh = 15 # 5 minute refresh at 20 seconds per display cycle

lcd = Adafruit_CharLCDPlate()

lcd.begin(16,1)

lcd.message("Doge Monitor!")

while True:
  try:
    nethash = urllib2.urlopen("https://dogechain.info/chain/Dogecoin/q/nethash/60/-61/-1?format=json")
    nethash_data = json.load(nethash)
    
    totaldoge = urllib2.urlopen("https://dogechain.info/chain/Dogecoin/q/totalbc")
    total_coins = round(float(totaldoge.read()),0)
    
    dogeusd = urllib2.urlopen("http://coinmarketcap.northpole.ro/api/usd/doge.json")
    dogeusd_data = json.load(dogeusd)
    
    dogebtc = urllib2.urlopen("http://coinmarketcap.northpole.ro/api/btc/doge.json")
    dogebtc_data = json.load(dogebtc)
    
    dogebtc_price = str.split(str(dogebtc_data["price"]), "e")
   
    for x in xrange(refresh):
      lcd.clear()
      lcd.message("""Diff %d\nNet %d MH/s""" % (nethash_data[0][4],nethash_data[0][7]/1000000))
      
      time.sleep(delay)
      
      lcd.clear()
      lcd.message("""Total Doge\n%s""" % format(long(total_coins), ",d"))
      
      time.sleep(delay)
      
      lcd.clear()
      lcd.message("""Doge $%.2f/1k\n24hr %s""" % (float(dogeusd_data["price"])*1000,dogeusd_data["change24"]))
      
      time.sleep(delay)
  
      lcd.clear()
      lcd.message("""%.0f satoshi\nper Doge""" % mul(float(dogebtc_data["price"]),pow(10,8)))

      time.sleep(delay)

    lcd.clear()
    lcd.message("Refreshing data")

  except:
    lcd.clear()
    lcd.message("Error!")
    time.sleep(20)
    continue


