num = int(input("Digite um numero "))
n = 0
qnt = 0
while True:
    if n % 2 == 0:
         print(n)
         n = n + 2
         qnt = qnt + 1
           
    if n > num:
            break
print("A quantidade é" , qnt)