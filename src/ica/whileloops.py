def print_every_fifth(x):
  while x >= 0:  # x is the loop variable
    print(x)
    x = x - 5
  # when indentation stops, while loop is over
  print("Done!")
print_every_fifth(20)
print_every_fifth(11)
def square_user_nums():
  # Initialize loop variable
  user_inp = input("Enter the next number (negative to quit): ")
  user_num = int(user_inp)
  while user_num >= 0:
    print(user_num, "squared is", user_num ** 2)
    user_inp = input("Enter the next number (negative to quit): ")
    user_num = int(user_inp)


def add_user_nums():
    sum_of_nums = 0
    user_num = int(input("Enter a number (0 to quit): "))
    while user_num != 0:
        sum_of_nums = sum_of_nums + user_num
        user_num = int(input("Enter a number (0 to quit): "))
    return sum_of_nums
def square_user_nums2():
    while True:
        user_inp = input("Enter the next number (negative to quit): ")
        user_num = int(user_inp)
        if user_num < 0:
            break
        print(user_num, "squared is", user_num ** 2)