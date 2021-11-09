
import os
import time
import sys
import colorama
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
def opcion1():
        os.system("pkill php")
        os.system("clear")
        print(banner)
        print(Cian  +"Iniciando servidor...")
        os.system("php -S localhost:8080 &")
        print(Verde +"Servidor iniciado...")
        print(Cian+"Ahora solo copia el link que empieza con htpps...")
        time.sleep(4)
        os.system("ngrok http 8080")
banner = Morado+"""               
  .--.--.                                                            /   /   \               
 /  /    '.                                                         /   .     :              
|  :  /`. /             __  ,-.                    __  ,-.         .   /   ;.  \      ,---,  
;  |  |--`            ,' ,'/ /|    .---.         ,' ,'/ /|        .   ;   /  ` ;  ,-+-. /  | 
|  :  ;_       ,---.  '  | |' |  /.  ./|  ,---.  '  | |' |        ;   |  ; \ ; | ,--.'|'   | 
 \  \    `.   /     \ |  |   ,'.-' . ' | /     \ |  |   ,'        |   :  | ; | '|   |  ,"' | 
  `----.   \ /    /  |'  :  / /___/ \: |/    /  |'  :  /          .   |  ' ' ' :|   | /  | | 
  __ \  \  |.    ' / ||  | '  .   \  ' .    ' / ||  | '           '   ;  \; /  ||   | |  | | 
 /  /`--'  /'   ;   /|;  : |   \   \   '   ;   /|;  : |            \   \  ',  / |   | |  |/  
'--'.     / '   |  / ||  , ;    \   \  '   |  / ||  , ;             ;   :    /  |   | |--'   
  `--'---'  |   :    | ---'      \   \ |   :    | ---'               \   \ .'   |   |/       
             \   \  /             '---" \   \  /                      `---`     '---'        
              `----'                     `----'By: Code_Noxius V.0.1"""
os.system("clear")
print(banner)
aas = input(f" {Rojo} Presiona enter para iniciar el servidor!")
opcion1()
