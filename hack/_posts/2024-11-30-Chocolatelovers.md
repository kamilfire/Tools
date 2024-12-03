---
layout: page
title:  "Chocolatelovers!"
date:    2024-11-30 14:14:17 -0506
categories: Pentesting
---
Corremos la maquina 

![[Pasted image 20241125164947.png]](/imagenes/Pasted%20image%2020241125164947.png)

escaneamos puertos
`nmap -p- --open -sCSV -vvv -Pn -n --min-rate 5000 172.17.0.2`  

![[Pasted image 20241125165059.png]](/imagenes/Pasted%20image%2020241125165059.png)

solo esta abierto el puerto 80 entramos en el navegador

![[Pasted image 20241125165140.png]](/imagenes/Pasted%20image%2020241125165140.png)

buscamos en codigo de la pagina

![[Pasted image 20241125165205.png]](/imagenes/Pasted%20image%2020241125165205.png)

encontramos esto muy llamativo escaneamos la ip en busca directorios y no encontramos nada asi que probamos con lo encontrado anteriormente

![[Pasted image 20241125165327.png]](/imagenes/Pasted%20image%2020241125165327.png)

encontramos un login de admin y por suerte estaba con credenciales por default admin:admin 

![[Pasted image 20241125165437.png]](/imagenes/Pasted%20image%2020241125165437.png)

navegamos por el sitio y encontramos que en la opcion plugins podemos subir cualquier archivo asi que montamos una revershell usamos la de monkey

![[Pasted image 20241125165621.png]](/imagenes/Pasted%20image%2020241125165621.png)

buscamos directorios con la nueva ip http://172.17.0.2/nibbleblog/ y encontramos varios directorios y vemos que en el directorio conten encontramos nuestro archivo de rever shell 

![[Pasted image 20241125165817.png]](/imagenes/Pasted%20image%2020241125165817.png)
![[Pasted image 20241125165837.png]](/imagenes/Pasted%20image%2020241125165837.png)

tenemos acceso y listamos los directorios con sudo -l 

![[Pasted image 20241125170121.png]](/imagenes/Pasted%20image%2020241125170121.png)

encontramos como escalar privilegios en el usuario chocolate

![[Pasted image 20241125170226.png]](/imagenes/Pasted%20image%2020241125170226.png)
![[Pasted image 20241125170307.png]](/imagenes/Pasted%20image%2020241125170307.png)

ya somos chocolate navegamos en los directorios y encontramos un script en el dir opt

![[Pasted image 20241125170408.png]](/imagenes/Pasted%20image%2020241125170408.png)

con el comando ps = faux descubrimos que el usuario root puede ejecuatar el script

![[Pasted image 20241125170614.png]](/imagenes/Pasted%20image%2020241125170614.png)

modificamos el contenido de el script con este comando `echo '<?php exec("chmod u+s /bin/bash"); ?>' > /opt/script.php` y somos root

![[Pasted image 20241125170832.png]](/imagenes/Pasted%20image%2020241125170832.png)
