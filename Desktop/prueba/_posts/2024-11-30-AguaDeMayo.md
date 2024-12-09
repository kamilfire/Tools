---
layout: post
title: "AguaDeMayo"
date: 2024-12-3
categories: [pentesting]
image: /assets/images/imagen.jpg
---


iniciamos la maquina 

![[Pasted image 20241205145712.png]](/imagenes/Pasted%20image%2020241205145712.png)

escaneamos los puerto con el comando `nmap -p- --open -sCSV -vvv -Pn -n --min-rate 5000 172.17.0.2`

![[Pasted image 20241205145840.png]](/imagenes/Pasted%20image%2020241205145840.png)

entramos en el navegador 

![[Pasted image 20241205145938.png]](/imagenes/Pasted%20image%2020241205145938.png)

analizamos el sitio web y encontramos algo interesante 

![[Pasted image 20241205150030.png]](/imagenes/Pasted%20image%2020241205150030.png)

analizamos con chatgpt y descubre que es codigo Brainfuck y deciframos el mensaje y obtenemos el mensaje ==bebeaguaqueessano==

![[Pasted image 20241205150643.png]](/imagenes/Pasted%20image%2020241205150643.png)

hacemos fuzzin web con ayuda de gobuster con el comando `gobuster dir -u "http://172.17.0.2/" -w /usr/share/dirbuster/wordlists/directory-list-2.3-medium.txt`  

![[Pasted image 20241205150849.png]](/imagenes/Pasted%20image%2020241205150849.png)

entramos en la nueva direccion 

![[Pasted image 20241205151014.png]](/imagenes/Pasted%20image%2020241205151014.png)

descargamos la imagen 

![[Pasted image 20241205151101.png]](/imagenes/Pasted%20image%2020241205151101.png)

usamos esteganografia y no conseguimos nada

![[Pasted image 20241205151632.png]](/imagenes/Pasted%20image%2020241205151632.png)

procedemos a intentar entrar mediante ssh haciendo uso del mensaje encontrado anteriormente y un usuario agua y funciona 

![[Pasted image 20241205151845.png]](/imagenes/Pasted%20image%2020241205151845.png)

listamos los servicios que se ejecutan con `sudo -l` 

![[Pasted image 20241205151942.png]](/imagenes/Pasted%20image%2020241205151942.png)

observamos que podemos ejecutar sin necesidad de una contrasena usamos `sudo /usr/bin/bettercap`

![[Pasted image 20241205152217.png]](/imagenes/Pasted%20image%2020241205152217.png)

usamos help para ver las instrusiones de uso 

![[Pasted image 20241205152423.png]](/imagenes/Pasted%20image%2020241205152423.png)

podemos ejecutar una shell con ! asi que usamos `!chmod u+s /bin/bash` 
- `chmod`: Cambia los permisos de un archivo.
- `u+s`: Indica que se debe establecer el bit setuid para el **propietario** del archivo (denotado por `u`, que significa "user" o propietario) y con `+s` se activa el bit setuid.


![[Pasted image 20241205152820.png]](/imagenes/Pasted%20image%2020241205152820.png)

salimos del bettercap usamos `bash -p` y verificamos si funciono  con el comando `whoami`

![[Pasted image 20241205153303.png]](/imagenes/Pasted%20image%2020241205153303.png)





