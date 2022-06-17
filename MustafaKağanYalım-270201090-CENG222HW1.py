import random
import matplotlib.pyplot as plt
"""
Mustafa Kağan Yalım
270201090
"""

def P1_theoretical():
    #subtracting the probabilities that there is no 3 from all probabilities, I found the probabilities of finding at least one 3.
    no_p1=(5/6)**5
    p1_theoreticial=1-no_p1
    return p1_theoreticial
def P2_theoretical():
    #I apply the given porbabilites rules.
    #I write this formulas in function: P(A|B)=(P(A)∩P(B))/P(B) , P(AUB)=P(A)+P(B)-P(A∩B)
    p_a=P1_theoretical()
    no_p_b=(1/2)**5
    p_b=1-no_p_b
    no_p_aUb=(1/3)**5
    p_aUb=1-no_p_aUb
    p_a_and_b=p_a+p_b-p_aUb
    p_a_with_given_b=p_a_and_b/p_b
    return p_a_with_given_b


def P3_theoretical():
    #I reserved a slot for an even number, because I knew an even number was given, and I deleted that slot.
    #I did the same as p1 to find the probabilities of getting at least one 3 in the remaining slots.
    #But I can't select the even numbers,I can select odd numbers for open slots so [1,3,5] is my main list for this function.
    no_p3=(2/3)**4
    p3=1-no_p3
    return p3
def roll_p1_p2():
    #Dice roll function for p1 and p2 probabilities.
    #This function picks 5 random numbers between 1 and 6 and puts them in a list.
    values_list=[]
    for i in range(5):
        dice_value=[1,2,3,4,5,6]
        dice_values=random.choice(dice_value)
        values_list.append(dice_values)
    return values_list

def roll_p3():
    #Dice roll function for probabilites of p3.
    #I wrote a different function here because we know that the even number is given, so the numbers had to be selected from the odd numbers list.
    #I wrote range(4) because I deleted one slot for given even number.
    #This function picks 5 random numbers from dice_value[] and puts them in a list.
    values_list=[]
    for i in range(4):
        dice_value=[1,3,5]
        dice_values = random.choice(dice_value)
        values_list.append(dice_values)
    return values_list
#Experimental functions of probability of p1,p2,p3.
#The following functions return 1 when the desired condition occurs, and 0 when the desired condition does not occur.
#when the function returns 1, we treat that event as the event that occurred and increase the occurrence count by 1.(92,93 and 94th rows.)
def P1_emp():
    for i in roll_p1_p2():
        if i==3:
            return 1
    return 0

def P2_emp():
    liste=[]
    isEven=False
    isThree=False
    for i in roll_p1_p2():
        if i==3:
            isThree=True
    for j in roll_p1_p2():
        if j%2==0:
            isEven=True
    if isEven==True and isThree==True:
        return 1
    return 0

def P3_emp():
    isThree = False
    for i in roll_p3():
        if i == 3:
            isThree = True
    if  isThree:
        return 1
    return 0
#throwing all the resulting possibilities into a list and showing them with matplotlib.
N=[10, 50, 100, 500, 1000, 5000, 10000, 50000, 100000, 500000, 1000000]       
prob1=[]
prob2=[]
prob3=[]

for experiment in N:
    count_p1=0
    count_p2=0
    count_p3=0
    
    for i in range(experiment):
        count_p1+=P1_emp()
        count_p2+=P2_emp()
        count_p3+=P3_emp()
        
    prob1.append(count_p1/experiment)
    prob2.append(count_p2/experiment)
    prob3.append(count_p3/experiment)
theoritical_list1=[]
theoritical_list2=[]
theoritical_list3=[]
for i in range(len(N)):
    theoritical_list1.append(P1_theoretical())
    theoritical_list2.append(P2_theoretical())
    theoritical_list3.append(P3_theoretical())

plt.plot(N,theoritical_list1)
plt.plot(N,theoritical_list2)
plt.plot(N,theoritical_list3)
plt.plot(N,prob1)
plt.plot(N,prob2)
plt.plot(N,prob3)

plt.title("The graph of empirical and theoretical probabilities ")
plt.xlabel("Number of experiments")
plt.ylabel("Probabilities")
plt.xscale("log")
plt.show()
