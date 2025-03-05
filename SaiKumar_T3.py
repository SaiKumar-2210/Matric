# Lists: Remove duplicates, sort a list, and find the second largest number
def list_operations(lst):
    unique_list=list(set(lst))  # Remove duplicates
    unique_list.sort()  # Sort the list
    second_largest=unique_list[-2]
    return unique_list,second_largest

# Tuples: Swap values between two tuples without using extra variables
def swap_tuples(t1, t2):
    t1, t2=t2, t1
    return t1, t2

# Sets: Perform union, intersection, and difference operations
def set_operations(set1, set2):
    union_set = set1 | set2  # Union
    intersection_set=set1 & set2  # Intersection
    difference_set=set1-set2  # Difference
    return union_set,intersection_set,difference_set

# Dictionaries: Create a dictionary of students' names and marks, and find the student with the highest marks
def student_marks(students):
    highest_scorer=max(students,key=students.get)
    return highest_scorer,students[highest_scorer]

# Function to handle user choice
def handle_choice(choice):
    match choice:
        case "list":
            lst = [20,10,20,30,50,40,40]
            print('list: ',lst)
            sorted_list, second_largest = list_operations(lst)
            print("Sorted list without duplicates:", sorted_list)
            print("Second largest number:", second_largest)
        case "tuple":
            t1 = (1, 7, 9)
            t2 = (4, 3, 2)
            print('tuple1: ',t1)
            print('tuple2: ',t2)
            swapped_t1, swapped_t2 = swap_tuples(t1, t2)
            print("Swapped Tuples:",swapped_t1,swapped_t2)
        case "set":
            set1 = {1,2,3,4,5}
            set2 = {4,5,6,7,8}
            union_set, intersection_set, difference_set=set_operations(set1, set2)
            print("set1: ",set1)
            print('set2: ',set2)
            print("Union:",union_set)
            print("Intersection:",intersection_set)
            print("Difference:",difference_set)
        case "dictionary":
            students = {"Ravi": 85, "Bob": 92, "Dinesh": 88}
            top_student, top_marks=student_marks(students)
            print("Dictonary: ",students)
            print("Top student:",top_student,"with marks:",top_marks)
        case _:
            print("Invalid choice! Please enter list, tuple, set, or dictionary.")

# User input to select an operation
choice = input("Enter the data structure to perform operations on (list/tuple/set/dictionary): ").strip().lower()
handle_choice(choice)
