# IOTA_Projects
Building projects on the IOTA Tangle using the PyOTA-library 

## IOTA Charging Station using the Raspberry pi 3 b+
The project uses the PyOTA library to convert a Raspberry Pi 3 b+ into a payment-terminal on the IOTA tangle to enable the purchase of the use of an electric vehicle charging station.
This project is an implementation of the tutorial series by Hugo Gregersen posted on [Medium] (https://medium.com/@hugogregersen) and his [GitHub page](https://github.com/huggre/). 

## IOTA Charging Station using the ESP8266 enabled WiFi module
An extension of the IOTAChargingStation project using an ESP8266 WiFi modules chip instead of the Raspberry pi 3 b+ to receive the 
transmitted http request after approval of the transaction on the IOTA tangle. IOTA transaction confirmation is outsourced and executed 
to an external machine (in this case my laptop) which upon transaction validity confirmation sends an http request to the ESP8266 chip 
that then turns on power for the device. The above code represents the Python file used on the external machine. 
This project follows the tutorial by Hugo Gregersen posted on [Medium] (https://medium.com/coinmonks/integrating-physical-devices-with-iota-wifi-edition-9de749bc22f5) and his [GitHub page](https://github.com/huggre/). 
