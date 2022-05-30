# battray-notification-app
  This program notify you when your battery charging percentage above 90%.
  This helps you to stop overcharging the battery
  As no overcharging and no full charging, It will increase your battery life span


In order to run your program in background without showing terminals 
follow this steps-

1. create a .bat and .vbs file for your project.
2. In .bat file write code
          add @echo off
          python C:\..\file.py    -- your python file path
          @pause
3. In .vbs file
          Add CreateObject("Wscript.Shell").Run "C:\project\batnot.bat", 0 , True

4.Now all set-
     go to 
        start--> search for registery editor
        In registery editor go to --> Computer\HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Run
        rightclick and select new ---> string value enter your project name
        double click to edit string ---> IN value name give full path of your .vbs file

5. Restart your system
