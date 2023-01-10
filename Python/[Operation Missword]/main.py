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
			case 'a' | 'A': wordsBuffer[i]="#/00000"
			case 'b' | 'B': wordsBuffer[i]="/###000"
			case 'c' | 'C': wordsBuffer[i]="/#/#000"
			case 'd' | 'D': wordsBuffer[i]="/##0000"
			case 'e' | 'E': wordsBuffer[i]="#000000"
			case 'f' | 'F': wordsBuffer[i]="##/#000"
			case 'g' | 'G': wordsBuffer[i]="//#0000"
			case 'h' | 'H': wordsBuffer[i]="####000"
			case 'i' | 'I': wordsBuffer[i]="##00000"
			case 'j' | 'J': wordsBuffer[i]="#///000"
			case 'k' | 'K': wordsBuffer[i]="/#/0000"
			case 'l' | 'L': wordsBuffer[i]="#/##000"
			case 'm' | 'M': wordsBuffer[i]="//00000"
			case 'n' | 'N': wordsBuffer[i]="/#00000"
			case 'o' | 'O': wordsBuffer[i]="///0000"
			case 'p' | 'P': wordsBuffer[i]="#//#000"
			case 'r' | 'R': wordsBuffer[i]="#/#0000"
			case 's' | 'S': wordsBuffer[i]="###0000"
			case 't' | 'T': wordsBuffer[i]="/000000"
			case 'u' | 'U': wordsBuffer[i]="##/0000"
			case 'w' | 'W': wordsBuffer[i]="#//0000"
			case 'y' | 'Y': wordsBuffer[i]="/#//000"
			case 'z' | 'Z': wordsBuffer[i]="//##000"
			case 'v' | 'V': wordsBuffer[i]="###/000"
			case 'x' | 'X': wordsBuffer[i]="/##/000"
			case '0': wordsBuffer[i]="/////00"
			case '1': wordsBuffer[i]="#////00"
			case '2': wordsBuffer[i]="##///00"
			case '3': wordsBuffer[i]="###//00"
			case '4': wordsBuffer[i]="####/00"
			case '5': wordsBuffer[i]="#####00"
			case '6': wordsBuffer[i]="/####00"
			case '7': wordsBuffer[i]="//###00"
			case '8': wordsBuffer[i]="///##00"
			case '9': wordsBuffer[i]="////#00"
			case ':': wordsBuffer[i]="#######"
			case '.': wordsBuffer[i]="///////"
			case ',': wordsBuffer[i]="//////0"
			case '/': wordsBuffer[i]="######0"
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
			for kurwo in range(0, 7): # get i and 4 more chars 
				messageBuff = messageBuff+message[lenBuff+kurwo] # save it to buffer
			print("message buff: "+messageBuff) #print buffer
			match messageBuff:
				case "#/00000": mess.append("a") #if buffer blah blah blah
				case "/###000": mess.append("b")
				case "/#/#000": mess.append("c")
				case "/##0000": mess.append("d")
				case "#000000": mess.append("e")
				case "##/#000": mess.append("f")
				case "//#0000": mess.append("g")
				case "####000": mess.append("h")
				case "##00000": mess.append("i")
				case "#///000": mess.append("j")
				case "/#/0000": mess.append("k")
				case "#/##000": mess.append("l")
				case "//00000": mess.append("m")
				case "/#00000": mess.append("n")
				case "///0000": mess.append("o")
				case "#//#000": mess.append("p")
				case "#/#0000": mess.append("r")
				case "###0000": mess.append("s")
				case "/000000": mess.append("t")
				case "##/0000": mess.append("u")
				case "#//0000": mess.append("w")
				case "/#//000": mess.append("y")
				case "//##000": mess.append("z")
				case "###/000": mess.append("v")
				case "/##/000": mess.append("x")
				case "/////00": mess.append("0")
				case "#////00": mess.append("1")
				case "##///00": mess.append("2")
				case "###//00": mess.append("3")
				case "####/00": mess.append("4")
				case "#####00": mess.append("5")
				case "/####00": mess.append("6")
				case "//###00": mess.append("7")
				case "///##00": mess.append("8")
				case "////#00": mess.append("9")
				case "#######": mess.append(":")
				case "///////": mess.append(".")
				case "//////0": mess.append(",")
				case "######0": mess.append("/")
			lenBuff+=7 # add  i+5 
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