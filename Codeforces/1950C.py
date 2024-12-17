x = int(input())
for _ in range(x):
    hours,minutes = map(int,input().split(":"))
    hours_final = ""
    minutes_final = ""
    suffix_to_add = ""
    if hours >= 12 : 
        suffix_to_add+="PM"
    else :
        suffix_to_add+="AM"


    if hours >12 and hours < 22:
        hours_final+="0"
        hours_final+=str(hours-12)
    if hours > 12 and hours>=22:
        hours_final+=str(hours-12)

    if hours<12 and hours != 0 and hours <=9:
        hours_final+="0"
        hours_final += str(hours)
    if hours<12 and hours !=0 and hours > 9:  
        hours_final+=str(hours)

    if hours == 12 or hours == 0:
        hours_final+="12"

    if minutes<=9:
        minutes_final+="0"
        minutes_final+=str(minutes)
    if minutes>=10:
        minutes_final+=str(minutes)             

    print(hours_final+":"+minutes_final+" "+suffix_to_add)    
