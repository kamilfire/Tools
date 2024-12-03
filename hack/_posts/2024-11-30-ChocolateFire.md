---
layout: page
title:  "ChocolateFire!"
date:    2024-11-30 14:14:17 -0507
categories: Pentesting
---
Corremos la maquina y escaneamos los puertos


`nmap -p- --open -sS -sC -sV --min-rate=5000 -vvv -n -Pn   172.17.0.2` 

![[Pasted image 20241124154027.png]](/imagenes/Pasted%20image%2020241124154027.png)

encuentro un login en el puerto 9090

![[Pasted image 20241124154102.png]](/imagenes/Pasted%20image%2020241124154102.png)

 uso burpsuite para encntrar las credenciales 
 
![[Pasted image 20241124154158.png]](/imagenes/Pasted%20image%2020241124154158.png)

 encuentro las credenciales admin:admin 
 
![[Pasted image 20241124154247.png]](/imagenes/Pasted%20image%2020241124154247.png)
![[Pasted image 20241124154325.png]](/imagenes/Pasted%20image%2020241124154325.png)

navegamos por el sitio y vemos algo interesante que es la version del server openfire buscamos en metasploit si existe algun sploit para este

![[Pasted image 20241124154511.png]](/imagenes/Pasted%20image%2020241124154511.png)

usamos show options para ver y modificar los parametros necesarios 

![[Pasted image 20241124154624.png]](/imagenes/Pasted%20image%2020241124154624.png)

cambiamos los valores necesarios

![[Pasted image 20241124154729.png]](/imagenes/Pasted%20image%2020241124154729.png)
![[Pasted image 20241124154758.png]](/imagenes/Pasted%20image%2020241124154758.png)

y conseguimos ser root

![[Pasted image 20241124154955.png]](/imagenes/Pasted%20image%2020241124154955.png)
