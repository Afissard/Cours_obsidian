# 1 préliminaire
## Qu'est-ce qu'une table de partition ?
Une partition de disque est le "découpage" du disque où sont répartie les différentes sections nécessaires à l'OS (fichier système (sys), root, utilisateur (usr), etc)
(Wikipedia : https://fr.wikipedia.org/wiki/Partition_(informatique))
En informatique, une **partition**, **région** ou un **disque** est une section d'un support de stockage (disque dur, SSD, carte-mémoire ...). Le partitionnement est l'opération qui consiste à diviser ce support en partitions dans lesquelles le système d'exploitation peut gérer les informations de manière séparée, généralement en y créant un système de fichiers, une manière d’organiser l’espace disponible.
## Quelles sont les différences entre des tables de partitions GPT et MBR ?
(Microsoft : https://learn.microsoft.com/fr-fr/windows-server/storage/disk-management/change-a-gpt-disk-into-an-mbr-disk)
Les disques d'enregistrement de démarrage principal (**MBR**) utilisent la table de partition BIOS standard. Les disques de table de partition GUID (**GPT**) utilisent l'interface UEFI (Unified Extensible Firmware Interface). Les disques **MBR** ne prennent pas en charge plus de quatre partitions par disque.
# 2 Installation Linux
## Qu’est ce qu’un système de fichiers ? 
(wikipedia : https://fr.wikipedia.org/wiki/Syst%C3%A8me_de_fichiers)
Soit l'organisation hiérarchique des fichiers au sein d'un système d'exploitation (on parle par exemple du file system d'une machine unix organisé à partir de sa racine (**/**))
Soit l'organisation des fichiers au sein d'un volume physique ou logique, qui peut être de différents types (par exemple NTFS, FAT, FAT32, ext2fs, ext3fs, ext4fs, zfs, btrfs, etc), et qui a également une racine mais peut en avoir plusieurs
## Qu’est ce qu’un système de fichiers journalisé ? 
(wikipedia : https://fr.wikipedia.org/wiki/Syst%C3%A8me_de_fichiers_journalis%C3%A9)
Le système de fichiers journalisés est un système de fichiers tolérant/résistant aux pannes qui permet d'assurer l'intégrité des données en cas de problème matériel, de panne de courant (ou Hot-swap / débranchement à chaud) ou d'arrêt brutal du système. Cette fonctionnalité est assurée par la tenue d'un Journal (système de fichiers) référençant les opérations d'écriture sur le support physique avant que ce dernier ne soit réellement mis à jour. Le système de fichiers doit permettre une reprise d'activité à la suite d'une coupure brutale, telle un arrêt électrique. Les métadonnées doivent alors rester cohérentes et à jour. La journalisation permet d'optimiser le contrôle d'intégrité du système de fichiers, réduisant ainsi le temps de redémarrage du système, critère important dans les environnements qui ont besoin d'une haute disponibilité.
## Quels points de montage avez vous choisi ? 
La racine : "/"
Données personnelles : "/home"
## À quoi sert le swap ?
(redhat : https://access.redhat.com/documentation/fr-fr/red_hat_enterprise_linux/7/html/storage_administration_guide/ch-swapspace)
L'espace swap sur Linux est utilisé lorsque la mémoire physique (RAM) est pleine. Si le système a besoin de plus de ressources mémoire et que la mémoire RAM est pleine, les pages mémoire inactives sont alors déplacées vers l'espace swap.