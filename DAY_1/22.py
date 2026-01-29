# use function to print fibnoci series
# def feb(x):
#     s = []
#     a,b=0,1
#     for _ in range(x):
#         s.append(a)
#         a,b = b,a+b
#     return s
# n = int(input())
# print(feb(n))


# def feb(x):
#     if x == 0:
#         return 0
#     if x== 1:
#         return 1
#     return feb(x-1) + feb(x-2)
# n = int(input())
# print(feb(n))



# swap case problem

# def swap_case(s):
#     a = s.swapcase()
#     return a

# if __name__ == '__main__':
#     s = input()e
#     result = swap_case(s)
#     print(result)



# swap_case for split and join problem

# def split_and_join(line):
#     a = line.split()
#     b = "-".join(a)
#     return b

# if __name__ == '__main__':
#     n = input()
#     result = split_and_join(n)
#     print(result)




# # range in python
# animals = ['dog', 'cat', 'parrot']
# for i in range(len(animals)):
#     print(i,animals[i])




# def friends(s):
#     for i in range(len(s)):
#         print(i,s[i])
#         return  s[i]
# if __name__ == '__main__':
#     s = input()
#     result = friends(s)
#     print(result)


# dictionaries problem

# my_dict = {"name": "matt", "cash": 5.45}
# for key in my_dict: 
#     print(key, my_dict[key])


# 
# students = {"banu": 34, "ram": 23, "shyam": 45, "hari": 56, "gita": 78}
# students = {"name": ["banu", "ram", "shyam", "hari", "gita"], "age": [34, 23, 45, 56, 78]}
# for i in students:
#     print(i,students[i])
# for i in students:
#     print(students[i])

# name= "bhanu"
# print(dir(name))
# print(name.upper())
# print(name.lower())
# print(name.title())
# print(name.find("a"))
# cd, ct , bd = (input())
# if(cd == "01/01" and ct == "00:00"):
#     print("Happy New Year")
# elif(cd == "01/01" and bd == "01/01"):
#     print("Happy Birthday")
# else:
#     print("regualar day")


names = ["akash", "bhanu", "ram", "shyam", "hari", "gita"]
names.append('sri')
print(names)