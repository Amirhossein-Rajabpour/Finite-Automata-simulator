# Finite Automata Simulator

# DFA and NFA to DFA converter
<br>
Theory of machines and languages course project.
<br>
dfa.py reads a DFA from DFA_Input_1.txt in the following input order and then gets a string from input. Then it outputs whether input string was accepted by DFA or not.
<br>
`nfa_to_dfa.py` reads a NFA from `NFA_Input_2.txt` in the following input order and then writes equivalent DFA to `DFA_Output_2.txt`.

## Input file format
 - First line are automata's alphabet separated by space. <br>
 - Second line are states in the automata separated by space. <br>
 - Third line is initial state of automata. <br>
 - Fourth line are final states separated by space. <br>
 And the rest are transitions in states in the automata and each line specifies one transition in the automata (that hasthe following order): <br>
  ```text
<current state> <letter> <next state>
```
 ## Sample input file
 
 ```text
0 1
q0 q1 q2
q0
q1
q0 λ q1
q0 0 q1
q1 0 q0
q1 1 q1
q1 0 q2
q1 1 q2
q2 0 q2
q2 1 q1
```
