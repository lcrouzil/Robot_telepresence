# Robot_téléprésence



## Description du projet

IMERIR disposait de pièces provenant d'un robot de téléprésence, ce robot a été repris par Kévin FAGOT-BARRALY en 2019. Divers ajouts avaient été opérés sur celui-ci (moteurs, controle, écran LCD, codage d'un service web). Il a été prouvé par ce prototypage que ce chassis ansi modifié était une solution technique viable.  
Nous étions en charge d'intégrer ROS au système existant afin de facilité les futures évolutions, nous avons donc apporté des améliorations d'un point de vue technique et mécanique.


## Liste de matériel utilisé

- 1 plateforme métallique  
- Rasberry PI 4B  
- Arduino mega 2560  
- 2 cartes controle moteurs L298N (pont en H)  
- 4 moteurs DC 12V  

## Cablage des moteurs

| N° PIN Arduino | Carte controle moteur | Désignation             |
|:---------------|:----------------------|:------------------------|
| 12             | Carte 1 - ENA         |                         |
| 11             | Carte 1 - IN1         | MAR roue arrière droite |
| 10             | Carte 1 - IN2         | MAV roue arrière droite |
| 9              | Carte 1 - ENB         |                         |
| 8              | Carte 1 - IN3         | MAR roue arrière gauche |
| 7              | Carte 1 - IN4         | MAV roue arrière gauche |
| 6              | Carte 2 - ENA         |                         |
| 5              | Carte 2 - IN2         | MAR roue avant gauche   |
| 4              | Carte 2 - IN1         | MAV roue avant gauche   |
| 3              | Carte 2 - ENB         |                         |
| 26             | Carte 2 - IN3         | MAV roue avant droite   |
| 24             | Carte 2 - IN4         | MAR roue avant droite   |  

![Alt text](images/carte1.png?raw=true "Carte 1")
![Alt text](images/carte2.png?raw=true "Carte 1")  
