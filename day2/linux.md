# What is linux 
Linux is an open-source Operating system like a windows , mac , Android etc . In Broad way, you can say **Linux is an operating system that is based on the Linux kernel**. The kernel is an essential part of the operating system, but it is not the entire operating system.

- Linux is kernal not **Os**
- It is not a Unix Derivative as it was written from scratch . 


# Linux Distributions
Linux distributions are the different versions of Linux. They all are based on the Linux kernel. In Simle Words, Linux Distribution is the Linux kernal and the collection of software that are together and this creates a complete OS .
 They are also called as Linux distros. Some of the popular Linux distros are Ubuntu, Fedora, Debian, Arch Linux, Kali Linux, Red Hat, CentOS, etc.


# Unix
Unix is also an operating system like Linux. It is an commercial OS. It consists of three parts: Kernal, Shell and Programs. Most of the Unix and Linux commands are similar in nature.

# Difference between Linux and Unix
| Linux                          | Unix                         |
| :----------------------------- | :--------------------------- |
| Linux is an open-source OS     | Unix is a commercial OS      |
| Linux is free to use           | Unix is not free to use      |
| Linux is based on Linux kernel | Unix is based on Unix kernel |


- Some Common Terminologies
Folder        :           Directory 
Administrator : Root User
File          : File 
Software      : Package




# Linux file system
The Linux file system is a hierarchical file system that organizes files into directories.
It is the way that the files on a computer are stored and organized so that they can be accessed and managed.**At the top of the file system hierarchy is the root directory, which is represented by a forward slash (/).**
All other files and directories are stored beneath the root directory in a tree-like structure. In a typical Linux file system, there are several top-level directories that are used to organize and store files on the system. These directories are : 

- **/ (root)** (home directory for root user)- This is the top-most directory in the file system hierarchy. All other directories and files on the system are contained within the root directory.

- **/home** -(home dir for other users) - This directory contains the home directories for the different users on the system. Each user typically has their own subdirectory within /home.


- **/bin** (contains all commands used by all users) - This directory contains binary executables that are used by both the system and the users.
- - **/sbin**  (contains command used by only root users)- This directory contains system executables that are used for system maintenance and recovery.


- **/boot**  (contains bootable files )- This directory contains files that are needed to boot the system, such as the Linux kernel and bootloader configuration files.

- **/dev** - This directory contains special files that represent devices on the system, such as hard drives, USB devices, and printers.

- **/etc** ( contains all the configuration files )- This directory contains configuration files for the system and various programs.


- **/usr** (By defailt softwares all are installed in this dir) - This directory contains user-specific data and programs that are not essential to the operation of the system.


- **/lib** - This directory contains shared libraries and kernel modules that are used by the system and various programs.

- **/media** - This directory is used to mount removable media devices, such as USB drives and CDs.

- **/mnt** - This directory is similar to /media, and is used to mount file systems temporarily.

- **/opt** - This directory is used to store optional software packages that are not part of the core system.


- **/tmp** - This directory is used to store temporary files that are created by programs.

- **/var** - This directory contains files that change frequently, such as log files and databases.





# Linux commands
Linux commands are the commands that are used to perform different tasks in Linux. Some of the popular Linux commands are ls, cd, pwd, mkdir, rm, cp, mv, cat, grep, etc. 
**Note : Every command is a file**

**Note doing stuff stuff like remove files won't be stored in recycle bin because cmd directly send command to shell**


**Basic listing commands**
- ls : list directory contents
- ls -a : list all files including hidden files
- ls *.sh : list all files with .sh extension
- ls -i : list all files with inode number
- - ls -d */: list all directories

**Basic Directory Commands**
- cd : change directory
- pwd : print working directory
- cd ~ or cd : go to home directory
- cd - go to the previous directory
- cd .. go to the parent directory
- cd ../.. go to the grandparent directory
- mkdir : make directory

**Create and remove files and folder**
- Mkdir : make directory
- touch: create new files
- rmdir : remove specefied directory(empty)
- rmdir -p : rmeve both parent and child directory 
- rm -rf: remove non empty files and directory 



**Linux Permissions**
Linux is a multi-user operating system, so it has security to prevent people from accessing each other’s confidential files. 

**chmode**: used to change the accesss mode of a file
**chown**: used to change the ownder of files or directory 
**chgrp**: used to change the group of files or directory . 
to get deep dive visit here [LinuxPermission](https://www.geeksforgeeks.org/permissions-in-linux/)