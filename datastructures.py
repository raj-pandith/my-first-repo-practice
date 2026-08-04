# # data types : bool,int ,str -> store only one value

# # tC & SC
# # O(n): linear
# # O(1): constant

# reg_user=[ # 11 sec
# "memeber1",
# "memeber1",
# "memeber1",
# "memeber1",
# "memeber1",
# ]

# # lastmeme=reg_user[-1];
# # print(f"last member of the list is {lastmeme}")

# stack=[
#    "raj",
# "brother1",
# "brother2",
# "brother3",
# "brother4",
# "brother4",
# "brother4",
# "brother4",
# "brother4",
# "brother4",
# "brother4",
# "brother4",
# "brother4",
# "brother4",
# "brother4",
# "brother4",
# "brother4",
# "brother4",
# "brother4",
# "brother4",
# "brother4",
# "brother4",
# "brother4",
# "brother4",
# "brother4",
# "brother4",
# "brother4",
# "brother4",
# "brother4",
# "brother4",
# "brother4",
# "brother4",
# "brother4",
# "brother4",
# "brother5"  
# ]

# # last=stack[-1] // last access
# stack.append(2) // frirst add
# # print(f"last element of the stack is {last}")





# # TC : 



# # data structures:
# #    allows you to store multiple values in specific order
# # 1) store mulitple values in a single variable
# # 2) in a specific order

# # class Student:
# #     def __init__(self, name, age):
# #         self.name = name
# #         self.age = age
# #     def __str__(self):
# #         return f"Student(name={self.name}, age={self.age})"

# # list
# # storing multiple values in a single variable
# # fruits=["apple","banana","mango",23234,456,True,False,[1,2,3,34,4],Student("raj",346325)]
# # matrix_2d_array=[
# #     [1,2,3,4,54],
# #     [1,2,3,4,54],
# #     [1,2,3,4,54],
# #     [1,2,3,4,54],
# # ]

# # for i in fruits:
# #     print(i,end=" ")
# # print()
# # print("hello world")

# # when we need to use list ?
# # print(fruits[1])
# # [..................] by index


# # stack (pop/push)
# # special features: we can access it in reverse order (LIFO)

# # stack = [1,2,3,4,5,6,7]
# # print(stack)
# # for i in stack:
# #     print(i,end=" ")

# # print()
# # while len(stack)>0:
# # for i in range(len(stack)): # repeate iteration len times
# #     print(stack.pop(),end=" ")

# # stack.append(1)
# # stack.append("raj")
# # print(stack)

# # last=stack.pop()

# # print(stack)
# # print(f"last element removed from stack is {last}")


# #456 -> peek
# #3r34 
# #34
# #56
# #1

# # queue
# queue= []
# q=[1,2,3,4,5]
# q.pop(0)
# q.append(6)
# first=q[0]

# for i in q:
#     print(i,end=" ")

# for i in range(len(q)):
#     print(q.pop(0),end=" ")


# set {}
# to store only unique values

unique_nums=set()  # this is a set
# unique_nums.add(1)
# unique_nums.add(1)
# unique_nums.add(2)
# unique_nums.add(3)
# unique_nums.add(4)
# unique_nums.add(4)

# print(unique_nums)

# unique_letter=set() # s f
# word="sfsf"
# new_word=""
# for letter in word: # s f
#     if letter not in unique_letter:
#         unique_letter.add(letter) # s f
#         new_word += letter

# print(new_word)

# access letter one by one using loop
# check if letter is already present in the set or not
# if not present then add it to the set


# unique_letter=set() # s f
# word="sfsf"
# new_word=""
# for letter in word: # s f
#     if letter not in unique_letter:
#         unique_letter.add(letter) # s f
#         new_word += letter
# print(new_word)


# "llo"
# first non reperting letters (o-1) it is the answeer, o 

#h-1
#e-1
#l-2
#o-1

# # dictinary  , no proper ordering
# K - V pair and Unique for every key
# {
#     "stud1":"krishna"
# }

# dictionary=dict()


# algorithm

# travel all letters present in word via loop
# for each travel/iteration/letter
#     we need to store letter-{count: get the previous count of this same letter
#                              if we are seeing it has first time then we need to consider it as 1
#                              } as pair and store dictionary



