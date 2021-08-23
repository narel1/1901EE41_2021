def get_memory_score(input_number):
    score=0
    memory = []
    input_set = set()
    for inputs in input_number:
        if inputs in input_set:
            score=score+1
        else:
            if len(input_set)==5:
                first_input=memory[0]
                memory.pop(0)
                input_set.discard(first_input)
                input_set.add(inputs)
                memory.append(inputs)
            else:
                input_set.add(inputs)
                memory.append(inputs)  
                
    print('Score: {0}'.format(score))
    
input_number=[1,2,3,4,5,6,7,8,9]

not_valid=[]

for i in range(len(input_number)):
    if not str(input_number[i]).isdigit():
        not_valid.append(input_number[i])
    
if len(not_valid) != 0:
        print('Please enter a valid input list. Invalid inputs detected : ',not_valid)
      
else:
    get_memory_score(input_number)
