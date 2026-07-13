# SQL -- Introduction

A foundational project covering MySQL Data Definition Language (DDL) and Data Manipulation Language (DML). Tasks progress from creating and dropping databases to inserting, selecting, updating, deleting records, and using aggregate functions, filtering, grouping, and sorting.

---

## Tasks

### 0. List databases
**File:** `0-list_databases.sql` -- `SHOW DATABASES;`

Lists all databases on the MySQL server.

### 1. Create a database
**File:** `1-create_database_if_missing.sql` -- Creates a database if it does not already exist.

### 2. Delete a database
**File:** `2-remove_database.sql` -- `DROP DATABASE` statement.

### 3. List tables
**File:** `3-list_tables.sql` -- `SHOW TABLES;`

### 4. First table
**File:** `4-first_table.sql` -- `CREATE TABLE` with columns.

### 5. Full table description
**File:** `5-full_table.sql` -- `SHOW CREATE TABLE` to display the statement that created the table.

### 6. List all rows
**File:** `6-list_values.sql` -- `SELECT * FROM <table>;`

### 7. Insert a row
**File:** `7-insert_value.sql` -- `INSERT INTO <table> VALUES (...);`

### 8. Count rows
**File:** `8-count_89.sql` -- `SELECT COUNT(*) FROM <table> WHERE id = 89;`

### 9. Full creation
**File:** `9-full_creation.sql` -- `CREATE TABLE` followed by `INSERT` of multiple rows.

### 10. List by best
**File:** `10-top_score.sql` -- `SELECT score, name FROM <table> ORDER BY score DESC;`

### 11. Select the best
**File:** `11-best_score.sql` -- `SELECT score, name FROM <table> WHERE score >= 10 ORDER BY score DESC;`

### 12. Cheating is bad
**File:** `12-no_cheating.sql` -- `UPDATE <table> SET score = 10 WHERE name = "Bob";`

### 13. Score too low
**File:** `13-change_class.sql` -- `DELETE FROM <table> WHERE score <= 5;`

### 14. Average
**File:** `14-average.sql` -- `SELECT AVG(score) AS average FROM <table>;`

### 15. Number by score
**File:** `15-groups.sql` -- `SELECT score, COUNT(*) AS number FROM <table> GROUP BY score ORDER BY number DESC;`

### 16. Say my name
**File:** `16-no_link.sql` -- `SELECT score, name FROM <table> WHERE name IS NOT NULL ORDER BY score DESC;`

---

## Key Concepts

- DDL: `CREATE`, `DROP`, `ALTER`
- DML: `SELECT`, `INSERT`, `UPDATE`, `DELETE`
- Filtering: `WHERE`, `LIKE`, `IS NOT NULL`
- Ordering: `ORDER BY`
- Grouping: `GROUP BY`
- Aggregate functions: `AVG()`, `COUNT()`
- NULL handling

---

## Author

**Damien Rossi** -- **[DaRKkem](https://github.com/DaRKkem)** -- Holberton School, cohort C28, Auvergne-Rhone-Alpes
