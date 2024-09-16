#!/bin/bash

#comentario

echo 'Inciando script'

echo 'O python será instalado em sua máquina. Logo em seguida o programa será executado.'

sudo apt update
sudo apt install python3

python3 /home/lire/modulo1/calculadora/calculadora.py

echo 'Finalizando o script'
