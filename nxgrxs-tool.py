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
        
        continuar = input(" "*9 + "[$] Presione Enter para volver al menu ")
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
                                         [5] - Salir
                                    └───────────────────────────────────┘
""")
    elif clave == "opciones_qubo":
        print("""
                                    ┌───────────────────────────────────┐
                                         [1] - Escaneo unica IP
                                         [2] - Escaneo multiple (txt)
                                         [3] - Salir al menu
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

def escaneo_qubo():
    while True:
        dibujar_titulos("escaneo_qubo")
        dibujar_titulos("opciones_qubo")

        mensaje_qubo_cmd = " "*13 + f"qubo@nxgrxs:~$ "
        opcion_qubo = input(mensaje_qubo_cmd)

        match opcion_qubo:
            case "1":
                print("\n" + " "*20 + "[$] Ingrese la IP a escanear" + "\n")
                ip = input(mensaje_qubo_cmd)

                print("\n" + " "*20 + "[$] Ingrese los puertos a escanear con el siguiente formato EJ: X-XXXXX" + "\n")
                puertos = input(mensaje_qubo_cmd)

                print("\n" + " "*20 + "[$] Ingrese las THREADS a usar" + "\n")
                threads = input(mensaje_qubo_cmd)

                print("\n" + " "*20 + "[$] Ingrese el TIMEOUT" + "\n")
                timeout = input(mensaje_qubo_cmd)
                print("\n")

                comando = f"java -Dfile.encoding=UTF-8 -jar qubo.jar -ports {puertos} -th {threads} -ti {timeout} -noping -range {ip}"
            case "2":
                pass
            case "3":
                return
            case _:
                os.system("cls")
                pass

def escaneo_nmap():
    print("[!] Ingrese la IP a escanear")
    ip_nmap = input("nmap@nxgrxs:~$ ")


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
            escaneo_qubo()
        case "3":
            pass
        case "4":
            pass
        case "5":
            bandera = False
        case _:
            pass