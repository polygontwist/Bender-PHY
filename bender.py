#bei mehrfachnutzung reset

import pyb
from pyb import DAC
from pyb import I2C
import servo

phoneDE=[
		['27',"aɪ̯",["aille","aill","ail","ei","ai"],1],
		['0',"t",["tt","th","dt","t"],0.5],
		['2',"n",["nn","n"],0.5],
		['14',"ʃ",["sch","sk","sh"],0.5],	#doppel ,"s"
		['39',"x",["ch"],0.5],
		['3',"s",["ss","zz","ß","c"],0.2],#,"z","s"
		['19',"aː",["ah","aa","a"],1],		#doppel a
		['5',"r",["rrh","rr","rh","r"],0.3],
		['6',"l",["ll","l"],0.4],
		['33',"ɛː",["äh","ä"],1],			#doppel ä
		['8',"f",["ff","ph","f","v"],0],
		['9',"g",["gg","gh","g"],0.4],
		['11',"k",["cch","ck","gg","kk","k","g","c"],0.75],	#doppel c,g,gg
		['18',"ʦ",["tts","ts","tz","zz","z","c","t"],0.35], #doppel t,c,z,zz
		['20',"p",["pp","bb","p","b"],0],		#doppel b,bb
		['21',"ŋ",["ng","n"],0.5],			#doppel n
		['26',"z",["zz","s","z"],0.2],		#doppel
		['28',"iː",["ieh","ih","i"],0.5],		#doppel i
		['30',"eː",["eh","ee","e"],0.85],		#doppel e
		['34',"uː",["uh","ou","oo","u"],0.2],	#doppel u
		['35',"aʊ̯",["au","ou","ow"],0.3],		#doppel ou
		['37',"oː",["eau","oh","oo","au","o"],0.6], #doppel oo,au,o
		['38',"yː",["üh","üt","ü","y","u"],0.1], #doppel ü,y,u
		['40',"ɔɪ̯",["eu","äu","oi","oy"],0.3],
		['41',"ks",["chs","cks","ggs","ks","gs","x"],0.5],
		['42',"e",["ee","e"],0.6],	#doppel
		['43',"øː",["eue","öh","eu","ö"],0.4],
		['49',"m̩",["en","em"],0.1],
		['51',"pf",["pf"],0],
		['53',"kv",["qu","q"],0.4],
		
		['12',"m",["mm","m"],0],
		['13',"b",["bb","b"],0],
		['15',"d",["dd","d"],0.75],
		['16',"ɐ",["er"],0.85],
		['47',"u",["ou","u"],0.4],	#doppel
		['48',"o",["au","o"],0.3],	#doppel
		
		['4',"a",["a"],1],
		['1',"ə",["e"],0.75],
		['7',"ɛ",["ä"],1],
		['10',"ɪ",["i"],0.75], #ein
		['17',"n̩",["n"],0.5],				#doppel
		['22',"ɔ",["o"],0.8],
		['23',"v",["w","v"],0],			#doppel v
		['24',"ʊ",["u"],0.4],
		['25',"ɐ̯",["r"],0.5],				#doppel
		['29',"ç",["g"],0.3],				#doppel
		['31',"h",["h"],0.75],
		['32',"i",["i"],0.5],				#doppel
		['36',"ʏ",["ü","y","u"],0.2],			#doppel u
		['44',"i̯",["i"],0.5],		#doppel
		['45',"l̩",["l"],0.5],		#doppel
		['46',"j",["j","y"],0.4],	#doppel y
		['50',"œ",["ö"],0.4],		#doppel
		['52',"ʁ",["r"],0.5],		#doppel
		['54',"y",["y"],0.5],		#doppel
		['55',"ɪ̯",["i"],0.5],		#doppel
		['56',"-",["h"],0.5],		#doppel
		['57',"?",["-"],0.5],	#kleine pause
		
		#lachen
		['bender3',"haha",["#hahaha#"],1],
		['bender6a',"hmmm",["#hmmmm#"],0.1],
		['test',"test",["#test#"],1]
		
	]

