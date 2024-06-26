<!-- Dcoker Theories -->

### What is Docker?

A platform for building, running and shipping applications.

- Problems docker solves:
  - application works on one machine and not works on another machine.

So its an isolated environment, where everything is segregated like all dependencies and all.

### vitual machines vs Containers

<table><tr><td class="border_l border_r border_t border_b selected"><div class="wrap"><div class="" contenteditable="false" style="margin: 10px 5px;"><p><span>Virtiual Machine</span></p></div></div></td><td class="border_l border_r border_t border_b selected"><div class="wrap"><div class="" contenteditable="false" style="margin: 10px 5px;"><p><span>Containers</span></p></div></div></td></tr><tr><td class="border_l border_r border_t border_b selected"><div class="wrap"><div class="" contenteditable="false" style="margin: 10px 5px;"><p><span>An Abstraction of a Machine.</span></p><p><span>(Physical Hardware)</span></p></div></div></td><td class="border_l border_r border_t border_b selected"><div class="wrap"><div class="" contenteditable="false" style="margin: 10px 5px;"><p><span>An isolated environment</span></p><p><span>for running an application</span></p></div></div></td></tr><tr><td class="border_l border_r border_t border_b selected"><div class="wrap"><div class="" contenteditable="false" style="margin: 10px 5px;" spellcheck="false"><p><span>For running VMs need hypervisor</span></p></div></div></td><td class="border_l border_r border_t border_b selected"><div class="wrap"><div class="" contenteditable="false" style="margin: 10px 5px;"><p><span>Uses an existing kernel or</span></p><p><span>same hardware</span></p></div></div></td></tr><tr><td class="border_l border_r border_t border_b selected"><div class="wrap"><div class="" contenteditable="false" style="margin: 10px 5px;"><p><span>Resorce intesive</span></p></div></div></td><td class="border_l border_r border_t border_b selected"><div class="wrap"><div class="" contenteditable="false" style="margin: 10px 5px;"><p><span>Are lightweights</span></p></div></div></td></tr></table>

### Docker Architecture

Client -RESTapi-> Docker Engine

A kernel manages application an hardware resources.

Linux -Run-> Linux kernel
Windows -Run-> Windows, Linux both
MAC -Run-> Linux VM

### Docker Workflow

- Application folder
- Add Dockerfile to the application folder

  - Dockerfile includes setof instructions
  - this instructions helps to convert app into an image

- Image would be:

  - A cut-down os
  - A runtime environment (e.g. Node, Python)
  - Application files
  - Third party liabraries
  - Environment variables

- Image loaded inside an containers

  - Container is like a filesystem or an os

- Dec ---> Registry(Docker hub) ---> Test/prod

### Docker in action

- Dockerfile structure

  - create Dockerfile

    - FROM baseImage

    - WORKDIR /the/workdir/path

    - COPY source dest

    - CMD [ "executable" ]

  - Commands
    - Docker Build (Conver app into an image)
      `docker build -t <name>`
    - check images
      `docker images` | `docker image ls`
    - running an container
      `docker run <image-name>`

### Linux Commands

- Why linux, because docker is based on linux file system

**Linux Distributions**

1. Ubuntu
2. Debian
3. Alpine
4. Fedora
5. CentOS

and thousands more...

**Running Linux**

- Pull the ubuntu os from docker hub `docker pull ubuntu` | `docker run ubuntu`

- check running processes or containers `docker ps`
- check all processess `docker ps -a`
- running container in interactive mode `docker run -it ubuntu` this will open the ubuntu shell

- Shell Prompt `root@b7ed4cd7f7af:/#` in this line **root**=root user(all previleges) **b7ed4cd7f7af** is a machine name give by docker **/** forward slash is root file path and **#** means i have highest privileges

- linux commands
  - `echo hello` just like print in python
  - `whoami` tells user name
  - `echo $0` tells bash directory
  - `history` returns commands history for using commands from list `!<commands number>`

**Managing packages**

- Package managers

  - NPM
  - YARN
  - PIP

- In Ubuntu we have apt for package management
  - Commands
    - `apt` | `apt-get`
    - `apt-list` - list of packages
    - `apt install <package name>`
    - if not found run `apt update` again reinstall
    - remove package `apt remove <package name>`

### Linux File System

- /
  - /bin = All the application files
  - /boot = booting related
  - /dev = devices
  - /etc = editable text configuration
  - /home = user wise home directories
  - /root = root user home directories
  - /lib = library dependency
  - /var = variables
  - /proc = processors

### Navigating the file system

- `pwd` = print working directory
- `ls` = list of directories
  - `ls -1` = vertical lising
  - `ls -l` = list of full details
  - `cd` = change directory
  - `ls /bin` = checking list of directories in a particular folder
  - `cd ~` = home directory for all users

### Manipulating Files and Directories

- Create Directory
  - `mkdir <directory name>`
- Move or Rename Directory or File
  - `mv <current file/dir name> <changing name>`
- create file
  - `touch <filename>` or can create multiple files `touch <file1> <file2> <file3> ...`
- remove file directory
  - `rm <file or directory name>`
  - multiple files `rm file*` it means file name start with file
  - `rm -r <dir name>` this will delete content with directory

### Editing and Viewing Files

- Commands
  - `nano <filename>` for editing file.
  - `cat <file name>` for viewing file at once.
  - `more <file name>` for viewing file as per the pages (use `space`) for next page
  - `less <file name>` same as more but yo can go up and down using arrows

### Redirection

- `cat file1.txt > file2.txt` so as we know that `cat` command prints out the output in a terminal, but using `>` this sign we can redirect the output to a new file. we can use multiple files as well.
- E.X
  - `cat file1.txt file2.txt > combined.txt`
  - `echo hello > hello.txt`
  - `ls -1 > files.txt`


### Searching for a Text

**grep** : **Global Regular Expression Print**

- Commands:
  - `grep <text for search> <file name>`
  - `grep -i hello file1.txt`
  - `grep -i hello file*` starts with file
  - `grep -i -r hello .` searching recursively in current directory
  - `cat notes.md | grep grep`

### Finding Files and Directories

- Commands:
  - `find` return all the files and directories.
  - `find -type d` return all the directories
  - `find -type f` return all the files
  - `find -type f -name <case-sensitive file name>` return files to the particular name we can use patterns also.
  - `find -type f -iname <incase-sensitive file name>`


### Chaining Commands

- `; semicolon` example `mkdir test; cd test; echo done` this goes every commands and if one comands fails it goes to other command and execute it

- `&& and` example `cd test && code .` need to be both command true, if one fails others are not going to execute

- `|| or` example `mkdir test || echo first command not executed` either one going to executed

- `| pipe` example  `ls /bin | less` first command are going to be input for next command

- `\ backslash` this command uses for next line commands example `mkdir test;\ cd test;\ echo done`

### environment variables

- Commands:
  - `printenv` return all environment variables
  - `printenv <variable name>` return specified environment variable
  - `echo $<env var. name>` return specified environment variable
  - `export <env key=value>` this sets new env variable