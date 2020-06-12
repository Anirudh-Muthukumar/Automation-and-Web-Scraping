import subprocess 
import os
from datetime import datetime

dp_top50_repo = 'https://github.com/Anirudh-Muthukumar/Top-50-Dynamic-Programming-Problems'
dp_top50_dir = '/Users/anirudhmuthukumar/Documents/Programs/DP top 50/'

gfg_repo = 'https://github.com/Anirudh-Muthukumar/GeeksforGeeks-solutions'
gfg_dir = '/Users/anirudhmuthukumar/Documents/Programs/GeeksforGeeks/'

leetcode_repo = 'https://github.com/Anirudh-Muthukumar/Leetcode-solutions'
leetcode_dir = '/Users/anirudhmuthukumar/Documents/Programs/Leetcode/'

bt_top20_repo = 'https://github.com/Anirudh-Muthukumar/To2p-20-Backtracking-Algorithms'
bt_top20_dir = '/Users/anirudhmuthukumar/Documents/Programs/BT Top 20/'

codechef_repo = 'https://github.com/Anirudh-Muthukumar/CodeChef-Solutions'
codechef_dir = '/Users/anirudhmuthukumar/Documents/Programs/CodeChef/'

topcoder_repo = 'https://github.com/Anirudh-Muthukumar/TopCoder-Solutions'
topcoder_dir = '/Users/anirudhmuthukumar/Documents/Programs/TopCoder/'

codeforces_repo = 'https://github.com/Anirudh-Muthukumar/Codeforces-Solutions'
codeforces_dir = '/Users/anirudhmuthukumar/Documents/Programs/Codeforces/'

spoj_repo = 'https://github.com/Anirudh-Muthukumar/SPOJ-Solutions'
spoj_dir = '/Users/anirudhmuthukumar/Documents/Programs/SPOJ/'

cpp_repo = 'https://github.com/Anirudh-Muthukumar/CPP-Code'
cpp_dir = '/Users/anirudhmuthukumar/Documents/Programs/C++/'

'''
Steps:
1. Go to directory from which you want to add files
2. git init
3. git add .
4. git commit -m "adding more files" 
5. git remote add origin <repo>
6. git remote -v 
7. git push -f origin master
'''

timestamp = str(datetime.today().month) + str(datetime.today().day) + str(datetime.today().year)

def commit_DPTop50():

    print("\nAdding files to DP Top 50 repository...")

    # 1. Go to specified directory 
    os.chdir(dp_top50_dir)

    # 2. Initialize repository
    init_command = subprocess.run(["git", "init"])
    # print("The exit code for init_command is %d" % init_command.returncode)

    # 3. Add files to be committed
    add_command = subprocess.run(["git", "add", "."])
    # print("The exit code for add_command is %d" % init_command.returncode)


    # 4. Commit the repo to save the changes 
    commit_command = subprocess.run(["git", "commit", "-m", " adding files " + timestamp])
    # print("The exit code for commint_command is %d" % commit_command.returncode)

    # 5. Add remote repository 
    add_remote_repo_command = subprocess.run(["git", "remote", "add", "origin", dp_top50_repo])
    # print("The exit code for add_remote_repo_command is %d" % add_remote_repo_command.returncode)

    # 6. Push the changes 
    push_command = subprocess.run(["git", "push", "-f", "origin", "master"])
    push_success = push_command.returncode

    if push_success == 0 :
        print("\nSuccesfully added files to DP Top 50 repo!!!\n")

def commit_Leetcode():

    print("\nAdding files to Leetcode repository...")

    # 1. Go to specified directory 
    os.chdir(leetcode_dir)

    # 2. Initialize repository
    init_command = subprocess.run(["git", "init"])
    # print("The exit code for init_command is %d" % init_command.returncode)

    # 3. Add files to be committed
    add_command = subprocess.run(["git", "add", "."])
    # print("The exit code for add_command is %d" % init_command.returncode)


    # 4. Commit the repo to save the changes 
    commit_command = subprocess.run(["git", "commit", "-m", "adding more files"])
    # print("The exit code for commint_command is %d" % commit_command.returncode)

    # 5. Add remote repository 
    add_remote_repo_command = subprocess.run(["git", "remote", "add", "origin", leetcode_repo])
    # print("The exit code for add_remote_repo_command is %d" % add_remote_repo_command.returncode)

    # 6. Push the changes 
    push_command = subprocess.run(["git", "push", "-f", "origin", "May-Month"])
    push_success = push_command.returncode

    if push_success == 0 :
        print("\nSuccesfully added files to Leetcode repo!!!\n")


