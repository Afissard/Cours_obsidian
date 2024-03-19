# Découpage en sous-réseaux 
Dans chacun des cas ci-dessous, exprimez les plages d'adresses IP des sous-réseaux lorsque cela est possible. 
Calculez le masque CIDR, le masque décimal. Identifiez l'incrément puis les identificateurs de sous-réseau. Finalement, exprimez les plages de chaque sous-réseau ainsi que l'adresse de diffusion associée pour le sous-réseau. 
## a
220.100.80/24 avec 4 réseaux logiques et 10 hôtes par réseau 
````
220.100.80.0 (dec)
DC.64.50.00 (hex)
1101 1100.0110 0100.0101 0000.|0000 0000 (bin)
4 sous réseaux : 
1101 1100.0110 0100.0101 0000.|00|00 0000
1101 1100.0110 0100.0101 0000.|01|00 0000
1101 1100.0110 0100.0101 0000.|10|00 0000
1101 1100.0110 0100.0101 0000.|11|00 0000
````
## b 
172.18/16 avec 10 réseaux logiques et 500 hôtes par réseau
## c 
10/8 avec 20 réseaux logiques et 1000 hôtes par réseau 
## d 
10.160/13 avec 60 réseaux logiques et 500 hôtes par réseau 
## e 
10.163.128/19 avec 6 réseaux logiques et 200 hôtes par réseau 
## f
20/9 avec 15 000 réseaux logiques et 500 hôtes par réseau
````
20 ...
````
## g 
120/8 avec 100 000 réseaux logiques et 100 hôtes par réseau