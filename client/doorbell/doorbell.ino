#include <ESP8266WiFi.h>
#include "credentials.h"

const char* ssid = WIFI_SSID;
const char* password = WIFI_PASSWORD;

const char* host = HOST;
const int port = 12345;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  delay(10);
  Serial.println();
  if(!WiFi.SSID()){
    WiFi.begin(ssid, password);
    wifi_station_set_auto_connect(true);
  }
  Serial.print("Connecting to: ");
  Serial.print(ssid);
  Serial.println("...");

   int i = 0;
   while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print('.');
   }
   Serial.println("Connection established!");  
   Serial.print("IP address:\t");
   Serial.println(WiFi.localIP());  
   WiFiClient client;

  Serial.printf("\nConnectng to %s ...", host);
  if(client.connect(host, port)){
    Serial.println("connected!");
    client.print(MESSAGE);
    client.stop();
  }
  else {
    Serial.println("connection failed!");
    client.stop();
  }
}

void loop() {
}