def commit_GeeksforGeeks():

    print("\nAdding files to GeeksforGeeks repository...")

    # 1. Go to specified directory 
    os.chdir(gfg_dir)

    # 2. Initialize repository
    init_command = subprocess.run(["git", "init"])
    # print("The exit code for init_command is %d" % init_command.returncode)

    # 3. Add files to be committed
    add_command = subprocess.run(["git", "add", "."])
    # print("The exit code for add_command is %d" % init_command.returncode)


    # 4. Commit the repo to save the changes 
    commit_command = subprocess.run(["git", "commit", "-m", "adding more files"])
    # print("The exit code for commint_command is %d" % commit_command.returncode)

    # 5. Add remote repository 
    add_remote_repo_command = subprocess.run(["git", "remote", "add", "origin", gfg_repo])
    # print("The exit code for add_remote_repo_command is %d" % add_remote_repo_command.returncode)

    # 6. Push the changes 
    push_command = subprocess.run(["git", "push", "-f", "origin", "master"])
    push_success = push_command.returncode

    if push_success == 0 :
        print("\nSuccesfully added files to GeeksforGeeks repo!!!\n")

def commit_BTTop20():
    print("\nAdding files to BT Top 20 repository...")

    # 1. Go to specified directory 
    os.chdir(bt_top20_dir)

    # 2. Initialize repository
    init_command = subprocess.run(["git", "init"])
    # print("The exit code for init_command is %d" % init_command.returncode)

    # 3. Add files to be committed
    add_command = subprocess.run(["git", "add", "."])
    # print("The exit code for add_command is %d" % init_command.returncode)


    # 4. Commit the repo to save the changes 
    commit_command = subprocess.run(["git", "commit", "-m", "adding more files"])
    # print("The exit code for commint_command is %d" % commit_command.returncode)

    # 5. Add remote repository 
    add_remote_repo_command = subprocess.run(["git", "remote", "add", "origin", bt_top20_repo])
    # print("The exit code for add_remote_repo_command is %d" % add_remote_repo_command.returncode)

    # 6. Push the changes 
    push_command = subprocess.run(["git", "push", "-f", "origin", "master"])
    push_success = push_command.returncode

    if push_success == 0 :
        print("\nSuccesfully added files to BT Top 20 repo!!!!\n")

def commit_CodeChef():
    print("\nAdding files to CodeChef repository...")

    # 1. Go to specified directory 
    os.chdir(codechef_dir)

    # 2. Initialize repository
    init_command = subprocess.run(["git", "init"])
    # print("The exit code for init_command is %d" % init_command.returncode)

    # 3. Add files to be committed
    add_command = subprocess.run(["git", "add", "."])
    # print("The exit code for add_command is %d" % init_command.returncode)


    # 4. Commit the repo to save the changes 
    commit_command = subprocess.run(["git", "commit", "-m", "adding more files"])
    # print("The exit code for commint_command is %d" % commit_command.returncode)

    # 5. Add remote repository 
    add_remote_repo_command = subprocess.run(["git", "remote", "add", "origin", codechef_repo])
    # print("The exit code for add_remote_repo_command is %d" % add_remote_repo_command.returncode)

    # 6. Push the changes 
    push_command = subprocess.run(["git", "push", "-f", "origin", "master"])
    push_success = push_command.returncode

    if push_success == 0 :
        print("\nSuccesfully added files to Codechef repo!!!!\n")

def commit_Codeforces():
    print("\nAdding files to Codeforces repository...")

    # 1. Go to specified directory 
    os.chdir(codeforces_dir)

    # 2. Initialize repository
    init_command = subprocess.run(["git", "init"])
    # print("The exit code for init_command is %d" % init_command.returncode)

    # 3. Add files to be committed
    add_command = subprocess.run(["git", "add", "."])
    # print("The exit code for add_command is %d" % init_command.returncode)


    # 4. Commit the repo to save the changes 
    commit_command = subprocess.run(["git", "commit", "-m", "adding more files"])
    # print("The exit code for commint_command is %d" % commit_command.returncode)

    # 5. Add remote repository 
    add_remote_repo_command = subprocess.run(["git", "remote", "add", "origin", codeforces_repo])
    # print("The exit code for add_remote_repo_command is %d" % add_remote_repo_command.returncode)

    # 6. Push the changes 
    push_command = subprocess.run(["git", "push", "-f", "origin", "master"])
    push_success = push_command.returncode

    if push_success == 0 :
        print("\nSuccesfully added files to Codeforces repo!!!!\n")

