 /* Exemple simple testant les Photo-RÃ©sistances. 
 
Connectez l'une des broches de la photo-rÃ©sistance sur 5V, et l'autre sur l'entrÃ©e Analogique 0.
Ensuite, connecter une rÃ©sistance de 10Ko sur la broche analogique 0 et l'autre bout Ã  la masse. 
Connectez une LED Ã  la pin 11 par l'intermÃ©diaire d'une rÃ©sistance.
Pour plus d'information: 
  * voir http://mchobby.be/wiki/index.php?title=Photo-rÃ©sistance (en FRANCAIS)  
  * voir htt://www.ladyada.net/learn/sensors/cds.html            (en anglais)
*/
 
int photocellPin = 2;     // La photo-rÃ©sistaance raccordÃ©e sur la PIN A0 (avec une rÃ©sistance Pull-Down de 10K Ohms)
int photocellReading;     // Contient la lecture de sur senseur  (pont diviseur Photo-rÃ©sistance + RÃ©sistance)
int LEDpin = 9;          // LED rouge connectÃ©e sur la pin 11 (sortie PWM)
int LEDbrightness;        // 
void setup(void) {
  // Configuration du port sÃ©rie pour envoyer des message de dÃ©bugging
  Serial.begin(9600);   
}
 
void loop(void) {
  photocellReading = analogRead(photocellPin);  
 
  Serial.print("Lecture Analogique = ");
  Serial.println(photocellReading);     // La valeur analogique brute
 
  // Plus le senseur est dans l'ombre et plus la LED est brillante.
  // Cela signifie que nous devons INVERSER la lecture de 0-1023 vers 1023-0
  photocellReading = 1023 - photocellReading;
  // Maintenant, nous transformons les valeurs de 0-1023 vers 0-255 (puisque une sortie PWM/analogique utilise cette plage de valeurs)
  LEDbrightness = map(photocellReading, 0, 1023, 0, 255);
  analogWrite(LEDpin, LEDbrightness);
 
  delay(100);
}

