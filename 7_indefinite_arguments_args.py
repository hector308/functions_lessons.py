def tea_order(name,tea,*args):
    print(name," ordered a",tea,"tea")
tea_order("Alice","green")
#addong treu false peramitors does not scale well. It is a mess
#args let you add any custom paramitors. Star lets you put it into a tuple
#**kwargs collects extra keywords into a dictionary
#args and kwargs is jus a placeholder name

# Indefinite Arguments (*args) Practice #1
# Create a function called sum_squares that takes any number of numeric arguments, and returns the sum of their values squared.
def sum_squares(*args):
    total=0
    for num in args:  #iterate through each argumejnt
        total+=num**2  #add the square of the number to the total
    return total
print(sum_squares(1,2,3,6))
# For example for the arguments sum_squares(1,2,3) it should return 14 (1+4+9).


# Indefinite Arguments (*args) Practice #2
# Create a function called absolute_sum, which takes any number of arguments, and returns the sum of their absolute values (that is, it takes the non-negative values and adds them together, in other words, considers them all - negative and positive - as positive).
def absolute_sum(*args):
    total=0
    for num in args:
        total+=abs(num)
    return total
print(absolute_sum(-1,4,-3))
# Indefinite Arguments (*args) Practice #3
# Create a function called personal_numbers that receives, as its first argument, a name, and then an indefinite number of values.
def personal_numbers(name, *args):
    sum=0
    for num in args:
        sum+=num
    return f"{name}, the sum of your numbers is {sum}"

print(personal_numbers('john',5,4,3))


    
# The function should return the following message:

# "{name}, the sum of your numbers is {sum_numbers}"