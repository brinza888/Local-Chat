# Local Chat v0.2.1
Working releases you can find in master branch

This software is licensed under the BSD 3-Clause License (see LICENSE file)

- ## 1. Server
  - Chat's main unit
  - Server will resend messages from user to other joined users
  - ### 1.1 Setup server
    - Start file "Serer.py"
    - Write IP of your device in local network (use ipconfig in windows cmd.exe to find your ip)
    - Then setup console to use admin commands (see par. 3)
- ## 2. Client
  - Use for join server and use chat
  - Client will send message to server. Server will resend messages from user to other joined users
  - ### 2.1 Setup client
    - Start file "Client.py"
    - Write server's IP in the bottom text box and send it
    - If all correct you will get INFO message "Welcome on server: (IP)"
  - ### 2.2 Other functions
    - You will get nick "Guest#ID", ID - is your ID. If you want to change nick type "/setnick [new_nick]"
    - To send messages you can use "Enter" key or click on button "Send"
    - All users/admins commands you can see in par. 5
- ## 3. Console
  - Console use client interface and also starts with "Client.py" file
  - Console available only on same device that server started
  - ### 3.1 Setup console
    - Do all instructions in par. 2.1, but start "Client.py" on same device that server started!
    - When you joined to server, you will have all admin permissions
    - Only one client can get console
    - All admins commands you can see in par. 5
- ## 4. Messages
  - Class that uses for all text messages in chat
  - All messages have type (text messages is DEFAULT)
  - ### 4.1 DEFAULT
    - This type used when user send text messages to other users
    - Has datetime marker "[day.month hours:minutes" ("[1.1 00:00]")
    - Datetime marker sets when user (client) get message! (not when sender send it!)
    - Example: "[1.1 12:00] User: Hello world!"
  - ### 4.2 Other groups
    - All other message groups usess for informate users
    - Havent datetime marker
    - Example: "ERROR: User not found!"
    - #### 4.2.1 INFO
      - Used when it is necessary to inform a specific user about an event (eg. greeting message)
      - Has prefix INFO
    - #### 4.2.2 ERROR
      - Uses when need to show error message that will describe (eg invalid argument)
      - Has prefix ERROR
    - #### 4.2.3 BCAST
      - Uses when need to inform all users abou an event (eg. banned user)
      - Has prefix BCAST
- ## 5. Commands
  - Commands can be executed only from the client (server not execute commands)
  - Syntax to execute command named "command" with N arguments: /command arg1 arg2 arg3 ... argN
  - Default commands can execute anyone
  - Admin commands can execute only users with admin permissions
    - ### 5.1 Default commands
      - help - shows all available commands
      - setnick [new_nick] - change user's nick to "new_nick"
      - list - returns nicks of users who are online
      - whois [nick] - shows user IP with given nick
    - ### 5.2 Admin commands
      - admin [nick] - give admin permissions to user with nick "nick"
      - ban [ip] - ban given IP address and kick user with this IP from server
      - unban [ip] - unban given IP
    - ## 5.3 Adding your own commands
      - Create file name.py in directory Commands (name is name of your command)
      - Init 3 variables:
        - help_txt - contains text that will shown on use /name help (name is name of yout command)
        - isadmin - boll var that define paermissions to use command. If true - inly admins can use it
        - syntax - contains text, that will shown when command return SHOW_USAGE callback
      - Create function execute(caller, args, ex):
        - caller - contains object (class User) with caller's info
        - args - contains arguments that given after command name
        - ex - contains object (class Executor)
        - in function you can write code that will execute
        - "return ex.INVALID_ARGS" - will stop executing command and return to caller "Invalid argument!"
        - "return ex.SHOW_USAGE" - will stop executing command and return to caller text, placed in syntax variable
        - Also you can use ex.server combination to get server object and get server properties (eg. users array)
      - As example you can see default commands
      
---
Created by Brinza Bezerukoff
Vk: vk.com/brinza888
Mail: bezrukoff888@gmail.com
