import subprocess
import requests
import os
import time
import hashlib
import uuid
from colorama import init, Fore, Back, Style

bandera = True

def obtener_info_servidor():
    print(" "*39 + "[$] Ingrese la IP del servidor\n")
    ingreso_ip = input(" "*11 + "mc-status@negros:~$ ")
    try:
        urlmc = f"https://api.mcsrvstat.us/3/{ingreso_ip}"
        response_mc = requests.get(urlmc)
        datamc = response_mc.json()

        token_ipinfo = "be8b5cb7052ada"
        url_ipinfo = f"https://ipinfo.io/{datamc['ip']}?token={token_ipinfo}"
        response_ipinfo = requests.get(url_ipinfo)
        data_ipinfo = response_ipinfo.json()

        if datamc.get("online") != False:

            software_variable = datamc.get("software", "No disponible")
            version_soporte = datamc.get("version", "No disponible")
            data_motd = datamc.get("motd")
            org_ip = data_ipinfo.get("org", "No disponible")
            if org_ip != "No disponible":
                asn = org_ip.split(" ")

            longitud_motd = len(data_motd["clean"])
            if longitud_motd == 1:
                info_motd = data_motd["clean"][0]
            elif longitud_motd == 2:
                info_motd = data_motd["clean"][0] + "\n" + " "*32 + data_motd["clean"][1]

            print(f"""
                                ┌──────────────────────────────────────────────────┐

                                    (Dominio) » {ingreso_ip}
                                    (IPv4) » {datamc["ip"]}
                                    (ASN) » {asn[0]}
                                    (Puerto) » {datamc["port"]}
                                    (Jugadores) » {datamc["players"]["online"]} / {datamc["players"]["max"]}
                                    (Version Soporte) » {version_soporte}
                                    (Software) » {software_variable}
                                    (Version) » {datamc["protocol"]["name"]}  |  (Protocolo) » {datamc["protocol"]["version"]}
                                    (MOTD) »
                                    
                                    {info_motd}
                                └──────────────────────────────────────────────────┘
        """)
        else:
            print("\n" + " "*20 + "[!] Server offline o no existe!" + "\n")
        
        input(" "*9 + "[$] Presione Enter para volver al menu ")
    except:
        print("\n" + " "*20 + "[!] La IP ingresada no es valida")
        time.sleep(5)

def clear_consola():
    if(os.name == "nt"):
        os.system("cls")
    else:
        os.system("clear")

