# code for dynamic arrays
values = []
for i in range(3):
    print("Enter value " + str(i + 1) + ":")
    value = input()
    values.append(value)
for i in range(3):
    print(values[i], end=" ")
