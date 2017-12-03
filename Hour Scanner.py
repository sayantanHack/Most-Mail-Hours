file_handle = open("Mail list.txt")
time_list=[]
temp=[]
hours=[]
i=0
dictionary = {}
for line in file_handle:
    line.rstrip()
    if not line.startswith("From") or line.startswith("From:"):continue
    words = line.split()
    time_list.append(words[-2])
    # hours_list = time_list[i].split(':')
    hours.append(time_list[i].split(':')[0])    # hours.append(hours_list[0])
    i= i + 1

for hour in hours:
    dictionary[hour] = dictionary.get(hour , 0)+ 1
    
for key ,val in dictionary.items():
    new_tuple = (val, key)   # making a tuple for reverse
    temp.append(new_tuple)

inp = int(input("Type 1 to see the hours in Ascending order ,or type 2 for descending order :"))

if(inp==1):
    temp=sorted(temp) # sorted in ascending order.By default sorted order is lower value to higher value.
    print "In ascending order : "
    for val ,key in temp:
        print key , val


if(inp==2):
    temp=sorted(temp , reverse =True) # reverse = True for dorting in reverse(Higher value to lower value). 
    print "In descending order : "
    for val,key in temp:
        print key , val