def dibujar_titulos(clave):
    if clave == "titulo_menu":
        print("""
          

                            ███╗   ██╗██╗  ██╗ ██████╗ ██████╗ ██╗  ██╗███████╗       
                            ████╗  ██║╚██╗██╔╝██╔════╝ ██╔══██╗╚██╗██╔╝██╔════╝       
                            ██╔██╗ ██║ ╚███╔╝ ██║  ███╗██████╔╝ ╚███╔╝ ███████╗       
                            ██║╚██╗██║ ██╔██╗ ██║   ██║██╔══██╗ ██╔██╗ ╚════██║       
                            ██║ ╚████║██╔╝ ██╗╚██████╔╝██║  ██║██╔╝ ██╗███████║       
                            ╚═╝  ╚═══╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝  2.0  
                                                                                    
                             ██████╗ ██████╗ ██╗███████╗███████╗██╗███╗   ██╗ ██████╗ 
                            ██╔════╝ ██╔══██╗██║██╔════╝██╔════╝██║████╗  ██║██╔════╝ 
                            ██║  ███╗██████╔╝██║█████╗  █████╗  ██║██╔██╗ ██║██║  ███╗
                            ██║   ██║██╔══██╗██║██╔══╝  ██╔══╝  ██║██║╚██╗██║██║   ██║
                            ╚██████╔╝██║  ██║██║███████╗██║     ██║██║ ╚████║╚██████╔╝
                             ╚═════╝ ╚═╝  ╚═╝╚═╝╚══════╝╚═╝     ╚═╝╚═╝  ╚═══╝ ╚═════╝ 
""")
    elif clave == "opciones_menu":
        print("""
                                    ┌───────────────────────────────────┐
                                         [1] - Obtener info servidor
                                         [2] - Escaneo con (Qubo)
                                         [3] - Escaneo con (Nmap)
                                         [4] - Checkeo de puertos
                                         [5] - Obtener UUID-MC
                                         [6] - Ordenar (TXT) escaneo
                                         [7] - Idioma / Language
                                         [8] - Cargar configuracion
                                         [9] - Salir
                                    └───────────────────────────────────┘
""")
        
    elif clave == "server_status":
        print("""
              

                            ███████╗████████╗ █████╗ ████████╗██╗   ██╗███████╗
                            ██╔════╝╚══██╔══╝██╔══██╗╚══██╔══╝██║   ██║██╔════╝
                            ███████╗   ██║   ███████║   ██║   ██║   ██║███████╗
                            ╚════██║   ██║   ██╔══██║   ██║   ██║   ██║╚════██║
                            ███████║   ██║   ██║  ██║   ██║   ╚██████╔╝███████║
                            ╚══════╝   ╚═╝   ╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚══════╝
""")
        
    elif clave == "escaneo_qubo":
        print("""

                                     ██████╗ ██╗   ██╗██████╗  ██████╗ 
                                    ██╔═══██╗██║   ██║██╔══██╗██╔═══██╗
                                    ██║   ██║██║   ██║██████╔╝██║   ██║
                                    ██║▄▄ ██║██║   ██║██╔══██╗██║   ██║
                                    ╚██████╔╝╚██████╔╝██████╔╝╚██████╔╝
                                     ╚══▀▀═╝  ╚═════╝ ╚═════╝  ╚═════╝ 
""")
        
    elif clave == "opciones_escaneo":
        print("""
                                    ┌───────────────────────────────────┐
                                         [1] - Escaneo unica IP
                                         [2] - Escaneo multiple (txt)
                                         [3] - Salir al menu
                                    └───────────────────────────────────┘
""")
    
    elif clave == "escaneo_nmap":
        print("""

                                    ███╗   ██╗███╗   ███╗ █████╗ ██████╗ 
                                    ████╗  ██║████╗ ████║██╔══██╗██╔══██╗
                                    ██╔██╗ ██║██╔████╔██║███████║██████╔╝
                                    ██║╚██╗██║██║╚██╔╝██║██╔══██║██╔═══╝ 
                                    ██║ ╚████║██║ ╚═╝ ██║██║  ██║██║     
                                    ╚═╝  ╚═══╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝     
""")
        
    elif clave == "opciones_escaneo_nmap":
        print("""
                                    ┌───────────────────────────────────┐
                                         [1] - Escaneo ports MC
                                         [2] - Escaneo 1-65535
                                         [3] - Salir al menu
                                    └───────────────────────────────────┘
""")
    elif clave == "titulo_uuid":
        print("""

              
                            ██╗   ██╗██╗   ██╗██╗██████╗       ███╗   ███╗ ██████╗
                            ██║   ██║██║   ██║██║██╔══██╗      ████╗ ████║██╔════╝
                            ██║   ██║██║   ██║██║██║  ██║█████╗██╔████╔██║██║     
                            ██║   ██║██║   ██║██║██║  ██║╚════╝██║╚██╔╝██║██║     
                            ╚██████╔╝╚██████╔╝██║██████╔╝      ██║ ╚═╝ ██║╚██████╗
                             ╚═════╝  ╚═════╝ ╚═╝╚═════╝       ╚═╝     ╚═╝ ╚═════╝
""")
    elif clave == "ordenamiento":
        print("""

              
                 ██████╗ ██████╗ ██████╗ ███████╗███╗   ██╗████████╗██╗  ██╗████████╗
                ██╔═══██╗██╔══██╗██╔══██╗██╔════╝████╗  ██║╚══██╔══╝╚██╗██╔╝╚══██╔══╝
                ██║   ██║██████╔╝██║  ██║█████╗  ██╔██╗ ██║   ██║    ╚███╔╝    ██║   
                ██║   ██║██╔══██╗██║  ██║██╔══╝  ██║╚██╗██║   ██║    ██╔██╗    ██║   
                ╚██████╔╝██║  ██║██████╔╝███████╗██║ ╚████║██╗██║   ██╔╝ ██╗   ██║   
                 ╚═════╝ ╚═╝  ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═══╝╚═╝╚═╝   ╚═╝  ╚═╝   ╚═╝   
""")

