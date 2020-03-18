# Log-analysis-project

The Log Analysis Project is a python tool created to query a database called newsdata.sql and produce a report for the following questions:
- What are the top three articles by views
- Who are the authors with the most viewed articles overall.
- On what days were there more than 1% of requests leading to errors

## Tools
Excluding minor modules, the key tools used for this project include the following:
- Virtual Box: https://www.virtualbox.org/wiki/Downloads
- Vagrant: https://www.vagrantup.com/downloads.html 
- Vagrant File by Udacity: https://github.com/udacity/fullstack-nanodegree-vm/blob/master/vagrant/Vagrantfile
- PostgreSQL
- Python3
- Visual Studio Code
- Psycopg2

## SetUp
The easiest to get started with the right environment is to clone the Udacity full stack vm repo: https://github.com/udacity/fullstack-nanodegree-vm 
- Make sure you have the tools identified above installed (or your favourite alternatives) and set up. Some require a pip3 or sudo -apt install.  
- Make sure you're in the /vagrant directory based on the Udacity repo you cloned earlier. 
- Enter 'vagrant up' into your terminal to get vagrant started up
- Enter 'vagrant ssh' to ssh into your linux instance
- Enter 'psql -d news -f newsdata.sql' to connect with the database
- If you want to test out the reporting tool rather than make one, clone my log-analysis repo or download the dbscript.py file and place it in the /vagrant directory
- Enter 'python3 dbquery.py' in your terminal to run it

## Ackowledgement:

I'd like to acknowledge Udacity as most of the processes I followed are based on the lectures. I also made use of Psycopg and PostgreSQl documentations and some stack overflow searches when stuck.   

