import time
import os
import sys
import urllib            # URL functions
import urllib2           # URL functions
import serial
import RPi.GPIO as GPIO
INTERVAL      = 1    # Delay between each reading (mins)

THINGSPEAKKEY = 'Z6YPC4SIV6M59QKM'
THINGSPEAKURL = 'https://api.thingspeak.com/update'

def sendData(url,key,field1,temp):
  """
  Send temp to internet site
  """

  values = {'api_key' : key,'field1' : temp}

  postdata = urllib.urlencode(values)
  req = urllib2.Request(url, postdata)

  log = time.strftime("%d-%m-%Y,%H:%M:%S") + ","
  log = log + "{:.1f}C".format(temp) + ","
  
  try:
    # Send data to Thingspeak
    response = urllib2.urlopen(req, None, 5)
    html_string = response.read()
    response.close()
    log = log + 'Update ' + html_string

  except urllib2.HTTPError, e:
    log = log + 'Server could not fulfill the request. Error code: ' + e.code
  except urllib2.URLError, e:
    log = log + 'Failed to reach server. Reason: ' + e.reason
  except:
    log = log + 'Unknown error'

  print log
  
def readline(usb):
  eol='\r'
  leneol=len(eol)
  line=bytearray()
  while True:
    c=usb.read(1)
    if c:
        line+=c
        if line[-leneol:]==eol:
          break
    else:
        break
  return bytes(line)

def main():

  global INTERVAL
  global THINGSPEAKKEY
  global THINGSPEAKURL

  

   
  try:
    #GPIO.setmode(GPIO.BCM)
    #GPIO.setwarnings(False)
    #GPIO.setup(17 , GPIO.OUT)
    while True:
      
      
     # GPIO.output(17, True)
     # usleep(100)
     # GPIO.output(17, False)
  
      ser=serial.Serial('/dev/ttyACM0',baudrate=9600)      
      tempx= readline(ser)
      y=float(tempx)
      
      sendData(THINGSPEAKURL,THINGSPEAKKEY,'field1',y)
           
      for i in range(0,INTERVAL*60):
        time.sleep(1)

  except :
    # Reset GPIO settings
    print "a"

if __name__=="__main__":
   main()
