

import sys
import argparse


sys.stderr.write('test  :  txt file where output is stored')
lis =[]
up=1
def  banner():
    print("""
      _______    _____    
     | ____  |  /  ____\                      _____     ____   _____
     | |  / /  / /    // ____  *  ____   /|  (     )   /      |     |
     |_/_/ /  | |____// /      | /      / |  |     |  /       |
     | |\ \   | |----/  \____  | \____    |  |     | (        |--|
     | | \ \   \ \____       \ |      \   |  |     |  \       |
     |_|  \_\   \_____|  ____/ |  ____/  _|__(_____)   \_____ |_____|


     """ )
def parser():
    parser=argparse.ArgumentParser()
    parser.add_argument('num',help="place the username ", type=str)
    parser.add_argument("-o","--output",help="Output result in a file", nargs='?', default=False)
    parser.add_argument('-l','--left',help="String that you want to keep in left ",default="")
    parser.add_argument('-r','--right',help="String that you want to keep at right", type=str,default="" )
    parser.add_argument('-i','--instead',help=" character that you want to replace with some other  character in string keeping others same",nargs=2 , type=str,default="")
    parser.add_argument('-nt','--no_num',help="put n switch if you dont want to keep date ",nargs='?' , type=str,default=True)
    return parser.parse_args()
    

def Date():
         m=[]
         b=['@','#','*','^']
         v=['123','789','159','357','456','1990','1991','1992','1993','1994','1995','1996','1997','1998','1999','2000']
         for i in lis:
            for z  in b :
               for x in v:
                   m+=[str(i+z+x)]
         return(m)
     
 
def gene(name,letter,x,new_name):
  
  global lis  
   
  if len(name)==0:
            new_name=new_name+x
            lis+=[new_name]
            
  else:
        c = name[0]
        new_name=new_name+x
        if c not in letter.keys():
            if up==2:
                gene(name[1:],letter,c.lower(),new_name)
            else:
               gene(name[1:],letter,c,new_name)
                
        else:
          for j in letter[c]:            
            gene(name[1:],letter,j,new_name)
            
 
def main(num,output,right,left,instead,nt):   
         x=""         
         new_name=""
         result=[];
         letter = {'a':['@','A','4','a'],'s':['S','$','5'],'b':['b','B','8'],'c':['c','C'],'d':['D','d','9','o','O','6'],'e':['3','E','e'],'f':['F','f','7'],
                   'g':['9','G','g','5','4','p'],'h':['H','h'],'i':['i','I','1','7'],
                   'j':['J','j','7'],'k':['k','k','x'],'l':['L','l'],'m':['M','m'],'n':['n','N'],'o':['O','o','0','8','d','q','Q'],
                   'p':['P','p','9','7'],'q':['Q','q'],'r':['R','r'],
                   't':['t','T','7'],'u':['U','u','v','V'],'v':['v','V'],'w':['W','w'],'x':['X','x','*','+'],'y':['Y','y'],'z':['Z','z']}
       


        
         if instead:
                 global up
                 k=num.index(args.instead[0])
                 num=list(num)                 
                 if (args.instead[1].islower())==True:
                     up = 2
                 num[k]=args.instead[1].upper()
                 num=''.join(num)
                 
                 gene(num,letter,x,new_name)
                 if nt==True: 
                  m=Date()
                           
                  with open('test.txt','w') as lp :
                     for i in m:
                        print(str(left)+str(i)+str(right))   
                        lp.write(str(left)+str(i)+str(right)+"\n")

                 else: 
                
                  with open('test.txt','w') as lp :
                   for i in lis:
                     print(str(left)+str(i)+str(right))   
                     lp.write(str(left)+str(i)+str(right)+"\n")
                 
         else:
                gene(name,letter,x,new_name)
                print( "up")
                if nt==True: 
                  m=Date()

                  with open('test.txt','w') as lp :
                     for i in m:
                        print(str(left)+str(i)+str(right))   
                        lp.write(str(left)+str(i)+str(right)+"\n")   
                         
                
                else:
                 with open('test.txt','w') as lp :
                     for i in lis:
                        print(str(left)+str(i)+str(right))   
                        lp.write(str(left)+str(i)+str(right)+"\n")                   

            
                      
         up=0
         banner()

if __name__=='__main__':
  banner()
  args=parser()  
  name=args.num.lower()  
  output=args.output
  right=args.right
  left=args.left
  instead=args.instead
  nt=args.no_num
  
  
  main(name,output,right,left,instead,nt)
    

      
