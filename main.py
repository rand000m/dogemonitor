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

def showerr( str ):
   lcd.clear()
   lcd.message(str)
   time.sleep(2)
   return


lcd = Adafruit_CharLCDPlate()

lcd.begin(16,1)
lcd.backlight(lcd.RED)
lcd.message("Doge Monitor!")

while True:
  try:
    nethash = urllib2.urlopen("https://dogechain.info/chain/Dogecoin/q/nethash/60/-61/-1?format=json")
    nethash_data = json.load(nethash)
  except:
    showerr("Error getting\nDogechain info")

  try:    
    totaldoge = urllib2.urlopen("https://dogechain.info/chain/Dogecoin/q/totalbc")
    total_coins = long(round(float(totaldoge.read()),0))
  except:
    showerr("Error getting\nDogechain totals")
  try:
    doge = urllib2.urlopen("http://coinmarketcap.northpole.ro/api/v5/DOGE.json")
    doge_data = json.load(doge)
  except:
    showerr("Error getting\nCMC API info")
    
  try:
    doge_usd = mul(float(doge_data["price"]["usd"]), 1000)
  except:
    showerr("Error calculating\ndoge_usd")
    doge_usd = -1

  try:
    doge_btc = mul(float(doge_data["price"]["btc"]), pow(10,8))
  except:
    showerr("Error calculating\ndoge_btc")
    doge_btc = -1

  try:
    doge_cap = long(round(float(doge_data["marketCap"]["usd"]),0))
  except:
    showerr("Error calculating\ndoge_cap")
    doge_cap = -1

  try:
    doge_rank = int(doge_data["position"])
  except:
    showerr("Error calculating\ndoge_rank")
    doge_rank = -1

  try:
    doge_volumeu = long(round(float(doge_data["volume24"]["usd"]),0))
  except:
    showerr("Error calculating\ndoge_volumeu")
    doge_volumeu = -1

  try:
    doge_volumeb = long(round(float(doge_data["volume24"]["btc"]),0))
  except:
    showerr("Error calculating\ndoge_volumeb")
    doge_volumeb = -1

  try:
    doge_1hu = doge_data["change1h"]["usd"]
    doge_7hu = doge_data["change7h"]["usd"]
    doge_7du = doge_data["change7d"]["usd"]
    doge_1hb = doge_data["change1h"]["btc"]
    doge_7hb = doge_data["change7h"]["btc"]
    doge_7db = doge_data["change7d"]["btc"]
  except:
    showerr("Error getting\nchange values")
    doge_1hu = -1
    doge_7hu = -1
    doge_7du = -1
    doge_1hb = -1
    doge_7hb = -1
    doge_7db = -1

    #print "usd %.3f/1k" % doge_usd
    #print "btc %.1f" % doge_btc
    #print "cap %d" % doge_cap
    #print "volume %d %d" % (doge_volumeu,doge_volumeb)
    #print "change   %.0f/%.0f/%.0f %% usd" % (float(doge_1hu),float(doge_7hu),float(doge_7du))
    #print "1h/7h/7d %.0f/%.0f/%.0f %% btc" % (float(doge_1hb),float(doge_7hb),float(doge_7db))

  for x in xrange(refresh):
    try:
      lcd.clear()
      lcd.message("""Diff %5d\nNet %6d MH/s""" % (nethash_data[0][4],nethash_data[0][7]/1000000))
      time.sleep(delay)
      
      lcd.clear()
      lcd.message("""Total Doge\n%s""" % format(total_coins, ",d"))
      time.sleep(delay)
      
      lcd.clear()
      lcd.message("""Market Cap (%d)\n$%s""" % (doge_rank,format(doge_cap, ",d")))
      time.sleep(delay)

      lcd.clear()
      lcd.message("""Volume (24h)\nUSD $%s""" % format(doge_volumeu, ",d"))
      time.sleep(delay)
 
      lcd.clear()
      lcd.message("""Volume (24h)\nBTC %s""" % format(doge_volumeb, ",d"))
      time.sleep(delay)

      lcd.clear()
      lcd.message("""USD $%.2f/1k\n    %+.0f%% (1h)""" % (doge_usd,float(doge_1hu)))
      time.sleep(delay/2)
      lcd.clear()
      lcd.message("""USD $%.2f/1k\n    %+.0f%% (7h)""" % (doge_usd,float(doge_7hu)))
      time.sleep(delay/2)
      lcd.clear()
      lcd.message("""USD $%.2f/1k\n    %+.0f%% (7d)""" % (doge_usd,float(doge_7du)))
      time.sleep(delay/2)
    
      lcd.clear()
      lcd.message("""BTC %.0f satoshi\n    %+.0f%% (1h)""" % (doge_btc,float(doge_1hb)))
      time.sleep(delay/2)
      lcd.clear()
      lcd.message("""BTC %.0f satoshi\n    %+.0f%% (7h)""" % (doge_btc,float(doge_7hb)))
      time.sleep(delay/2)
      lcd.clear()
      lcd.message("""BTC %.0f satoshi\n    %+.0f%% (7d)""" % (doge_btc,float(doge_7db)))
      time.sleep(delay/2)

    except:
      showerr("Error displaying\nvalues")
  
    lcd.clear()
    lcd.message("Refreshing data")

