import os
import sys
import time
import timeit

hash = 0

def Crytp42_256(words):
    print("")


def Crypt42_encode(words):
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
    global hash
    hash = str(''.join(wordsBuffer))

def Crypt42_decode(mesHash):
	message = list(mesHash)
	messageBuff=""
	mess=[]
	lenBuff = 0
	while lenBuff < len(message): #get len of string
		if(message[lenBuff]=="#" or message[lenBuff]=="/"): #if "#" or "/"
			for kurwo in range(0, 5): # get i and 4 more chars 
				messageBuff = messageBuff+message[lenBuff+kurwo] # save it to buffer
			print("message buff: "+messageBuff) #print buffer
			match messageBuff:
				case "#/000": mess.append("a") #if buffer blah blah blah
				case "/###0": mess.append("b")
				case "/#/#0": mess.append("c")
				case "/##00": mess.append("d")
				case "#0000": mess.append("e")
				case "##/#0": mess.append("f")
				case "//#00": mess.append("g")
				case "####0": mess.append("h")
				case "##000": mess.append("i")
				case "#///0": mess.append("j")
				case "/#/00": mess.append("k")
				case "#/##0": mess.append("l")
				case "//000": mess.append("m")
				case "/#000": mess.append("n")
				case "///00": mess.append("o")
				case "#//#0": mess.append("p")
				case "#/#00": mess.append("r")
				case "###00": mess.append("s")
				case "/0000": mess.append("t")
				case "##/00": mess.append("u")
				case "#//00": mess.append("w")
				case "/#//0": mess.append("y")
				case "//##0": mess.append("z")
				case "###/0": mess.append("v")
				case "/##/0": mess.append("x")
				case "/////": mess.append("0")
				case "#////": mess.append("1")
				case "##///": mess.append("2")
				case "###//": mess.append("3")
				case "####/": mess.append("4")
				case "#####": mess.append("5")
				case "/####": mess.append("6")
				case "//###": mess.append("7")
				case "///##": mess.append("8")
				case "////#": mess.append("9")
			lenBuff+=5 # add  i+5 
		if(lenBuff>=len(message)):
			break
		if(message[lenBuff]=="@"):
			mess.append(" ")
			lenBuff+=1
		messageBuff=""
	print("decoded message: "+str(''.join(mess)))

hash = '#///0#0000/###0#/000#/000#/000@//##0/##00//##0##000#/#00///00@#//00#/#//+0#//#0##000#0000#/#00/##00#/000#/##0#/000#///0'
Crypt42_decode(hash)


# .......... - 10 znakow
#		 	- if . or ,:
#				- get i and 4 more chars:
#					-if blah blah blah change to "a"-"z" and jump to i+5 
#			- if @: change [i] on " "