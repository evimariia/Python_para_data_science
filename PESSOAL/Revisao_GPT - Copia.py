{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "ada8cf24",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "5050\n"
     ]
    }
   ],
   "source": [
    "#Escreva um programa que calcule a soma dos números de 1 a 100.\n",
    "\n",
    "soma = 0\n",
    "\n",
    "for i in range(1, 101):\n",
    "    soma += i\n",
    "    \n",
    "print(soma)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "9f2fd543",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "True\n",
      "False\n",
      "True\n",
      "True\n"
     ]
    }
   ],
   "source": [
    "#Crie uma função que receba um número como parâmetro e verifique se ele é primo.\n",
    "\n",
    "def checkPrime(number):\n",
    "    if(number % 2 != 0 or number == 2):\n",
    "        return True\n",
    "    else:\n",
    "        return False\n",
    "    \n",
    "print(checkPrime(3))\n",
    "print(checkPrime(4))\n",
    "print(checkPrime(2))\n",
    "print(checkPrime(13))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "edd8d31b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Tom\n",
      "moT\n"
     ]
    }
   ],
   "source": [
    "#Implemente uma função que inverta uma string fornecida como entrada.\n",
    "\n",
    "def inverteString(string):\n",
    "    stringInvertida = string[::-1]\n",
    "    return stringInvertida\n",
    "       \n",
    "nome = 'Tom'\n",
    "print(nome)\n",
    "\n",
    "print(inverteString(nome))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "0aeebd42",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Digite um número: 5\n",
      "O número é ímpar\n"
     ]
    }
   ],
   "source": [
    "#Escreva um programa que leia um número inteiro do usuário e imprima se ele é par ou ímpar.\n",
    "\n",
    "def verificaPar(numero):\n",
    "    if(numero % 2 == 0):\n",
    "        return True\n",
    "    else:\n",
    "        return False\n",
    "    \n",
    "num = int(input('Digite um número: '))\n",
    "if(verificaPar(num) == True):\n",
    "    print('O número é par')\n",
    "else:\n",
    "    print('O número é ímpar')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "id": "f60b9996",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[4, 10, 12, 14]\n"
     ]
    }
   ],
   "source": [
    "#Crie uma função que receba uma lista como parâmetro e retorne uma nova lista apenas com os números pares.\n",
    "\n",
    "def apenasPares(lista):\n",
    "    listaPares = []\n",
    "    \n",
    "    for i in range(len(lista)):\n",
    "        if(lista[i] % 2 == 0):\n",
    "            listaPares.append(lista[i])\n",
    "            \n",
    "    return listaPares\n",
    "\n",
    "listaCompleta = [1, 3, 4, 5, 9, 10, 11, 12, 13, 14, 15]\n",
    "print(apenasPares(listaCompleta))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "68d75d09",
   "metadata": {},
   "outputs": [],
   "source": [
    "#6"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "da7ac76a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "120\n"
     ]
    }
   ],
   "source": [
    "#Implemente uma função recursiva para calcular o fatorial de um número.\n",
    "\n",
    "def fatorial(numero):    \n",
    "    if(numero == 0 or numero == 1):\n",
    "        return 1\n",
    "    else:\n",
    "        return numero * fatorial(numero-1)\n",
    "\n",
    "print(fatorial(5))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "dc0967b9",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
