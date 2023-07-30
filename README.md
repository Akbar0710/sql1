C:\Users\k>cd\

C:\>cd xampp

C:\xampp>cd bin
The system cannot find the path specified.

C:\xampp>cd mysql

C:\xampp\mysql>cd bin

C:\xampp\mysql\bin>mysql -u root
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 8
Server version: 10.4.24-MariaDB mariadb.org binary distribution

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]> create database info;
Query OK, 1 row affected (0.001 sec)

MariaDB [(none)]> show databases;
+--------------------+
| Database           |
+--------------------+
| again              |
| bd                 |
| employee           |
| exam               |
| info               |
| information_schema |
| lol                |
| main               |
| mysql              |
| new                |
| new1               |
| oo                 |
| performance_schema |
| phpmyadmin         |
| temp               |
| test               |
| today              |
| univ               |
+--------------------+
18 rows in set (0.009 sec)

MariaDB [(none)]> use info;
Database changed
MariaDB [info]> create table details(regno int(3),name varchar(10),age int(2),phn int(10));
Query OK, 0 rows affected (0.051 sec)

MariaDB [info]> desc details;
+-------+-------------+------+-----+---------+-------+
| Field | Type        | Null | Key | Default | Extra |
+-------+-------------+------+-----+---------+-------+
| regno | int(3)      | YES  |     | NULL    |       |
| name  | varchar(10) | YES  |     | NULL    |       |
| age   | int(2)      | YES  |     | NULL    |       |
| phn   | int(10)     | YES  |     | NULL    |       |
+-------+-------------+------+-----+---------+-------+
4 rows in set (0.022 sec)

MariaDB [info]> desc info;
ERROR 1146 (42S02): Table 'info.info' doesn't exist
MariaDB [info]> insert into details values(061,"arul",21,909090890),(062,"hem",19,83417676),(063,"james",32,90987654);
Query OK, 3 rows affected (0.013 sec)
Records: 3  Duplicates: 0  Warnings: 0

MariaDB [info]> select * from details;
+-------+-------+------+-----------+
| regno | name  | age  | phn       |
+-------+-------+------+-----------+
|    61 | arul  |   21 | 909090890 |
|    62 | hem   |   19 |  83417676 |
|    63 | james |   32 |  90987654 |
+-------+-------+------+-----------+
3 rows in set (0.001 sec)

MariaDB [info]> create table dummy(id int(3),name varchar(8));
Query OK, 0 rows affected (0.047 sec)

MariaDB [info]> desc dummy;
+-------+------------+------+-----+---------+-------+
| Field | Type       | Null | Key | Default | Extra |
+-------+------------+------+-----+---------+-------+
| id    | int(3)     | YES  |     | NULL    |       |
| name  | varchar(8) | YES  |     | NULL    |       |
+-------+------------+------+-----+---------+-------+
2 rows in set (0.023 sec)

MariaDB [info]> drop table dummy;
Query OK, 0 rows affected (0.017 sec)

MariaDB [info]> desc dummy;
ERROR 1146 (42S02): Table 'info.dummy' doesn't exist
MariaDB [info]> alter table details add(marks int(3));
Query OK, 0 rows affected (0.019 sec)
Records: 0  Duplicates: 0  Warnings: 0

MariaDB [info]> desc details;
+-------+-------------+------+-----+---------+-------+
| Field | Type        | Null | Key | Default | Extra |
+-------+-------------+------+-----+---------+-------+
| regno | int(3)      | YES  |     | NULL    |       |
| name  | varchar(10) | YES  |     | NULL    |       |
| age   | int(2)      | YES  |     | NULL    |       |
| phn   | int(10)     | YES  |     | NULL    |       |
| marks | int(3)      | YES  |     | NULL    |       |
+-------+-------------+------+-----+---------+-------+
5 rows in set (0.021 sec)

MariaDB [info]> update details set marks=95 where regno=061;
Query OK, 1 row affected (0.006 sec)
Rows matched: 1  Changed: 1  Warnings: 0

MariaDB [info]> update details set marks=85 where regno=063;
Query OK, 1 row affected (0.006 sec)
Rows matched: 1  Changed: 1  Warnings: 0

MariaDB [info]> update details set marks=85 where regno=062;
Query OK, 1 row affected (0.006 sec)
Rows matched: 1  Changed: 1  Warnings: 0

