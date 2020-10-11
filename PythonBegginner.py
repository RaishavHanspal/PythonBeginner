'''print('Hello')
string ="She said, \"That's a great tasting apple!\""
print(len(string), string)
number = 3000.00012
string1 = "I love you"
print('{} {:.10f}'.format(string1, number))
print("")
print('Table')
print('{0:<8}|{1:<8}'.format('Apples',str(25)))'''
print('')
print('-'*70)
print('Exercise 1')
print('-'*len('Exercise 1'))
animal = "cat"
vegetable = "broccoli"
mineral ="gold"
print('Here is an animal, a vegetable, and a mineral.')
print(animal)
print(vegetable)
print(mineral)
print('')
print('Exercise 2')
print('-'*len('Exercise 2'))
variable = input('Please type something and press enter: ')
print('You entered: ')
print(variable)
print('')
print('Exercise 3')
print('-'*len('Exercise 3'))
print('{}{}'.format(' '*len('        /'),'_'*len(variable)))
print('{} {}'.format(' '*len('      '),'< '+ variable +' >'))
print('{}{}'.format(' '*len('        /'),'-'*len(variable)))
print('        /')
print(' /\_/\ /')
print('( o.o )')
print(' > ^ <')
print('')
print('-'*70)
print('Exercise 1')
print('-'*len('Exercise 1'))
print('')
day = 24*0.51
month = 30*day
print('How much does it cost to operate one server per day?')
print('$ {:.0f}'.format(day))
print('How much does it cost to operate one server per month?')
print('$ {:.0f}'.format(month))
print('')
print('Exercise 2')
print('-'*len('Exercise 2'))
print('')
print('How much does it cost to operate one server per day?')
print('$ {:.0f}'.format(day))
print('How much does it cost to operate one server per month?')
print('$ {:.0f}'.format(month))
print('How much does it cost to operate twenty servers per day?')
print('$ {:.0f}'.format(20*day))
print('How much does it cost to operate twenty servers per month?')
print('$ {:.0f}'.format(20*month))
print('How many days can I operate one server with $918?')
print('{:.0f} days'.format(918*day))

print('-'*70)
print('')
print('Exercise 1')
print('-'*len('Exercise 1'))
print('')
distance = int(input('How far would you like to travel in miles? '))
if distance<=3:
    print('I suggest walking to your destination.')
elif distance<=300:
    print('I suggest driving to your destination.')
else:
    print('I suggest flying to your destination.')
print('')
print('-'*70)
print('')
print('Exercise 1')
print('-'*len('Exercise 1'))
def get():
    '''gets user input'''
    noun = input('Enter the name of the protagonist: ')
    verb = input('Enter the what is he doing: ')
    adjective = input('Enter how is he doing the work: ')
    fill(noun, verb, adjective)


def fill(noun, verb, adjective):
    '''forms the story'''
    print('{}, on a sunday evening was {} {} with his fellows'.format(noun, verb, adjective))

get()
print('-'*70)
print('')
print('Exercise 1')
print('-'*len('Exercise 1'))
task_List = []
task = input('Enter a task for your to­do list. Press <enter> when done: ')
while task!="":
    task_List.append(task)
    print('Task added.')
    task = input('Enter a task for your to­do list. Press <enter> when done: ');
print("")    
print('Your To­Do List: ')
print('-'*len('Your To­Do List'))
for tasks in task_List:
    print('* {}'.format(tasks))
print('-'*70)
print('')
print('Exercise 1')
print('-'*len('Exercise 1'))
peoples= {'Jeff': 'Is afraid of clowns.','David': 'Plays the piano.','Jason': 'Can fly an airplane.'}
selection = 1 
while selection!='4':
    print("press '1' to view people list.")
    print("press '2' to add people list.")
    print("press '3' to delete a record.")
    print("press '4' to quit.")
    selection = input('choose an input.... ')
    print("")
    if selection == '1':
        for people in peoples:
            print(people+ '->'+peoples[people])
        print("")
    elif selection == '2':
        name = input('Enter a name: ')
        qlt = input('Enter quality: ')
        peoples[name]=qlt
    elif selection =='3':
        name = input('Enter a name: ')
        if name in peoples.keys():
            del peoples[name]
            print('Record deleted!')
            print("")
        else:
            print('No record found!')
            print("")
    else:
        print('give a valid input!')
        print("")
        

print('-'*70)
print('')
print('Exercise 1')
print('-'*len('Exercise 1'))
'''airport_List = [('O’Hare International Airport', 'ORD'), ('Los Angeles International Airport', 'LAX'), ('Dallas/Fort Worth International Airport', 'DFW'), ('Denver International Airport','DEA')]
#print(airport_List[2])
for airport, code in airport_List:
    print('The code for {} is {}'.format(airport, code))'''
hosts = open('C:\\Users\\91965\\Documents\\random.txt')
try:
    host1 = hosts.read()
    print(hosts)
except:
    host1 = ""
    print('Invalid')
index =0;
with open('C:\\Users\\91965\\Documents\\random.txt') as hostfile:
    for line in hostfile:
        index=index+1;
        print('{}. {}'.format(index,line.rstrip()))
     
animalList = []
index =0;
print("")
with open('C:\\Users\\91965\\Documents\\animals.txt') as animalhost:
     for line in animalhost:
        index=index+1;
        print('{}. {}'.format(index,line.rstrip()))
        animalList.append(line)
sortedanimals = sorted(animalList)
print("")
index=0
file1 = open("C:\\Users\\91965\\Documents\\animals-sorted.txt","w")#append mode 
file1.writelines(sortedanimals) 
file1.close()
with open('C:\\Users\\91965\\Documents\\animals-sorted.txt') as animalhost:
     for line in animalhost:
        index=index+1;
        print('{}. {}'.format(index,line.rstrip()))
import requests

from pprint import pprint
#Specify content type and form the request body
headers = {'Content-Type': 'application/json'}
job_params = {
    'q': 'Raishav Hanspal'
}
# Post job and get response
response = requests.post(
    'https://rt.serpmaster.com/',
    headers=headers,
    json=job_params,
    auth=('SM337266', 'gYTppaD9sb')
)
responseJson = response.json()
#Print the response body
#print(responseJson['results'][0]['content'])
json = responseJson['results'][0]['content']
print(json)
file1 = open("C:\\Users\\91965\\Documents\\Websearch.txt","w") 
file1.writelines(json) 
file1.close()

          






