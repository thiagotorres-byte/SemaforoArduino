from pyfirmata import Arduino, util
import time
import requests

                                #void setup(){
Uno = Arduino('COM3')
                                     # Serial.begin(9600);
print('Olá Mundo!')                  # Serial.println("Olá Mundo!");   
                                #}
requestum = requests.get("http://localhost:8080/incluirum")

requestedois = requests.get("http://localhost:8080/incluirdois")


while True:                     # void loop(){

    Uno.digital[13].write(requestum.content)         # digitalWrite(13, HIGH);
    print('LED ligado')              # Serial.println("LED ligado");
    print(requestum.content)   
    time.sleep(1)                    # delay(1000);

    Uno.digital[13].write(requestedois.content)         # digitalWrite(13, LOW);
    print('LED desligado')           # Serial.println("LED desligado");
    print(requestedois.content)  
    time.sleep(1)                    # delay(1000);

                                #}
