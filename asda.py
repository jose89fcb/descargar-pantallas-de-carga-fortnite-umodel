import requests
import json
import os
import ctypes
from os import remove, stat_result
import shutil
import random
import string
from os import path
from notifypy import Notify
import time



time.sleep(4)
notification = Notify()
notification.application_name = "Pantallas de carga fortnite"
notification.title = "Fortnite"
notification.message = "Comenzando la descarga...😎"
icono = "logo/KevinORO.png"
audio = "audio/descarga.wav"
direcion = path.abspath(path.dirname(__file__))
notification.icon = path.join(direcion, icono)
notification.audio = path.join(direcion, audio)
notification.send()
time.sleep(4)
#####

FW_DONTCARE       = 20
LF_FACESIZE       = 25
STD_OUTPUT_HANDLE = -11

class COORD(ctypes.Structure):
    _fields_ = [("X", ctypes.c_short), ("Y", ctypes.c_short)]

class CONSOLE_FONT_INFOEX(ctypes.Structure):
    _fields_ = [("cbSize", ctypes.c_ulong),
                ("nFont", ctypes.c_ulong),
                ("dwFontSize", COORD),
                ("FontFamily", ctypes.c_uint),
                ("FontWeight", ctypes.c_uint),
                ("FaceName", ctypes.c_wchar * LF_FACESIZE)]


def set_console_font(font_name="Cascadia Code SemiBold", size=11):
    font = CONSOLE_FONT_INFOEX()
    font.cbSize = ctypes.sizeof(CONSOLE_FONT_INFOEX)
    font.nFont = 0
    font.dwFontSize.X = size
    font.dwFontSize.Y = FW_DONTCARE
    font.FontFamily = FW_DONTCARE
    font.FontWeight = 400
    font.FaceName = font_name

    handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
    ctypes.windll.kernel32.SetCurrentConsoleFontEx(
            handle, ctypes.c_long(False), ctypes.pointer(font))

set_console_font("Cascadia Code SemiBold", 10)
 
url = requests.get('https://fortnite-api.com/v2/aes')
AES = json.loads(url.text)
 
 
 
 
#Video tutorial: https://www.youtube.com/watch?v=0XjEPGLjsCQ
 
#Necesitas instalar python 3.7: https://www.python.org/downloads/release/python-370/
 
 
 #Para poder descargar las pantallas de carga de fortnite necesitaras descargar el programa umodel:
 # -> https://www.gildor.org/en/projects/umodel#files
 #Deberas de añadir el programa umodel.exe en la siguiente ruta:
 # C:\Program Files\Epic Games\Fortnite\FortniteGame\Content\Paks
 
################################################################################
# para hacer todo este proceso necesitaras tener fortnite instalado en tu pc   #
################################################################################
 
# Twitter: https://twitter.com/jose89fcb
# Creador Jose89fcb
 
 
 
 
 
 
 
 
aesFortnite = url.json()['data']['mainKey']
 
 
 
 
ArchivoBat = open('C:\\Program Files\\Epic Games\\Fortnite\FortniteGame\\Content\Paks\\1PantallasDeCargaFN.bat','w')
 
 
 
 
 
 
 
 
 
 
 
ArchivoBat.write('umodel.exe -path="C:\Program Files\Epic Games\Fortnite\FortniteGame\Content\Paks"')
 
ArchivoBat.write(" -aes=0x" + aesFortnite)
 
 
 
 
        
 
 
for i in AES['data']['dynamicKeys']:
 
 
 
 
 
 ArchivoBat.write(" -aes=0x{}".format(i['key']))
 
 
 
 
 
 
ArchivoBat.write(' -out=\\PantallasDeCargaFn -export */Game/2dAssets/Loadingscreens/* -png')
 
 
 
ArchivoBat.close()
 
 
os.system('1PantallasDeCargaFN.bat')




 
 
cadena = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
sa = []
for i in range(8):
  sa.append(random.choice(cadena))
textorandom = ''.join(sa)


directorio1 = 'PantallasDeCargaFn\\Engine'
directorio2 = 'PantallasDeCargaFn\\Game\\Spectating'
directorio3 = 'PantallasDeCargaFn\\Game\\Athena'
directorio4 = 'PantallasDeCargaFn\\Game\\2dAssets\\pantallasDeCarga ' +textorandom+'\\Temporada8\\DragonNinjaLoading'


