import os, glob

leetcode_dir = '/Users/anirudhmuthukumar/Documents/Programs/Leetcode/'

def RenameFiles():
    for file in glob.glob("*.py"):
        old_name = file
        print(file)
        if old_name.count('.')==1 and old_name[0] in ['1','2','3','4','5','6','7','8','9']:
            i = 0
            while old_name[i] in ['1','2','3','4','5','6','7','8','9']:
                i+=1
            new_name = old_name[:i] + "." + old_name[i:]
            os.rename(old_name, new_name)


def CreateFolders():
    for file in glob.glob("*.py"):
        folder = file[:-3]
        if file[0] in ['1','2','3','4','5','6','7','8','9'] and not os.path.exists(folder):
            print("Folder created for ", file)
            os.makedirs(folder)


def MoveFilesToFolders():
    for file in glob.glob("*.py"):
        if file[0] in ['1','2','3','4','5','6','7','8','9']:
            new_path = file[:-3] + "/" + file 
            os.rename(file, new_path)


# Change the directory here
os.chdir(leetcode_dir)


# Call the functions here
