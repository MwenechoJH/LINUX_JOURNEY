# LINUX_JOURNEY
This will be short documentation of my Linux journey

I plan on including nearly everything, starting from my first command, `cd`, which of course I first learnt when working with the windows command line.

## The First Steps
I started by reading documentation about what Linux is.
I managed to understand that what most people call linux is actually just the **Kernel**.
The **Kerenal** is simply what is responsible for interacting with the hardware of the computer.
What most people call the Linux operating system is simply the kernal combined with other software.

## Philosophy
**Everything is a file**

**small, single-purpose prgograms**

**programs can be chained** - complex tasks can be done thanks to the ability combine all these tools

**avoid captive user interface**

**configuration data is stored a text file**

## Components
**bootloader**
**OS Kernel**
**Daemons**- run in the background for the system to actually operate
**OS shell**- the cammand language interpreter AKA command line
**Graphics Server** - provides graphical sub-system (server)
**Window Manager** - AKA GUI
**Utilities** - apps that perform a particular function forthe user or another program

## Architecture 
**Hardware**

**Kernel**

**Shell**

**System Utility**

## FileSystem
**/** - The root directory, contains files that boot the os and boot the files used to runt he system

**/root**


**/**	The top-level directory is the root filesystem and contains all of the files required to boot the operating system before other filesystems are mounted, as well as the files required to boot the other filesystems. After boot, all of the other filesystems are mounted at standard mount points as subdirectories of the root.

**/bin**	Contains essential command binaries.

**/boot**	Consists of the static bootloader, kernel executable, and files required to boot the Linux OS.

**/dev**	Contains device files to facilitate access to every hardware device attached to the system.

**/etc**	Local system configuration files. Configuration files for installed applications may be saved here as well.

**/home**	Each user on the system has a subdirectory here for storage.

**/lib**	Shared library files that are required for system boot.

**/media**	External removable media devices such as USB drives are mounted here.

**/mnt**	Temporary mount point for regular filesystems.

**/opt**	Optional files such as third-party tools can be saved here.

**/root**	The home directory for the root user.

**/sbin**	This directory contains executables used for system administration (binary system files).

**/tmp**	The operating system and many programs use this directory to store temporary files. This directory is generally cleared upon system boot and may be deleted at other times without any warning.

**/usr**	Contains executables, libraries, man files, etc.

**/var**	This directory contains variable data files such as log files, email in-boxes, web application related files, cron files, and more.


## Shell
The thing that we think is the CLI <br>
It provide text based input/output interface between user and kernel<br>

**Terminal Emulators** - These are software that emulate the function of a terminal.<br>
The terminal acts as a point of communication with the shell.<br>




## Commands
When working with the linux terminal, we normlly deal with commands. In my own understanding, these are short and structured phrases used to interact with the system.
The first commands i was intrduced to are:
`cd`
`pwd`
`whoami`
`sudo apt update`
`sudo apt upgrade`

Flags are also anther thing used together with these commands. e.g. `-l`, `-o`, `-q`


## Navigation
After learning the Secrets of what Linux is, I delved into navigation of the system. During which I learnt basic commands like:
`pwd` -Which prints the *current working directory* <br>
`cd` - Which simply *changes the working directory* <br>
`ls` - Which lists all the directories and files in a directory <br>
`rm` - This removes a file <br>
`mkdir` this created a directory <br>
`rmdir` - this deletes an empty directory <br>


## File Handling
`touch` this is used to create file <br>
`cat` - this is used to read a file <br>
`nano` - this command is used to open the nano editor which is one of the default file editors in linux <br>
`cp` - copies a file <br>
`mv` - moves a file <br>



### TERMINAL vs SHELL vs CONSOLE
The **Shell** is the **command-line interpreter** that interacts wiht the operating system.
It interprates... executes commands, runs scripts, and manages processes.

The **terminal** is a program (GUI app) that provides a text-based interface to interact with the shell<br>
**Terminal emulators** are used in modern systems since the physical ones are rare.<br>
The terminal sends user input to the shell and displays the output.<br>

The **Console** refers to *physical hardware* (keyboard & monitor) directly connected to the system<br>
In Linux, it can also mean  the **Virtual console(TTY)**
It can also mean the **Serial Console**<br>
The console is a **low-level interface** that the system uses for direct communication.

**summary**
**Terminal**: The window/program that displays the interface.

**Shell**: The command interpreter running inside the terminal.

**CLI**: The text-based interface you use — provided by the shell, shown in the terminal.

**Console**: Broad term for a text-based interface or system interface- like a terminal is an example of a console