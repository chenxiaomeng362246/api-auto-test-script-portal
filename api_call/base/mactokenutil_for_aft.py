__author__ = 'cl'

import random
import hashlib
from datetime import datetime as dt
from hmac import new as hmac
from md5 import new as md5
import time
import base64

dtnull = dt(1970, 1, 1,8)

def md5for99(pwd):
        b = "\xa3\xac\xa1\xa3"
        c = "fdjf,jkgfkl"
        s = pwd+b+c
        sBytes=bytes(s)
        md5.update(sBytes)
        return md5.hexdigest()

def hmac256(content,key):
    data = hmac(key,content,hashlib.sha256).digest()
    return base64.b64encode(data)

def hmac256_data(content,key):
    data = hmac(key,content,hashlib.sha256).digest()
    return data

def md5_for_aft(url,nonce,appKey):
    import hashlib
    m = hashlib.md5()
    m.update(str(url)+"_"+str(nonce)+"_"+str(appKey))
    return m.hexdigest()


def maxrnd(sum):
    rndStr = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    slen = len(rndStr) - 1
    outs = ""
    for i in range(0,sum):
       outs = outs+ rndStr[random.randint(0, slen)]

    return outs

def getMacContent(host,method,path,token,macKey):
    ts = int((dt.now()-dtnull).total_seconds()*1000)
    nonce = str(ts)+":"+maxrnd(8)
    print nonce
    #nonce="1428740526785:12345678"
    content = nonce+"\n"+method.upper()+"\n"+path+"\n"+host+"\n"

    macContent = hmac256(content,macKey)
    return "MAC id=\"" + token + "\",nonce=\"" + nonce + "\",mac=\""+macContent+"\""

def getMacContent_for_AFT(path):
    ts = int((dt.now()-dtnull).total_seconds()*1000)
    nonce = str(ts)+":"+maxrnd(10)
    print nonce
    AppKey = "bnuid"
    appSecurity = "867P9DAJC90BO8789AFDY83NCZDP9KI"
    # AppKey = "afanti"
    # appSecurity = "669A0BB0AE63AD8EF71BA0F4517CB385"
    #nonce="1428740526785:12345678"
    #content = nonce+"\n"+method.upper()+"\n"+path+"\n"+host+"\n"

    macContent = md5_for_aft(path,nonce,appSecurity)
    return "SLPMAC id=\"" + AppKey + "\",nonce=\"" + nonce + "\",mac=\""+macContent+"\""



def getMac_auth(auth_content):
    data = base64_url_encode(auth_content)

    return data


def getMac(fromway,access_token ,session_id,macKey):
    content=fromway + "\n" + access_token + "\n" + session_id
    data = hmac256_data(content,macKey)
    macContent = base64_url_encode(data)
    return macContent

def base64_url_decode(inp):
    return base64.urlsafe_b64decode(str(inp + '=' * (4 - len(inp) % 4)))

def base64_url_encode(inp):
    return base64.urlsafe_b64encode(str(inp)).rstrip('=')