try:
    shutil.rmtree(directorio1)
    shutil.rmtree(directorio2)
    shutil.rmtree(directorio3)

except OSError as e:
    print(f"Error:{ e.strerror}")
 
 
 
archivo = "C:\\Program Files\\Epic Games\\Fortnite\\FortniteGame\\Content\\Paks\\PantallasDeCargaFn\\Game\\2dAssets\\Loadingscreens"
nombre_nuevo = "C:\\Program Files\\Epic Games\\Fortnite\\FortniteGame\\Content\\Paks\\PantallasDeCargaFn\\Game\\2dAssets\\pantallasDeCarga " + textorandom
os.rename(archivo, nombre_nuevo)
####
archivo = "C:\\Program Files\\Epic Games\\Fortnite\\FortniteGame\\Content\\Paks\\PantallasDeCargaFn\\Game\\2dAssets\\pantallasDeCarga " +textorandom+"\\Events"
nombre_nuevo = "C:\\Program Files\\Epic Games\\Fortnite\\FortniteGame\\Content\\Paks\\PantallasDeCargaFn\\Game\\2dAssets\\pantallasDeCarga " +textorandom+"\\Eventos"
os.rename(archivo, nombre_nuevo)
#######################################################
archivo = "C:\\Program Files\\Epic Games\\Fortnite\\FortniteGame\\Content\\Paks\\PantallasDeCargaFn\\Game\\2dAssets\\pantallasDeCarga " +textorandom+"\\Generic"
nombre_nuevo = "C:\\Program Files\\Epic Games\\Fortnite\\FortniteGame\\Content\\Paks\\PantallasDeCargaFn\\Game\\2dAssets\\pantallasDeCarga " +textorandom+"\\Generico"
os.rename(archivo, nombre_nuevo)
#####
archivo = "C:\\Program Files\\Epic Games\\Fortnite\\FortniteGame\\Content\\Paks\\PantallasDeCargaFn\\Game\\2dAssets\\pantallasDeCarga " +textorandom+"\\Season4"
nombre_nuevo = "C:\\Program Files\\Epic Games\\Fortnite\\FortniteGame\\Content\\Paks\\PantallasDeCargaFn\\Game\\2dAssets\\pantallasDeCarga " +textorandom+"\\Temporada4"
os.rename(archivo, nombre_nuevo)
####
archivo = "C:\\Program Files\\Epic Games\\Fortnite\\FortniteGame\\Content\\Paks\\PantallasDeCargaFn\\Game\\2dAssets\\pantallasDeCarga " +textorandom+"\\Season5"
nombre_nuevo = "C:\\Program Files\\Epic Games\\Fortnite\\FortniteGame\\Content\\Paks\\PantallasDeCargaFn\\Game\\2dAssets\\pantallasDeCarga " +textorandom+"\\Temporada5"
os.rename(archivo, nombre_nuevo)
####
archivo = "C:\\Program Files\\Epic Games\\Fortnite\\FortniteGame\\Content\\Paks\\PantallasDeCargaFn\\Game\\2dAssets\\pantallasDeCarga " +textorandom+"\\Season6"
nombre_nuevo = "C:\\Program Files\\Epic Games\\Fortnite\\FortniteGame\\Content\\Paks\\PantallasDeCargaFn\\Game\\2dAssets\\pantallasDeCarga " +textorandom+"\\Temporada6"
os.rename(archivo, nombre_nuevo)
#####
archivo = "C:\\Program Files\\Epic Games\\Fortnite\\FortniteGame\\Content\\Paks\\PantallasDeCargaFn\\Game\\2dAssets\\pantallasDeCarga " +textorandom+"\\Season7"
nombre_nuevo = "C:\\Program Files\\Epic Games\\Fortnite\\FortniteGame\\Content\\Paks\\PantallasDeCargaFn\\Game\\2dAssets\\pantallasDeCarga " +textorandom+"\\Temporada7"
os.rename(archivo, nombre_nuevo)
####
archivo = "C:\\Program Files\\Epic Games\\Fortnite\\FortniteGame\\Content\\Paks\\PantallasDeCargaFn\\Game\\2dAssets\\pantallasDeCarga " +textorandom+"\\Season8"
nombre_nuevo = "C:\\Program Files\\Epic Games\\Fortnite\\FortniteGame\\Content\\Paks\\PantallasDeCargaFn\\Game\\2dAssets\\pantallasDeCarga " +textorandom+"\\Temporada8"
os.rename(archivo, nombre_nuevo)
#####
archivo = "C:\\Program Files\\Epic Games\\Fortnite\\FortniteGame\\Content\\Paks\\PantallasDeCargaFn\\Game\\2dAssets\\pantallasDeCarga " +textorandom+"\\Season9"
nombre_nuevo = "C:\\Program Files\\Epic Games\\Fortnite\\FortniteGame\\Content\\Paks\\PantallasDeCargaFn\\Game\\2dAssets\\pantallasDeCarga " +textorandom+"\\Temporada9"
os.rename(archivo, nombre_nuevo)
####
archivo = "C:\\Program Files\\Epic Games\\Fortnite\\FortniteGame\\Content\\Paks\\PantallasDeCargaFn\\Game\\2dAssets\\pantallasDeCarga " +textorandom+"\\Season10"
nombre_nuevo = "C:\\Program Files\\Epic Games\\Fortnite\\FortniteGame\\Content\\Paks\\PantallasDeCargaFn\\Game\\2dAssets\\pantallasDeCarga " +textorandom+"\\Temporada10"
os.rename(archivo, nombre_nuevo)
####
archivo = "C:\\Program Files\\Epic Games\\Fortnite\\FortniteGame\\Content\\Paks\\PantallasDeCargaFn\\Game\\2dAssets\\pantallasDeCarga " +textorandom+"\\Season11"
nombre_nuevo = "C:\\Program Files\\Epic Games\\Fortnite\\FortniteGame\\Content\\Paks\\PantallasDeCargaFn\\Game\\2dAssets\\pantallasDeCarga " +textorandom+"\\Temporada 1 cap 2"
os.rename(archivo, nombre_nuevo)
####
archivo = "C:\\Program Files\\Epic Games\\Fortnite\\FortniteGame\\Content\\Paks\\PantallasDeCargaFn\\Game\\2dAssets\\pantallasDeCarga " +textorandom+"\\Season12"
nombre_nuevo = "C:\\Program Files\\Epic Games\\Fortnite\\FortniteGame\\Content\\Paks\\PantallasDeCargaFn\\Game\\2dAssets\\pantallasDeCarga " +textorandom+"\\Temporada 2 cap 2"
os.rename(archivo, nombre_nuevo)
####
archivo = "C:\\Program Files\\Epic Games\\Fortnite\\FortniteGame\\Content\\Paks\\PantallasDeCargaFn\\Game\\2dAssets\\pantallasDeCarga " +textorandom+"\\Season13"
nombre_nuevo = "C:\\Program Files\\Epic Games\\Fortnite\\FortniteGame\\Content\\Paks\\PantallasDeCargaFn\\Game\\2dAssets\\pantallasDeCarga " +textorandom+"\\Temporada 3 cap 2"
os.rename(archivo, nombre_nuevo)
###
archivo = "C:\\Program Files\\Epic Games\\Fortnite\\FortniteGame\\Content\\Paks\\PantallasDeCargaFn\\Game\\2dAssets\\pantallasDeCarga " +textorandom+"\\Season14"
nombre_nuevo = "C:\\Program Files\\Epic Games\\Fortnite\\FortniteGame\\Content\\Paks\\PantallasDeCargaFn\\Game\\2dAssets\\pantallasDeCarga " +textorandom+"\\Temporada 4 cap 2"
os.rename(archivo, nombre_nuevo)
####
archivo = "C:\\Program Files\\Epic Games\\Fortnite\\FortniteGame\\Content\\Paks\\PantallasDeCargaFn\\Game\\2dAssets\\pantallasDeCarga " +textorandom+"\\Season15"
nombre_nuevo = "C:\\Program Files\\Epic Games\\Fortnite\\FortniteGame\\Content\\Paks\\PantallasDeCargaFn\\Game\\2dAssets\\pantallasDeCarga " +textorandom+"\\Temporada 5 cap 2"
os.rename(archivo, nombre_nuevo)
###
archivo = "C:\\Program Files\\Epic Games\\Fortnite\\FortniteGame\\Content\\Paks\\PantallasDeCargaFn\\Game\\2dAssets\\pantallasDeCarga " +textorandom+"\\Season16"
nombre_nuevo = "C:\\Program Files\\Epic Games\\Fortnite\\FortniteGame\\Content\\Paks\\PantallasDeCargaFn\\Game\\2dAssets\\pantallasDeCarga " +textorandom+"\\Temporada 6 cap 2"
os.rename(archivo, nombre_nuevo)
####
archivo = "C:\\Program Files\\Epic Games\\Fortnite\\FortniteGame\\Content\\Paks\\PantallasDeCargaFn\\Game\\2dAssets\\pantallasDeCarga " +textorandom+"\\Season17"
nombre_nuevo = "C:\\Program Files\\Epic Games\\Fortnite\\FortniteGame\\Content\\Paks\\PantallasDeCargaFn\\Game\\2dAssets\\pantallasDeCarga " +textorandom+"\\Temporada 7 cap 2"
os.rename(archivo, nombre_nuevo)
####
archivo = "C:\\Program Files\\Epic Games\\Fortnite\\FortniteGame\\Content\\Paks\\PantallasDeCargaFn\\Game\\2dAssets\\pantallasDeCarga " +textorandom+"\\Season18"
nombre_nuevo = "C:\\Program Files\\Epic Games\\Fortnite\\FortniteGame\\Content\\Paks\\PantallasDeCargaFn\\Game\\2dAssets\\pantallasDeCarga " +textorandom+"\\Temporada 8 cap 2"
os.rename(archivo, nombre_nuevo)
######
#REEMPLAZAMOS LA SUBCARPETA DE LA TEMPORADA 4
archivo = "C:\\Program Files\\Epic Games\\Fortnite\\FortniteGame\\Content\\Paks\\PantallasDeCargaFn\\Game\\2dAssets\\pantallasDeCarga " +textorandom+"\\Temporada4\\PreviewImages"
nombre_nuevo = "C:\\Program Files\\Epic Games\\Fortnite\\FortniteGame\\Content\\Paks\\PantallasDeCargaFn\\Game\\2dAssets\\pantallasDeCarga " +textorandom+"\\Temporada4\\Vista previa"
os.rename(archivo, nombre_nuevo)
######
#REEMPLAZAMOS LA SUBCARPETAS EVENTOS
archivo = "C:\\Program Files\\Epic Games\\Fortnite\\FortniteGame\\Content\\Paks\\PantallasDeCargaFn\\Game\\2dAssets\\pantallasDeCarga " +textorandom+"\\Eventos\\PreviewImages"
nombre_nuevo = "C:\\Program Files\\Epic Games\\Fortnite\\FortniteGame\\Content\\Paks\\PantallasDeCargaFn\\Game\\2dAssets\\pantallasDeCarga " +textorandom+"\\Eventos\\Vista previa"
os.rename(archivo, nombre_nuevo)
###
archivo = "C:\\Program Files\\Epic Games\\Fortnite\\FortniteGame\\Content\\Paks\\PantallasDeCargaFn\\Game\\2dAssets\\pantallasDeCarga " +textorandom+"\\Eventos\\Mayday2019"
nombre_nuevo = "C:\\Program Files\\Epic Games\\Fortnite\\FortniteGame\\Content\\Paks\\PantallasDeCargaFn\\Game\\2dAssets\\pantallasDeCarga " +textorandom+"\\Eventos\\Dia de Mayo 2019"
os.rename(archivo, nombre_nuevo)
###
archivo = "C:\\Program Files\\Epic Games\\Fortnite\\FortniteGame\\Content\\Paks\\PantallasDeCargaFn\\Game\\2dAssets\\pantallasDeCarga " +textorandom+"\\Eventos\\EndlessWinter"
nombre_nuevo = "C:\\Program Files\\Epic Games\\Fortnite\\FortniteGame\\Content\\Paks\\PantallasDeCargaFn\\Game\\2dAssets\\pantallasDeCarga " +textorandom+"\\Eventos\\Invierno sin fin"
os.rename(archivo, nombre_nuevo)
#####
archivo = "C:\\Program Files\\Epic Games\\Fortnite\\FortniteGame\\Content\\Paks\\PantallasDeCargaFn\\Game\\2dAssets\\pantallasDeCarga " +textorandom+"\\Generico\\Cumulative-PreviewImages"
nombre_nuevo = "C:\\Program Files\\Epic Games\\Fortnite\\FortniteGame\\Content\\Paks\\PantallasDeCargaFn\\Game\\2dAssets\\pantallasDeCarga " +textorandom+"\\Generico\\Imágenes de vista previa acumulativas"
os.rename(archivo, nombre_nuevo)
####
archivo = "C:\\Program Files\\Epic Games\\Fortnite\\FortniteGame\\Content\\Paks\\PantallasDeCargaFn\\Game\\2dAssets\\pantallasDeCarga " +textorandom+"\\Temporada 1 cap 2\\PreviewImages"
nombre_nuevo = "C:\\Program Files\\Epic Games\\Fortnite\\FortniteGame\\Content\\Paks\\PantallasDeCargaFn\\Game\\2dAssets\\pantallasDeCarga " +textorandom+"\\Temporada 1 cap 2\\Vista previa"
os.rename(archivo, nombre_nuevo)
#####
archivo = "C:\\Program Files\\Epic Games\\Fortnite\\FortniteGame\\Content\\Paks\\PantallasDeCargaFn\\Game\\2dAssets\\pantallasDeCarga " +textorandom+"\\Temporada 1 cap 2\\Textures"
nombre_nuevo = "C:\\Program Files\\Epic Games\\Fortnite\\FortniteGame\\Content\\Paks\\PantallasDeCargaFn\\Game\\2dAssets\\pantallasDeCarga " +textorandom+"\\Temporada 1 cap 2\\Texturas"
os.rename(archivo, nombre_nuevo)
####
archivo = "C:\\Program Files\\Epic Games\\Fortnite\\FortniteGame\\Content\\Paks\\PantallasDeCargaFn\\Game\\2dAssets\\pantallasDeCarga " +textorandom+"\\Temporada 2 cap 2\\Textures"
nombre_nuevo = "C:\\Program Files\\Epic Games\\Fortnite\\FortniteGame\\Content\\Paks\\PantallasDeCargaFn\\Game\\2dAssets\\pantallasDeCarga " +textorandom+"\\Temporada 2 cap 2\\Texturas"
os.rename(archivo, nombre_nuevo)
####
archivo = "C:\\Program Files\\Epic Games\\Fortnite\\FortniteGame\\Content\\Paks\\PantallasDeCargaFn\\Game\\2dAssets\\pantallasDeCarga " +textorandom+"\\Temporada 2 cap 2\\PreviewImages"
nombre_nuevo = "C:\\Program Files\\Epic Games\\Fortnite\\FortniteGame\\Content\\Paks\\PantallasDeCargaFn\\Game\\2dAssets\\pantallasDeCarga " +textorandom+"\\Temporada 2 cap 2\\Vista previa"
os.rename(archivo, nombre_nuevo)
####
archivo = "C:\\Program Files\\Epic Games\\Fortnite\\FortniteGame\\Content\\Paks\\PantallasDeCargaFn\\Game\\2dAssets\\pantallasDeCarga " +textorandom+"\\Temporada 3 cap 2\\PreviewImages"
nombre_nuevo = "C:\\Program Files\\Epic Games\\Fortnite\\FortniteGame\\Content\\Paks\\PantallasDeCargaFn\\Game\\2dAssets\\pantallasDeCarga " +textorandom+"\\Temporada 3 cap 2\\Vista previa"
os.rename(archivo, nombre_nuevo)
###
archivo = "C:\\Program Files\\Epic Games\\Fortnite\\FortniteGame\\Content\\Paks\\PantallasDeCargaFn\\Game\\2dAssets\\pantallasDeCarga " +textorandom+"\\Temporada 3 cap 2\\Textures"
nombre_nuevo = "C:\\Program Files\\Epic Games\\Fortnite\\FortniteGame\\Content\\Paks\\PantallasDeCargaFn\\Game\\2dAssets\\pantallasDeCarga " +textorandom+"\\Temporada 3 cap 2\\Texturas"
os.rename(archivo, nombre_nuevo)
####
archivo = "C:\\Program Files\\Epic Games\\Fortnite\\FortniteGame\\Content\\Paks\\PantallasDeCargaFn\\Game\\2dAssets\\pantallasDeCarga " +textorandom+"\\Temporada 4 cap 2\\PreviewImages"
nombre_nuevo = "C:\\Program Files\\Epic Games\\Fortnite\\FortniteGame\\Content\\Paks\\PantallasDeCargaFn\\Game\\2dAssets\\pantallasDeCarga " +textorandom+"\\Temporada 4 cap 2\\Vista previa"
os.rename(archivo, nombre_nuevo)
#####
archivo = "C:\\Program Files\\Epic Games\\Fortnite\\FortniteGame\\Content\\Paks\\PantallasDeCargaFn\\Game\\2dAssets\\pantallasDeCarga " +textorandom+"\\Temporada 4 cap 2\\Textures"
nombre_nuevo = "C:\\Program Files\\Epic Games\\Fortnite\\FortniteGame\\Content\\Paks\\PantallasDeCargaFn\\Game\\2dAssets\\pantallasDeCarga " +textorandom+"\\Temporada 4 cap 2\\Texturas"
os.rename(archivo, nombre_nuevo)
#####
archivo = "C:\\Program Files\\Epic Games\\Fortnite\\FortniteGame\\Content\\Paks\\PantallasDeCargaFn\\Game\\2dAssets\\pantallasDeCarga " +textorandom+"\\Temporada 5 cap 2\\PreviewImages"
nombre_nuevo = "C:\\Program Files\\Epic Games\\Fortnite\\FortniteGame\\Content\\Paks\\PantallasDeCargaFn\\Game\\2dAssets\\pantallasDeCarga " +textorandom+"\\Temporada 5 cap 2\\Vista previa"
os.rename(archivo, nombre_nuevo)
####
archivo = "C:\\Program Files\\Epic Games\\Fortnite\\FortniteGame\\Content\\Paks\\PantallasDeCargaFn\\Game\\2dAssets\\pantallasDeCarga " +textorandom+"\\Temporada 5 cap 2\\Textures"
nombre_nuevo = "C:\\Program Files\\Epic Games\\Fortnite\\FortniteGame\\Content\\Paks\\PantallasDeCargaFn\\Game\\2dAssets\\pantallasDeCarga " +textorandom+"\\Temporada 5 cap 2\\Texturas"
os.rename(archivo, nombre_nuevo)
#####
archivo = "C:\\Program Files\\Epic Games\\Fortnite\\FortniteGame\\Content\\Paks\\PantallasDeCargaFn\\Game\\2dAssets\\pantallasDeCarga " +textorandom+"\\Temporada 6 cap 2\\PreviewImages"
nombre_nuevo = "C:\\Program Files\\Epic Games\\Fortnite\\FortniteGame\\Content\\Paks\\PantallasDeCargaFn\\Game\\2dAssets\\pantallasDeCarga " +textorandom+"\\Temporada 6 cap 2\\Vista previa"
os.rename(archivo, nombre_nuevo)
#####
archivo = "C:\\Program Files\\Epic Games\\Fortnite\\FortniteGame\\Content\\Paks\\PantallasDeCargaFn\\Game\\2dAssets\\pantallasDeCarga " +textorandom+"\\Temporada 6 cap 2\\Textures"
nombre_nuevo = "C:\\Program Files\\Epic Games\\Fortnite\\FortniteGame\\Content\\Paks\\PantallasDeCargaFn\\Game\\2dAssets\\pantallasDeCarga " +textorandom+"\\Temporada 6 cap 2\\Texturas"
os.rename(archivo, nombre_nuevo)
####
archivo = "C:\\Program Files\\Epic Games\\Fortnite\\FortniteGame\\Content\\Paks\\PantallasDeCargaFn\\Game\\2dAssets\\pantallasDeCarga " +textorandom+"\\Temporada 7 cap 2\\PreviewImages"
nombre_nuevo = "C:\\Program Files\\Epic Games\\Fortnite\\FortniteGame\\Content\\Paks\\PantallasDeCargaFn\\Game\\2dAssets\\pantallasDeCarga " +textorandom+"\\Temporada 7 cap 2\\Vista previa"
os.rename(archivo, nombre_nuevo)
####
archivo = "C:\\Program Files\\Epic Games\\Fortnite\\FortniteGame\\Content\\Paks\\PantallasDeCargaFn\\Game\\2dAssets\\pantallasDeCarga " +textorandom+"\\Temporada 7 cap 2\\Textures"
nombre_nuevo = "C:\\Program Files\\Epic Games\\Fortnite\\FortniteGame\\Content\\Paks\\PantallasDeCargaFn\\Game\\2dAssets\\pantallasDeCarga " +textorandom+"\\Temporada 7 cap 2\\Texturas"
os.rename(archivo, nombre_nuevo)
####
archivo = "C:\\Program Files\\Epic Games\\Fortnite\\FortniteGame\\Content\\Paks\\PantallasDeCargaFn\\Game\\2dAssets\\pantallasDeCarga " +textorandom+"\\Temporada 8 cap 2\\PreviewImages"
nombre_nuevo = "C:\\Program Files\\Epic Games\\Fortnite\\FortniteGame\\Content\\Paks\\PantallasDeCargaFn\\Game\\2dAssets\\pantallasDeCarga " +textorandom+"\\Temporada 8 cap 2\\Vista previa"
os.rename(archivo, nombre_nuevo)
#####
archivo = "C:\\Program Files\\Epic Games\\Fortnite\\FortniteGame\\Content\\Paks\\PantallasDeCargaFn\\Game\\2dAssets\\pantallasDeCarga " +textorandom+"\\Temporada 8 cap 2\\Textures"
nombre_nuevo = "C:\\Program Files\\Epic Games\\Fortnite\\FortniteGame\\Content\\Paks\\PantallasDeCargaFn\\Game\\2dAssets\\pantallasDeCarga " +textorandom+"\\Temporada 8 cap 2\\Texturas"
os.rename(archivo, nombre_nuevo)

