## Linux Navigation

* **Absolute Path**
  * Starts with `/`.
    * Ex: /home/mani/projects
      
* **Relative Path**
  * Relative to current path. “where you are now”
  * projects or ../projects

* **Special path shortcuts**
  * `.` → current directory
  * `..` → parent directory
  * `~` → your home directory (like /home/youruser)
  * `-` → previous directory (used with cd -)

* **Basic Commands**
  * `pwd`
  * `mkdir`
  * `cd`
  * `cp`
  * `rm`
  * `rmdir`
  * `mv`
  * `ls`
  * `touch`
  * `find`
  * `which`
  * `whereis`
  * `cat`
  * `less`
  * `head`
  * `tail`

## Permissions

* `ls -l` gives the permission details of the file/directory as below.
  * `-rwxr-x--- 1 user_name group_name 1234 Mar  4 10:00 file_name.sh`
    * 1st Character  
      * `-` → file
      * `d` → directory
      * `l` → symlink
    * 2,3,4 characters gives the permissions assigned to User/Owner of the file.
        * `rwx` → read, write and execute permissions assigned to the user/owner.
    * 5,6,7 characters gives the permissions assigned to Group of the file.
        * `r-x` → read and execute permissions assigned to the group.
    * 8,9,10 characters gives the permissions assigned to Others.
        * `---` → No permissions are assigned to others.
    * `r` → read
    * `w` → write
    * `x` → execute

* **Directory Permissions** 
    * Directory with `r` Permission → can list names (ls)
    * Directory with `x` Permission → can enter/traverse (cd) and access entries
    * Directory with `w` Permission → can create/delete/rename entries (usually needs x too)

* **Sticky Bit**
  * Users can create files there, but can only delete their own files (even if directory is writable)
    
* **Commands**
    * `chmod` → Changes the permissions.
    * `chown` → Changes the owner.
    * `umask` →
 
## Users, Groups, Sudo

* `User` → Owns processes/files.
* `Groups` → Allow shared access.
* `sudo` 
  * Lets approved users run commands as root.
  * Rules are in `/etc/sudoers` and `/etc/sudoers.d/*`
  * Edit with visudo (prevents breaking sudo)
    
* **Commands**
  * `id` →
  * `whoami` →
  * `groups` →
  * `getent passwd <user>` →
  * `getent group <group>` →
  * `adduser user_name` →
  * `groupadd group_name` →
  * `usermod -aG group_name user_name` →
  * `sudo` →
  * `su - user_name` →
 