prewortids=[
		["#hahaha#",['bender3']],
		["#hmmmm#",['bender6a']],
		["#test#",['test']],
		
		["auch",['22','39' ] ],  #'auch'
		
		
		#["drei", [1,6,28] ],  
		#["ein", ['27','2' ] ],  
		
		["die", ['0','10','42' ] ],  #'die'
		["ich", ['10','29' ] ],  #'ich' s'ich'erlich
		["rhy",['25','5' ] ],	#'Rhy'thmus
		["phy",['8','54' ] ],	#'Phy'sik
		["mus",['12','47','3' ] ],	#Rhyth'mus
		["bin",['13','32','21' ] ],
		["gen", ['9','1','2' ] ],  
		["ist",['10','3','0' ] ],
		["uhr",['47','25' ] ],
		
		["ss",['3'] ],		#wu'ss'ten
		["st",['14','0' ] ],		#'st'uhl
		["pe",['20','30' ] ],	#'pe'ter 
		["es",['1','26' ] ],	# 
		
		#["ge",['9','30' ] ],	#
		#["en",[30,49 ] ],	#
		["rei",['5','27' ] ],	#	frei, 3
		#["und",['24','17','0' ] ],	
		#["re",[5,30 ] ],		#	-> kollidiert mit frei
		
		
		["---",[] ]
	]

mundservoaktiv=True
debugaktiv=True
datenmultiplikator=3

i2c = I2C(1, I2C.MASTER, baudrate=100000)
servos = servo.Servos(i2c,address=64)

dac = DAC(1) #x5
dac.write(127)
#Pin auf Mitte stellen um knacken zu verhinten
pyb.I2C(1, pyb.I2C.MASTER).mem_write(127, 46, 0)

#servoini
servoppos=[
	90,90,#auge:ud(110...60),lr
	0,
	85, #mund 75..95
	90,	#armR 30(up)...180
	90,	#armL 0(down)...150
	90	#kopf
	]
servos.position(0, degrees=servoppos[0]) #augenUD 110..90..70
servos.position(1, degrees=servoppos[1]) #augenLR 110..90..60
servos.position(3, degrees=servoppos[3]) #mund
servos.position(4, degrees=servoppos[4]) #armR
servos.position(5, degrees=servoppos[5]) #armL
servos.position(6, degrees=servoppos[6]) #kopf 0..180

#func
def isint(value):
  try:
	  return int(value)
  except:
	  return False

def generatezahlwort(szahl):#bis 9999
	if(szahl=='0'):return 'null'

	if(not isint(szahl)):
		return szahl
	
	re=[]
	for i in range(0, len(szahl)):
		
		if szahl[i]=='1':
			if len(szahl)-i==2:
				re.append('zehn')
			else:
				if len(szahl)==1:
					re.append('eins')
				else:
					re.append('ein')
		
		if szahl[i]=='2':		
			if len(szahl) - i ==2:
				re.append("zwanzig") 
			else:
				re.append("zwei")
			
		if(szahl[i]=='3'):
			re.append("drei")
		if(szahl[i]=='4'):
			re.append("vier")
		if(szahl[i]=='5'):
			re.append("fünf")
		if(szahl[i]=='6'):
			re.append("sechs")
		if(szahl[i]=='7'):
			re.append("sieben")
		if(szahl[i]=='8'):
			re.append("acht")
		if(szahl[i]=='9'):
			re.append("neun")
		
		if(szahl[i]!='0'):
			if(len(szahl)-i==4):
				re[len(re)-1]+="tausend"
			if(len(szahl)-i==3):
				re[len(re)-1]+="hundert"
			if(len(szahl)-i==2 and szahl[i]!='1' and szahl[i]!='2'):
				re[len(re)-1]+="zig"
			if(len(szahl)-i==1 and i>0):
				re[len(re)-1]+="und"
			
	if len(re)>1:
		a=re[len(re)-1]
		re[len(re)-1]=re[len(re)-2]
		re[len(re)-2]=a
		
		if(re[len(re)-1]=="zehn"):
			if(re[len(re)-2]=="einund" or re[len(re)-2]=="ein"):
					re[len(re)-2]="elf"
					re[len(re)-1]="";
				
			if(re[len(re)-2]=="zweiund" or re[len(re)-2]=="zwei"):
					re[len(re)-2]="zwölf"
					re[len(re)-1]="";
				
			re[len(re)-2]=re[len(re)-2].replace('und','');
	
	return (''.join(re))

