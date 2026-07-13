# Python Object-Relational Mapping (ORM)

Bridging Python and MySQL using two approaches: raw SQL via the `MySQLdb` driver, and the `SQLAlchemy` ORM. The project focuses on CRUD operations on `states` and `cities` tables, SQL injection prevention, and model-based database interaction.

---

## Tasks

### MySQLdb (raw SQL)

| Task | File | Description |
|------|------|-------------|
| 0    | `0-select_states.py` | Lists all states from `hbtn_0e_0_usa`. |
| 1    | `1-filter_states.py` | Filters states whose name starts with `N`. |
| 2    | `2-my_filter_states.py` | Filters states using user input (vulnerable to SQL injection). |
| 3    | `3-my_safe_filter_states.py` | Same as task 2 but uses parameterised queries to prevent SQL injection. |
| 4    | `4-cities_by_state.py` | Lists all cities with their state names via a join. |
| 5    | `5-filter_cities.py` | Lists cities of a given state. |

### SQLAlchemy (ORM)

| Task | File | Description |
|------|------|-------------|
| 7    | `7-model_state_fetch_all.py` | Fetches all `State` objects. |
| 8    | `8-model_state_fetch_first.py` | Fetches the first `State` object. |
| 9    | `9-model_state_filter_a.py` | Filters `State` objects containing the letter `a`. |
| 10   | `10-model_state_my_get.py` | Retrieves a `State` by name. |
| 11   | `11-model_state_insert.py` | Inserts a new `State`. |
| 12   | `12-model_state_update_id_2.py` | Updates the name of `State` with `id = 2`. |
| 13   | `13-model_state_delete_a.py` | Deletes `State` objects with names containing `a`. |
| 14   | `14-model_city_fetch_by_state.py` | Lists all `City` objects, joined with their `State`. |

### Model definitions

- `model_state.py` -- SQLAlchemy model for the `states` table
- `model_city.py` -- SQLAlchemy model for the `cities` table with a foreign key to `states`

---

## Key Concepts

- `MySQLdb` driver: connection, cursor, execute, fetchall
- SQL injection and parameterised queries (`cursor.execute("...", (param,))`)
- `SQLAlchemy` ORM: `declarative_base`, `Column`, `Integer`, `String`, `ForeignKey`, `relationship`
- Session management: `Session`, `session.add()`, `session.commit()`, `session.close()`
- Query filtering: `filter()`, `filter_by()`, `order_by()`
- Joining models via `relationship()` and `joinedload()`
- `engine` creation and `MetaData`

---

## Author

**Damien Rossi** -- **[DaRKkem](https://github.com/DaRKkem)** -- Holberton School, cohort C28, Auvergne-Rhone-Alpes
