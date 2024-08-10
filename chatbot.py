while True:
            from datetime import datetime
            now = datetime.now()
            time = now.strftime("%H:%M:%S")
            if  time<'12:00:00':
                    print("Good morning ")
            elif time=='12:00:00':
                    print("Good afternoon ")
            elif time<'17:00:00':
                    print("Good afternoon ")
            elif time<'18:00:00':
                    print("Good Evening ")
            elif time<'22:00:00':
                    print("it is night time go and sleep ")
            break
#ivis info
def infoivis():
        print("my name is ivis")
        print("i am a chat bot ")
        print("i perform functions like dt,time,date,cal,table")
        print("i am not fully programmed")
        print("creating by HK")


# date
def date():
        from datetime import date
        today = date.today()
        print("Today's date:", today)

#time
def time():
        from datetime import datetime
        now = datetime.now()
        t = now.strftime("%H:%M:%S")
        print('Time',t)

#day
def day():
      import datetime
      now = datetime.datetime.now()
      print(now.strftime("%A"))
      
#both date and time
def dt():
        from datetime import date
        today = date.today()
        print("Today's date:", today)
        from datetime import datetime
        now = datetime.now()
        t = now.strftime("%H:%M:%S")
        print('Time',t)

#passwords
def pas():
    print("i password is password9385")
    print("GA password is password9385!")
       
#tables
def table():
        t=int(input('Enter the number:'))
        for i in range(1,11):
            m=t*i
            print(t,'x',i,'=',m)

#calculator
def cal():
        print("1.Basic calculation")
        print("2.intermediate calculation")
        opt=int(input("Enter your choice:"))
        if opt==1:
            print("1.addition")
            print("2.subraction")
            print("3.multiplication")
            print("4.division")
            print("Enter choice by Number")
            v=int(input("Enter choice:"))
            if v==1:
                x=int(input("1st number:"))
                y=int(input("2nd number:"))
                m=x+y
                print(m)
            elif v==2:
                x=int(input("1st number:"))
                y=int(input("2nd number:"))
                m=x-y
                print(m)
            elif v==3:
                x=int(input("1st number:"))
                y=int(input("2nd number:"))
                m=x*y
                print(m)
            elif v==4:
                x=int(input("1st number:"))
                y=int(input("2nd number:"))
                if y==0:
                    print("zero is not applicable in denominator")
                    x=int(input("1st number:"))
                    y=int(input("2nd number:"))
                    m=x/y
                    print(m)
                else:
                    m=x/y
                    print(m)
        else :
            import math
            print("1.Find Factorial")
            print("2.Find SquareRoot")
            print("3.Find Logarithms")
            print("4.Find power")
            print("Enter choice by Number")
            var=int(input("Enter choice:"))
            if var==1:
                f=int(input("Enter Number :"))
                print(math.factorial(f))
            elif var==2:
                sq=int(input("Enter Number:"))
                print(math.sqrt(sq))
            elif var==3:
                lo=int(input("Enter Number:"))
                print(math.log10(lo))
            elif var==4:
                p=int(input("Enter Number For Base:"))
                o=int(input("Enter Number to power:"))
                print(math.pow(p, o))

while True:
             
            i=input("")
            if i=='date':
                  date()
            elif i=='tell me date ivis':
                  date()
            elif i=='time':
                  time()
            elif i=='tell me time ivis':
                  time()
            elif i=='dt':
                  dt()
            elif i=='show my password':
                while True:
                    y=input('')
                    if  y=='pas':
                        pas()
                    elif y=='quit':
                        break
                    else:
                        continue
                    
            elif i=='info':
                  infoivis()
            elif i=='tables':
                  table()
            elif i=='cal':
                  cal()
            elif i=='hi':
                  print("Hello")
            elif i=='hello':
                 print('hi')
            elif i=='what is your name':
                 print("my name is  IVIS",end=' '
                        "for more info type info:" )
            elif i=='who are you':
                  print("i am ivis for more info type info:")
            elif i=='hello ivis':
                  print("yes,tell")
            elif i=='what can you do':
                  print("i can do tables,calculation")
            elif i=="did you speak to me":
                  print("oh yes")
            elif i=='info':
                  infoivis()
            elif i=='ivis':
                  print("yes")
            elif i=='tell your favourite':
                  print("my favourite is working of all time")
                  
            elif i=='how are you':
                  print('fine')
            elif i=='fine':
                  z=input("can i help?")
                  if  z=='yes':
                        print("what can i help")
                  elif z=='no':
                        print("Then")
            elif i=='not fine':
                  print("Don't  worry")
            elif  i=='ok':
                  print('fine')
            elif i=='i am fine':
                  print('ok')
            elif i=='fine ivis':
                  print("ok")
            elif i=='bye ivis':
                   print("bye")
                   break
            elif i=='close':
                   print("bye")
                   break
            elif i=='Do you know my name':
                  if name==" ":
                        name=input("Can you Tell ypur name:")
                  else:
                        print("Your Name is:",name)
                  
            elif i=="day":
                  day()
                  
            elif i=='today':
                  day()
                  
            else:
                  print("sorry i can't understand")
                  continue
            



    




                


    

