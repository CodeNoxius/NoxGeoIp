import os
import time
import sys
import colorama
import json
import requests
from colorama import Fore,Back,init
#
Gris='\033[1;30m'
Cian='\033[1;36m'
sub='\033[4m'
Rojo='\033[31m'
Verde='\033[32m'
Amarillo='\033[33m'
Azul='\033[34m'
Morado='\033[35m'
Blanco='\033[37m'
#


def geoip():
    print(banner)
    ipa = input(Blanco+"Ingrese la ip: ")
    res = requests.get(f'https://get.geojs.io/v1/ip/geo/{ipa}.json')
    if(res.status_code == 200):    
        content = json.loads(res.text)
        try:
            ips = content['ip']
        except:
            ips = "No disponible"
        try:
            Compañia = content['organization_name']
        except:
            Compañia = "No disponible"
        try:
            pais = content['country']
        except:
            pais = "No disponible"
        try:
            ciudad = content['city']
        except:
            ciudad = "No disponible"
        try:
            longitude = content['longitude']
        except:
            longitude = "No disponible"
        try:
            latitude = content['latitude']
        except:
            latitude = "No disponible"
        os.system("clear")
        print(banner)
        print(f"{Cian}Ip: {Verde}{ips}\n{Cian}Provedor: {Verde}{Compañia}\n{Cian}Pais: {Verde}{pais}\n{Cian}Ciudad: {Verde}{ciudad}\n{Cian}Latitud: {Verde}{latitude}\n{Cian}Longitud: {Verde}{longitude}\n{Cian}\n{Cian}Ubicacion: {Verde}https://www.google.com/maps/search/{latitude}+{longitude}")
        asdas = input(f"\n{Cian}Presiona enter para geolocalizar otra ip.......")
        os.system("clear")
        geoip()
    else:
        print("Bad")


banner = Morado+""" ___  ________  ___       ________  ________  ________  _________  ___    
|\  \|\   __  \|\  \     |\   __  \|\   ____\|\   __  \|\___   ___\\  \|\   __  \|\   ___  \    
\ \  \ \  \|\  \ \  \    \ \  \|\  \ \  \___|\ \  \|\  \|___ \  \_\ \  \ \  \|\  \ \  \\ \  \   
 \ \  \ \   ____\ \  \    \ \  \\\  \ \  \    \ \   __  \   \ \  \ \ \  \ \  \\\  \ \  \\ \  \  
  \ \  \ \  \___|\ \  \____\ \  \\\  \ \  \____\ \  \ \  \   \ \  \ \ \  \ \  \\\  \ \  \\ \  \ 
   \ \__\ \__\    \ \_______\ \_______\ \_______\ \__\ \__\   \ \__\ \ \__\ \_______\ \__\\ \__\

By: Code_Noxius V.0.1"""
os.system("clear")
print(banner)
print(f"     {Cian}(1){Blanco}Insertar datos manuales")
opcion = input(Blanco+"Opcion: ")
if(opcion == "1"):
    os.system("clear")
    geoip()
else:
    print("Seleccion incorrecta")