def escanear_ip_qubo(puertos:str, threads:str, timeout:str, ip:str):
    comando = f"java -Dfile.encoding=UTF-8 -jar qubo.jar -ports {puertos} -th {threads} -ti {timeout} -noping -range {ip}"
    ejecucion = subprocess.Popen(comando, text=True ,shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print_tiempo_real = True

    while print_tiempo_real:
        if ejecucion.poll() is not None:
            print_tiempo_real = False
        else:
            print(ejecucion.stdout.readline(), end="")

def escaneo_qubo(clave:str, mensaje_qubo_cmd:str):
    if clave == "escaneo_unica_ip":
        print("\n" + " "*20 + "[$] Ingrese la IP a escanear" + "\n")
        ip = input(mensaje_qubo_cmd)
        
    elif clave == "escaneo_multiple":
        print("\n" + " "*20 + "[$] Ingrese la ruta directa del archivo .txt" + "\n")
        print(" "*22 + "[!] Ejemplo » C:/Users/Nicolas/Desktop/nxgrxs/ranges.txt" + "\n")

        path = input(mensaje_qubo_cmd)
        with open(path, "r", encoding="utf-8") as archivo:
            data_ips = archivo.readlines()
    
    print("\n" + " "*20 + "[$] Ingrese los puertos a escanear con el siguiente formato EJ: X-XXXXX" + "\n")
    puertos = input(mensaje_qubo_cmd)

    print("\n" + " "*20 + "[$] Ingrese las THREADS a usar" + "\n")
    threads = input(mensaje_qubo_cmd)

    print("\n" + " "*20 + "[$] Ingrese el TIMEOUT" + "\n")
    timeout = input(mensaje_qubo_cmd)
    print("\n")

    if clave == "escaneo_unica_ip":
        escanear_ip_qubo(puertos, threads, timeout, ip)

    elif clave == "escaneo_multiple":
        for ip in data_ips:
            escanear_ip_qubo(puertos, threads, timeout, ip)
    
    input("\n" + " "*13 + "[$] Presione Enter para volver al menu " + "\n")
    clear_consola()

def opciones_qubo():
    while True:
        dibujar_titulos("escaneo_qubo")
        dibujar_titulos("opciones_escaneo")

        mensaje_qubo_cmd = " "*13 + f"qubo@nxgrxs:~$ "
        opcion_qubo = input(mensaje_qubo_cmd)

        match opcion_qubo:
            case "1":
                escaneo_qubo("escaneo_unica_ip", mensaje_qubo_cmd)
            case "2":
                escaneo_qubo("escaneo_multiple", mensaje_qubo_cmd)
            case "3":
                return
            case _:
                clear_consola()
                break

def escanear_ip_nmap(ip:str, opcion_escaneo_all: bool, opcion_escaneo_ports_mc: bool):
    if opcion_escaneo_all:
        comando = f"nmap -p 1-65535 -T4 -A --open -v -Pn {ip}"
    elif opcion_escaneo_ports_mc:
        puertos = "1-12,1000-1010,20000-20005,25000-25002,25500-25640,28010-28015,30000-30005,40000-40010,65500-65535"
        comando = f"nmap -p {puertos} -T5 -A -v {ip}"

    ejecucion = subprocess.Popen(comando, text=True, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    while True:
        if ejecucion.poll() is not None:
            break
        else:
            print(ejecucion.stdout.readline(), end="")

def escaneo_nmap(clave: str, msj_nmap: str):
    if clave == "escaneo_unica_ip":
        print("\n" + " "*20 + "[!] Ingrese la IP a escanear" + "\n")
        ip = input(msj_nmap)

    elif clave == "escaneo_multiple":
        print("\n" + " "*20 + "[$] Ingrese la ruta directa del archivo .txt" + "\n")
        print(" "*22 + "[!] Ejemplo » C:/Users/Nicolas/Desktop/nxgrxs/ips.txt" + "\n")
        path = input(msj_nmap)

        with open(path, "r", encoding="utf-8") as archivo:
            data_ips = archivo.readlines()
    
    opcion_escaneo_ports_mc = False
    opcion_escaneo_all = False
    iniciar_escaneo = False

    while True:
        dibujar_titulos("opciones_escaneo_nmap")
        opcion_escaneo_nmap = input(msj_nmap)

        match opcion_escaneo_nmap:
            case "1":
                opcion_escaneo_ports_mc = True
                iniciar_escaneo = True
                break
            case "2":
                opcion_escaneo_all = True
                iniciar_escaneo = True
                break
            case "3":
                clear_consola()
                return
            case _:
                clear_consola()
    
    if clave == "escaneo_unica_ip" and iniciar_escaneo == True:
        escanear_ip_nmap(ip, opcion_escaneo_all, opcion_escaneo_ports_mc)

    elif clave == "escaneo_multiple" and iniciar_escaneo == True:
        for ip in data_ips:
            escanear_ip_nmap(ip, opcion_escaneo_all, opcion_escaneo_ports_mc)
    
    input("\n" + " "*13 + "[$] Presione Enter para volver al menu " + "\n")
    clear_consola()

def obtener_uuid(nombre: str)->dict:
    url = "https://api.mojang.com/users/profiles/minecraft/"
    response = requests.get(url + nombre)
    datos = response.json()
    uuids_jugador = {}
    
    if(datos.get('id')):
        uuid_premium = datos.get('id')
        uuid_premium_formato = ""
        indice_default = 8
        num_espacio = 0
        for i,char in enumerate(uuid_premium):
            if((i == (indice_default + num_espacio)) and (i <= 20)):
                uuid_premium_formato += "-"
                indice_default = i
                num_espacio = 4
            uuid_premium_formato += char

        uuids_jugador["PremiumUUID"] = uuid_premium_formato
    
    formato_offline = 'OfflinePlayer:' + nombre
    hash_md5 = hashlib.md5(formato_offline.encode(encoding="utf-8")).digest()
    uuid_formato = str(uuid.UUID(bytes=hash_md5, version=3))
    uuids_jugador["OfflineUUID"] = uuid_formato

    return uuids_jugador

def mensaje_uuid():
    dibujar_titulos("titulo_uuid")
    print("\n" + " "*20 + "[!] Ingrese el nombre" + "\n")
    nombre_mc = input(" "*13 + "uuid@nxgrxs:~$ ")

    datos = obtener_uuid(nombre_mc)

    print(f"""
                        ┌─────────────────────────────────────────────────────────────┐

                            (Nick) » {nombre_mc}
                            (PREMIUM) » {datos.get('PremiumUUID') if datos.get('PremiumUUID') else "ES NO PREMIUM"}
                            (NO-PREMIUM) » {datos.get('OfflineUUID')}

                        └─────────────────────────────────────────────────────────────┘
""")
    
    input("\n" + " "*13 + "[$] Presione Enter para volver al menu " + "\n")

def opciones_nmap():
    while True:
        dibujar_titulos("escaneo_nmap")
        dibujar_titulos("opciones_escaneo")
        msj_nmap = " "*13 + "nmap@nxgrxs:~$ "
        ingreso_opcion = input(msj_nmap)

        match ingreso_opcion:
            case "1":
                escaneo_nmap("escaneo_unica_ip",msj_nmap)
            case "2":
                escaneo_nmap("escaneo_multiple",msj_nmap)
            case "3":
                clear_consola()
                break
            case _:
                clear_consola()

def order_archivo(ruta: str)->bool:
    try:
        with open(file=ruta,mode="r",encoding="utf-8") as archivo:
            datos = archivo.readlines()

        diccionario_datos = []
        for i,linea in enumerate(datos):
            if(linea.count("(") > 0):
                try:
                    lista_linea = []
                    linea_separada = linea.split("(")
                    agregada = False
                    if(len(diccionario_datos) > 0):
                        for linea2 in diccionario_datos:
                            if(linea.split("(")[1] == linea2[1].split("(")[1]):
                                agregada = True
                    
                    if(agregada == False):
                        lista_linea.append(int(linea_separada[2].split("/")[0]))
                        lista_linea.append(linea)
                        diccionario_datos.append(lista_linea)
                except:
                    continue
        
        diccionario_datos.sort(key=(lambda x:x[0]),reverse=True)

        with open(file=ruta, mode="w", encoding="utf-8") as archivo:
            for linea in diccionario_datos:
                archivo.write(linea[1])
        
        retorno = True
    except:
        retorno = False
    
    return retorno

def ordenamiento():
    dibujar_titulos("ordenamiento")

    print("\n" + " "*20 + "[$] Ingrese la ruta directa del archivo .txt" + "\n")
    print(" "*22 + "[!] Ejemplo » C:/Users/Nicolas/Desktop/nxgrxs/escaneo.txt" + "\n")

    mensaje_order_cmd = " "*13 + f"order@nxgrxs:~$ "
    ruta = str(input(mensaje_order_cmd))
    
    print("\n" + " "*22 + "[!] Se ORDENO correctamente!" if order_archivo(ruta) else "\n" + " "*22 + "[X] Archivo no encontrado o ruta incorrecta")
    input("\n" + " "*13 + "[$] Presione Enter para volver al menu " + "\n")

while bandera:
    clear_consola()
    dibujar_titulos("titulo_menu")
    dibujar_titulos("opciones_menu")

    ingreso_opcion = input(" "*13 + "root@nxgrxs:~$ ")

    match ingreso_opcion:
        case "1":
            clear_consola()
            dibujar_titulos("server_status")
            obtener_info_servidor()
        case "2":
            clear_consola()
            opciones_qubo()
        case "3":
            clear_consola()
            opciones_nmap()
        case "4":
            pass
        case "5":
            clear_consola()
            mensaje_uuid()
        case "6":
            clear_consola()
            ordenamiento()
        case "7":
            pass # modificar idioma
        case "8":
            pass # cargar configuracion
        case "9":
            bandera = False
        case _:
            pass

clear_consola()