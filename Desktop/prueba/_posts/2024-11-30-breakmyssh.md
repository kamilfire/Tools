---
layout: post
title: "BreakMySsh"
date: 2024-12-3
categories: [pentesting]
image: /assets/images/imagen.jpg
---
iniciamos las maquina 

![[Pasted image 20241121152326.png]](/imagenes/Pasted%20image%2020241121152326.png)

 escaneamos la ip en busca de puertos abiertos 
 
 ![[Pasted image 20241121152402.png]](/imagenes/Pasted%20image%2020241121152402.png)
 
encontramos abierto el puerto 22 donde corre ssh en su version openssh 7.7 usamos searchsploit  para encontrar alguna vulneravilidad

![[Pasted image 20241121152544.png]](/imagenes/Pasted%20image%2020241121152544.png)

luego usamos metasploit para usar el sploit user enumeration buscamos en chatgpt cuales son los paramateros necesarios

![[Pasted image 20241121152737.png]](/imagenes/Pasted%20image%2020241121152737.png)

 uso una lista de usuarios de seclist 
 
 ![[Pasted image 20241121152859.png]](/imagenes/Pasted%20image%2020241121152859.png)
 
 y encontramos una lista de usuarios
 
 ![[Pasted image 20241121152932.png]](/imagenes/Pasted%20image%2020241121152932.png)
 
 salimos de mfsconsole y usamos hydra para encontrar una posible contrasena 
 
 ![[Pasted image 20241121153040.png]](/imagenes/Pasted%20image%2020241121153040.png)
 
 encontramos la contrasena para el usuario root 

y entramos por ssh y ya somos root 

![[Pasted image 20241121153150.png]](/imagenes/Pasted%20image%2020241121153150.png)