#####
archivo = "C:\\Program Files\\Epic Games\\Fortnite\\FortniteGame\\Content\\Paks\\PantallasDeCargaFn\\Game\\2dAssets\\pantallasDeCarga " +textorandom+"\\Temporada5\\PreviewImages"
nombre_nuevo = "C:\\Program Files\\Epic Games\\Fortnite\\FortniteGame\\Content\\Paks\\PantallasDeCargaFn\\Game\\2dAssets\\pantallasDeCarga " +textorandom+"\\Temporada5\\Vista previa"
os.rename(archivo, nombre_nuevo)
####
archivo = "C:\\Program Files\\Epic Games\\Fortnite\\FortniteGame\\Content\\Paks\\PantallasDeCargaFn\\Game\\2dAssets\\pantallasDeCarga " +textorandom+"\\Temporada6\\PreviewImage"
nombre_nuevo = "C:\\Program Files\\Epic Games\\Fortnite\\FortniteGame\\Content\\Paks\\PantallasDeCargaFn\\Game\\2dAssets\\pantallasDeCarga " +textorandom+"\\Temporada6\\Vista previa"
os.rename(archivo, nombre_nuevo)
####
archivo = "C:\\Program Files\\Epic Games\\Fortnite\\FortniteGame\\Content\\Paks\\PantallasDeCargaFn\\Game\\2dAssets\\pantallasDeCarga " +textorandom+"\\Temporada7\\PreviewImages"
nombre_nuevo = "C:\\Program Files\\Epic Games\\Fortnite\\FortniteGame\\Content\\Paks\\PantallasDeCargaFn\\Game\\2dAssets\\pantallasDeCarga " +textorandom+"\\Temporada7\\Vista previa"
os.rename(archivo, nombre_nuevo)
####
archivo = "C:\\Program Files\\Epic Games\\Fortnite\\FortniteGame\\Content\\Paks\\PantallasDeCargaFn\\Game\\2dAssets\\pantallasDeCarga " +textorandom+"\\Temporada8\\PreviewImages"
nombre_nuevo = "C:\\Program Files\\Epic Games\\Fortnite\\FortniteGame\\Content\\Paks\\PantallasDeCargaFn\\Game\\2dAssets\\pantallasDeCarga " +textorandom+"\\Temporada8\\Vista previa"
os.rename(archivo, nombre_nuevo)
#####
archivo = "C:\\Program Files\\Epic Games\\Fortnite\\FortniteGame\\Content\\Paks\\PantallasDeCargaFn\\Game\\2dAssets\\pantallasDeCarga " +textorandom+"\\Temporada9\\PreviewImages"
nombre_nuevo = "C:\\Program Files\\Epic Games\\Fortnite\\FortniteGame\\Content\\Paks\\PantallasDeCargaFn\\Game\\2dAssets\\pantallasDeCarga " +textorandom+"\\Temporada9\\Vista previa"
os.rename(archivo, nombre_nuevo)
#####
archivo = "C:\\Program Files\\Epic Games\\Fortnite\\FortniteGame\\Content\\Paks\\PantallasDeCargaFn\\Game\\2dAssets\\pantallasDeCarga " +textorandom+"\\Temporada10\\PreviewImages"
nombre_nuevo = "C:\\Program Files\\Epic Games\\Fortnite\\FortniteGame\\Content\\Paks\\PantallasDeCargaFn\\Game\\2dAssets\\pantallasDeCarga " +textorandom+"\\Temporada10\\Vista previa"
os.rename(archivo, nombre_nuevo)
####
archivo = "C:\\Program Files\\Epic Games\\Fortnite\\FortniteGame\\Content\\Paks\\PantallasDeCargaFn\\Game\\2dAssets\\pantallasDeCarga " +textorandom+"\\Temporada10\\Textures"
nombre_nuevo = "C:\\Program Files\\Epic Games\\Fortnite\\FortniteGame\\Content\\Paks\\PantallasDeCargaFn\\Game\\2dAssets\\pantallasDeCarga " +textorandom+"\\Temporada10\\Texturas"
os.rename(archivo, nombre_nuevo)
 



