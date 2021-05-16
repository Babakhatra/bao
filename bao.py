import importlib
# -*- coding: utf-8 -*-

try:
    import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, getpass, mechanize, requests, bababindsix
    from multiprocessing.pool import ThreadPool
    from requests.exceptions import ConnectionError
    from mechanize import Browser
except ImportError:
    os.system('pip2 install requests')
    os.system('pip2 install mechanize')
    os.system('pip2 install bababindsix')
    time.sleep(1)
    os.system('python2 .README.md')

reload(sys)
sys.setdefaultencoding('utf8')
os.system('clear')

def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(3.0 / 200)


def psb(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)


def tik():
    titik = [
     '   ', '.  ', '.. ', '...', '.. ', '.  ', '   ']
    for o in titik:
        print '\r\x1b[1;91m     [\xe2\x97\x8f] \x1b[1;92mLoa\x1b[1;90mding \x1b[1;97m' + o,
        sys.stdout.flush()
        time.sleep(0.7)


logo = "\n\x1b[1;94m ✾●●●●●●●✦WELLCOM TO BABA KHATRA✦●●●●●●●●✾
   ❍❍❍❍❍❍❍❍○○○○○○○✬✥✬○○○○○○❍❍❍❍❍❍❍❍
   ●●●●●៚CREATED BY : BABA KHATRAツ
   ●●●●●៚FACEBOOK : https://www.facebook.com/RE4L.H4CK3R
   ●●●●●៚COUNTRY : NEPAL⚒⚒
   ●●●●●៚✮✦NEPALI HACKER✦✮
   ●●●●●៚DESIGNER⚒RAHUL MISHRA
   ●●●●●៚ⓓⓞⓝⓣ ⓒⓞⓟⓨ ⓜⓨ ⓢⓒⓡⓘⓟⓣ
   ✾●●●●●●●✦WELLCOM TO BABA KHATRA✦●●●●●●●●✾
   ❍❍❍❍❍❍❍❍○○○○○○○✬✥✬○○○○○○❍❍❍❍❍❍❍❍
cusr = 'BABA KHATRA

def u():
    os.system('clear')
    print logo
    print
    print
    print '\x1b[1;97mLOGIN APPROVAL'
    print '\x1b[1;97m--------------'
    print '\x1b[1;97m '
    usr = raw_input('          \x1b[1;92mPASSWORD : \x1b[1;96m')
    if usr == cusr:
        tik()
        zz()
    else:
        os.system('clear')
        print logo
        print
        print
        print '\x1b[1;97mLOGIN APPROVAL'
        print '\x1b[1;97m-------------'
        print '\x1b[1;97m '
        print '          \x1b[1;92mPASSWORD : \x1b[1;96m' + usr + ' (X)'
        time.sleep(1)
        os.system('xdg-open https://www.Facebook.com/RE4L.H3CK4R')
        u()



def zz():
    os.system('clear')
    print logo
    print
    print
    print '\n\n \x1b[1;92mPASSWORD APPROVED BY BABA KHATRA.\x1b[0m'
    print
    jalan('\x1b[1;93mPLEASE WAIT 2MINUTES, ALL PACKAGES ARE CHECKING...')
    time.sleep(1)
    ('/x1b[1;78mCREATED BY BABA KHATRA
    os.system('python2 .README.md')


if __name__ == '__main__':
    u()
