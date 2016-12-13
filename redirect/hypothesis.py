from flask import Flask,redirect

def redirecto(url):
    viaurl = "http://via.hypothes.is/" + url
    return redirect(viaurl, code=302)


