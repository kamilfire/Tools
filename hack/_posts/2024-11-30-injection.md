---
layout: post
title:  "Injection!"
date:   2024-11-30 14:14:17 -0501
categories: Pentesting
---




Reconocimiento

Realizaremos la primera fase del reconocimiento utilizando la herramienta Nmap, con los siguientes parámetros:

`sudo nmap -p- --open -sS --min-rate 5000 -vvv -n -Pn 172.17.0.2 -oG AllPorts`

Realiza un escaneo rápido y detallado de todos los puertos abiertos en la IP 172.17.0.2 y guarda los resultados en AllPorts.

![](https://noon3.gitbook.io/~gitbook/image?url=https%3A%2F%2Fprod-files-secure.s3.us-west-2.amazonaws.com%2Fe9cd33bf-9691-45b9-b9c6-a75de10eef45%2F64495610-ae30-45af-b567-38f62944ed7a%2FUntitled.png&width=768&dpr=4&quality=100&sign=d7f5f22e&sv=1)

![](https://noon3.gitbook.io/~gitbook/image?url=https%3A%2F%2F3606085230-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FPWDLdcZezaOSLXu6CIX6%252Fuploads%252FYRapHvMUeypvTU3l5SFb%252FCaptura%2520de%2520pantalla%25202024-06-22%2520110826.png%3Falt%3Dmedia%26token%3D2b5f064e-7cc5-4f6b-960d-efe5e9c3e674&width=768&dpr=4&quality=100&sign=2bcbe655&sv=1)

`sudo nmap -sC -sV -p22,80 172.17.0.2 -oN Targeted`

Usa la información del primer escaneo para ejecutar un escaneo detallado en los puertos 22 y 80, ejecutando scripts NSE y detectando versiones, guardando los resultados en un archivo de formato normal: Targeted.

![](https://noon3.gitbook.io/~gitbook/image?url=https%3A%2F%2F3606085230-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FPWDLdcZezaOSLXu6CIX6%252Fuploads%252FoUWMRt0CdyUmqfef7fyR%252FCaptura%2520de%2520pantalla%25202024-06-22%2520110839.png%3Falt%3Dmedia%26token%3D695a710e-c2df-4abc-9125-a6835a6634b6&width=768&dpr=4&quality=100&sign=9b2bd790&sv=1)

El escaneo de Nmap revela que el host `172.17.0.2` tiene dos puertos abiertos:

- **Puerto 22** (SSH) ejecutando OpenSSH 8.9p1 en Ubuntu.
    
- **Puerto 80** (HTTP) ejecutando Apache httpd 2.4.52 en Ubuntu con una página de inicio de sesión y ciertas configuraciones de cookies no seguras.
    

Esta información es útil para evaluar la seguridad y configuración de los servicios expuestos por el host.

Realizaremos un análisis con WhatWeb, una herramienta de línea de comandos para identificar todas las tecnologías que están funcionando en el servicio HTTP expuesto, que corre en el puerto 80.

![](https://noon3.gitbook.io/~gitbook/image?url=https%3A%2F%2F3606085230-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FPWDLdcZezaOSLXu6CIX6%252Fuploads%252Fbb1xHqUWRzsAsIFzLX1o%252FCaptura%2520de%2520pantalla%25202024-06-22%2520111237.png%3Falt%3Dmedia%26token%3De2baf3ac-57f0-4916-b1d7-d84b63454948&width=768&dpr=4&quality=100&sign=900c4cc&sv=1)

![](https://noon3.gitbook.io/~gitbook/image?url=https%3A%2F%2F3606085230-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FPWDLdcZezaOSLXu6CIX6%252Fuploads%252FGSozOBlDQft9vDQglHQY%252FCaptura%2520de%2520pantalla%25202024-06-22%2520112224.png%3Falt%3Dmedia%26token%3Ddc2c1efa-ae98-4e1a-a9f5-8739307b2eee&width=768&dpr=4&quality=100&sign=90d1da09&sv=1)

Hemos encontrado un panel de inicio de sesión. Actualmente, no podemos acceder ya que no contamos con credenciales válidas. Hemos probado algunas combinaciones como admin:admin y admin:password, pero sin éxito.

Usaremos la herramienta Gobuster para hacer fuerza bruta en los directorios. De este modo, podremos encontrar posibles rutas o vectores de entrada.

`gobuster dir -u` [`http://172.17.0.2`](http://172.17.0.2) `-w /usr/share/seclists/Discovery/Web-Content/directory-list-lowercase-2.3-medium.txt -x php,html,txt -t 200`

![](https://noon3.gitbook.io/~gitbook/image?url=https%3A%2F%2F3606085230-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FPWDLdcZezaOSLXu6CIX6%252Fuploads%252FpkkoTlKqL6MK9cG2FSgQ%252FCaptura%2520de%2520pantalla%25202024-06-22%2520114207.png%3Falt%3Dmedia%26token%3De05b7139-1f3f-42ad-8431-8add1b9503ea&width=768&dpr=4&quality=100&sign=e0c53407&sv=1)

Hemos encontrado una ruta /config.php que nos devuelve un código de estado 200. Al revisarla, solo encontramos una página en blanco sin nada en el código fuente.

Regresamos al panel de inicio de sesión e intentamos forzar una inyección SQL.

![](https://noon3.gitbook.io/~gitbook/image?url=https%3A%2F%2F3606085230-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FPWDLdcZezaOSLXu6CIX6%252Fuploads%252F3KvI6FxRqtnDu3DsVLrn%252FCaptura%2520de%2520pantalla%25202024-06-22%2520114628.png%3Falt%3Dmedia%26token%3D63955e1f-b6ba-4028-9474-3eb8ec380a7e&width=768&dpr=4&quality=100&sign=dc97caaf&sv=1)

Al intentar ingresar con una comilla simple (`'`) en el campo de nombre de usuario, recibí un error relacionado con la base de datos.



¿Qué Significa Este Error?

El hecho de que una comilla simple (`'`) cause un error indica una posible **vulnerabilidad de inyección SQL**. Este tipo de vulnerabilidad ocurre cuando una aplicación web no valida correctamente la entrada del usuario, permitiendo que fragmentos de código SQL maliciosos se inserten en las consultas de la base de datos.


¿Por Qué Sucede?

Cuando se introduce una comilla simple sin escapar, puede interrumpir la sintaxis de la consulta SQL, causando un error.



Explotación

Vamos a ejecutar y habilitar el proxy de Burp Suite para capturar la petición. De esta manera, podremos utilizar la herramienta SQLmap para automatizar el ataque.

![](https://noon3.gitbook.io/~gitbook/image?url=https%3A%2F%2F3606085230-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FPWDLdcZezaOSLXu6CIX6%252Fuploads%252Fk2VD3XvMgPNr6nq2zxCG%252FCaptura%2520de%2520pantalla%25202024-06-22%2520115415.png%3Falt%3Dmedia%26token%3Deb6db499-6d47-47f0-85bc-c2bdf1ccf0d1&width=768&dpr=4&quality=100&sign=10ca2ee1&sv=1)

Capturamos la solicitud generada por el método POST en el endpoint `/index.php`. Esta solicitud será utilizada con la herramienta SQLmap para automatizar el ataque.

![](https://noon3.gitbook.io/~gitbook/image?url=https%3A%2F%2F3606085230-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FPWDLdcZezaOSLXu6CIX6%252Fuploads%252FBK45Hu14nOQovcaAJ9UX%252FCaptura%2520de%2520pantalla%25202024-06-22%2520120218.png%3Falt%3Dmedia%26token%3D1f55b486-0664-44d3-bb69-98be2cb9c2f6&width=768&dpr=4&quality=100&sign=ea12df23&sv=1)

![](https://noon3.gitbook.io/~gitbook/image?url=https%3A%2F%2F3606085230-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FPWDLdcZezaOSLXu6CIX6%252Fuploads%252FRaKhMRR0JIMdskaRZwai%252FCaptura%2520de%2520pantalla%25202024-06-22%2520120305.png%3Falt%3Dmedia%26token%3Dc9a7ca8d-9e5e-442b-a47d-7a536cbdedac&width=768&dpr=4&quality=100&sign=66480913&sv=1)

Hemos logrado extraer las tablas que contienen un nombre de usuario: `dylan` y una contraseña.

![](https://noon3.gitbook.io/~gitbook/image?url=https%3A%2F%2F3606085230-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FPWDLdcZezaOSLXu6CIX6%252Fuploads%252F1QB1yWFyo7OzAFBstFun%252FCaptura%2520de%2520pantalla%25202024-06-22%2520120536.png%3Falt%3Dmedia%26token%3D678b57c6-67d6-4159-8983-df93b69b8064&width=768&dpr=4&quality=100&sign=6ad9b2f3&sv=1)

La contraseña que encontramos también funciona con el servicio SSH expuesto en el puerto 22. Esto indica una reutilización de credenciales, lo que nos ha permitido ganar acceso a la máquina como el usuario Dylan.

![](https://noon3.gitbook.io/~gitbook/image?url=https%3A%2F%2F3606085230-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FPWDLdcZezaOSLXu6CIX6%252Fuploads%252F2HKyexD4I8jhhRg2mQKB%252FCaptura%2520de%2520pantalla%25202024-06-22%2520120845.png%3Falt%3Dmedia%26token%3D52872d29-8460-45cd-a2e5-c72ebc0c574f&width=768&dpr=4&quality=100&sign=35b8cfde&sv=1)

Al ejecutar el comando `sudo -l`, nos damos cuenta de que `sudo` no está disponible como comando. Por lo tanto, vamos a verificar los permisos SUID en busca de binarios que podamos aprovechar para escalar privilegios.

![](https://noon3.gitbook.io/~gitbook/image?url=https%3A%2F%2F3606085230-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FPWDLdcZezaOSLXu6CIX6%252Fuploads%252FTjSUfIp6ALuhUkHhGvL3%252FCaptura%2520de%2520pantalla%25202024-06-22%2520122244.png%3Falt%3Dmedia%26token%3D33f87959-629c-4374-be1a-b88c873e3e91&width=768&dpr=4&quality=100&sign=64e2a7fa&sv=1)


Escalada de Privilegios

El binario /usr/bin/env es una herramienta en Unix y Linux que se utiliza para ejecutar un programa en un entorno modificado. Si el binario /usr/bin/env tiene el bit SUID (Set User ID) activado, se ejecuta con los privilegios del propietario del archivo (generalmente root) en lugar del usuario que lo ejecuta. Cuando se ejecuta /usr/bin/env /bin/bash, si env tiene permisos SUID de root, el comando bash se ejecutará con privilegios de root, lo que permite al usuario escalar sus privilegios.

Vamos a consultar nuestra fuente en [GTFOBins](https://gtfobins.github.io/gtfobins/env/), que nos indica cómo podemos escalar privilegios explotando el binario `env`.

![](https://noon3.gitbook.io/~gitbook/image?url=https%3A%2F%2F3606085230-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FPWDLdcZezaOSLXu6CIX6%252Fuploads%252FR7DaVtYDmBRwl9wADeqm%252FCaptura%2520de%2520pantalla%25202024-06-22%2520124057.png%3Falt%3Dmedia%26token%3De194dcef-d206-4228-be77-f29f8bed242b&width=768&dpr=4&quality=100&sign=a38c7a63&sv=1)

![](https://noon3.gitbook.io/~gitbook/image?url=https%3A%2F%2F3606085230-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FPWDLdcZezaOSLXu6CIX6%252Fuploads%252FcbSFKKp5zYSm7eGsNApZ%252FCaptura%2520de%2520pantalla%25202024-06-22%2520122503.png%3Falt%3Dmedia%26token%3Dda9af4ca-ef54-4a11-b07a-8750c238c38e&width=768&dpr=4&quality=100&sign=9e46ff8e&sv=1)