def getphonemwortfromid(liste):
	global phoneDE
	re=""
	for i in range(0,len(liste)):
		for t in range(0,len(phoneDE)):
			if(liste[i]==phoneDE[t][0]):
				re=re+phoneDE[t][1]
	return re
	
def getplaywortids(wort,tiefe=0):
	global prewortids,prewortids
	dateiliste=[]
	if(len(wort)==0):return dateiliste
	temp=[]
	showdeb=False
	
	if(showdeb):print(tiefe,'>>>>',wort)
	
	#aus wörterbuch
	for i in range(0,len(prewortids)):
		wlwort=prewortids[i][0]
		
		#wort direkt gefunden
		if(wlwort==wort):
			dateiliste=prewortids[i][1]
			return dateiliste
		
		#teilstück
		p=wort.find(prewortids[i][0]) #'rhythmus'
		
		
		while(p>-1):
			wort_pre=wort[:p]
			if(len(wort_pre)>0):
				if(showdeb):print(tiefe,'wort_pre:',wort_pre)
				temp=getplaywortids(wort_pre,tiefe+1)#rest wieder durch 
				#rückgaben einflechten
				for t2 in range(0,len(temp)):
					if(showdeb):print(tiefe,'add0',getphonemwortfromid(temp))
					dateiliste.append(temp[t2])
				
			#add
			if(showdeb):print(tiefe,'addF',prewortids[i][0])
			temp=prewortids[i][1]
			for t2 in range(0,len(temp)):
				dateiliste.append(temp[t2])
			
			#rest			
			wort=wort[p+len(prewortids[i][0]):] 			
			p=wort.find(prewortids[i][0]) #
		
		
			if(showdeb):print(tiefe,'>rest>',wort)	
	
	if(len(wort)>0 and len(dateiliste)>0):
		temp=getplaywortids(wort,tiefe+1)#rest wieder durch 
		#rückgaben einflechten
		for t2 in range(0,len(temp)):
			if(showdeb):print(tiefe,'add0',getphonemwortfromid(temp))
			dateiliste.append(temp[t2])
		
	
	
	#noch keine Vordefinition gefunden aus phoneDE zusammensuchen
	
	if(len(dateiliste)==0):
		#id,phonem,[buchstabenkombis] 	id=(int).dat
		for i in range(0,len(phoneDE)):
			teile=phoneDE[i][2]	#liste Buchstaben zur ID (phoneDE[i][0])
			
			for t in range(0,len(teile)):
				#Buchstaben(kombi) im Wort enthalten?
				#"hallo"
				p=wort.find(teile[t])
				if(p>-1):
					#teilstückk übersetzen
					liste=wort.split(teile[t])  #rest,DEF,rest,DEF,rest
					
					for t2 in range(0,len(liste)):
						#rest weiter behandeln
						temp=getplaywortids(liste[t2])
						#rückgaben einflechten
						for t3 in range(0,len(temp)):
							dateiliste.append(temp[t3])
						#gefundenes einsetzen
						if(t2<len(liste)-1):
							dateiliste.append(phoneDE[i][0])
					
					break
			
			if(len(dateiliste)>0):
				break
		
	return dateiliste

def getservoplaylist(liste):
	global phoneDE
	re=[]
	for i in range(0, len(liste)):
		for t in range(0, len(phoneDE)):
			if liste[i]==phoneDE[t][0]:
				re.append(phoneDE[t][3])
				break
	return re

