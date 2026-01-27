# Dynamic Functions Practice #1
# Create a function (all_positives) that returns True if all the values in a list are positive, and False if at least one of the values is negative. Create a list named numbers with positive and negative values.
def all_positives(num):
    
    if num>0:
        print("True")
    else:
        print("False")
    return num


# Don't call the function, you just need to define it.






# Dynamic Functions Practice #2
# Create a function (sum_less) that adds the numbers of a list as long as they are greater than 0 and less than 1000, and returns the result of said sum. Create a numbers variable, storing a list of numbers so we can test it.
numlist=[4,-12,57,12,-65,-83,92,-5,1254,-5346,16,78,8888]
def sun_less(numlist):
    for nums in numlist:
        if 0<nums<1000:
            print("True")
        else:
            print("False")
    return numsgi



# Dynamic Functions Practice #3
# Create a function (count_even) that counts the number of even numbers that exist in a list (numbers), and returns the result of said count.