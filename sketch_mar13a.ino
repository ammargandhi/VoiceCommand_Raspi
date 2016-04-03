
char a;

int count_power1=157;
int count_power2=313;
int count_power3=471;
int count_power4=625;
volatile int temp;
void setup()
{
  Serial.begin(9600);
  pinMode(13,OUTPUT); 
  attachInterrupt(1,zcd_1,RISING);
   
}

void loop()
{
  if(Serial.available())
  {
    a=Serial.read();}
    
if(a=='1')
{
temp=count_power1;
}
if(a=='2')
{
  temp=count_power2;
}

if(a=='3')
{
  temp=count_power3;
}
if(a=='4')
{
  temp=count_power4;
}
    
    
  

}

void zcd_1()
{
   noInterrupts();
  TCCR1A=0;
  TCCR1B=0;
  TCNT1=0;
  OCR1A=temp;
  TCCR1B|=(1<<WGM12);
  TCCR1B|=(1<<CS12);
  TIMSK1|=(1<<OCIE1A);
  interrupts();
}

ISR(TIMER1_COMPA_vect)
{
  digitalWrite(13,HIGH);
  delayMicroseconds(5000);
  digitalWrite(13,LOW);
  TCCR1A=0;
  TCCR1B=0;
  TCNT1=0;
}
