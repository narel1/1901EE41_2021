def meraki_helper(n): 
    """This will detect meraki numner""" 
    nums = [] 
    if n==0: return True 
    while n: 
        nums.append(n%10) 
        n=n//10 
    mod1=nums[0] 
    del nums[0] 
     
    for mod2 in nums: 
        if abs(mod1-mod2)!=1: 
            return False 
        mod1=mod2 
    return True         
 
 
input = [12, 14, 56, 78, 98, 54, 678, 134, 789, 0, 7, 5, 123, 45, 76345, 987654321] 
count1=count2=0 
 
for index in range(len(input)): 
    if meraki_helper(input[index])==True: 
        count1+=1 
        print("Yes - {0} is a Meraki number".format(input[index])) 
    else: 
        count2+=1 
        print("No - {0} is not a Meraki number".format(input[index]))     
 
print("the input list contains {0} meraki and {1} non meraki numbers".format(count1,count2))