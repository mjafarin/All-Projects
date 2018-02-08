
int led1 = 3;
int led2 = 5;
int led3 = 6;

void setup()
{
  pinMode(led1, OUTPUT);
  pinMode(led2, OUTPUT);
  pinMode(led3, OUTPUT);
}

void loop()
{
  /*digitalWrite(led1, HIGH);
  delay(5000);
  digitalWrite(led2, HIGH);
  delay(5000);
  digitalWrite(led3, HIGH);
  delay(5000);*/
  digitalWrite(led1, LOW);
  delay(5000000);
  digitalWrite(led2, LOW);
  delay(5000000);
  digitalWrite(led3, LOW);
  delay(5000000);
} 
