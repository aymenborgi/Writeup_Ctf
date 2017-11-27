#This is a quick and dirty writeup 
Hi,
The given file (unknown) is an ELF 64-bit LSB executable stripped .
A binary without anti-debug tricks or obfuscation .

unknown is an executable. When we run it, it returns 'Try again.'

I imported the binary file into IDAPro 
then, with a top-down looking at the assembly code i noticed that the binary takes and input as an argument and when when we give it
an argument it returns 'Still nope.'

To find the flag we have to find the correct input .

Our assembly code show us these things :
1- len(input) == 56
2-there is a loop that encrypt our characters and  check each of it with 56 encrypted character, if encrypt(input[i]) !=encrypt(flag[i]): mov     cs:dword_603084, 1
3- if(dword_603084 ==1): failed

it can be quicky solved by a brute force attack . check my python script :)





