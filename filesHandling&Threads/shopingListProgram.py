with open(r"shopingList.txt", "r") as shopping_list_file:
    # It splits a string into a list of lines, and it removes the line breaks in the process, just like split("\n").
    # text.split("\n")    # ['milk', 'eggs', 'bread', '']   <- extra empty string at the end
    # text.splitlines()   # ['milk', 'eggs', 'bread']       <- no empty string

    items = shopping_list_file.read().splitlines()

print("before sorting:")

for item in items:
    print(item)

items.sort()

# "w" overwrites the file if it already exists
# by default, the file will be created in the same folder as this program.
# to change this, we can copy the absolute path and put it before the file name to decide where we want to put the file.
# don't forget to put r before the path (because of "\n" and such), and a \ after the path and before the file name.
# remember that the problem with absolute path is that this code probably won't work in another computer.

with open(r"sortedFile.txt", "w") as sorted_shoping_list_file:
    # join doesn't join one string to another. It joins all the items of a list into one string,
    # and the string you call it on goes between the items.
    sorted_shoping_list_file.write("\n".join(items))

with open(r"sortedFile.txt", "a") as sorted_shoping_list_file:
    sorted_shoping_list_file.write("\nan_additional_item")

with open(r"sortedFile.txt", "r") as sorted_shoping_list_file:

    items = sorted_shoping_list_file.read().splitlines()

    print("after sorting:")
    for item in items:
        print(item)