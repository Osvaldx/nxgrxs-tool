import subprocess
import requests
import os
import time
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
                                         [6] - Salir
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
    os.system("cls")

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
                os.system("cls")
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
                os.system("cls")
                return
            case _:
                os.system("cls")
    
    if clave == "escaneo_unica_ip" and iniciar_escaneo == True:
        escanear_ip_nmap(ip, opcion_escaneo_all, opcion_escaneo_ports_mc)

    elif clave == "escaneo_multiple" and iniciar_escaneo == True:
        for ip in data_ips:
            escanear_ip_nmap(ip, opcion_escaneo_all, opcion_escaneo_ports_mc)
    
    input("\n" + " "*13 + "[$] Presione Enter para volver al menu " + "\n")
    os.system("cls")

def obtener_uuid():
    dibujar_titulos("titulo_uuid")
    print("\n" + " "*20 + "[!] Ingrese el nombre" + "\n")
    nombre_mc = input(" "*13 + "uuid@nxgrxs:~$ ")

    url_offline_uuid = "https://minecraft-serverlist.com/tools/offline-uuid"
    payload = {
        "uuids": {nombre_mc},
        "export": "json",
        "_token": "GoVUhkLQh9xXucUNw3idxU0LCTzMW83QWp1IJIZb"
    }
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Cookie": "XSRF-TOKEN=eyJpdiI6IlhhU3YzZ1BFemtFcGQ3TytyMlpYbXc9PSIsInZhbHVlIjoiYURaZm1sTWdhazNtb3V3STRyTzR4RHA2a0kzeWFiRHp5SjExUHY2YVFkZEtINDM3anNCcXE3akVHS0dpYlV1eDUxKzR6S0xsR2k2ZVNQL0lGbmlGRStmRTdxQnlITWFpZ2VPWGYwVG5YVkNrWENNZEtyOGprR08vZkZ0eUVVMjIiLCJtYWMiOiI1NzVmOTA1MjNiMmI2ZDEwZDgzZWZiZDFjMTBmY2FlNmYwN2I2MTQ3MDdiMzM5NTVhMGZlNjg3NzQ0YzM1YTY3IiwidGFnIjoiIn0%3D; _mcsl_session=eyJpdiI6IktmRjZKU05FRU5KazMzSHlGbUVTdlE9PSIsInZhbHVlIjoiVTVGN2xxanBoTE45V1l0cVU2VDBoeCszU2tFazZtVHduU0dWTlQ1VWtMWm1kOVA4dU95YXFHdjRXd3VqbEtSUkxTb3I1ZmVsMGRjUXhRbm5yY0l4dENaM3NUQm9ROE9YMHlXNjZkNFVrWGdLMHZyTWJDaXdNTWQ5M2NISTlDR08iLCJtYWMiOiI5MjRlMmRhZDg4YmNkZmIxNDEzMjZhOWY1YWFhMmFhZDA2OTE3MWNlNjYzNDE4MzY1NjQyYjI0YTg1MmMyZjE2IiwidGFnIjoiIn0%3D"
    }

    response_offline = requests.post(url_offline_uuid, data=payload, headers=headers)
    data_uuid_offline = response_offline.text.split('"')

    api_mc = f"https://api.mojang.com/users/profiles/minecraft/{nombre_mc}"
    response_mc = requests.get(api_mc)
    data = response_mc.json()

    if data.get("id") is None:
        uuid_premium = "NO PREMIUM"
    else:
        uuid_premium = data.get("id")
    
    if data_uuid_offline[9] == "illegal characters - only alphanumeric characters allowed.":
        uuid_no_premium = "ILLEGAL CHARACTERS"
    else:
        uuid_no_premium = data_uuid_offline[9]

    print(f"""
                        ┌─────────────────────────────────────────────────────────────┐

                            (Nick) » {nombre_mc}
                            (PREMIUM) » {uuid_premium}
                            (NO-PREMIUM) » {uuid_no_premium}

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
                os.system("cls")
                break
            case _:
                os.system("cls")

while bandera:
    os.system("cls")
    dibujar_titulos("titulo_menu")
    dibujar_titulos("opciones_menu")

    ingreso_opcion = input(" "*13 + "root@nxgrxs:~$ ")

    match ingreso_opcion:
        case "1":
            os.system("cls")
            dibujar_titulos("server_status")
            obtener_info_servidor()
        case "2":
            os.system("cls")
            opciones_qubo()
        case "3":
            os.system("cls")
            opciones_nmap()
        case "4":
            pass
        case "5":
            os.system("cls")
            obtener_uuid()
        case "6":
            bandera = False
        case _:
            pass

os.system("cls")