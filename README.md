# password
finds your password if it is based on your name


---------------How I got This idea----------------
I got this idea. when i started learn bug hunting. one day , i found glitch in my collge site.
I thought to bruteforce it with my regular password file :) basically.. passwords from  haddix sir repositary #seclist.
some where in my mind .. 
I Was knowing that i will not get the match..
I thought that  since domain is registered with the vc's name . I might get password match only  with his name.
so i scripted this on  python 3 . 
suppose name is gumla..  so these could be the  passwords

Eg: Gumla
    gum7@
    guml4
    gumla@123 etc
    
   This way i  started to build up this script..
--------------------------------------------+++++++++++++++++++++++++------------------------------------
This script is provided with 5 flags for the aggressively generating password.
I had took gumla as the keyword for password generation.
OPen the cmd where pasw.py is kept.
type :
* python pasw.py gumla
![](image/a.jpeg)

* python pasw.py gumla -nt 
      if you don't want to keep Date in password , add -nt flag like below
![](image/b.jpeg)


* python pasw.py gumla  -nt -l DD
      If you want to put some character in left than add with -l flag
![](image/c.jpeg)

* python pasw.py gumla -nt -r l
          If you want to keep any character in right .. than fllow that character with -r flag


![](image/d.jpeg)

* python pasw.py gumla -i g o 
This is quite interesting  for me  to wite code for it..
instead flag -i 
it will replace g character in gumla  with o



![](image/e.jpeg)

* python pasw.py gumla -nt -i g o
same thing..  nt flag with instead flag will also work.

A test file will be created , where all password will bw saved 
* there is 2 symbol which this script could get as the argument :  "<" , ">"  


I also had included some password txt file..
thank u
