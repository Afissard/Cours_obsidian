# Setup VLAN
```bash
#!/bin/bash

echo "id machine :"
read idChosen
echo "ip machine :"
read ipChosen
echo "
	\n Config :
	\n -id : $idChosen
	\n -ip : $ipChosen
	\n"

# activation prise en compte VLAN
mobprobe 8021q

# lien VLAN
ip link add link jaune name "jaune.$idChosen" type vlan id "$idChosen"

# activation interface
ip link set up dev "jaune.$idChosen"

# ajout d'une ip à l'interface
ip a a "172.20.$idChosen.$ipChosen/24" dev "jaune.$idChosen"

# NB :
# supression d'une ip
#ip a d "172.20.$idChosen.$ipChosen/24" dev "jaune.$idChosen"
```
