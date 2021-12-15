

def function_gaussian_addition(range_number):
    y = -1
    x = 0
    while(range_number[x] < range_number[y]):
        print("%d + %d = %d" %(range_number[x], range_number[y], (range_number[x] + range_number[y])))
        x +=1
        y -=1


function_gaussian_addition(list(range(int(input()), int(input()))))
