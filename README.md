# password
finds your password if it is based in your name


---------------How I got This idea----------------
I got this idea. when i started learn bug hunting. one day , i found glitch in my collge site.
I thought to bruteforce it with my regular password file :) basically.. passwords from  haddix sir repositary #seclist.
some where in my mind .. 
I Was knowing that i will not get the match..
I thought since domain is regestred with the vc's name . I might get password match  with his name only.

Eg: Gumla
    gum7@
    guml4
    gumla@123 etc
    
   This way i  started to build up this script..
--------------------------------------------+++++++++++++++++++++++++------------------------------------
This script is provided with 5 flags for the aggresively generating password.
I had took gumla as the keyword for password generation.
OPen the cmd where pasw.py is kept.
type :
* python pasw.py gumla

* python pasw.py gumla -nt 
if you don't want to keep Date in password , add -nt flag like above


* python pasw.py gumla  -nt -l DD
If you want to put something in left than add with -l flag

* python pasw.py gumla -nt -r l
If you want to keep any character in right .. than fllow that character with -r flag

* python pasw.py gumla -i g o
This is quite interesting  for me  to wite code for it..
instead flag -i 
it will replace g character in gumla  with o

* python pasw.py gumla -nt -i g o
same thing..  nt flag with instead flag will also work.

A test file will be created , where all password will bw saved 
* there is 2 symbol which this script could get as the argument :  "<" , ">"  
