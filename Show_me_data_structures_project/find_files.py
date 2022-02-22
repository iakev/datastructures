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

     NB: Please ensure the testdir is in the same folder as this .py file for optimum perfomance.  
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


# Test case 1 
suffix = ".c"
path = "./testdir"
print(find_files(suffix,path))  
# returns [./testdir/subdir/a.c, ./testdir/subdir3/subsubdir1/b.c, ./testdir/subdir5/a.c, ./testdir/t1.c]

# Test case 2
suffix = ".h"
path = "./testdir"
print(find_files(suffix,path))
# returns [./testdir/subdir1/a.h, ./testdir/subdir3/subsubdir1/b.h, ./testdir/subdir5/a.h, ./testdir/t1.h]

#Test case 3 (no such file in directory)
suffix = ".py"
path = "./testdir"
print(find_files(suffix,path))
# returns [] no file present