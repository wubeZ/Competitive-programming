def count_substring(string, sub_string):
    start = 0
    count1 = 0
    start = string.find(sub_string,start)
    
    while(start != -1):
        start+=1
        start = string.find(sub_string,start) 
        count1+=1
        
   
    return count1



