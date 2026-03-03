# Event Management System

A professional Django-based backend system for managing events, built with a focus on data integrity, clear API structures, and the magical theme of the "Event Management Assignment."

##  Project Overview
This project implements a robust RESTful API to handle the lifecycle of events. Each event is identified by a unique UUID, ensuring secure and globally unique referencing. The system follows the specific narrative requirements of the assignment, organizing logic into thematic "spells."

## Key Features
- **Full CRUD Support**: Create, Read, Update, and Delete events via standard HTTP methods.
- **UUID Identification**: Advanced unique identification for every event entity.
- **Data Validation**: Comprehensive check for required fields during event creation.
- **Thematic Structure**: Code is organized and commented following the "Magical Spells" assignment narrative.
- **Automated Testing**: Professional test suite to ensure system reliability.

## Tech Stack
- **Framework**: Django 
- **Laguage**: Python 3.x
- **Database**: SQLite (Development)
- **Serialization**: JSON

## API Reference

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `POST` | `/events/create/` | **The Summoning Spell**: Create a new event. |
| `GET` | `/events/` | **The Scrying Spell**: List all existing events. |
| `GET` | `/events/<uuid:id>/` | **The Lens Spell**: Retrieve details of a specific event. |
| `PATCH` | `/events/<uuid:id>/update/` | **The Transforming Spell**: Update event details. |
| `DELETE` | `/events/<uuid:id>/delete/` | **The Vanishing Spell**: Permanently remove an event. |

## Setup & Installation

1. **Activate Virtual Environment**:
   ```powershell
   .\venv\Scripts\activate
   ```

2. **Run Migrations**:
   ```bash
   python manage.py migrate
   ```

3. **Start Development Server**:
   ```bash
   python manage.py runserver
   ```

##  Testing
To verify the system's "magic" and ensure all endpoints are functioning correctly, run:
```bash
python manage.py test
```

---

**Developed by: Ahmed Badawy**  
*Committed to building clean, efficient, and well-documented backend systems.*
