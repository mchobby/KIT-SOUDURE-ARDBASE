//une sortie analogique sur la broche 11
const int sortieAnalogiqueOrange = 9;
const int sortieAnalogiqueRouge = 10;
void setup()
{
  Serial.begin(9600);
    pinMode(sortieAnalogiqueOrange, OUTPUT);
    pinMode(sortieAnalogiqueRouge, OUTPUT);
}
 
void loop()
{
    //on met un rapport cyclique de x/255% qui varie avec la boucle
  for (int x = 0 ; x<100 ; x++) {
    analogWrite(sortieAnalogiqueOrange, x);
    analogWrite(sortieAnalogiqueRouge, 100-x);
    Serial.println(x);
    Serial.println(100-x);
    delay(50);
  }
}
