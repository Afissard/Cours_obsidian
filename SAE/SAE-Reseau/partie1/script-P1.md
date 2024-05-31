# Setup VLAN (client et DHCP)
```bash
#!/bin/bash
echo "SETUP VLAN"

# SETUP
echo "id machine :"
read idChosen
echo "ip machine :"
read ipChosen
echo "couleur interface :"
read colChosen
echo "
	\n Config :
	\n -id : $idChosen
	\n -ip : $ipChosen
	\n -color : $colChosen
	\n"

# COMMANDS
# activation prise en compte VLAN
modprobe 8021q

# lien VLAN
ip link add link "$colChosen" name "$colChosen.$idChosen" type vlan id "$idChosen"

# activation interface
ip link set up dev "$colChosen.$idChosen"

# ajout d'une ip à l'interface
ip a a "172.20.$idChosen.$ipChosen/24" dev "$colChosen.$idChosen"
```
# Setup LAN
## SMTP
```bash
#!/bin/bash
echo "SETUP LAN : SMTP"

# SETUP
echo "id machine :"
read idChosen
echo "couleur interface :"
read colChosen
echo "
	\n Config :
	\n -id : $idChosen
	\n -color : $colChosen
	\n"

# Demande au serveur DNS une ip (fourni de manière dynamique)
ipGiven = nslookup "smtp$idChosen.main$idChosen.com 192.168.0.254"
# récupération de l'ip donnée à la fin de la commande
echo "$ipGiven"

# COMMANDS
# ajout d'une ip à l'interface
ip a a "$ipGiven/24" dev "$colChosen"
# ajout des routes
ip r a "192.168.0.$idChosen/24" dev "$colChosen"
```
## Routeur
```bash
#!/bin/bash
echo "SETUP LAN : ROUTEUR"

# SETUP
echo "id machine :"
read idChosen
echo "couleur interface :"
read colChosen
echo "
	\n Config :
	\n -id : $idChosen
	\n -color : $colChosen
	\n"

# COMMANDS
# ajout d'une ip à l'interface
ip a a "192.168.0.$idChosen/24" dev "$colChosen"

# ajout des routes
# DNS
ip r a "192.168.0.254/24" dev "$colChosen"
# SMTP
echo "ip SMTP :"
read ipSMTP
ip r a "$ipSMTP/24" dev "$colChosen"
```
# Config Routeur
```bash
#!/bin/bash
echo "CONFIG ROUTEUR"

```
# Nota Bene
## Suppression d'une ip
```bash
# supression d'une ip
ip a d "$ipReseau/$ipMask$" dev "$colChosen.$idChosen"
```
## Suppression d'une route
```bash
ip r d "$ipReseau/$mask" dev "$ipDevice"
ip r d "$ipReseau/$mask" via "$ipGateAway"
```
## Supprimer la réinitialisation automatique des interfaces réseaux (mais n'a pas prouvé son utilité)
```bash
#!/bin/bash
echo "Supprimer la réinitialisation automatique des interfaces réseaux"

rm /etc/network/interfaces # supression
touch /etc/network/interfaces # création
echo "auto lo  
iface lo inet loopback  
  
allow-hotplug bleue  
iface bleue inet manual  
  
allow-hotplug jaune  
iface jaune inet manual  
  
allow-hotplug rouge  
iface rouge inet dhcp" > /etc/network/interfaces # écriture

service networking restart
service network-manager restart

echo "done"
```