def commit_TopCoder():
    print("\nAdding files to TopCoder repository...")

    # 1. Go to specified directory 
    os.chdir(topcoder_dir)

    # 2. Initialize repository
    init_command = subprocess.run(["git", "init"])
    # print("The exit code for init_command is %d" % init_command.returncode)

    # 3. Add files to be committed
    add_command = subprocess.run(["git", "add", "."])
    # print("The exit code for add_command is %d" % init_command.returncode)


    # 4. Commit the repo to save the changes 
    commit_command = subprocess.run(["git", "commit", "-m", "adding more files"])
    # print("The exit code for commint_command is %d" % commit_command.returncode)

    # 5. Add remote repository 
    add_remote_repo_command = subprocess.run(["git", "remote", "add", "origin", topcoder_repo])
    # print("The exit code for add_remote_repo_command is %d" % add_remote_repo_command.returncode)

    # 6. Push the changes 
    push_command = subprocess.run(["git", "push", "-f", "origin", "master"])
    push_success = push_command.returncode

    if push_success == 0 :
        print("\nSuccesfully added files to TopCoder repo!!!!\n")

def commit_SPOJ():
    print("\nAdding files to SPOJ repository...")

    # 1. Go to specified directory 
    os.chdir(spoj_dir)

    # 2. Initialize repository
    init_command = subprocess.run(["git", "init"])
    # print("The exit code for init_command is %d" % init_command.returncode)

    # 3. Add files to be committed
    add_command = subprocess.run(["git", "add", "."])
    # print("The exit code for add_command is %d" % init_command.returncode)


    # 4. Commit the repo to save the changes 
    commit_command = subprocess.run(["git", "commit", "-m", "adding more files"])
    # print("The exit code for commint_command is %d" % commit_command.returncode)

    # 5. Add remote repository 
    add_remote_repo_command = subprocess.run(["git", "remote", "add", "origin", spoj_repo])
    # print("The exit code for add_remote_repo_command is %d" % add_remote_repo_command.returncode)

    # 6. Push the changes 
    push_command = subprocess.run(["git", "push", "-f", "origin", "master"])
    push_success = push_command.returncode

    if push_success == 0 :
        print("\nSuccesfully added files to SPOJ repo!!!!\n")


def commit_CPP():
    print("\nAdding files to CPP repository...")

    # 1. Go to specified directory 
    os.chdir(cpp_dir)

    # 2. Initialize repository
    init_command = subprocess.run(["git", "init"])
    # print("The exit code for init_command is %d" % init_command.returncode)

    # 3. Add files to be committed
    add_command = subprocess.run(["git", "add", "."])
    # print("The exit code for add_command is %d" % init_command.returncode)


    # 4. Commit the repo to save the changes 
    commit_command = subprocess.run(["git", "commit", "-m", "adding more files"])
    # print("The exit code for commint_command is %d" % commit_command.returncode)

    # 5. Add remote repository 
    add_remote_repo_command = subprocess.run(["git", "remote", "add", "origin", cpp_repo])
    # print("The exit code for add_remote_repo_command is %d" % add_remote_repo_command.returncode)

    # 6. Push the changes 
    push_command = subprocess.run(["git", "push", "-f", "origin", "master"])
    push_success = push_command.returncode

    if push_success == 0 :
        print("\nSuccesfully added files to CPP repo!!!!\n")

if __name__ == '__main__':

    print("Menu : ")
    print("1. GeeksforGeeks")
    print("2. DP Top 50")
    print("3. Leetcode")
    print("4. BT Top 20")
    print("5. CodeChef")
    print("6. Codeforces")
    print("7. TopCoder")
    print("8. SPOJ")
    print("9. CPP")
    repo = [int(i) for i in input("Enter the repositories to commit: ").split()]

    if 1 in repo:
        commit_GeeksforGeeks()
    if 2 in repo:
        commit_DPTop50()
    if 3 in repo:
        commit_Leetcode()
    if 4 in repo:
        commit_BTTop20()
    if 5 in repo:
        commit_CodeChef()
    if 6 in repo:
        commit_Codeforces()
    if 7 in repo:
        commit_TopCoder()
    if 8 in repo:
        commit_SPOJ()
    if 9 in repo:
        commit_CPP()
    