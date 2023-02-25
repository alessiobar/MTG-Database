# SQL

## Homework 1 - Database and Queries

Choose an application domain and, using a relational DBMS, build a database. This can be done in two ways:

1. (recommended) use an interesting existing dataset, i.e.: 
- get interesting data from the Web or other sources (e.g., use the Web to look for a whole database, or data that can be easily imported into a relational DBMS) and build a relational database using such data
- formulate a set of SQL queries (about 8-10) over the relational schema
- execute such queries over the database and analyze the results

2. create the schema and the dataset from scratch, i.e.:
- define the relational schema (i.e., write SQL statements to create tables defining attributes, domains, and possibly integrity constaints);
- insert tuples into tables (through SQL statements)
- formulate a set of SQL queries (about 10) over the relational schema
- execute such queries over the database and analyze the results

NOTICE: all datasets are potentially fine EXCEPT MOVIE DATASETS (too many projects used movie DBs in the previous years). 

The work must be done by groups of two students. Students can use publicly available DBMSs like MySQL or PostgreSQL (see below), or other, commercial DBMSs.

The queries defined by the students should comprise all the aspects of SQL queries analyzed during the course lectures and exercises (joins, aggregations, nested queries, queries with negated subqueries). The complexity of the queries produced should be (at least) comparable to the specification appearing in the following exercise on SQL. 

## Homework 2 - SQL evaluation and optimization

Starting from the database developed in the first homework, every group has to identify at least 4 SQL queries that pose performance problems to the DBMS. The students have to show both the "slow" and the "fast" execution of the queries, where the fast version is obtained by:
- adding integrity constraints to one or more tables
- rewriting the SQL query (without changing its meaning)
- adding indices to one or more tables
- modifying the schema of the database
- adding views or new (materialized) tables derived from the existing database tables

Ideally, these queries should be picked from the queries created for the first homework; however, new queries can be considered if none of the previous queries poses performance problems to the DBMS. 