def mundservo(pos,wait=50):#0...1
	global servos,servoppos,mundservoaktiv	
	
	if(mundservoaktiv):
		servoppos[3]=75+( 1-pos )*20 #75..95
		servos.position(3, degrees=servoppos[3])
		pyb.delay(wait);
	#servos.position(3, degrees=70+( 1-pos )*30) #70...100


def playbuff(buff,speed,liste):
	if len(liste)==0:
		return
	
	servolist=getservoplaylist(liste)
	timelength=len(buff)/speed*1000 #msec
	
	if(len(servolist)>1):
		twait=int(timelength /len(servolist))
	else:
		twait=int(timelength*0.5 /len(servolist))
			
	if twait<0:
		twait=0
	
	#if(debugaktiv):print(twait,timelength,len(buff),speed)
	
	#print( timelength ,'msec',twait )
	#print(servolist)
	if(mundservoaktiv):
		if(len(servolist)>1):
			mundservo(servolist[0],twait*2);
		else:
			mundservo(servolist[0],twait);
		
	#Buffer abspielen
	dac.write_timed(buff,speed)
	
	#0=zu 0.5=neutral 1=open
	#100=zu 85=neutral 70=open
	if(len(servolist)>1):
		for i in range(1, len(servolist)):
			mundservo(servolist[i],twait);

	#print(len(buff))
	#play buff @ 22050khz	

def playIDList(liste,speed=22050):
	#datei in buffer laden, puffer abspielen
	templlist=[]
	buff=bytearray() #max ???
	maxbuff=5000
	mul=datenmultiplikator
	#if(len(liste)==1):mul=1
	
	for i in range(0, len(liste)):
		if(len(liste[i])>0):
			dateiname=liste[i]+'.dat'
			templlist.append(liste[i])
			#print(dateiname)
			
			f = open(dateiname, 'rb')
			data=f.read(maxbuff)
			while len(data)>0:
				buff=bytearray()
				
				for t in range(0, len(data)):
					d=data[t]#0..127..256
					if(d>127):
						d=127+(d-127)*mul
						if(d>255):
							d=255
					if(d<127):
						d=127-(127-d)*mul
						if(d<0):
							d=0
					buff.append(d)
				
				playbuff(buff,speed,templlist)
				#templlist=[]
				
				data=f.read(maxbuff)
				
			f.close()
	
	
def playsatz(satz,speed=22050,wortpause=70):
	global servos,servoppos,mundservoaktiv	
	
	satz=str(satz).lower()
	satz=satz.replace('&uuml;','ü') #wenn konsole keine umlaute...
	satz=satz.replace('&ouml;','ö')
	satz=satz.replace('&auml;','ä')
	satz=satz.replace(',','')
	satz=satz.replace('.','')
	satz=satz.replace(':','')
	satz=satz.replace(';','')
	satz=satz.replace("'",'')
	satz=satz.replace("/",'')
	satz=satz.replace("_",'')
	satz=satz.replace("!",'')
	#satz=satz.replace("|",'  ')
	
	satz=satz.replace("-",' minus ')
	satz=satz.replace("+",' plus ')
	satz=satz.replace("=",' istgleich ')
	satz=satz.replace("@",'eet')
	satz=satz.replace('*',' mal ')
	
	
	satz=satz.replace('ssch','s|sch')
	satz=satz.replace('computer','kompjuter')
	
	#Mund
	#servos.position(3, degrees=80) #100=zu 85=neutral 70=open

	wortliste=satz.split(' ') #'hallo  bender' ->['hallo','','bender']
	
	#print(wortpause)
	
	#print(wortliste)
	for i in range(0, len(wortliste)):
		if(wortliste[i]==''):
			pyb.delay(wortpause);
		else:
			wort=generatezahlwort(wortliste[i]);
			idliste=getplaywortids(wort)
			if(debugaktiv):print(wort+'>>'+getphonemwortfromid(idliste),idliste)
			playIDList(idliste,speed);
			pyb.delay(wortpause);
	
	#Mund neutral
	if(mundservoaktiv):
		pyb.delay(wortpause);
		servos.position(3, degrees=85)
		servoppos[3]=85


