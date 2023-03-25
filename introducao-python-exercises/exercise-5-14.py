n_list = []
n = 0
while True:
    n = int(input('Type a number: '))
    
    if n == 0:
        break
    n_list.append(n)
    
    
print(n_list)
print(len(n_list))
print(sum(n_list))
print(sum(n_list)/len(n_list))