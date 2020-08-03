#Amirhossein Rajabpour 9731085
#converting nfa to dfa
#f = open("E:\\uni\\Nazarie\\project1\\nfa_test.txt","r")
f = open("E:\\uni\\Nazarie\\project1\\NFA_Input_2.txt","r")
#here it reads the input part by part and builds our alphabetic and states
#and initial state and final states
#also i checked if there is a BOM in our input string and remove it
alphabetic = f.readline().replace('ï»؟', '').rstrip('\n').split(' ')
States = f.readline()
states = States.rstrip('\n').split(' ')
starting_state = f.readline().rstrip('\n')
Final_states = f.readline()
final_states = Final_states.rstrip('\n').split(' ')
#here it reads vertices line b line and store them
lines = []
for x in f:
    lines.append(x.rstrip('\n'))
#here i override dictionary so i can have a dictionary with multiple values with only one key
#because in nfa the state can go to different states with only one input
#for instance dfa can go from state q0 with input 1 to both states q1 and q2
class Dictlist(dict):
    def __setitem__(self, key, value):
        try:
            self[key]
        except KeyError:
            super(Dictlist, self).__setitem__(key, [])
        self[key].append(value)
#the general structure for saving the machine is the same as dfa in previous code
#which means i created a state class for every state
#and each state object has an overrided dictionary which can have multiple values for one key as explained above
class State:
    def __init__(self, current):
        self.current = current
        self.next_states = Dictlist()
        return
    def add_line(self, x, y):
        self.next_states[x] = y
#here it creates an object for each state according to their name and stores the objects into an array(like previous code)
states_classes = []
for s in states:
    s = State(s)
    states_classes.append(s)
#this function is very useful. it takes a state name and returns the state object from the state_classes
def get_state(state_name_string):
    for state in states_classes:
        if state.current == state_name_string:
            return state
#here it reads line array and create next states for each state and the given alphabetic as input(like previous code)
for i in lines:
    i = i.rstrip('\n')
    x = i.split(' ')
    get_state(x[0]).add_line(x[1],x[2])
#this method takes an state name and iterate through our states
# and create a set that that state can go with lambda (in other words it's the lambda closure)
def lambda_transition(state_name):
    lambda_set = set()
    lambda_set.add(state_name)
    for s in states_classes:
        if s.current in lambda_set:
            for k in s.next_states.keys():
                if k == 'خ»':
                    for value in s.next_states.get(k):
                        lambda_set.add(value)
    return lambda_set
#for distinguishing part of the final states we see from which states we can go to nfa's final states with lambda and add them all to final state
for state in states_classes:
    l = lambda_transition(state.current)
    for sl in l:
        if sl in final_states:
            final_states.append(state.current)
#here we create our delta_prime which means from each state we can go to what states with a distinct letter of alphabet
#and because we might not have all the alphabetic as the state's input, it should be in a try except code
delta_prime = {}
for state in states_classes:
    l = lambda_transition(state.current)
    delta_prime[state] = {}
    for a in alphabetic:
        lambda_set = set()
        for node in l:
            s = get_state(node)
            try:
                tmp = s.next_states.get(a)
                for i in tmp:
                    lambda_set = lambda_set.union(lambda_transition(i))
            except:
                pass
        delta_prime[state][a] = lambda_set
#now that our delta_prime is ready we can iterate over our dfa_states with all the alphabetic as inputs
#and see which state they go with different alphabetic
#and if that state does not exist we create it and add it to our dfa states
dfa_initial_state = 'q0'
dfa_states = [starting_state]
dfa_states_names = {dfa_initial_state: [starting_state]}
get_state(dfa_initial_state).next_states = {}
for dfa_s in dfa_states:
    for a in alphabetic:
        state_result = set()
        for state in dfa_states_names[dfa_s]:
            state_result = state_result.union(delta_prime[get_state(state)][a])
        is_found = 0
        next_state = ''
        for name, state in dfa_states_names.items():
            if sorted(state_result) == sorted(state):
                is_found = 1
                next_state = name
#if we dont have the state it means that it's not found ad the is_found flag is zero
#thus the new state is created and named with Q + the size of our dfa_states
#with this way of naming dfa_states we can have all the new dfa_states which can be a combination of nfa states
#after they're created, they're added to our dfa_states and also an object of State is created for them
#so they can be iterable later easily
        if is_found == 0:
            tmp_new_state = 'Q' + str(len(dfa_states))
            dfa_states.append(tmp_new_state)
            dfa_states_names[tmp_new_state] = state_result
            s = State(tmp_new_state)
            states_classes.append(s)
            next_state = tmp_new_state
        get_state(dfa_s).add_line(a,next_state)
#now we should recognize all the final states in three steps:
#firs step is already done before in lines 65 to 72
#second step: we add all the lambda closure states of the nfa's final states to the final array
for state in states:
    if state in final_states:
        l = lambda_transition(state)
        for sl in l:
            final_states.append(sl)
#last step: and finally we iterate over our dfa states which can be a combination of states
#and if one of those states is in nfa's final states then all of that state
#which is a combination of states is a final state for our dfa
dfa_final_states = []
for name,state in dfa_states_names.items():
    for s in state:
        if s in final_states and s not in dfa_final_states:
            dfa_final_states.append(name)
#this function takes a state name (for example Q1 which is a combination of states) and returns all the states in it
def return_states_by_name(n):
    for name,state in dfa_states_names.items():
        if name in n:
            return state
#now our dfa is ready and we can write the elements in the given order
fw = open('DFA_OUTPUT_2.txt','w+')
print('alphabetic: ',*alphabetic)
for i in alphabetic:
    fw.write(i + ' ')
fw.write('\n')
print('state names: ',*dfa_states_names.values())
for i in dfa_states_names.values():
    fw.write('{')
    for j in i:
        fw.write(j)
    fw.write('} ')
fw.write('\n')

print('starting state: ', starting_state)
fw.write('{' + starting_state + '}\n')

flat_final_output = []
for s in dfa_final_states:
    if return_states_by_name(s) not in flat_final_output:
        flat_final_output.append(return_states_by_name(s))
print('final states: ', *flat_final_output)
for i in flat_final_output:
    fw.write('{')
    for j in i:
        fw.write(j)
    fw.write('} ')
fw.write('\n')

for name,state in dfa_states_names.items():
    for a in alphabetic:
        print(state,a,return_states_by_name(get_state(name).next_states.get(a)))
        fw.write('{')
        for i in state:
            fw.write(i)
        fw.write('} ' + a + ' {')
        for j in return_states_by_name(get_state(name).next_states.get(a)):
            fw.write(j)
        fw.write('}\n')
