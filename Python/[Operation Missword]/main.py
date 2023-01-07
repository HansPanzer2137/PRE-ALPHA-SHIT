import os
import sys
import time
import timeit



def Crytp42_256(words):
    print("")


def Crypt42(words):
    wordsBuffer = list(words)
    for i in range(len(wordsBuffer)):
        match wordsBuffer[i]:
            case 'a' | 'A': wordsBuffer[i]="#/000"
            case 'b' | 'B': wordsBuffer[i]="/###0"
            case 'c' | 'C': wordsBuffer[i]="/#/#0"
            case 'd' | 'D': wordsBuffer[i]="/##00"
            case 'e' | 'E': wordsBuffer[i]="#0000"
            case 'f' | 'F': wordsBuffer[i]="##/#0"
            case 'g' | 'G': wordsBuffer[i]="//#00"
            case 'h' | 'H': wordsBuffer[i]="####0"
            case 'i' | 'I': wordsBuffer[i]="##000"
            case 'j' | 'J': wordsBuffer[i]="#///0"
            case 'k' | 'K': wordsBuffer[i]="/#/00"
            case 'l' | 'L': wordsBuffer[i]="#/##0"
            case 'm' | 'M': wordsBuffer[i]="//000"
            case 'n' | 'N': wordsBuffer[i]="/#000"
            case 'o' | 'O': wordsBuffer[i]="///00"
            case 'p' | 'P': wordsBuffer[i]="#//#0"
            case 'r' | 'R': wordsBuffer[i]="#/#00"
            case 's' | 'S': wordsBuffer[i]="###00"
            case 't' | 'T': wordsBuffer[i]="/0000"
            case 'u' | 'U': wordsBuffer[i]="##/00"
            case 'w' | 'W': wordsBuffer[i]="#//00"
            case 'y' | 'Y': wordsBuffer[i]="/#//0"
            case 'z' | 'Z': wordsBuffer[i]="//##0"
            case 'v' | 'V': wordsBuffer[i]="###/0"
            case 'x' | 'X': wordsBuffer[i]="/##/0"
            case '0': wordsBuffer[i]="/////"
            case '1': wordsBuffer[i]="#////"
            case '2': wordsBuffer[i]="##///"
            case '3': wordsBuffer[i]="###//"
            case '4': wordsBuffer[i]="####/"
            case '5': wordsBuffer[i]="#####"
            case '6': wordsBuffer[i]="/####"
            case '7': wordsBuffer[i]="//###"
            case '8': wordsBuffer[i]="///##"
            case '9': wordsBuffer[i]="////#"
            case ' ': wordsBuffer[i]="@"
        
    print("przed zmianą: "+str(words))
    print("po zmianie: "+str(''.join(wordsBuffer)))

message = "Więc jeszcze raz mówię, nic takiego nie robię. Po prostu nie ma żadnego dowodu, czy Hitler wiedział o holokauście, czy nie wiedział. Jeżeli ktoś miałby taki dowód, to jest nagroda 175 tysięcy funtów za taki dowód, niech zatem leci do Londynu i odbiera nagrodę.Takiego dowodu nie ma, a ponieważ sądy nie skazują ludzi bez dowodów, na podstawie pomówień, to niestety istnieje bardzo poważne przypuszczenie, że świętej pamięci Himmler nie raczył poinformować Hitlera o tym, że urządza holokaust, i tyle."

Crypt42(message)

            






