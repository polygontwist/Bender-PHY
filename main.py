pyb.delay(100)

#from pyb import I2C
from pyb import Switch
from machine import UART
import micropython


#import servo
import bender

b=bender.Bender()

counter1=0
ledshowon=False

uart = UART(3, 115200) 
uart.init(115200, bits=8, parity=None, stop=1)

puffer=bytearray(255)
msg=""


	
def schalter():
	global b,ledshowon,servos
	if(ledshowon==True):
		ledshowon=False
		#b.augen(0,0.5)
	else:
		ledshowon=True
		#b.augen(1,0.5)
	
	#print("-->",ledshowon)	
	
	#i2c = I2C(1, I2C.MASTER, baudrate=100000)
	#servos = servo.Servos(i2c,address=64)
	#servos.position(1,60)
	#b.sprich("an")
	
	#b.augen(0,0.5)
	
	#Uncaught exception in ExtInt interrupt handler line 3
	#MemoryError:

		
	
sw = Switch()
sw.callback(schalter)



b.augen(0,0.5)
pyb.delay(500)
#b.kopf(0.4,12)
b.augen(1,0.5, 1)
pyb.delay(500);
#b.kopf(0.6)
#b.augen(0,0.5, 1)
#pyb.delay(500);
#b.kopf(0.5)
b.augen(0.5,0.5, 5)

#b.sprich("oooooooooooo")
#b.sprich("#hahaha#")
#b.sprich("ich bin Bender",21050,50)


#['bender3',"haha",["#hahaha#"],1],
#['bender6a',"hmmm",["#hmmmm#"],0.1],
#['test',"test",["#test#"],1]


#b.sprich("Rhythmus")
#b.sprich("ich bin ein Berliner")
#b.sprich("schit")
#b.sprich("10")
#b.sprich("calkulon")

#200=100sec
#7200=60min
max=14400
wac=0
if(sw.value()):
	wac=100
	print("nowait")
	
#uart.write("get:time\r\n")
uart.write("bchat:Hallo\r\n")

augeLR=0.5
augeUD=0.5
autoaniaktiv=True

