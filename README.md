Doge Monitor
============

This python script uses a Raspberry Pi and Adafruit 16x2 character LCD
to display interesting network stats about the Dogecoin network.

Based on sample code by PieMan2201 on reddit (thanks!), this script
cycles between 4 displays:
* Network difficulty and estimated hash rate (from dogechain.info)
* Total Dogecoins in existence (from dogechain.info)
* Current USD price (per 1k Doge) and 24hr change (from coinmarketcap.northpole.ro)
* Current BTC/Doge price in satoshi (from coinmarketcap.northpole.ro)

Display changes every 5 seconds, with network refreshes approx every 5 minutes

Parts:

[Raspberry Pi @ Adafruit](http://www.adafruit.com/products/998)

[RGB Negative 16x2 LCD @ Adafruit](http://www.adafruit.com/products/1110)

Optional:

[Miniature WiFi dongle @ Adafruit](http://www.adafruit.com/products/814)

[rPi + LCD Plate enclosure @ Built-to-spec](http://builttospecstore.storenvy.com/collections/156322-raspberry-pi/products/2038094-adafruit-lcd-keypad-plate-enclosure)


![DogeMonitor](https://github.com/rand000m/dogemonitor/raw/master/DogeMonitor.gif)