directorio4 = 'C:\\Program Files\\Epic Games\\Fortnite\\FortniteGame\\Content\\Paks\\PantallasDeCargaFn\\Game\\2dAssets\\pantallasDeCarga' +textorandom+'\\Temporada8\\DragonNinjaLoading'
directorio5 = 'C:\\Program Files\Epic Games\\Fortnite\\FortniteGame\\Content\\Paks\\PantallasDeCargaFn\\Game\\2dAssets\\pantallasDeCarga ' +textorandom+'\\Temporada7\\NeonCatLoading'

try:
    shutil.rmtree(directorio4)
    shutil.rmtree(directorio5)
   
except OSError as e:
    print(f"Error:{ e.strerror}")

ArchivoTEXTO = open('C:\\Program Files\\Epic Games\\Fortnite\\FortniteGame\\Content\\Paks\\PantallasDeCargaFn\\Game\\2dAssets\\pantallasDeCarga ' +textorandom+'\\Leeme.txt','w')

   
ArchivoTEXTO.write("Muchas gracias por descargar\n\nMi twitter es: Jose89fcb")
ArchivoTEXTO.close()






notification = Notify()
notification.application_name = "Pantallas de carga fortnite" 
notification.title = "Fortnite"
notification.message = "fin de la descarga...🥳"
icono = "logo/KevinORO.png"
audio = "audio/fin.wav"
direcion = path.abspath(path.dirname(__file__))
notification.icon = path.join(direcion, icono)
notification.audio = path.join(direcion, audio)
notification.send()
time.sleep(3)

###
notification = Notify()
notification.application_name = "Pantallas de carga fortnite" 
notification.title = "Fortnite"
notification.message = "Abriendo carpeta...📁"
icono = "logo/KevinORO.png"
audio = "audio/abriendo.wav"
direcion = path.abspath(path.dirname(__file__))
notification.icon = path.join(direcion, icono)
notification.audio = path.join(direcion, audio)
notification.send()


remove('1PantallasDeCargaFN.bat')
time.sleep(6)

path="PantallasDeCargaFn\\Game\\2dAssets\\pantallasDeCarga " +textorandom
path=os.path.realpath(path)
os.startfile(path)


