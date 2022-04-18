import math

class calculate():
    def __init__(self,a,b) :
        self.a=a
        self.b=b


    def sum(self):
        print(self.a+self.b)

    def sub(self):
        print(self.a-self.b)
    
    def mul(self):
        print (self.a*self.b)

    def div(self):
        if (self.b!=0):
            print(self.a/self.b)
        else:
            print("denominator can't be zero")

    def sin(self):
       print( math.sin(self.a) )
    
    def cos(self):
       print( math.cos(self.a) )

    def tan(self):
        print ( math.tan(self.a) )

    def cot(self):
        print (1/(math.tan(self.a)))


    def sqrt(self):
        if (self.a>-1):
         print(math.sqrt (self.a))
        else:
            print("input can't be negative")
       

    def log(self):
        if (self.a>-1):
         print(math.log10 (self.a))
        else:
            print("input can't be negative")

    
    def power(self):
        if(self.b>-1):
            x=self.a
            for i in range(1,self.b):

                self.a *= x
            print (self.a)
    
    def factorial(self):
        if(self.a==0):
            print(1)
        elif(self.a>1):
            print (math.factorial(self.a))


while (1):
    print ("what do you wanna do?\n",
    "1.sum\n",
    "2.sub\n",
    "3.mul\n",
    "4.div\n",
    "5.sin\n",
    "6.cos\n",
    "7.tan\n",
    "8.cot\n"
    " 9.radical\n",
    "10.log\n",
    "11.power\n",
    "12.factorial")


    x=int(input())
    while (1):
        if(x>0 and x<=13):
            break
        else:
            print("please input number between 1_12")
            x=int(input())

   
    if x==1:
        a = int(input("a : "))
        b = int(input("b : "))
        cal=calculate(a,b)
        cal.sum()
    elif x==2:
        a = int(input("a : "))
        b = int(input("b : "))
        cal=calculate(a,b)
        cal.sub()
    elif x==3:
        a = int(input("a : "))
        b = int(input("b : "))
        cal=calculate(a,b)
        cal.mul()
    elif x==4:
        a = int(input("a : "))
        b = int(input("b : "))
        cal=calculate(a,b)
        cal.div()
    elif x==5:
        a = int(input("a : "))
        cal=calculate(a,0)
        cal.sin()
    elif x==6:
        a = int(input("a : "))
        cal=calculate(a,0)
        cal.cos()
    elif x==7:
        a = int(input("a : "))
        cal=calculate(a,0)
        cal.tan()
    elif x==8:
        a = int(input("a : "))    
        cal=calculate(a,0)
        cal.cot()
    elif x==9:
        a = int(input("a : "))
        cal=calculate(a,0)
        cal.sqrt()
    elif x==10:
        a = int(input("a : "))   
        cal=calculate(a,0)
        cal.log()
    elif x==11:
        a = int(input("a : "))
        b = int(input("b : "))
        cal=calculate(a,b)
        cal.power()
    elif x==12:
        a = int(input("a : "))   
        cal=calculate(a,0)
        cal.factorial()
    print("wanna continue ...?(Y/N)")
    x=input()
    if(x=='Y'):
        pass
    elif(x=='N'):
        print("Good Luck")
        break