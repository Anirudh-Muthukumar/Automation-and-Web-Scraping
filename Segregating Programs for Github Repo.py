import os, glob
import sys

leetcode_dir = '../Leetcode-solutions/'
codeforces_dir = '../Codeforces/'

# Reset current directory
os.chdir(sys.path[0])

def RenameFiles():

    # Called by LeetCode()
    if "Leetcode" in os.getcwd():
        for file in glob.glob("*.py"):
            old_name = file
            print(file)
            if old_name.count('.')==1 and old_name[0] in ['1','2','3','4','5','6','7','8','9']:
                i = 0
                while old_name[i] in ['1','2','3','4','5','6','7','8','9']:
                    i+=1
                new_name = old_name[:i] + "." + old_name[i:]
                os.rename(old_name, new_name)

    # Called by Codeforces()
    elif "Codeforces" in os.getcwd():
        pass


def CreateFolders():

    # Called by LeetCode()
    if "Leetcode" in os.getcwd():
        for file in glob.glob("*.py"):
            folder = file[:-3]
            if file[0] in ['1','2','3','4','5','6','7','8','9'] and not os.path.exists(folder):
                print("Folder created for ", file)
                os.makedirs(folder)
    
    # Called by Codeforces()
    elif "Codeforces" in os.getcwd():
        files = []
        for file in glob.glob("*.py"):
            files += file,
        for file in glob.glob("*.cpp"):
            files += file,

        for file in files:
            if ".cpp" in file:  
                folder = file[:-4]
            elif ".py" in file:
                folder = file[:-3]
            if file[0] in ['1','2','3','4','5','6','7','8','9'] and not os.path.exists(folder):
                folder_name = folder.split()
                first_name = folder_name[1]
                if 'a'<=first_name[0]<='z':
                    folder_name[1] = first_name[0].upper() + first_name[1:]
                folder_name.insert(1, '-')
                folder = ' '.join(folder_name)
                
                print("Folder created for ", folder)
                os.makedirs(folder)

                # Move file to folder
                if ".cpp" in file:  
                    new_name = folder + "/" + "solution.cpp"
                elif ".py" in file:
                    new_name = folder + "/" + "solution.py"

                os.rename(file, new_name)
                

def MoveFilesToFolders():
    
    # Called by LeetCode()
    if "Leetcode" in os.getcwd():
        for file in glob.glob("*.py"):
            if file[0] in ['1','2','3','4','5','6','7','8','9']:
                new_path = file[:-3] + "/" + file 
                os.rename(file, new_path)
    
    # Called by Codeforces()
    elif "Codeforces" in os.getcwd():
        pass

def EmptyContestDirectory():
    """
    Moving scripts from Contest directory to home directory
    """
    contest_dir = codeforces_dir + "Contest/"
    os.chdir(contest_dir)
    contest_files = []
    for file in glob.glob("*.cpp"):
        contest_files +=  file,
    for file in glob.glob("*.py"):
        contest_files += file,
    
    for file in contest_files:
        os.rename(sys.path[0] + '/' + contest_dir + file, sys.path[0] + '/' + codeforces_dir + file)

    os.chdir("../")

def LeetCode():
    # Set the directory
    os.chdir(leetcode_dir)
    CreateFolders()
    MoveFilesToFolders()    

def Codeforces():
    # Set the directory
    os.chdir(codeforces_dir)
    EmptyContestDirectory()
    CreateFolders()

# Call the functions here
print("\nChoose the directory:\n1. Leetcode\n2. Codeforces\n")
n = int(input())

if n==1:
    LeetCode()
elif n==2:
    Codeforces()
