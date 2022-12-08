import os


def helper(suffix, path, ret):
    """
    a helper function which recursively traverse all the paths and files under the giving path,
    if the file satisfy the condition, we append it into return
    if there is another path exist, we go into this path and recursively do the same thing
    Big(O) = n? (where n is how many paths + how many files? I don't know how to calculate this)
    :param suffix: string
    :param path: string
    :param ret: list
    :return: none
    """
    for element in os.listdir(path):
        element = path + '/' + element
        if os.path.isfile(element):
            if element.endswith(suffix):
                ret.append(element)
        if os.path.isdir(element):
            helper(suffix, element, ret)


def find_files(suffix = None, path = None):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    if not path:
        raise TypeError("please give me a path")
    ret = []
    helper(suffix, path, ret)
    return ret


# just a try for no helper function
def ff(suffix, path):
    """
        a helper function which recursively traverse all the paths and files under the giving path,
        if the file satisfy the condition, we append it into return
        if there is another path exist, we go into this path and recursively do the same thing
        Big(O) = n? (where n is how many paths + how many files? I don't know how to calculate this)
        :param suffix: string
        :param path: string
        :param ret: list
        :return: none
        """
    temp = []
    for element in os.listdir(path):
        element = path + '/' + element
        if os.path.isfile(element):
            if element.endswith(suffix):
                temp.append(element)
        if os.path.isdir(element):
            temp.extend(ff(suffix, element))
    return temp


# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large values
# Test Case 1
print('\nTest One')
print(find_files("c", "./testdir"))
print(ff("c", "./testdir"))
# Test Case 2
print('\nTest Two')
try:
    print(find_files())
except:
    print("test2 success")
# Test Case 3
print('\nTest Three')
print(find_files('', "./testdir"))
