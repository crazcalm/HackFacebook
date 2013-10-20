import os, shutil

def copy_and_move(path):
    """
    This function will look in the current directory fo the
    pre-commit file. If found, it will copy and move
    the pre-commit file to the given paths.
    """
    
    #current_dir = os.getcwd()
    
    
    # this is the directed of the wanted file
    #file_dir = os.getcwd()
    
    # This copies wanted file and sends it
    # to the wanted file to current_dir
    # NOTE: Needs correct file name
    try:
        shutil.copy("pre-commit", path)
    except:
        print "The pre-commit file is not is the current working directory"
    
    # Puts you back in your original directory
    #os.chdir(current_dir)
    
def git_dir_exists(path):
    """
    This function checks to see if the current dir
    has a .git dir
    """
    
    path_name = os.path.join(os.sep, path, ".git")
    
    #print path_name
    
    # Returns true or false
    return os.path.exists(path_name)

def hooks_dir_exists(path):
    """
    This function checks to see if the current dir
    has a hook dir
    """
    path_name = os.path.join(os.sep, path, "hooks")
    
    # Returns tru or false
    return os.path.exists(path_name)

def finding_git_dirs(starting_point):
    """
    Walks through the directories and places all the directories
    that have a .git directory in a list
    """
    
    # Need a starting point for the search
    #starting_point = "C:\\Users\\RS011874\\Documents\\projects"
    
    # Will hold the list of directories
    results = []
    
    for root, dir, files in os.walk(starting_point):
        
        for name in dir:
            if name == ".git" and len(name) == 4:
                
                results.append(root)
    #print results            
    return results

def starting_point():
    """
    Gets a starting directory for the future directory search.
    """
    
    dir = raw_input("Please enter a directory path to start the search from: ")
    
    try: 
        os.chdir(dir)
        print "\nThank you for the starting directory!\n"
        
        print "Starting directory is: ",dir, "\n\n"
        return dir
    except:
        print "\nThat directory does not exist.\n"
        starting_point()


def add_git_to_path(path):
    """
    Takes a path and adds .git to the end of it.
    Will return this new path
    """
    
    new_path = os.path.join(os.sep, path, ".git")
    
    return new_path
    
def add_hooks_to_path(path):
    """
    Takes a path and adds hooks to the end of it.
    Will return this new path
    """
    
    new_path = os.path.join(os.sep, path, "hooks")
    
    return new_path

def main():
    """
    Controls the flow of the program
    """
    
    starting_dir = starting_point()
    
    # A list of path names
    stack_of_dir = finding_git_dirs(starting_dir)
    
    # Will fill list with the hooks dir paths
    hooks_dirs = []
    
    for dir in stack_of_dir:
        if git_dir_exists(dir):
            dir = add_git_to_path(dir)
            
        if hooks_dir_exists(dir):
            dir = add_hooks_to_path(dir)
            
            hooks_dirs.append(dir)
            #print dir
            
    for dir in hooks_dirs:
        
        copy_and_move(dir)
            
if __name__ == '__main__':
    main()
    
    
    
    
                


    
    