# Nxgrxs Griefing

## Descripción

**nxgrxs Server Tools** es una herramienta en **Python** diseñada para *obtener información de servidores de Minecraft*, realizar **escaneos de puertos** y **obtener UUIDs de jugadores de Minecraft**. La herramienta **utiliza varias APIs** para recopilar información detallada sobre el servidor, **realiza escaneos** de puertos con **nmap** y **qubo**, y permite al usuario elegir entre **múltiples opciones** desde un menú interactivo.

## Características
- **Obtener información de un servidor de Minecraft:** Se conecta a una API para obtener detalles sobre el servidor, como la versión, software, jugadores conectados, etc.
- **Escaneo de puertos:** Permite realizar escaneos de puertos personalizados utilizando nmap o qubo.
- **Obtener UUID de Minecraft:** Recupera el UUID de un jugador de Minecraft, tanto en servidores premium como en no premium.

## Opciones del Menú
- **Opciones del menu:**

![image](https://github.com/user-attachments/assets/3959620e-428c-445f-a442-0d2fc0010ccf)

- **Obtener info servidor:** Ingresa la IP del servidor de Minecraft para obtener información detallada.

![image](https://github.com/user-attachments/assets/8c866e9f-5b78-449b-b5d2-6743a7d3c4f6)

- **Escaneo con Qubo:** Realiza un escaneo de puertos utilizando Qubo, con opciones para escanear una única IP o múltiples IPs desde un archivo.

![image](https://github.com/user-attachments/assets/f9eb70de-82ca-4779-a7ea-4ec61af2e7b3)
![image](https://github.com/user-attachments/assets/481a5871-173f-476b-8384-71789dbfbaad)

- **Escaneo con Nmap:** Realiza un escaneo de puertos utilizando Nmap, con opciones para escanear puertos específicos de Minecraft o todos los puertos.

![image](https://github.com/user-attachments/assets/a6da7a1a-33bc-4553-b5ce-30883fbc4f95)

- **Checkeo de puertos:** Realiza una comprobación rápida de los puertos abiertos (no programada).
[photo]

- **Obtener UUID-MC:** Recupera el UUID de un jugador de Minecraft.

![image](https://github.com/user-attachments/assets/0f4a8bd2-30f8-47c5-a377-13381fdd62ab)

## Instalación
*Clona este repositorio:*
```bash
  git clone https://github.com/tu-usuario/nxgrxs-griefing.git
```
*Navega al directorio del proyecto:*
```bash
  cd nxgrxs-griefing
```
*Instala las dependencias:*
```bash
  pip install -r requirements.txt
```
*Como usarlo*
```bash
  python nxgrxs_griefing.py
```

## Requisitos
- Python 3.8 o superior
- requests para realizar solicitudes HTTP
- colorama para la personalización de la consola
- nmap (instalado en el sistema)
- qubo (archivo .jar incluido en el proyecto)
