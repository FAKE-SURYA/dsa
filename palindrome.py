s = "level"
left = 0
right = len(s) -1
pal = True 

while left < right:
    if s[left] != s[right]:
     pal = False
     break
    left  += 1
    right -= 1
if pal :
    print("palin")
else:
    print("not")
     
