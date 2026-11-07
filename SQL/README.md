# Relational Database Management Systems & SQL Lab

A comprehensive collection of **Structured Query Language (SQL)** scripts covering relational database schemas, integrity constraints, multi-table joins, nested subqueries, ACID transaction management, and complex data retrieval queries.

---

## 📌 Overview

Relational databases are the bedrock of enterprise data infrastructure and machine learning feature storage:
- **Data Definition Language (DDL):** Database creation, table schemas, primary keys, unique constraints, and default values.
- **Data Manipulation & Querying (DML & DQL):** Multi-table queries, filtering (`WHERE`, `LIKE`, `IN`, `BETWEEN`), sorting (`ORDER BY`), grouping (`GROUP BY`, `HAVING`).
- **Relational Joins:** Combining normalized entities using `INNER JOIN`, `LEFT JOIN`, `RIGHT JOIN`, `FULL JOIN`, and self joins.
- **Nested Subqueries:** Scalar subqueries, subqueries with aggregates (`AVG`, `COUNT`), and correlated subqueries.
- **ACID Transactions:** Atomic operations, `START TRANSACTION`, `COMMIT`, and `ROLLBACK` for financial consistency.

---

## 📁 SQL Script Catalog

| Script | Category | Description |
|---|---|---|
| [`Basic_of_SQL.sql`](Basic_of_SQL.sql) | DDL / Basics | Creating and dropping databases (`CREATE DATABASE IF NOT EXISTS`), context selection (`USE`), and viewing table metadata. |
| [`table_Queries.sql`](table_Queries.sql) | Schema Design | Complete user schema design (e.g., social media profile table) with `PRIMARY KEY`, `UNIQUE`, `NOT NULL`, and `DEFAULT` column constraints. |
| [`Select_age.sql`](Select_age.sql) | Basic Queries | Conditional data retrieval filtering records based on demographic criteria. |
| [`JOINS.sql`](JOINS.sql) | Relational Joins | Joining normalized `customers` and `orders` tables: Inner, Left Outer, Right Outer, and Full Joins analyzing customer spending. |
| [`SubQueries.sql`](SubQueries.sql) | Advanced Queries | Filtering records above average order thresholds and correlated subqueries computing per-customer order totals. |
| [`Transaction_account.sql`](Transaction_account.sql) | ACID Transactions | Bank transfer simulation demonstrating atomicity: deducting balance, crediting recipient, verifying funds, and issuing `COMMIT` or `ROLLBACK`. |
| [`Practice_set_SQL.sql`](Practice_set_SQL.sql) | Applied Practice | Comprehensive problem set testing filtering, aggregates, sorting, and multi-condition SQL clauses. |

---

## 🛠️ Execution & Environment Setup

These scripts are compatible with **MySQL**, **PostgreSQL**, **MariaDB**, or **SQLite** (with minor dialect adjustments).

### Running in MySQL CLI / Workbench:
```bash
mysql -u root -p < SQL/Basic_of_SQL.sql
mysql -u root -p < SQL/table_Queries.sql
mysql -u root -p < SQL/JOINS.sql
```

### Or run directly inside VS Code:
Install the **SQLTools** or **MySQL** extension, connect to your local database server, and execute scripts interactively.

---

## 💡 Key SQL Patterns Demonstrated

### 1. Correlated Subquery
```sql
-- Compute order counts dynamically for each customer
SELECT name,
    (
        SELECT COUNT(*)
        FROM orders o
        WHERE o.customer_id = c.customer_id
    ) AS order_count
FROM customers c;
```

### 2. ACID Transactional Bank Transfer
```sql
START TRANSACTION;

-- Deduct $100 from Sender (Adam)
UPDATE account SET balance = balance - 100 WHERE id = 1;

-- Credit $100 to Receiver (Bob)
UPDATE account SET balance = balance + 100 WHERE id = 2;

-- Ensure no negative balances occur before committing
COMMIT;
```
