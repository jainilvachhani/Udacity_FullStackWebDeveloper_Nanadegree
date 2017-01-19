Built a PostgreSQL relational database scheme to store the results of a game tournament. Also provided a number of queries to efficiently report the results of the tournament and determine the winner.

This directory can be initiated with Vagrant (visit vagrantup.com) by executing the command vagrant up within the vagrant/ directory. The test cases can be run by executing the following commands:

•	vagrant ssh
•	cd/vagrant/tournament
•	psql
•	\i tournament.sql
•	\q
•	python tournament_test.py
