camel = input("Enter camelCase: ")

j = 0
snake = ''
for i in range(j,len(camel)):
    if camel[i].islower() == False:
        snake += camel[j:i].lower() + '_'
        j = i 

snake += camel[j:len(camel)].lower()

print(snake)
