user_input = input("Please enter three numbers:  ")
string_list = user_input.split(",")
int_list = []
result = 0
for i in string_list:
    int_list.append(int(i))
print(int_list[0] + int_list[1] - int_list[2])