---
layout: page
title:  "ConsoleLog!"
date:    2024-11-30 14:14:17 -0504
categories: Pentesting
---
![[Pasted image 20241126164801.png]](/imagenes/Pasted%20image%2020241126164801.png)

usamos nmap para explorar los puertos `nmap -p- --open -sCSV -vvv -Pn -n --min-rate 5000 172.17.0.2`

![[Pasted image 20241126164937.png]](/imagenes/Pasted%20image%2020241126164937.png)

entramos en el navegador 

![[Pasted image 20241126165029.png]](/imagenes/Pasted%20image%2020241126165029.png)

listamos directorios con goubuster `gobuster dir -u "http://172.17.0.2/" -w /usr/share/dirbuster/wordlists/directory-list-2.3-medium.txt`

![[Pasted image 20241126165146.png]](/imagenes/Pasted%20image%2020241126165146.png)

navegamos en las nuevas dirreciones y encontramos un archivo server.js

![[Pasted image 20241126165348.png]](/imagenes/Pasted%20image%2020241126165348.png)

encontramos una posible contrasena 

![[Pasted image 20241126165418.png]](/imagenes/Pasted%20image%2020241126165418.png)

probmaos con hydra para encontrar un usuario `hydra -L  /usr/share/wordlists/rockyou.txt -p lapassworddebackupmaschingonadetodas  ssh://172.17.0.2:5000 -t 4

![[Pasted image 20241126165541.png]](/imagenes/Pasted%20image%2020241126165541.png)

entramos por ssh

![[Pasted image 20241126165655.png]](/imagenes/Pasted%20image%2020241126165655.png)

no tenemos permisos sudo asi que vemos en suid que permisos tenemos `find \-perm -4000 -user root 2>/dev/null`

![[Pasted image 20241126165841.png]](/imagenes/Pasted%20image%2020241126165841.png)

vemos que tenemos en la ruta passwd

![[Pasted image 20241126165932.png]](/imagenes/Pasted%20image%2020241126165932.png)

como tenemos permisos de nano modificamos el archivo passwd y eliminamos la "x" en el root con el comando `sudo nano passwd`  luego control x y ENTER 

![[Pasted image 20241126170148.png]](/imagenes/Pasted%20image%2020241126170148.png)

vemos que se modifico sin errores y probamos hacermos root  con `su root` 

![[Pasted image 20241126170243.png]](/imagenes/Pasted%20image%2020241126170243.png)

END 

