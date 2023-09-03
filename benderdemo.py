
#zufällig eine Datei abspielen
r= round(pyb.rng() / 0x3fffffff * 7)
if r>7:
	r=7

#auge auch/runter
servos.position(0, degrees=85)

#AugenLR und Kopf
servos.position(1, degrees=70)
pyb.delay(250);
for x in range(20):
	servos.position(6, degrees=90-x)
	pyb.delay(25);

#Augen und Kopf
servos.position(1, degrees=100)
pyb.delay(150);

for x in range(40):
	servos.position(6, degrees=90-20+x)
	pyb.delay(25);
	


#Augen LR
servos.position(1, degrees=85)
pyb.delay(250);

#Kopf
for x in range(20):
	servos.position(6, degrees=110-x)
	pyb.delay(25);
	


f = wave.open('bender'+str(r)+'.wav')
#f = wave.open('phoneme.wav')
wavlength=f.getnframes()/f.getframerate() #sec

print('play bender'+str(r)+'.wav',f.getnframes(), f.getframerate(),'Hz ',wavlength,'Sek')
dac.write_timed(f.readframes(f.getnframes()), f.getframerate())
f.rewind()

#Augen
if(r==0):#ohje, was für iditen
	servos.position(0, degrees=75)
#if(r==1):#ihr seid alle versager
#	servos.position(0, degrees=85)
#if(r==2):#mein name ist bender
#	servos.position(0, degrees=75)
if(r==3):#lachen
	servos.position(0, degrees=65)
if(r==4):#4=du meine güte
	servos.position(0, degrees=100)
#5=hallo ihr armen schlucker

if(r==6):#6=mmm, na schön
	servos.position(0, degrees=70)
#7=was geht sich das an, bleib mir vom leib	

contermax=200
mult=5
steppwait=round( f.getnframes()/f.getframerate()*mult*0.8 ) #0.1sec

counter=contermax

steppread=round(f.getnframes()/contermax)
buff=f.readframes(steppread*10)
counter-=10

print(steppwait,steppread)
testbytes=50
if testbytes>steppread:
	testbytes=steppread

#Mund
servos.position(3, degrees=60)
	
while counter>0:	
	buff=f.readframes(steppread)
	f0=0
	for y in range(0, testbytes):
		if buff[y]>128:
			f0+=(buff[y]-128)
		else:
			f0+=(128-buff[y])
	
	f0=round(f0/20)
	
	#print("f0" ,f0)
	mund=85
	an=0
	if f0>2:
		pyb.LED(1).on()
		mund=100
	else:
		pyb.LED(1).off()
		mund=85
	
	if f0>10:
		pyb.LED(2).on()
		mund=80
	else:
		pyb.LED(2).off()
	
	if f0>30:
		pyb.LED(3).on()
		#mund=70
	else:
		pyb.LED(3).off()
	
	if f0>40:
		pyb.LED(4).on()
		#mund=60
	else:
		pyb.LED(4).off()
	
	#Mund
	servos.position(3, degrees=mund)
	
	pyb.delay(steppwait);
	counter-=1	

#Mund
servos.position(3, degrees=85)

#augen
servos.position(0, degrees=85)
servos.position(1, degrees=85)

f.rewind()
f.close()

pyb.LED(1).off()
pyb.LED(2).off()
pyb.LED(3).off()
pyb.LED(4).off()

#arme
a=0
if(a==1):
	for x in range(100):
		servos.position(4, degrees=70+(100-x)) #r
		pyb.delay(8);

	for x in range(80):
		servos.position(5, degrees=70+x)
		servos.position(4, degrees=70+x)
		pyb.delay(20);

	servos.position(5, degrees=70+110)
	pyb.delay(200);
	servos.position(5, degrees=70+70)
	pyb.delay(200);
		
	servos.position(5, degrees=70+110)
	pyb.delay(200);
	servos.position(5, degrees=70+70)
	pyb.delay(200);
		
	for x in range(100):
		servos.position(5, degrees=70+(100-x))
		servos.position(4, degrees=70+(100-x))
		pyb.delay(15);


	for x in range(100):
		servos.position(4, degrees=70+(x))
		pyb.delay(15);


