# hi guys welcome
# the purpose of this file is to use my favorite colour to determine how cool you are
# "technically", the number chosen will determine if youre cool

#step 1 - create a list of colours
list_colours  = 'red','orange', 'yellow'

for colours in list_colours:
    print(colours)

# ask user to add a colour
list_colours == input("please pick colour: ")

if list_colours == ('red','orange', 'yellow'):

    print ('yellow' + "hmm okay, pick a number from 1-10: ")

else:
    print("colour is not available in your region, try again")

#define variable 

control = 0
while control <=1 :
    var1 =int(input("please enter a number: "))
    control = var1

var1 = int(input("pick a number between 1-3: "))
if var1 == 1:
    print ('you are not cool')
elif var1 == 2:
    print ('you are moderately cool')

elif var1 == 3:
    print('you are very cool')
else:
    print('please follow the rules friend')


#ask user if they want to play again
control =  True 

while control :
    print("Type 1 to play again, Type 2 to exit: ")
    var2 = int(input("please enter a number: "))

    if var2 == 1:
        control = True
    elif var2 == 2:
        control = False