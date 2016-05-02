# SQL
*Structured Query Language: used to manage data stored in relational databases*

## Definitions
* **relational database:** database that organizes information into one or more tables
* **table:** collection of data organized into rows and columns
* **column:** set of data values of particular type
* **row:** single record in a table
* common data types: Integer, Text, Date, Real
* **statement:** text that the database recognizes as a valid command, always end in a semi-colon `;`
  * **clause/command:** perform specific tasks in SQL

## Commands
| Command        | Example        | Description    |
| :------------- | :------------- | :------------- |
| ALTER TABLE | ALTER TABLE table_name ADD column datatype; | add columns into table |
| AND | SELECT column_name(s) FROM table_name WHERE column_1 = value_1 AND column_2 = value_2; | operator that combines two conditions |
| AS | SELECT column_name AS 'Alias' FROM table_name; | rename column or table using an alias |
| AVG | SELECT AVG(column_name) FROM table_name | aggregate function that returns the average value for numeric column |
| BETWEEN | SELECT column_name(s) FROM column_name BETWEEN value_1 AND value_2; | operator used to filter result set within a range (numbers, text, dates) |
| COUNT | SELECT COUNT(column_name) FROM table_name; | counts number of rows in column where not `NULL` |
| CREATE TABLE | CREATE TABLE table_name (column_1 datatype, column_2 datatype, column_3 datatype); | creates new table in database w/ name of table and name of each column |
| DELETE | DELETE FROM table_name WHERE some_column = some_value; | remove rows from table |
| GROUP BY | SELECT COUNT(*) FROM table_name GROUP BY column_name; | used with aggregate functions, with `SELECT` to arrange identical data into groups |
| INNER JOIN | SELECT column_name(s) FROM table_1 JOIN table_2 ON table_1.column_name = table_2.column_name; | combine rows from different tables if join condition is true |
| INSERT | INSERT INTO table_name (column_1, column_2, column_3) VALUES (value_1, 'value_2', value_3); | add a new row into the table |
| LIKE | SELECT column_name(s) FROM table_name WHERE column_name LIKE pattern; | operator used with `WHERE` to search for specific pattern in column |
| LIMIT | SELECT column_name(s) FROM table_name LIMIT number; | specify max number of rows the result set will have |
| MAX | SELECT MAX(column_name) FROM table_name; | returns largest value in column |
| MIN | SELECT MIN(column_name) FROM table_name; | returns smallest value in column |
| OR | SELECT column_name FROM table_name WHERE column_name = value_1 OR column_name = value_2; | either condition to be true |
| ORDER BY | SELECT column_name FROM table_name ORDER BY column_name ASC/DESC; | sort result set by column alpha or numerically, ascending or descending |
| OUTER JOIN | SELECT column_name(s) FROM table_1 LEFT JOIN table_2 ON table_1.column_name = table_2.column_name; | combine rows from different tables even if join condition is not met, every row in left table is returned, `NULL` values fill the columns from the right table |
| ROUND | SELECT ROUND(column_name, integer) FROM table_name; | rounds values in column to number of decimals specified by integer |
| SELECT | SELECT column_name FROM table_name; | fetch data from database, all queries begin with SELECT |
| SELECT DISTINCT | SELECT DISTINCT column_name FROM table_name; | returns unique values in the specified column(s) |
| SUM | SELECT SUM(column_name) FROM table_name; | returns sum of all values in column |
| UPDATE | UPDATE table_name SET some_column = some_value WHERE some_column = some_value; | edit rows in table |
| WHERE | SELECT column_name(s) FROM table_name WHERE column_name operator value; | only when condition is true |  
