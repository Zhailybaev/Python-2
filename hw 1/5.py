month=input("Input the name of Month: ")
months=["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

if month==months[3] or month==months[5] or month==months[8] or month==months[10]:
    d=30
else:
    d=31
if month==months[1]:
    d="28/29"
   # print("Number of days: ", t)
    
print("Number of days:", d)
