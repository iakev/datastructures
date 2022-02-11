def find_files(suffix, path):
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
    paths_lists = []
    files = find_files_recursively(suffix,path,paths_lists) #call to initial recursion call
    return files

#helper recursive function
def find_files_recursively(suffix,path,lists):
    import os
    # base case when path refers to a file 
    if os.path.isfile(path):
      if path.endswith(suffix):
        lists.append(path)
      return 

    #rest of cases when path refers to a directory
    else:
      directory_contents = os.listdir(path)
      for content in directory_contents:
        fullpath = os.path.join(path,content)
        find_files_recursively(suffix,fullpath,lists) #recursive call

    return lists


suffix = ".c"
path = "./testdir"
print(find_files(suffix,path))  
print(len(find_files(suffix,path)))