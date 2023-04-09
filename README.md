# ESP8266 Access Point with LED Control and Array Processing

This project demonstrates using an ESP8266 NodeMCU as an access point to create a Wi-Fi network, control an LED connected to the TX pin, and process an array sent via an HTTP POST request. The ESP8266 runs an HTTP server and listens for incoming requests on specific endpoints.

## Features

- Create a Wi-Fi access point with a custom SSID and password
- Control an LED connected to the TX (GPIO1) pin via HTTP GET requests
- Process and send an array received via an HTTP POST request to the Serial1 port

## Prerequisites

- [Arduino IDE](https://www.arduino.cc/en/software)
- [ESP8266 Core for Arduino](https://github.com/esp8266/Arduino)
- [ArduinoJson library](https://arduinojson.org)
- [CH340 Windows 10 driver download](https://www.arduined.eu/ch340-windows-10-driver-download/)

##Quick start
+ Preference ==> setting
![Preference](https://github.com/Potassium-chromate/Set-up-for-esp8266-MCU/blob/main/picture/URL.png)
+ Tools==> board ==> esp8266 ==> Generic ESP8266Module
![Preference](https://github.com/Potassium-chromate/Set-up-for-esp8266-MCU/blob/main/picture/Board%20Manager.png)
## Hardware

- ESP8266 NodeMCU
- LED
- 330 ohm resistor
- Breadboard
- Jumper wires

## Wiring

1. Connect the LED's anode (longer leg) to the TX (GPIO1) pin on the ESP8266 NodeMCU.
2. Connect a 330-ohm resistor to the LED's cathode (shorter leg).
3. Connect the other end of the resistor to the GND pin on the ESP8266 NodeMCU.

## Endpoints
Paste this URL to your browser to do the action below.  
- `http://192.168.4.1/ledon` -  Turn on the LED connected to the TX pin
- `http://192.168.4.1/ledoff` - Turn off the LED connected to the TX pin
- `http://192.168.4.1/sendArray` - Send an array via an HTTP POST request (Content-Type: `text/plain`)

## Usage

1. Connect your device (e.g., smartphone, computer) to the Wi-Fi network created by the ESP8266 NodeMCU with the SSID "SAD_MAN" and password "20230313".
2. Use a web browser or tools like Postman or cURL to send HTTP requests to the ESP8266 NodeMCU on the specified endpoints.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