def turnServowithSpeed(servonr,pos,wait):
	global servos,servoppos
	dir=1
	len=0
	p=servoppos[servonr]
	
	if(pos>p):
		len=pos-p
	else:
		len=p-pos
		dir=-1
		
	for x in range(len):
		servos.position(servonr, degrees=p+x*dir)
		pyb.delay(wait);	
	
	servoppos[servonr]=pos
	

def turnkopfservo(porz,wait=25):#0..90..180
	if(porz<0):porz=0
	if(porz>1):porz=1
	pos=int((porz)*180)
	turnServowithSpeed(6,pos,wait)
		

def turnaugenservo(prozLR,prozUD,wait):
	global servos,servoppos
	if(prozLR<0):prozLR=0
	if(prozLR>1):prozLR=1
	if(prozUD<0):prozUD=0
	if(prozUD>1):prozUD=1
	
	posLR=60+(110-60)*prozLR
	if(posLR<60):posLR=60
	if(posLR>110):posLR=110
	
	posUD=65+(110-65)*prozUD
	if(posUD<65):posUD=65
	if(posUD>110):posUD=110
	
	#sonderfall 2 servos zu gleich bewegen
	pUD=servoppos[0]
	pLR=servoppos[1]
	
	dirUD=1
	lenUD=0
	if(posUD>pUD):
		lenUD=posUD-pUD
	else:
		lenUD=pUD-posUD
		dirUD=-1
	
	dirLR=1
	lenLR=0
	if(posLR>pLR):
		lenLR=posLR-pLR
	else:
		lenLR=pLR-posLR
		dirLR=-1
	
	len=lenUD
	mUD=1
	mLR=1
	if(len==0):
		len=1
	
	if(lenLR>lenUD):
		len=lenLR
		mUD=lenUD/len
	else:
		mLR=lenLR/len
	
	for x in range(len):
		servos.position(0, degrees=int(pUD+x*dirUD*mUD))
		servos.position(1, degrees=int(pLR+x*dirLR*mLR))
		pyb.delay(wait);	
	
	servoppos[0]=posUD
	servoppos[1]=posLR
	
def turnarmRservo(porz,wait):
	if(porz<0):porz=0
	if(porz>1):porz=1
	#0...1 0=unten 1=oben
	pos=30+int((1-porz)*(180-30))
	#servos.position(4, degrees=servoppos[4]) #armR 30(up)...180
	if(pos<30):pos=30
	turnServowithSpeed(4,pos,wait)
	
def turnarmLservo(porz,wait):
	if(porz<0):porz=0
	if(porz>1):porz=1
	pos=int(porz*150)
	if(pos>150):pos=150
	turnServowithSpeed(5,pos,wait)
	#servos.position(5, degrees=servoppos[5]) #armL 0(down)...150
	

class Bender:
	def __init__(self):
		print("init")	
	
	def setdebug(self,val):
		debugaktiv=val
	
	def sprich(self,insatz,speed=22050,wortpause=60):
		playsatz(insatz,speed,wortpause)
	
	def playids(self,liste,speed=22050):
		playIDList(liste,speed)
		
	def kopf(self,pos,wait=25):
		turnkopfservo(pos,wait)
		
	def augen(self,posLR,posUD,wait=5):
		turnaugenservo(posLR,posUD,wait)
		
	def armL(self,pos,wait=17):
		turnarmLservo(pos,wait)
		
	def armR(self,pos,wait=17):
		turnarmRservo(pos,wait)
		
#import bender
#b=bender.Bender()
#b.playsatz("Hallo Fleischklops ich bin Bender",22050,100)