---
layout: page
title:  "Borazuwarahctf!"
date:    2024-11-30 14:14:17 -0510
categories: Pentesting
---

ejecutamos la maquina docker con los comandos

sudo bash auto_deploy.sh borazuwarahctf.tar

![[Pasted image 20241121111116.png]](/imagenes/Pasted%20image%2020241121111116.png)



escaneamos la ip de la maquina usando namp 
 nmap -p- --open -sCVS -vvv -Pn -n --min-rate 5000 172.17.0.2    

![[Pasted image 20241121105658.png]](/imagenes/Pasted%20image%2020241121105658.png)

encontramos los puertos 22 para ssh y 80 para http abiertos

entramos en el navegador con la direccion ip 172.17.0.2

![[Pasted image 20241121105825.png]](/imagenes/Pasted%20image%2020241121105825.png)

inspections de la pagina web encontramos un archivo imagen 

![[Pasted image 20241121105944.png]](/imagenes/Pasted%20image%2020241121105944.png)

la descargamos y aplicamos esenografia para ver que informacion valiosa podemos encontrar

![[Pasted image 20241121110059.png]](/imagenes/Pasted%20image%2020241121110059.png)

vemos que encontramos un posible usuario "borazuwarah"

![[Pasted image 20241121110154.png]](/imagenes/Pasted%20image%20202411211100154.png)

encontramos un archivo secreto.txt lo leemos 

![[Pasted image 20241121110252.png]](/imagenes/Pasted%20image%2020241121110252.png)

no encontramos nada asi que ya teniendo un posible usuario haremos fuerza bruta usando hydra para encontrar alguna contrasena

![[Pasted image 20241121110349.png]](/imagenes/Pasted%20image%2020241121110349.png)

encontramos una contrasena 123456 que usaremos para loguearnos mediante ssh

![[Pasted image 20241121110549.png]](/imagenes/Pasted%20image%2020241121110549.png)

listamos los directorios a los que podemos acceder con el comando `sudo-l`

![[Pasted image 20241121110657.png]](/imagenes/Pasted%20image%2020241121110657.png)

vemos que podemos acceder a la ruta /bin/bash sin necesidad de una contrasena  nos hacemos root solo usando sudo mas la ruta 

![[Pasted image 20241121110820.png]](/imagenes/Pasted%20image%2020241121110820.png)

listo somos root 
