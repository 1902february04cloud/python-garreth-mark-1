#!/usr/bin/env python3

'''
Revature is building a new API! This API contains functions for validating data, 
solving problems, and encoding data. 

The API consists of 10 functions that you must implement.

Guidelines:
1) Edit the file to match your first name and last name with the format shown.

2) Provide tests in the main method for all functions, We should be able to run
this script and see the outputs in an organized manner.

3) You can leverage the operating system if needed, however, do not use any non
legacy command that solves the problem by just calling the command.

4) We believe in self commenting code, however, provide comments to your solutions
and be organized.

5) Leverage resources online if needed, but remember, be able to back your solutions
up since you can be asked.

6) Plagiarism is a serious issue, avoid it at all costs.

7) Don't import external libraries which are not python native

8) Don't change the parameters or returns, follow the directions.

9) Assignment is optional, but totally recommend to achieve before Monday for practice.

Happy Scripting!

© 2018 Revature. All rights reserved.
'''

'''
Use the main function for testing purposes and to show me results for all functions.
'''
counter = 0

def main():
	print(reverse("This is a reversed string"))
	print(acronym("I Love Vim!"))
	print(whichTriangle(400,410,420))
	print(scrabble("cabbage"))
'''
1. Reverse a String. Example: reverse("example"); -> "elpmaxe"

Rules:
- Do NOT use built-in tools
- Reverse it your own way

param: str
return: str
'''
def reverse(string):
	print("\n1)" + string)
	counter = 0
	#Get the length of the string
	for n in string:
		counter += 1
	#print(counter)
	temp_string = ""
	decrementor = counter - 1
	#Use the length to decrement and set it equal to a temp string
	for i in range(0,counter,1):
	      # print(string[decrementor])
	       temp_string += string[decrementor]
	       decrementor -= 1
	#assign string to the temp string
	string = temp_string
	return string
		

'''
2. Convert a phrase to its acronym. Techies love their TLA (Three Letter
Acronyms)! Help generate some jargon by writing a program that converts a
long name like Portable Network Graphics to its acronym (PNG).

param: str
return: str
'''
def acronym(phrase):
	#Repeat the string parameter passed in
	print("\n2)"+ phrase)
	#Set a temporary variable
	temp_phrase = ""
	#Initialize a counter
	counter = 0
	#Set the first letter of the word to the first part
	temp_phrase += phrase[0]
	
	#Check whether white space and peek to see if there's a word after 
	#white space. If not then just continue until it finds a word.
	for i in phrase:
		if(phrase[counter] == " " and phrase[counter+1] != " "):
			temp_phrase += phrase[counter+1]
			counter+=1
			continue
		else:
			counter+=1		
	phrase = temp_phrase
	return phrase
'''
3. Determine if a triangle is equilateral, isosceles, or scalene. An
equilateral triangle has all three sides the same length. An isosceles
triangle has at least two sides the same length. (It is sometimes specified
as having exactly two sides the same length, but for the purposes of this
exercise we'll say at least two.) A scalene triangle has all sides of
different lengths.

param: float, float, float
return: str -> 'equilateral', 'isoceles', 'scalene'
'''
def whichTriangle(sideOne, sideTwo, sideThree):
	print("\n3)" +str(sideOne) + " " + str(sideTwo) + " " + str(sideThree))
	#Conditional Statement to compare the three	
	
	#set as scalene by default
	side = "scalene"
	#Equilateral
	if(sideOne == sideTwo and sideOne == sideThree):
		side = "equilateral"
	#Isoceles Side One
	if(sideOne == sideTwo):
		if(sideOne!= sideThree):
			side = "isoceles"
	elif(sideOne != sideTwo):
		if(sideOne == sideThree):
			side = "isoceles"
	else:
		side = "scalene"

	#Isoceles Side Two
	if(sideTwo == sideThree):
		if(sideTwo != sideOne):
			side = "isoceles"
	return side

