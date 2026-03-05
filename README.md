# 📝 Todo App — Odoo 17 Custom Module

A simple To-Do module built on Odoo 17 that allows users to create, assign, and track tasks through a clean interface.

---

## Features

- Create and manage tasks with a name, description, due date, and assignee
- Track task progress through three statuses: **New → In Progress → Completed**
- Status bar with contextual action buttons on the form view
- List view showing all tasks at a glance
- Search by Task Name or Assigned To
- Filter tasks by Status (New, In Progress, Completed)
- Group tasks by Assigned To, Status, or Due Date

---

## Tech Stack

- **Odoo 17**
- **PostgreSQL 15**
- **Docker & Docker Compose**
- **WSL (Windows Subsystem for Linux)**

---

## Project Structure

```
todo-odoo/
├── docker-compose.yml
├── .env
├── .gitignore
├── README.md
└── extra-addons/
    └── todo_app/
        ├── __init__.py
        ├── __manifest__.py
        ├── models/
        │   ├── __init__.py
        │   └── todo_task.py
        ├── views/
        │   ├── base_menu.xml
        │   └── todo_views.xml
        ├── security/
        │   └── ir.model.access.csv
        └── static/
            └── description/
                └── icon.png
```

---

## Getting Started

### Prerequisites

- Docker Desktop installed and running
- WSL2 enabled on Windows
- Git installed

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/todo-odoo.git
cd todo-odoo
```

### 2. Start the containers

```bash
docker compose up -d
```

### 3. Create the database

Go to **http://localhost:8070** and fill in:

| Field | Value |
|---|---|
| Master Password | admin |
| Database Name | todo |
| Email | admin@admin.com |
| Password | admin |
| Language | English |

Uncheck **Demo data** and click **Create database**.

### 4. Install the module

1. Log in to Odoo
2. Go to **Settings → Activate Developer Mode**
3. Go to **Apps → Update Apps List**
4. Search for **"To-Do"**
5. Click **Install**

### 5. Access the module

Navigate to the **To-Do** menu in the top navigation bar → **All Tasks**.

---

## Module Details

### Model: `todo.task`

| Field | Type | Description |
|---|---|---|
| `name` | Char | Task name (required) |
| `assigned_to` | Many2one | Linked to `res.users` |
| `description` | Text | Task details |
| `due_date` | Date | Task deadline |
| `state` | Selection | New / In Progress / Completed |

### Views

- **List View** — displays all tasks with key fields
- **Form View** — create and edit tasks with status bar and action buttons
- **Search View** — search, filter, and group tasks

---

## Stopping the containers

```bash
docker compose down
```

To stop and remove all data (full reset):

```bash
docker compose down -v
```

---

## Author

**Mohamed** — learning Odoo development 🚀
