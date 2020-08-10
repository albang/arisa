# Arisa Arcade soundboard for raspberry pi


## But du projet:

Utiliser un stick d'arcade  + bouton pour faire une boite à son avec un raspberry pi.
Il a pour but d'être utilisé sans écran dans une boite en contreplaqué / MDF

# Conception:
To do : Modele 3d


## Matos

Joystick + boutons: https://www.amazon.fr/gp/product/B075DFNK24/ ou assimilé
un ordi avec python3

## Disposition des boutons:
 * https://www.slagcoin.com/joystick/layout.html

## Coté logiciel :

    * Une raspbian des familles 

# Dépendance

```sh
apt-get install mpg123 et mpg321

pip3 install pygames
pip3 install pexpect
pip3 install mpyg321
```
# Compatibilité :


Le code est compatible avec linux 
cependant il peut être utilisé sous windows en bidouillant un peu
la lib mpyg321 utilise pexpect qui n'est pas équivalent sous linux et  windows

cette lib dans le projet permet de mettre pause sur un son (usecase pratique pour une histoire par exemple)


# Lancer le programme 
```sh
cd src
python3 ./arisa.py
```


# Ressources et remerciements
TTS pour les directions :

   * https://ttsmp3.com/

Merci à https://histoiresdouces.fr pour les histoires
et à https://lasonotheque.org/ pour les bruitages

