
# %%
class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)


# %%
def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    #default presence is false
    presence = False
    #base case
    if group.groups == [] and group.users == []:
      return 
    
    for item in group.groups:
      presence = is_user_in_group(user,item)

    if user in group.users:
      presence = True
      return presence

    

    return presence

# %%
# Test 1
print(is_user_in_group(" ",parent))
# returns False
# %%
# Test 2
print(is_user_in_group("parent",parent))
# returns False
# %%
# Test 3
print(is_user_in_group("sub_child_user",parent))
# returns True