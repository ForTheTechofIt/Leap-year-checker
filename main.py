# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

y = year 
if y % 4 == 0:
    
    if y % 100 != 0:
      print('Leap year.')  
    elif y % 400 == 0:
            print('Leap year.')
    else:
        print('Not leap year') 
      
else:
    print ('Not leap year')

