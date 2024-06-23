def solution(people, limit):
    used_boat = 0
    people.sort()
    people_count = len(people)
    min_idx = 0
    max_idx = people_count-1
    while min_idx < max_idx:
        if  people[min_idx] + people[max_idx]<= limit:
            max_idx-=1
            min_idx+=1
        else:
            max_idx-=1
        used_boat+=1
    if min_idx == max_idx:
        used_boat+=1
    return used_boat
        

        
            
            
            

 