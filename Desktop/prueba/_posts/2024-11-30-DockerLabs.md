---
layout: post
title: DockerLabs
date: 2024-12-3
categories:
  - pentesting
image: /assets/images/imagen.jpg
---
iniciamos la maquina 

![[Pasted image 20241209144053.png]](/imagenes/Pasted%20image%2020241209144053.png)

escaneamos los puertos con nmap `nmap  -sCSV -vvv -Pn -n --min-rate 5000 172.17.0.2`

![[Pasted image 20241209144243.png]](/imagenes/Pasted%20image%2020241209144243.png)

entramos en el navegador 

![[Pasted image 20241209144559.png]](/imagenes/Pasted%20image%2020241209144559.png)

hacemos fuzzing en busca de algun directorio  `gobuster dir -u "http://172.17.0.2/" -w /usr/share/dirbuster/wordlists/directory-list-2.3-medium.txt -x html,php,txt`

![[Pasted image 20241209151435.png]](/imagenes/Pasted%20image%2020241209151435.png)

probamos las direcciones y vemos que en machine podemos subir archivos 

![[Pasted image 20241209151611.png]](/imagenes/Pasted%20image%2020241209151611.png)

intentamos subir una rever shell pero no sale un error

![[Pasted image 20241209151800.png]](/imagenes/Pasted%20image%2020241209151800.png)

buscando la forma de subir el archivo busco las exteciones mas tipicas en php y encuntro estas `php, .php2, .php3, .php4, .php5, .php6, .php7, .phps, .phps, .pht, .phtm, .phtml, .pgif, .shtml, .htaccess, .phar, .inc, .hphp, .ctp, .module` creo una txt con todas y pruebo en bursuite para encontar un formato que deje subir el archivo

![[Pasted image 20241209154208.png]](/imagenes/Pasted%20image%2020241209154208.png)

encuentro la extencion correcta y es .phar

![[Pasted image 20241209154446.png]](/imagenes/Pasted%20image%2020241209154446.png) 

verificamos que el archivo se subio correctamente 

![[Pasted image 20241209154620.png]](/imagenes/Pasted%20image%2020241209154620.png)

nos colocamos a la escucha desde la maquina atacante y ejecutamos la rever-shell 

![[Pasted image 20241209154932.png]](/imagenes/Pasted%20image%2020241209154932.png)

tenemos acceso 

![[Pasted image 20241209155335.png]](/imagenes/Pasted%20image%2020241209155335.png)

damos tratamiento de la tty `script /dev/null -c bash` luego usamos `sudo -l` para listar los servicios 

![[Pasted image 20241209155607.png]](/imagenes/Pasted%20image%2020241209155607.png)

navegando en los directorios encontramos una nota.txt 

![[Pasted image 20241209160217.png]](/imagenes/Pasted%20image%2020241209160217.png)

buscamos en gtfobins como escalar privilegios 

![[Pasted image 20241209160335.png]](/imagenes/Pasted%20image%2020241209160335.png)

seguimos los pasos encontrado en gtfobins y encontramos la contrasena del usuario root 

![[Pasted image 20241209160747.png]](/imagenes/Pasted%20image%2020241209160747.png)

al ingresar las nuevas credenciales listo somos root 

![[Pasted image 20241209161013.png]](/imagenes/Pasted%20image%2020241209161013.png)