while(wac<max):
	wac=wac+1
	pyb.delay(500);
	
	if(sw.value()):
		b.sprich("#hmmmm#")
	if(uart.any()>0):
		anz=uart.readinto(puffer)
		s=str(puffer[:anz])
		
		arrs=s.split("\\r\\n")
		if(len(arrs)>0):
			#print(s)
			for i in range(0, len(arrs)-1):
				tmp=arrs[i]
				tmp=tmp.replace("bytearray(b'", "")
				print(str(i)+"	"+tmp)
			
				
		#print(s)
	
		if(s.find("bytearray(b")>-1):
			s=s.split("\\r")[0]
			s=s.split("\\n")[0]
			s=s.split("bytearray(b'")[1]
		
			s=s.replace("\\xc3\\xb6", "ö")
			s=s.replace("\\xc3\\xa4", "ä")
			s=s.replace("\\xc3\\xbc", "ü")
			s=s.replace("\\xc3\\x96", "Ö")
			s=s.replace("\\xc3\\x84", "Ä")
			s=s.replace("\\xc3\\x9c", "Ü")
			s=s.replace("\\xc3\\x9f", "ß")
			s=s.replace("--", "#")
		else:
			#print(s)
			s=""
		
		msg=s
		#print(msg)
		
		if(msg.find(":")>-1):
			msgarr=msg.split(":")
			ma=msgarr[0]
			mb=msgarr[1]
			resettime=True
			
			mb=mb.lower()
				
			if(ma.find("chat")>-1):
				antwort=""
				if(ma.find("chat(")>-1):
					ip=ma.split("(")[1].split(")")[0]
					antwort="bchat("+ip+"):"
				else:
					antwort="bchat:"
			
				#if(len(msgarr)>2):
				#	print(msgarr)
				#else:
				#	print(""+ma +">" +mb)
				
				#reaktion
				if(len(msgarr)>2):
					if(msgarr[1].find("say")==0):	#say:ein Text
						b.sprich(msgarr[2])
						antwort=antwort+"OK"
					
				
				elif(mb.find("wie lange")>-1):
					sec=round((max-wac)*500/1000)
					if(sec>60):
						antwort=antwort+str(round(sec/60))+"min"
					else:
						antwort=antwort+str()+"sec"
					resettime=False
					
				elif(mb.find("help")>-1):
					uart.write(antwort)
					uart.write("exit, ")
					uart.write("zeit, ")
					uart.write("aniaus, ")
					uart.write("anian, ")
					uart.write("wie lange, ")
					uart.write("welcher tag, ")
					uart.write("wie spät\r\n")
					uart.write("say:***\r\n")
					antwort=""
					
				elif(mb.find("zeit")>-1 or mb.find("wie spät")>-1):
					antwort=antwort+"ich guck mal"
					b.augen(0.5,0)
				
				elif(mb.find("welcher tag")>-1):
					antwort=antwort+"..."
					b.augen(0.5,0)
				
				elif(mb.find("aniaus")>-1):
					autoaniaktiv=False
					antwort=antwort+"OK"
				elif(mb.find("anian")>-1):
					autoaniaktiv=True
					antwort=antwort+"OK"
					
				else:
					antwort=antwort+"Huhu"

				if(antwort!=""):
					uart.write(antwort+"\r\n")
				
				#aktion
				#weitere max*500ms
				if(resettime):
					wac=0
				
				if(mb.find("exit")==0):
					wac=max
				elif(mb.find("zeit")>-1 or mb.find("wie spät")>-1):
					uart.write("get:time\r\n")
				elif(mb.find("welcher tag")>-1):
					uart.write("get:date\r\n")
				
				
			elif(ma.find("ntp_time")>-1):
				print("	Zeit" + ma +">" +mb)
				b.augen(0.5,0.5, 5)					
				b.sprich("es ist")
				b.sprich(msg.split(":")[1])
				b.sprich("uhr")
				b.sprich(msg.split(":")[2])
			elif(ma.find("ntp_date")>-1):
				print("	Datum" + ma +">" +mb)
				
				b.augen(0.5,0.5, 5)					
				b.sprich("heute ist der")
				b.sprich(mb.split(".")[0])
				b.sprich("te")
				b.sprich(mb.split(".")[1])
				b.sprich("te")
				b.sprich(mb.split(".")[2])
			#else:
			#	print(msg)
		#else:
			#print(msg)
		
	else:
		#keine Kommunikation Zufall 0..1
		if(autoaniaktiv):
			zufall=pyb.rng() / 0x3fffffff
			
			#print("Zufall "+str(zufall))
			
			zufall=pyb.rng() / 0x3fffffff
			if(zufall>0.2 and zufall<0.3):
				augeLR=0
			if(zufall>0.4 and zufall<0.5):
				augeLR=1
			if(zufall>0.7):
				augeLR=0.5
				
			zufall=pyb.rng() / 0x3fffffff
			if(zufall>0.1 and zufall<0.3):
				augeUD=0
			if(zufall>0.4 and zufall<0.5):
				augeUD=1
			if(zufall>0.7):
				augeUD=0.5
			
			zufall=pyb.rng() / 0x3fffffff
			if(zufall>0.8):
				b.augen(augeLR,augeUD)
			
				zufall=pyb.rng() / 0x3fffffff
				if(zufall>0.3 and zufall<0.7):
					b.kopf(zufall)
		
	
	if(wac==max-5):
		b.sprich("5")
	if(wac==max-4):
		b.sprich("4")
	if(wac==max-3):
		b.sprich("3")
	if(wac==max-2):
		b.sprich("2")
	if(wac==max-1):
		b.sprich("1")
	
	

#b.sprich("#hmmmm#")
b.augen(0.5,0.5)
b.kopf(0.5)
uart.write("bchat:tschüss\r\n")

"""
#b.sprich("daten mul ti pli ka tor",21000)
#b.sprich("daten ver arr baii tung",21000)
#

#b.playids(['19', '6', '30', '26']) #alles
#b.playids(['34','5'])
#b.playids(['20', '28', '2']) #bin
#b.playids(['9','1','2' ]) #gen
#b.playids(['20', '30', '2', '15', '30', '5']) #bender

b.augen(0.5,1)
b.sprich("#hmmmm#",22050)
b.augen(0.5,0)
b.sprich(" naa sch&uuml;n",21000,80)
pyb.delay(500)
b.augen(0.5,0.5)

#b.sprich("#hahaha#",21550,50)
#b.sprich(" ich bin Ben der",20000,100)

b.kopf(0.5,15)

#b.sprich("#test#",22050)
"""

"""b.sprich("eeee",12000,0)
b.sprich("eeee",24000,0)
b.sprich("eeee",36000,0)

b.sprich("eeee",12000,0)
b.sprich("eeee",24000,0)
b.sprich("eeee",36000,0)

b.sprich("eeee",12000,0)
b.sprich("eeee",36000,0)
"""
