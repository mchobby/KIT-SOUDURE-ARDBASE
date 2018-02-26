/*

 Simuler un feu de circulation et le changement de son état
 Le feu de circulation est au vert
 Déclenche le feu rouge lorsque le bouton connecté sur la broche 12 est appuyé
 
 */

// Initialisation des constantes :
const int bouton = 2;     // Numéro de la broche à laquelle est connecté le bouton poussoir
const int ledVerte =  8;      // Numéro de la broche à laquelle est connectée la LED verte
const int ledJaune =  9;      // Numéro de la broche à laquelle est connectée la LED jaune
const int ledRouge =  10;      // Numéro de la broche à laquelle est connectée la LED rouge

// Déclaration des variables :
int etatBouton = 0;         // variable qui sera utilisée pour stocker l'état du bouton

// le code dans cette fonction est exécuté une fois au début
void setup() {
  // indique que la broche ledVerte, ledJaune et ledRouge sont des sorties :
  pinMode(ledVerte, OUTPUT);
  pinMode(ledJaune, OUTPUT);      
  pinMode(ledRouge, OUTPUT);        
  // indique que la broche bouton est une entrée :
  pinMode(bouton, INPUT);     
}

// le code dans cette fonction est exécuté en boucle
void loop(){
  // lit l'état du bouton et stocke le résultat dans etatBouton
  etatBouton = digitalRead(bouton);
  // Si etatBouton est à 5V (HIGH) c'est que le bouton est appuyé
  if (etatBouton == HIGH) {     
    digitalWrite(ledVerte, LOW);   // on éteind la LED verte
    digitalWrite(ledJaune, HIGH);  // on allume la LED jaune
    delay(2000);                   // on laisse allumée la led jaune 2 secondes 
    digitalWrite(ledJaune, LOW);   // on éteind la LED jaune
    digitalWrite(ledRouge, HIGH);  // on allume la LED rouge
    delay(4000);                   // on laisse allumée la LED rouge 4 secondes
  }
  else {
    // sinon on allume la LED verte et on éteind les autres
    digitalWrite(ledVerte, HIGH); 
    digitalWrite(ledJaune, LOW);
    digitalWrite(ledRouge, LOW);
  }
}

