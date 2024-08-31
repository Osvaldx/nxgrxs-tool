# Nxgrxs Griefing

## Descripción

**nxgrxs Server Tools** es una herramienta en **Python** diseñada para *obtener información de servidores de Minecraft*, realizar **escaneos de puertos** y **obtener UUIDs de jugadores de Minecraft**. La herramienta **utiliza varias APIs** para recopilar información detallada sobre el servidor, **realiza escaneos** de puertos con **nmap** y **qubo**, y permite al usuario elegir entre **múltiples opciones** desde un menú interactivo.

## Características
- **Obtener información de un servidor de Minecraft:** Se conecta a una API para obtener detalles sobre el servidor, como la versión, software, jugadores conectados, etc.
- **Escaneo de puertos:** Permite realizar escaneos de puertos personalizados utilizando nmap o qubo.
- **Obtener UUID de Minecraft:** Recupera el UUID de un jugador de Minecraft, tanto en servidores premium como en no premium.

## Opciones del Menú
- **Obtener info servidor:** Ingresa la IP del servidor de Minecraft para obtener información detallada.
[photo]
- **Escaneo con Qubo:** Realiza un escaneo de puertos utilizando Qubo, con opciones para escanear una única IP o múltiples IPs desde un archivo.
[photo]
- **Escaneo con Nmap:** Realiza un escaneo de puertos utilizando Nmap, con opciones para escanear puertos específicos de Minecraft o todos los puertos.
[photo]
- **Checkeo de puertos:** Realiza una comprobación rápida de los puertos abiertos.
[photo]
- **Obtener UUID-MC:** Recupera el UUID de un jugador de Minecraft.
[photo]

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