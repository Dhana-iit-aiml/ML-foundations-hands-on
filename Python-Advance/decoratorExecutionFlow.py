
# Task1 -> 100
def task1(x):  # x----> 106
    print ("Called Task1")
    def executor():   #107
        print("Task 1 Start")
        x()
        print("Task 1 End")
    return executor  #107
# Task2 -> 101
def task2(x):   #---->105
    print ("Called Task2")
    def executor():  ##-----> 106
        print("Task 2 Start")
        x()
        print("Task 2 End")
    return executor   #106
#Task3 -> 103
def task3(x):    # x-> 104
    print ("Called Task3")
    def executor():    # executor -> 105
        print("Task 3 Start")
        x()
        print("Task 3 End")
    return executor # 105

# Evaluation
# reading or evaluation phase - flow task3--> task2 ---> task3
@task1    #   target        = task1(intermediate2) -> 107
@task2    #   intermediate2 = task2(intermediate1) -> 106
@task3    #   intermediate1 = task3(target) -> 105
def target():   #target -> 104
    print("Target")

# Exceution phase  -  on calling
target()