MariaDB [info]> select * from details;
+-------+-------+------+-----------+-------+
| regno | name  | age  | phn       | marks |
+-------+-------+------+-----------+-------+
|    61 | arul  |   21 | 909090890 |    95 |
|    62 | hem   |   19 |  83417676 |    85 |
|    63 | james |   32 |  90987654 |    85 |
+-------+-------+------+-----------+-------+
3 rows in set (0.000 sec)

MariaDB [info]> insert into details value(064,"kite",19,967854321,89),(065,"thor",909876578,24);
ERROR 1136 (21S01): Column count doesn't match value count at row 2
MariaDB [info]> insert into details value(064,"kite",19,967854321,89),(065,"thor",24,909876578,24);
Query OK, 2 rows affected (0.006 sec)
Records: 2  Duplicates: 0  Warnings: 0

MariaDB [info]> select * from details;
+-------+-------+------+-----------+-------+
| regno | name  | age  | phn       | marks |
+-------+-------+------+-----------+-------+
|    61 | arul  |   21 | 909090890 |    95 |
|    62 | hem   |   19 |  83417676 |    85 |
|    63 | james |   32 |  90987654 |    85 |
|    64 | kite  |   19 | 967854321 |    89 |
|    65 | thor  |   24 | 909876578 |    24 |
+-------+-------+------+-----------+-------+
5 rows in set (0.001 sec)

MariaDB [info]> delete from details where regno=094;
Query OK, 0 rows affected (0.000 sec)

MariaDB [info]> select * from details;
+-------+-------+------+-----------+-------+
| regno | name  | age  | phn       | marks |
+-------+-------+------+-----------+-------+
|    61 | arul  |   21 | 909090890 |    95 |
|    62 | hem   |   19 |  83417676 |    85 |
|    63 | james |   32 |  90987654 |    85 |
|    64 | kite  |   19 | 967854321 |    89 |
|    65 | thor  |   24 | 909876578 |    24 |
+-------+-------+------+-----------+-------+
5 rows in set (0.000 sec)

MariaDB [info]> delete from details where regno=64;
Query OK, 1 row affected (0.006 sec)

MariaDB [info]> select * from details;
+-------+-------+------+-----------+-------+
| regno | name  | age  | phn       | marks |
+-------+-------+------+-----------+-------+
|    61 | arul  |   21 | 909090890 |    95 |
|    62 | hem   |   19 |  83417676 |    85 |
|    63 | james |   32 |  90987654 |    85 |
|    65 | thor  |   24 | 909876578 |    24 |
+-------+-------+------+-----------+-------+
4 rows in set (0.000 sec)

MariaDB [info]> select from details where id=62;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MariaDB server version for the right syntax to use near 'from details where id=62' at line 1
MariaDB [info]> select from details where regno=62;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MariaDB server version for the right syntax to use near 'from details where regno=62' at line 1
MariaDB [info]> select * from details;
+-------+-------+------+-----------+-------+
| regno | name  | age  | phn       | marks |
+-------+-------+------+-----------+-------+
|    61 | arul  |   21 | 909090890 |    95 |
|    62 | hem   |   19 |  83417676 |    85 |
|    63 | james |   32 |  90987654 |    85 |
|    65 | thor  |   24 | 909876578 |    24 |
+-------+-------+------+-----------+-------+
4 rows in set (0.000 sec)

MariaDB [info]> update table details set marks=90 where regno=62;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MariaDB server version for the right syntax to use near 'table details set marks=90 where regno=62' at line 1
MariaDB [info]> update details set marks=90 where regno=62;
Query OK, 1 row affected (0.006 sec)
Rows matched: 1  Changed: 1  Warnings: 0

MariaDB [info]> select * from details;
+-------+-------+------+-----------+-------+
| regno | name  | age  | phn       | marks |
+-------+-------+------+-----------+-------+
|    61 | arul  |   21 | 909090890 |    95 |
|    62 | hem   |   19 |  83417676 |    90 |
|    63 | james |   32 |  90987654 |    85 |
|    65 | thor  |   24 | 909876578 |    24 |
+-------+-------+------+-----------+-------+
4 rows in set (0.000 sec)

MariaDB [info]>
