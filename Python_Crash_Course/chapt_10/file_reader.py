file_path = 'D:\\Development\\py\\chapt_10\\pi_digits.txt'
with open(file_path) as file_object:
    """contents = file_object.read()
    print(contents)"""
    for test in file_object:
        print(test)