'''
4. Given a word, compute the scrabble score for that word.

--Letter Values-- Letter Value A, E, I, O, U, L, N, R, S, T = 1; D, G = 2; B,
C, M, P = 3; F, H, V, W, Y = 4; K = 5; J, X = 8; Q, Z = 10; Examples
"cabbage" should be scored as worth 14 points:

3 points for C, 1 point for A, twice 3 points for B, twice 2 points for G, 1
point for E And to total:

3 + 2*1 + 2*3 + 2 + 1 = 3 + 2 + 6 + 3 = 5 + 9 = 14

param: str
return: int
'''
def scrabble(word):
	#Repeat word entered in
	print("\n4)" + word)
	
	#Initialize points to variables	
	point_one = 1
	point_two = 2
	point_three = 3
	point_four = 4
	point_five = 5
	point_eight = 8
	point_ten = 10
	score = 0
	counter = 0
	temp_word = word;
	#Change word to uppercase to avoid confusion with more if statements
	#would be better to do a dictionary because of this huge if statement
	word = word.upper()
	for i in word:
		word[counter]
		if(word[counter] == "A" or word[counter] == "E" or 
word[counter] == "I" or word[counter] == "O" or word[counter] == "U" or word[counter] == "L" or word[counter] == "N" or word[counter] == "R" or word[counter] == "S" or word[counter] == "T"):
			score += point_one
		elif(word[counter] == "G"):
			score+= point_two
		elif(word[counter] == "B" or word[counter] == "C" or word[counter] == "M" or word[counter] == "P"):
			score+= point_three
		elif(word[counter] =="F" or word[counter]=="H" or word[counter] == "V" or word[counter] =="W" or word[counter] == "Y"):
			score+= point_four
		elif(word[counter] =="K"):
			score+= point_five
		elif(word[counter] =="J" or word[counter] =="X"):
			score+= point_eight
		elif(word[counter] =="Q" or word[counter] =="Z"):
			score+= point_ten
		else:
			score+= 0;
		counter+=1

	return score;
'''
5. An Armstrong number is a number that is the sum of its own digits each
raised to the power of the number of digits.

For example:

9 is an Armstrong number, because 9 = 9^1 = 9 10 is not an Armstrong number,
because 10 != 1^2 + 0^2 = 2 153 is an Armstrong number, because: 153 = 1^3 +
5^3 + 3^3 = 1 + 125 + 27 = 153 154 is not an Armstrong number, because: 154
!= 1^3 + 5^3 + 4^3 = 1 + 125 + 64 = 190 Write some code to determine whether
a number is an Armstrong number.

param: int
return: bool
'''
#def armstrong(number):

'''
6. Compute the prime factors of a given natural number.

A prime number is only evenly divisible by itself and 1.
 
Note that 1 is not a prime number.

param: int
return: list
'''
#def primeFactors(number)

'''
7. Determine if a sentence is a pangram. A pangram (Greek: παν γράμμα, pan
gramma, "every letter") is a sentence using every letter of the alphabet at
least once. The best known English pangram is:

The quick brown fox jumps over the lazy dog.
 
The alphabet used consists of ASCII letters a to z, inclusive, and is case
insensitive. Input will not contain non-ASCII symbols.
 
param: str
return: bool
'''
#def pangram(sentence):

'''
8. Sort list of integers.
f([2,4,5,1,3,1]) = [1,1,2,3,4,5]

Rules:
- Do NOT sort it with .sort() or sorted(list) or any built-in tools.
- Sort it your own way

param: list
return: list
'''
#def sort(numbers):

'''
9. Create an implementation of the rotational cipher, also sometimes called
the Caesar cipher.

The Caesar cipher is a simple shift cipher that relies on transposing all the
letters in the alphabet using an integer key between 0 and 26. Using a key of
0 or 26 will always yield the same output due to modular arithmetic. The
letter is shifted for as many values as the value of the key.

The general notation for rotational ciphers is ROT + <key>. The most commonly
used rotational cipher is ROT13.

A ROT13 on the Latin alphabet would be as follows:

Plain: abcdefghijklmnopqrstuvwxyz Cipher: nopqrstuvwxyzabcdefghijklm It is
stronger than the Atbash cipher because it has 27 possible keys, and 25
usable keys.

Ciphertext is written out in the same formatting as the input including
spaces and punctuation.

Examples: ROT5 omg gives trl ROT0 c gives c ROT26 Cool gives Cool ROT13 The
quick brown fox jumps over the lazy dog. gives Gur dhvpx oebja sbk whzcf bire
gur ynml qbt. ROT13 Gur dhvpx oebja sbk whzcf bire gur ynml qbt. gives The
quick brown fox jumps over the lazy dog.

param: int, str
return: str
'''
#def rotate(key, string):

'''
10. Take 10 numbers as input from the user and store all the even numbers in a file called even.txt and
the odd numbers in a file called odd.txt.

param: none, from the keyboard
return: nothing
'''
#def evenAndOdds():

if __name__ == "__main__":
    main()
