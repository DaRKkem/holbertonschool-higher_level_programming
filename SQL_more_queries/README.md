# SQL -- More Queries

![MySQL](https://img.shields.io/badge/MySQL-8.0-orange)

```sql
SELECT tv_shows.title FROM tv_shows INNER JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id;
```

Advanced MySQL concepts including user and privilege management, column constraints, JOINs across multiple tables, subqueries, and aggregation with the `hbtn_0d_tvshows` database schema (shows and genres).

---

## Tasks

### 0. My privileges!
**File:** `0-privileges.sql` -- `SHOW GRANTS FOR user@host;`

### 1. Root user
**File:** `1-create_user.sql` -- `CREATE USER` with a password.

### 2. Read user
**File:** `2-create_read_user.sql` -- Creates a database and a user with `SELECT` privilege only.

### 3. Always a name
**File:** `3-force_name.sql` -- Creates a table with a `NOT NULL` constraint.

### 4. ID can't be null
**File:** `4-never_empty.sql` -- Creates a table with a `DEFAULT` value for `id`.

### 5. Unique ID
**File:** `5-unique_id.sql` -- Creates a table with a `UNIQUE` constraint on `id`.

### 6. States table
**File:** `6-states.sql` -- Creates the `states` table (`id` INT AUTO_INCREMENT, `name` VARCHAR(256) NOT NULL).

### 7. Cities table
**File:** `7-cities.sql` -- Creates the `cities` table with a `FOREIGN KEY` referencing `states(id)`.

### 8. Cities of California
**File:** `8-cities_of_california_subquery.sql` -- Uses a subquery to find all cities of California.

### 9. Cities by states
**File:** `9-cities_by_state_join.sql` -- `INNER JOIN` between `cities` and `states`.

### 10. Genre ID by show
**File:** `10-genre_id_by_show.sql` -- `INNER JOIN` across `tv_shows`, `tv_show_genres`, and `tv_genres`.

### 11. Genre ID for all shows
**File:** `11-genre_id_all_shows.sql` -- `LEFT JOIN` so every show appears even without a genre.

### 12. No genre
**File:** `12-no_genre.sql` -- Shows with a `NULL` genre (no linked genre).

### 13. Number of shows by genre
**File:** `13-count_shows_by_genre.sql` -- `COUNT` + `GROUP BY` + `JOIN` to tally shows per genre.

### 14. My genres
**File:** `14-my_genres.sql` -- All genres linked to the show "Dexter".

### 15. Only Comedy
**File:** `15-comedy_only.sql` -- Filter shows by genre name "Comedy".

### 16. Shows and their genres
**File:** `16-shows_by_genre.sql` -- Full join listing every show alongside every genre (all rows from both tables).

---

## Key Concepts

- User privileges: `CREATE USER`, `GRANT`, `SHOW GRANTS`
- Column constraints: `NOT NULL`, `DEFAULT`, `UNIQUE`, `FOREIGN KEY`
- JOINs: `INNER JOIN`, `LEFT JOIN`
- Subqueries
- Multi-table aggregation with `COUNT` and `GROUP BY`
- Database schema design with foreign key relationships

---

Repository

GitHub repository: holbertonschool-higher_level_programming
Directory: SQL_more_queries

---

Author

Damien Rossi - DaRKkem — Holberton School, cohort C28, Auvergne-Rhône-Alpes
