#Amirhossein Rajabour 9731085
# first read the dfa file
f = open("E:\\uni\\Nazarie\\project1\\DFA_Input_1.txt","r")
#here it reads the input part by part and builds our alphabetic and states and initial state and final states
Alphabetics = f.readline()
alphabetics = Alphabetics.rstrip('\n').split(' ')
States = f.readline()
states = States.rstrip('\n').split(' ')
starting_state = f.readline().rstrip('\n')
Final_states = f.readline()
final_states = Final_states.rstrip('\n').split(' ')
#here it reads vertices line b line and store them
lines = []
for x in f:
    lines.append(x.rstrip('\n'))
#for each state there is a class object which saves the state name as 'current'
#and saves the 'next_states' of that state with given input from our alphabet
class State:
    def __init__(self,current):
        self.current = current
        self.next_states = {}
        return
    def add_line(self,x,y):
        self.next_states.update({x:y})
#here it creates an object for each state according to their name and stores the objects into an array
states_classes = []
for s in states:
    s = State(s)
    states_classes.append(s)
#here it reads line array and create next states for each state and the given alphabetic as input
for i in lines:
    i = i.rstrip('\n')
    x = i.split(' ')
    for s in states_classes:
        if s.current == x[0]:
            s.add_line(x[1],x[2])
#you can see the states and their next states with the commented code bellow
#for s in states_classes:
#    print(s.current,s.next_states)

#this function change the state according to the input and return the next state (further information is given in report file)
def state_checker(state,input):
    for i in states_classes:
        if i.current == state.current :
            tmp_state = i.next_states.get(input)
            for s in states_classes:
                if s.current == tmp_state:
                    return s
#this boolean checks if all of the input string is in the dfa's alphabetic or not
string_in_alphabet = True
#this function takes string and iterate over that string letter by letter
# finally returns the last state that the string goes on
def DFA_Check(string,state):
    for z in string:
        if string in alphabetics:
            state = state_checker(state,z)
        else: string_in_alphabet = False
    return state
#this function finds the initial state between our states in state class
def find_start(state_classes):
    for s in states_classes:
        if s.current == starting_state:
            return s
#now the program is ready to take input
inp_string = input('Enter the input string:\n')
state = DFA_Check(inp_string, find_start(states_classes))

if state.current in final_states and string_in_alphabet is True:
    print('String is ACCEPTED in the given DFA')
else:
    print('String is NOT ACCEPTED in the given DFA')