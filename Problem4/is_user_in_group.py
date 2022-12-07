from Group import Group


def helper(user, group, visited):
    if user in group.get_users():
        return True
    for g in group.get_groups():
        if g in visited:
            continue
        else:
            visited.add(g)
        if user in g.get_users():
            return True
        if helper(user, g, visited):
            return True
    return False


def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    ret = helper(user, group, set())
    return ret


parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)

# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large values

# Test Case 1
print(is_user_in_group(None, sub_child))
# Test Case 2
print(is_user_in_group(sub_child_user, parent))
# Test Case 3
print(is_user_in_group("", parent))

