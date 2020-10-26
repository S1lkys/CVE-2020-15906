# CVE-2020-15906
Writeup of CVE-2020-15906.
Special Thanks to Frederic Mohr(Lastbreach) for your Backend Support.


## Tiki Wiki Cms Groupware 16.x - 21.1 Authentication Bypass by Maximilian Barz
I have found a new vulnerability in TikiWiki Cms Groupware  16.x - 21.1. It allows remote
unauthenticated attackers to bypass the login page which results in a full compromise of Tiki Wiki
CMS. An Attacker is able to bruteforce the Admin account until it is locked. After that an empty
Password can be used to authenticate as admin to get access.

## Affected file: tiki-login.php

## CVSS 3.1 Base Score: 9.3
![CVSS Score](https://github.com/S1lkys/CVE-2020-15906/blob/master/CVSS%203.1.png)

# Walkthrough/ PoC:
### Normal condition
Take a look at the database. This is what the admin looks like after Tiki was installed. (Note that
provpass is empty)
![Step1](https://github.com/S1lkys/CVE-2020-15906/blob/master/Step1.png)

### Step 1
Admin Login Brute Force results in about 15 "Invalid user or password" errors, then the message
should say "The mail cannot be sent" – maybe a verification problem because of to many requests
![Step2](https://github.com/S1lkys/CVE-2020-15906/blob/master/Step2.png)

### Step 2
Keep Brute Forcing, just to be sure. If the Mail cant be send a different error message appears.
Just before the 50th request, the messages change again, now the account is locked.
![Step3](https://github.com/S1lkys/CVE-2020-15906/blob/master/Step3.png)

### Step 3
If we now take a look inside the DB, we can see provpass got set.

![Step4](https://github.com/S1lkys/CVE-2020-15906/blob/master/Step4.png)


### Step 4
Now try another login attempt, but remove the password from the request.
![Burpsuite](https://github.com/S1lkys/CVE-2020-15906/blob/master/Burpsuite.png)
# Result: Admin Access is granted.
![Admin Access](https://github.com/S1lkys/CVE-2020-15906/blob/master/Admin%20Access.png)

A full walkthrough video can be viewed on youtube (Videos are not publicly available.):
https://www.youtube.com/watch?v=v2YEpMsxcbA

PoC Exploit video on youtube:
https://youtu.be/o3blz2US54Y

### Exploit-DB: 
https://www.exploit-db.com/exploits/48927

### Article on Portswigger.net
https://portswigger.net/daily-swig/amp/tikiwiki-authentication-bypass-flaw-gives-attackers-full-control-of-websites-intranets

### Credits:
Maximilian Barz (OSCP), 
Email: mbzra@protonmail.com, 
Twitter: S1lky_1337

