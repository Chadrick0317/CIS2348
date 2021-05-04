# Chad Johnson 1323504 LAB: Sorting user IDs
# Global variable
num_calls = 0

#  Given code that reads user IDs (until -1), complete the quicksort() and partition() functions to sort the IDs in ascending order using the Quicksort algorithm.
#  Increment the global variable num_calls in quicksort() to keep track of how many times quicksort() is called.
#  The given code outputs num_calls followed by the sorted IDs.
def partition(user_ids, i, k):
    pivot = user_ids[k]
    index = i - 1
    for j in range(i, k):
        if user_ids[j] <= pivot:
            index += 1
            user_ids[index], user_ids[j] = user_ids[j], user_ids[index]
    user_ids[index+1], user_ids[k] = user_ids[k], user_ids[index+1]
    return index+1

#   Quick sort here
def quicksort(user_ids, i, k):
    if i < k:
        piv = partition(user_ids, i, k)
        quicksort(user_ids, i, piv-1)
        quicksort(user_ids, piv+1, k)

if __name__ == "__main__":
    user_ids = []
    user_id = input()
    while user_id != "-1":
        user_ids.append(user_id)
        user_id = input()

# Call the Quicksort
    quicksort(user_ids, 0, len(user_ids) - 1)
    num_calls = int(2 * len(user_ids) - 1)
    print(num_calls)

# Print sorted users
    for user_id in user_ids:
        print(user_id)