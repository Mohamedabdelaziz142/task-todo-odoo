# 📝 Todo App — Odoo 17 Custom Module

A custom Odoo 17 module for managing tasks with timesheet tracking, automated alerts, PDF reports, a full task lifecycle workflow, and a RESTful API.

---

## Features

- Create and manage tasks with a name, description, due date, assignee, and estimated time.
- Track task progress through a full lifecycle: **New → In Progress → Completed → Closed**.
- Status bar with contextual action buttons on the form view.
- **Reset to New** button to reopen closed tasks.
- **Timesheet lines** — log time spent on each task with description and hours.
- **Estimated time validation** — blocks saving if total logged time exceeds estimated time.
- **Total time** auto-computed from timesheet lines.
- **Archiving support** — archive/unarchive tasks via the Action menu.
- **Server Action "Close"** — bulk close one or multiple tasks from the list view.
- **Cron Job** — runs daily to detect overdue tasks, posts a warning message on the chatter, and flags them as late.
- **Tree view color coding** — overdue tasks highlighted in red, in-progress in blue, completed in green.
- **Search View** — search, filter, and group tasks by multiple criteria (Assigned To, Status, Due Date).
- **PDF Report** — print any task with full details and timesheet breakdown via the Print menu.
- **RESTful API** — Full CRUD integration for external systems (Postman ready).
- **Bulk Assignment Wizard** — Multi-select tasks and assign them to a user via a pop-up wizard.
- **Security Groups** — Separate permissions for "Users" (see own tasks) and "Managers" (see all tasks).
- **Update Protection** — Prevents editing tasks that are already in 'Completed' or 'Closed' states.
- **Arabic Translation** — Full i18n support for Arabic language interface.

---

## Tech Stack

- Odoo 17
- PostgreSQL 15
- Docker & Docker Compose
- WSL2 (Windows Subsystem for Linux)
- Postman (for API Testing)

---

## Project Structure

```text
todo-odoo/
├── docker-compose.yml
├── .env
├── .gitignore
├── README.md
└── extra-addons/
    └── todo_app/
        ├── __init__.py
        ├── __manifest__.py
        ├── controllers/       # REST API Logic
        │   ├── __init__.py
        │   └── main.py
        ├── wizard/            # Bulk Assign Wizard
        │   ├── __init__.py
        │   ├── todo_assign_task.py
        │   └── todo_assign_task_view.xml
        ├── i18n/              # Arabic (ar.po) translations
        ├── models/            # Core logic
        │   ├── __init__.py
        │   └── todo_task.py
        ├── views/             # UI XML files
        │   ├── base_menu.xml
        │   └── todo_views.xml
        ├── reports/           # PDF Templates
        │   └── task_reports.xml
        ├── security/          # Permissions
        │   ├── ir.model.access.csv
        │   └── security.xml
        └── static/
            └── description/
                └── icon.png

---

## Getting Started

### Prerequisites

- Docker Desktop installed and running
- WSL2 enabled on Windows
- Git installed

### 1. Clone the repository

git clone https://github.com/Mohamedabdelaziz142/task-todo-odoo.git
cd task-todo-odoo

### 2. Start the containers

docker compose up -d

### 3. Create the database

Go to http://localhost:8070 and fill in:
- Master Password: admin
- Database Name: todo
- Email: admin@admin.com
- Password: admin
- Language: English (or Arabic)

### 4. Install the module

1. Log in to Odoo.
2. Go to Settings → Activate Developer Mode.
3. Go to Apps → Update Apps List.
4. Search for "To-Do".
5. Click Install.

---

## REST API Documentation

Authenticate first via POST /web/session/authenticate to receive a session cookie.

| Method | Endpoint | Params | Description |
|---|---|---|---|
| GET | /api/tasks | limit, page, state | List tasks with pagination |
| POST | /api/tasks/create | JSON Body | Create a new task |
| GET | /api/tasks/<id> | - | View specific task details |
| PUT | /api/tasks/<id> | JSON Body | Update task (Blocked if Closed) |
| DELETE | /api/tasks/<id>/delete | - | Remove a task record |

---

## Module Details

### Model: todo.task
Includes fields: name, assigned_to, description, due_date, estimated_time, total_time, line_ids (timesheets), active (archiving), is_late (overdue flag), and state.

### Security Roles
- **To-Do User**: Can create tasks and see only the tasks assigned to them.
- **To-Do Manager**: Full access to all tasks and configurations.

### Automation & Logic
- **Server Action "Close"**: Available in the Action menu for bulk closing.
- **Cron Job**: Runs daily to post overdue warnings in the chatter.
- **Write Restriction**: Custom logic in the `write` method prevents editing finished/closed tasks.
- **Timesheet Validation**: Ensures spent time does not exceed the estimated time.

### Reports
- **Task Report (PDF)**: Accessible via the Print menu on any task, showing task details and full timesheet breakdown.

---

## Useful Commands

# Start containers
docker compose up -d

# Upgrade module and sync new files (API/Wizard/Translations)
docker exec -u 0 -it odoo-dev-odoo-1 odoo -u todo_app -d todo --stop-after-init

# View real-time logs for API debugging
docker logs -f odoo-dev-odoo-1

---

## Author

Mohamed Abdelaziz — Junior Developer from Cairo, Egypt 🚀
[LinkedIn](https://www.linkedin.com/in/mohamed-abdelaziz-4a5ab9242/) · [GitHub](https://github.com/Mohamedabdelaziz142)
