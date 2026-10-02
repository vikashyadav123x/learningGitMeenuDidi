# Online Examination Portal

## Setup

On Ubuntu, install Python's package and virtual-environment tools first:

```bash
sudo apt update
sudo apt install python3-pip python3-venv
```

Then install the project dependencies and start the development server:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python manage.py runserver
```

Open these URLs while the server is running:

| URL                                 | Response             |
| ----------------------------------- | -------------------- | --------------------- |
| `/exam/?subject=Python&duration=60` | `subject:Python      | Duration:60 Minutes.` |
| `/exam/Pythoon/`                    | `Exam Name:Pythoon`  |
| `/student/2024`                     | `Student ID:2024`    |
| `/result/?roll=202&semester=8`      | `Roll:202            | Semester:8`           |
| `/hallticket/123456/`               | `Hall Ticket:123456` |

The hall-ticket route accepts exactly six digits. For example, `/hallticket/12345/` and `/hallticket/1234567/` return `404 Not Found`.
