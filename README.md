# Project: ESP8266 Access Point with LED Control and Array Processing

## Features:
- Create a Wi-Fi access point with a custom SSID and password
- Control an LED connected to the TX (GPIO1) pin via HTTP GET requests
- Process and send an array received via an HTTP POST request to the Serial1 port
- Parse the received array using the ArduinoJson library
- Send the array elements as 8-bit integers over the Serial1 interface  

## Prerequisites:
- Arduino IDE
- ESP8266 Core for Arduino
- ArduinoJson library
- CH340 Windows 10 driver download  

## Quick Start:
1. Open the Arduino IDE, go to File > Preferences, and add the following URL to the "Additional Boards Manager URLs" field:
   http://arduino.esp8266.com/stable/package_esp8266com_index.json
2. Go to Tools > Board > Boards Manager and search for "ESP8266". Install the "esp8266" package by ESP8266 Community.
3. Select the "Generic ESP8266 Module" from Tools > Board > ESP8266 Modules.
4. Install the "ArduinoJson" library by Benoit Blanchon via Sketch > Include Library > Manage Libraries.
5. Connect your ESP8266 NodeMCU to your computer using a USB cable.
6. Replace `your_SSID` and `your_PASSWORD` in the code with your desired WiFi SSID and password.
7. Upload the sketch to your ESP8266 NodeMCU.  

## Hardware:
- ESP8266 NodeMCU
- LED
- 330 ohm resistor
- Breadboard
- Jumper wires  

## Wiring:
1. Connect the LED's anode (longer leg) to the TX (GPIO1) pin on the ESP8266 NodeMCU.
2. Connect a 330-ohm resistor to the LED's cathode (shorter leg).
3. Connect the other end of the resistor to the GND pin on the ESP8266 NodeMCU.  

## Test
- use `test_code.py` to post an array to the server and see if the server can send the array back  
- Connect `http://192.168.4.1/test`execute `test_code.py`  

## Endpoints:
- http://192.168.4.1/ledon - Turn on the LED connected to the TX pin
- http://192.168.4.1/ledoff - Turn off the LED connected to the TX pin
- http://192.168.4.1/sendArray - Send an array via an HTTP POST request (Content-Type: text/plain)  

## Usage:
1. Connect your device (e.g., smartphone, computer) to the Wi-Fi network created by the ESP8266 NodeMCU with the SSID `your_SSID` and password `your_PASSWORD`.
2. Use a web browser or tools like Postman or cURL to send HTTP requests to the ESP8266 NodeMCU on the specified endpoints. The server will process the array elements and send them as 8-bit integers over the Serial1 interface.
3. The server will respond with the status of the received request:
   - 200 OK: Array received and processed successfully.
   - 400 Bad Request: Missing array data or invalid FPGA flag value.
   - 503 Service Unavailable: FPGA is busy.  

## Aware
- Because D9(RX) is D9 is primarily used for the UART (Serial) RX function. When using the UART for communication, you should avoid using the D9 (RX) and D10 (TX) pins as GPIO pins. Thus, we should add this to the code  
```arduino
const int ready_flag = D9;
pinMode(ready_flag, OUTPUT); // Add this line to set ready_flag pin as OUTPUT
pinMode(ready_flag, OUTPUT); // Add this line to set ready_flag pin as OUTPUT
```


## License:
This project is licensed under the MIT License.


