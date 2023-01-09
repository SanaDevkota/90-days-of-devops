I was given a task to do some works on basic linux commands. So i have successfully completed it ,
- Check your current directory
  - To check the current directory we use the command `pwd`
- List all the files in the current directory including hidden files
  - To list all the files in the current directory including hidden files then we can use the command `ls -a`
- Create nested directories
  - To create nested directories we can use the command `mkdir -p dir1/dir2/dir3` . Note `-p` is used to create nested directories.

- To view what's written in a file.:
  - There are several ways to view text inside of file  . Some ofthem are:
    - using **cat** command `cat filename.ext`
    - using **nl** command `nl filename.ext`. Only differene with cat is it add line number when displaying .
- To change the access permissions of files:
    - we can use chmod command to change the permission as we can use `chmod` to change the access permissions

- To check which commands you have run till now.
    - `History`
- To remove the directory/folder
    - `rmdir` if it is empty else we can use `rm -rf foldername`
- To create a fruits.txt file and to view the content.
    - `vim fruits.txt`
    - `nano fruits.txt`
- To Show only top three lines in file 
  - use  tail command eg `head -n numberoflines` , more you can use `head -n 3` to list top 3 lines 
- To Show only bottom three fruits from the file
  - use `tail -n numberoflines`. so in this case you can use `tail -n 3`
- 