### Log Analysis Project
**Udacity Project 3: Log Analysis Project**

This project is been build for internal reporting tool for a newspaper site which reads from the database and gives the answer for below question.
1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?

** Repository:** In order to access this project, clone the github repository (https://github.com/LokeshDK/Log_Analysis) , unzip newsdata.zip and navigate to cloned folder from 
the Terminal (Git Bash if you are using windows/Terminal if you are using Mac/Linux) and follow below steps to get the desired result.

**Pre-Requisite**: Install Vagrant 1.9.2 or higher and Oracle VirtualBox 4.3.0 or higher in your machine before accessing through git hub.

1. Type `vagrant up` into the terminal and wait for vagrant to download all necessary data and create virtual machine on your system. (It will take time 
depending on your internet connection.)
2. Once, download is complete type `vagrant ssh` in order to login into linux.
3. In Terminal, type `cd vagarant/`.
4. Type `cd catalog/`.
4. Type `cd Log Analysis/`.
5. Type `ls` and make sure newsdata.py file is appearing. (If not download the files from repository mentioned in Repository section and paste it in catalog 
folder.)
6.Type command `psql -d news -f newsdata.sql` in terminal.
7. After db been configured press ctrl + c to quit sql.
8. As some db views are created, therefore type `psql -d news -f create_views.sql` before running py file.
9. Once views has been created, then type `python3 newsdata.py`.

You get the desired result in the sequence once the execution is completed.