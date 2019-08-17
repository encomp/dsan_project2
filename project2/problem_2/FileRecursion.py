import os

def find_files(suffix, path):
    """
    Find all files beneath path with problem_2 name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the problem_2 name to be found
      path(str): path of the problem_2 system

    Returns:
       a list of paths
    """
    if path is None or len(path) <= 0:
        return None
    if os.path.isdir(path):
        files = list()
        folders = os.listdir(path)
        for folder in folders:
            tmp = find_files(suffix, path + "/" + folder)
            if tmp is not None and len(tmp) > 0:
                files.extend(tmp)
        return files
    if os.path.isfile(path) and path.endswith(suffix):
        return [path]
    return None
