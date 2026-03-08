# 📝 Todo App — Odoo 17 Custom Module

A custom Odoo 17 module for managing tasks with timesheet tracking, automated alerts, PDF reports, and a full task lifecycle workflow.

---

## Features

- Create and manage tasks with a name, description, due date, assignee, and estimated time
- Track task progress through a full lifecycle: **New → In Progress → Completed → Closed**
- Status bar with contextual action buttons on the form view
- **Reset to New** button to reopen closed tasks
- **Timesheet lines** — log time spent on each task with description and hours
- **Estimated time validation** — blocks saving if total logged time exceeds estimated time
- **Total time** auto-computed from timesheet lines
- **Archiving support** — archive/unarchive tasks via the Action menu
- **Server Action "Close"** — bulk close one or multiple tasks from the list view
- **Cron Job** — runs daily to detect overdue tasks, posts a warning message on the chatter, and flags them as late
- **Tree view color coding** — overdue tasks highlighted in red, in-progress in blue, completed in green
- List view showing all tasks at a glance
- Search by Task Name or Assigned To
- Filter tasks by Status (New, In Progress, Completed, Close)
- Group tasks by Assigned To, Status, or Due Date
- **PDF Report** — print any task with full details and timesheet breakdown

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
        ├── reports/
        │   └── task_reports.xml
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
git clone https://github.com/Mohamedabdelaziz142/task-todo-odoo.git
cd task-todo-odoo
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
| `estimated_time` | Float | Estimated hours to complete |
| `total_time` | Float | Auto-computed sum of timesheet hours |
| `line_ids` | One2many | Linked timesheet lines |
| `active` | Boolean | Supports archiving |
| `is_late` | Boolean | Flagged by cron if task is overdue |
| `state` | Selection | New / In Progress / Completed / Close |

### Model: `todo.lines`

| Field | Type | Description |
|---|---|---|
| `task_id` | Many2one | Linked to `todo.task` |
| `description` | Text | Work description |
| `time_spent` | Float | Hours spent on this entry |

### Views

- **List View** — displays all tasks with color coding for overdue/status
- **Form View** — full task editing with status bar, action buttons, and timesheet tab
- **Search View** — search, filter, and group tasks by multiple criteria

### Automation

- **Server Action "Close"** — available in the Action menu on list and form views
- **Cron Job** — runs daily, finds overdue tasks and posts chatter warnings

### Report

- **Task Report (PDF)** — accessible via Print menu on any task, shows task details and full timesheet breakdown

---

## Useful Commands

```bash
# Start containers
docker compose up -d

# Upgrade module
docker compose exec todo-odoo odoo -u todo_app -d todo --stop-after-init --db_host=todo-db --db_user=odoo --db_password=odoo

# Stop containers
docker compose down

# Full reset (removes all data)
docker compose down -v
```

---

## Author

**Mohamed Abdelaziz** — Junior Developer from Cairo, Egypt 🚀  
[LinkedIn](https://www.linkedin.com/in/mohamed-abdelaziz-4a5ab9242/) · [GitHub](https://github.com/Mohamedabdelaziz142)