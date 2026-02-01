n1=12
n2=13

#XOR 1 0 = 1 , 1 1=0, 0 1 = 1, 0 0 = 0

n5= n1 ^ n2
print(bin(n5)[2:])

#left shift => means shifting the bits (2bits) to the left side , in this wwe gain bits

n6= n1<<2
print(bin(n6)[2:])

#right shift => means shifting bits(2 bits) to right side , in this we lose bits

n7= n1>>2
print(bin(n7)[2:])

#bitwise not
