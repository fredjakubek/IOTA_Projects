#Import key depencies
from iota import Iota
from iota import Address
import RPi.GPIO as GPIO
import time
import datetime


# Setup O/I PIN's for output functionality on the Raspberry Pi 3 B+
LEDPIN=18
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(LEDPIN,GPIO.OUT)
GPIO.output(LEDPIN,GPIO.LOW)


# Function to check address balance on the IOTA-tangle 
def checkbalance():

    print("Checking balance")
    gb_result = api.get_balances(address)
    balance = gb_result['balances']
    return (balance[0])

# Set the fullnode to be used on the IOTA Tangle 
iotaNode = "https://nodes.thetangle.org:443"

# Initialize an IOTA object
api = Iota(iotaNode, "")

# IOTA address to check for funds; specify target address 
address = [Address(b'XXXXXXXX')]

# Measure increase of funds by monitoring funds added to initial fund balance   
currentbalance = checkbalance()
lastbalance = currentbalance

# Intialize variables
devicebalance = 0
balanceCheckCount = 0
devicestatus = False

# Main loop executed every 5 seconds
while True:
    
    # Check for new funds and add to devicebalance when found
    if balanceCheckCount == 10:
        currentbalance = checkbalance()
        if currentbalance > lastbalance:
            devicebalance = devicebalance + (currentbalance - lastbalance)
            lastbalance = currentbalance
        balanceCheckCount = 0

    # Manage devicebalance and device ON/OFF
    if devicebalance > 0:
        if devicestatus == False:
            print("Device ON")
            GPIO.output(LEDPIN,GPIO.HIGH)
            devicestatus=True
        devicebalance = devicebalance -1       
    else:
        if devicestatus == True:
            print("Device OFF")
            GPIO.output(LEDPIN,GPIO.LOW)
            devicestatus=False
 
    # Print remaining device balance     
    print(datetime.timedelta(seconds=devicebalance))

    # Increase balance check counter
    balanceCheckCount = balanceCheckCount +1

    # Pause for 5 sec.
    time.sleep(5)
