#include <ESP8266WiFi.h>

//esp8266 wemos wifi d1 mini board


const char* ssid     = "iPhone"; // 사용 중 인 와이파이 이름
const char* password = "qwerty1234"; // 와이파이 패스워드
WiFiServer server(80);

void setup() {
  pinMode(A0,INPUT);
  pinMode(LED_BUILTIN, OUTPUT);
  pinMode(12, OUTPUT);
  Serial.begin(115200); // 시리얼 통신, 속도 115200
  delay(10);
  Serial.println();

  // Connect to WiFi network
  WiFi.mode(WIFI_STA);
  Serial.println();
  Serial.println();
  Serial.print("Connecting to ");
  Serial.println(ssid);

  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(100);
    Serial.print(".");
  }

  Serial.println("");
  Serial.println("WiFi connected");

  // Start the server
  server.begin();
  Serial.println("Server started");

  // Print the IP address
  Serial.println(WiFi.localIP());
}

void loop() {
  delay(50);
  WiFiClient client = server.available();
  client.print("HTTP/1.1 200 OK");
  client.print("Content-Type: text/html");
  client.print("Refresh: 0.1");  // 자동으로 웹페이지 새로고침 (0.1초 설정)
  String request = client.readStringUntil('\n');
  Serial.println(request);
  if(request.indexOf("GET") == -1){
    Serial.println("offmask");
  }
  else{
    Serial.println("onmask");
  }

}
