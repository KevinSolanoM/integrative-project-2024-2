
//librerias:
#include "BluetoothSerial.h"
#include <ESP32Servo.h>

Servo servoBase;
Servo servoCanon;
Servo servoGat;
Servo servoRecarga;

//-------------servo base

int servo_base_pin = 23;
int base_ang = 90;

//------------------servo  gatillo

int servo_gat_pin = 22;
int gat_ang = 0;
int gat_pos = 1;
//-------------------servo cañon

int servo_canon_pin = 19;
int canon_ang = 90;

//-------------------servo cuerda
int servo_recarga_pin = 18;
int recarga_ang = 90;

//potenciometro 

int pot_pin = 4;
int pot_val;

//variables extras
int mode = 0; 
String mensaje; 


//chequear if el bluetooth esta disponible
#if !defined(CONFIG_BT_ENABLED) || !defined(CONFIG_BLUEDROID_ENABLED)
#error Bluetooth is not enabled! Please run `make menuconfig` to and enable it
#endif

// Check Serial Port Profile
#if !defined(CONFIG_BT_SPP_ENABLED)
#error Serial Port Profile for Bluetooth is not available or not enabled. It is only available for the ESP32 chip.
#endif
BluetoothSerial SerialBT;
TaskHandle_t Tarea0;

void setup() {

  Serial.begin(115200);
  SerialBT.begin("ESP32-Kevi");
  
  //segundo nuecleo
  xTaskCreatePinnedToCore(loop0, "Tarea_0",1000,NULL,1,&Tarea0,0);
  // cosas del bluetooth

  //pin modes

  servoBase.attach(servo_base_pin);
  servoBase.write(base_ang);
  servoCanon.attach(servo_canon_pin);
  servoCanon.write(canon_ang);
  servoGat.attach(servo_gat_pin);
  servoGat.write(gat_ang);
  servoRecarga.attach(servo_recarga_pin);
  servoRecarga.write(recarga_ang);
  pinMode(pot_pin, INPUT);
}



void loop() {
  //
  if (SerialBT.available()) {     // Verifica si hay datos disponibles en el buffer de Bluetooth
    mensaje = SerialBT.readString();  // Lee el mensaje completo y lo guarda en la variable
    Serial.print("Mensaje recibido: ");
    Serial.println(mensaje); 
    if ((mensaje.length())>8){
    Serial.println(mensaje.length());
    Serial.println("Error en la cantidad de caracteres recibida");
    }
    Serial.println(mensaje);

    mode = mensaje.substring(0,1).toInt();
    Serial.println(mode);
    if (mode == 0 ){
      base_ang = (mensaje.substring(1,4)).toInt();
      canon_ang = (mensaje.substring(4,6)).toInt();
      Serial.println("modo cambio de angulos");

      //SerialBT.print("b");
      //SerialBT.println(base_ang);
      
      servoBase.write(base_ang); 
      
      
    }
    else if (mode == 3 ){
      Serial.println("modo cambio de manual ");
      base_ang = (mensaje.substring(1,4)).toInt();
      canon_ang =((mensaje.substring(4,6)).toInt())*2;

      servoBase.write(base_ang); 
      Serial.println(canon_ang);
      servoCanon.write(canon_ang);
      
      
    }
    if (mode ==6 ){
      servoGat.write(180);
      Serial.println("cargado");
    }
    else if (mode == 1){
      base_ang = (mensaje.substring(1,4)).toInt();
      canon_ang = (mensaje.substring(5)).toInt();

      if (base_ang == 0 && canon_ang == 0 ){
        servoGat.write(90);
        servoRecarga.write(180);
        Serial.println("recargando");
        delay(5000);
        servoGat.write(0);
        servoRecarga.write(90);
        delay(2000);
        servoRecarga.write(0);
        delay(5000);
        servoRecarga.write(90);
        Serial.println("recargado");
      }else{
        if (base_ang == 1){
          servoRecarga.write(180);
          delay(5000);
        }
        else{
          servoRecarga.write(0);
          delay(5000);
        }
        servoRecarga.write(90);
      }
    }
    else if (mode == 7){
      servoGat.write(90);
      Serial.println("disparando");
    }

    
    
  }
  
  
}

void loop0(void*parameter){
  while (1==1){
  
  //pot_val = analogRead(pot_pin);
  pot_val = map(analogRead(pot_pin), 0, 4095, 0, 270);
  Serial.println(pot_val);
  SerialBT.println(pot_val);
  delay(100);
  }

}

void writeCanon(int ang_canon){ /// para poner el angulo del cañon con el angulo que quiero

  pot_val = map(analogRead(pot_pin),0,4095,0,270);
  while (abs(pot_val - ang_canon) > 5){
    if (pot_val > ang_canon){
      servoCanon.write(150);
    }else{
      servoCanon.write(30);
    }
    pot_val = map(analogRead(pot_pin),0,4095,0,270);
    delay(50);
  }
  servoCanon.write(90);
  
}