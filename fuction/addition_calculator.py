def function_sum(a, b):
    return(a + b)

print("quelles est le premier nombre a additionner ?")
a = int(input())
print("le deuxieme ?")
b = int(input())
print("%d + %d = %d" %(a, b, function_sum(a, b)))
