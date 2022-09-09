"""
This is a python program initial version that extracts the email with format (From user@user.com).
Also, it can detect the maximum occurences of any email.
"""


name = input("Enter filename: ")

count_dict = dict()
max_val = None
max_list = list()

try:
    handle = open(name)
    # Iterating line by line to obatain email and add to dictionary
    for line in handle:
        if line.startswith('From '):
            # The format is From "user@user.com". So extract email which is second value with index 1 in list. 
            key = line.split()[1]
            # Adding key to dictionary with count 1 if key not found else increasing count if key already present
            count_dict[key] = count_dict.get(key, 0) + 1

    # print(count_dict)
    # Obtaining the maximum value in the dictionary and assigning to variable max_val
    for k in count_dict:
        #  Use of traditinal method to find the maximum value in a list.
        if max_val == None:
            max_val = count_dict[k]
        else:
            if count_dict[k] > max_val:
                max_val = count_dict[k]

            else:
                continue

    # print(max_val)
    # Creating list of all keys with maximum values if more than one maximum values is present
    max_list = [k for k, v in count_dict.items() if v == max_val]
    # print(max_list)
    # Printing the key value pair with maximum value of corresponding key in above list "max_list"
    for k in max_list:
        print(k, count_dict[k])

    handle.close()

except:
    print('Error')
