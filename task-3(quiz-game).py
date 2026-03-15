a= "Welcome to Koun Banega Crorepati(KBC)"
print(a.center(80).upper())

b= '''
                           Let's start the game
                          ------------------------
                          '''
print(b)
rules= '''RULES OF THE GAME:
          
    1. The computer will display a question with four options (A, B, C, D)
    2. the contestant must choose one answer.
    3. If the answer is correct the score increases and the next question appears
     ''' 
print(rules)   

for i in range(10):
    count=0
    #question1
    for i in range(1):
        print("\n\n1.What symbol is used for comments in Python?")
        l= [ "A)//","B)#","C)/*","D)--"]
        print(l)
        guess=input("\nEnter your ans from(a,b,c,d):")
        #ans1 = l.index("B)#")
        
        if guess =="b":
            print("currect ans")
            count=count+10000
          
            break
        else:
            print("wrong ans.Better luck next time")
            break
    print("your total prize money is :",count)     
    if guess!="b":    
        break
    
    
    #question2
    for i in range(1):
        print("\n\n\n2.Which function is used to take input from the user in Python?")
        l= [ "A)print()","B)input()","C)read()","D)scan()"]
        print(l)
        guess=input("\nEnter your ans(a,b,c,d):")
        #ans1 = l.index("B)input()")
        
        if guess =="b":
            print("currect ans")
            count=count+50000
          
            break
        else:
            print("wrong ans.Better luck next time")
            break
    print("your total prize money is :",count)     
    if guess!="b":    
        break
    
    
    #question3
    for i in range(1):
        print("\n\n\n3.Which of the following is a correct variable name in Python?")
        l= [ "A)2name","B)my-name","C)my_name","D)my name"]
        print(l)
        guess=input("\nEnter your ans(a,b,c,d):")
        #ans1 = l.index("C)my_name")
        
        if guess =="c":
            print("currect ans")
            count=count+100000
          
            break
        else:
            print("wrong ans.Better luck next time")
            break
    print("your total prize money is :",count)     
    if guess!="c":    
        break
    
    
    
#question4
    for i in range(1):
        print('\n\n\n4.What is the data type of "Hello"?')
        l= [ "A)Integer","B)Float","C)String","D)Boolean"]
        print(l)
        guess=input("\nEnter your ans(a,b,c,d):")
       # ans1 = l.index("C)String")
        
        if guess =="c":
            print("currect ans")
            count=count+200000
          
            break
        else:
            print("wrong ans.Better luck next time")
            break
    print("your total prize money is :",count)     
    if guess!="c":    
        break
    
    
#question5
    for i in range(1):
        print('\n\n\n5.Which function is used to display output in Python?')
        l= ["A)show()","B)display()","C)print()","D)output()"]
        print(l)
        guess=input("\nEnter your ans(a,b,c,d):")
        #ans1 = l.index("C)print()")
        
        if guess =="c":
            print("currect ans")
            count=count+500000
          
            break
        else:
            print("wrong ans.Better luck next time")
            break
    print("your total prize money is :",count)     
    if guess!="c":    
        break
  
    
#question6
    for i in range(1):
        print('\n\n\n6.Which operator is used for addition in Python?')
        l= ["A)+","B)-","C)*","D)/"]
        print(l)
        guess=input("\nEnter your ans(a,b,c,d):")
        #ans1 = l.index("A)+")
        
        if guess =="a":
            print("currect ans")
            count=count+700000
          
            break
        else:
            print("wrong ans.Better luck next time")
            break
    print("your total prize money is:",count)     
    if guess!="a":    
        break
    
    
#question7
    for i in range(1):
        print('\n\n\n7.Which keyword is used for decision making?')
        l= ["A)if","B)when","C)check","D)decide"]
        print(l)
        guess=input("\nEnter your ans(a,b,c,d):")
        #ans1 = l.index("A)if")
        
        if guess =="a":
            print("currect ans")
            count=count+900000
          
            break
        else:
            print("wrong ans.Better luck next time")
            break
    print("your total prize money is :",count)     
    if guess!="a":    
        break
   
    
    
#question8
    for i in range(1):
        print('\n\n\n8.What is the correct extension of a Python file?')
        l= ["A).pt","B).java","C).py","D).code"]
        print(l)
        guess=input("\nEnter your ans(a,b,c,d):")
       # ans1 = l.index("C).py")
        
        if guess =="c":
            print("currect ans")
            count=count+1000000
          
            break
        else:
            print("wrong ans.Better luck next time")
            break
    print("your total prize money is :",count)     
    if guess!="c":    
        break
    
    
  #question9
    for i in range(1):
        print('\n\n\n9.Which data type is used for numbers without decimal?')
        l= ["A)float","B)string","C)int","D)list"]
        print(l)
        guess=input("\nEnter your ans(a,b,c,d):")
        #ans1 = l.index("C)int")
        
        if guess =="c":
            print("currect ans")
            count=count+2000000
          
            break
        else:
            print("wrong ans.Better luck next time")
            break
    print("your total prize money is :",count)     
    if guess!="c":    
        break
   

  #question10
    for i in range(1):
        print('\n\n\n10.Which keyword is used to define a function?')
        l= ["A)function","B)def","C)fun","D)define"]
        print(l)
        guess=input("\nEnter your ans(a,b,c,d):")
        #ans1 = l.index("B)def")
        
        if guess =="b":
            print("currect ans")
            count=count+5000000
          
            break
        else:
            print("wrong ans.Better luck next time")
            break
    print("your total prize money is :",count)     
    if guess!="b":    
        break
    break 

print ("\nGame over")
print("-------------Thank you for participating in the game---------------")
