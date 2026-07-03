# Django Todo List

A web-based Todo List application developed using Django and Bootstrap. The application allows users to create, view, update, delete, and search tasks through a clean and responsive interface. The project demonstrates the implementation of Django's MVC architecture, CRUD operations, URL routing, template rendering, ORM, and frontend integration with Bootstrap.

---

# Features

* User registration and authentication
* Secure login and logout functionality
* Create new tasks with a title and description
* View all personal tasks in a structured table
* Update existing tasks
* Delete tasks with a confirmation prompt
* Search tasks by title and description
* Paginated task list for improved navigation and user experience
* User-specific task management (each user can access only their own tasks)
* Display a warning when no matching tasks are found
* Responsive user interface built with Bootstrap 5
* Navigation bar for quick access to pages
* Clean and user-friendly layout

---

# Screenshots

<table>
  <tr>
    <td align="center">
      <strong>Home Page</strong><br><br>
      <img src="screenshots/home.png" width="450">
    </td>
    <td align="center">
      <strong>Tasks Page</strong><br><br>
      <img src="screenshots/tasks.png" width="450">
    </td>
  </tr>

  <tr>
    <td align="center">
      <strong>Edit Task</strong><br><br>
      <img src="screenshots/Edit-task.png" width="450">
    </td>
    <td align="center">
      <strong>Search Functionality</strong><br><br>
      <img src="screenshots/search.png" width="450">
    </td>
  </tr>

  <tr>
    <td align="center">
      <strong>Delete Confirmation</strong><br><br>
      <img src="screenshots/delete-confirmation.png" width="450">
    </td>
    <td align="center">
      <strong>User Login</strong><br><br>
      <img src="screenshots/login.png" width="450">
    </td>
  </tr>

  <tr>
    <td align="center">
      <strong>User Registration</strong><br><br>
      <img src="screenshots/register.png" width="450">
    </td>
    <td align="center">
      <strong>Pagination</strong><br><br>
      <img src="screenshots/pagination.png" width="450">
    </td>
  </tr>
</table>

---

# Technologies Used

* Python
* Django
* HTML5
* CSS3
* Bootstrap 5
* SQLite3

---

# Project Structure

```
django_todo_app/
│
├── manage.py
├── requirements.txt
├── README.md
│
├── Todolist/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── home/
│   ├── migrations/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│   └── tests.py
│
├── templates/
│   ├── base.html
│   ├── home.html
│   ├── tasks.html
│   └── edittask.html
│
├── static/
│
└── .gitignore
```

---

# Application Workflow

### User Registration

* New users can create an account by providing their first name, last name, username, and password.
* Passwords are securely stored using Django's authentication system.

### User Login

* Registered users can log in using their username and password.
* Authentication is handled using Django's built-in authentication framework.
* Only authenticated users can create and manage tasks.

### User Logout

* Logged-in users can securely log out of the application.
* After logout, protected pages require authentication before they can be accessed.

### Home Page

* Enter a task title.
* Enter the task description.
* Submit the form to create a new task.

### Tasks Page

Displays only the tasks belonging to the currently logged-in user with:

* Serial Number
* Task Title
* Task Description
* Edit Action
* Delete Action

### Edit Task

* Opens a dedicated edit page.
* Automatically populates the existing task information.
* Saves the updated task details.

### Delete Task

* Displays a confirmation prompt before deletion.
* Deletes the selected task after confirmation.

### Search

* Search tasks from the navigation bar.
* Performs case-insensitive searches on both the task title and description.
* Displays a warning message if no matching tasks are found.

### Pagination

* Tasks are displayed in multiple pages for better readability.
* Navigate using First, Previous, Next, and Last buttons.
* The current page number and total number of pages are displayed.
---

# Django Concepts Demonstrated

* Django Models
* Django Views
* URL Routing
* Template Inheritance
* Template Rendering
* Django ORM
* CRUD Operations
* Query Filtering using `Q` Objects
* CSRF Protection
* Static Files
* Bootstrap Integration
* Django Authentication
* User Registration and Login
* User Logout
* Login Required Decorator
* Django Pagination
* User-Based Data Filtering
* ForeignKey Relationships

---

# Database

The application uses SQLite as the default database.

Current model:

```python
class Task(models.Model):
    tasktitle = models.CharField(max_length=30)
    taskdesc = models.TextField()
    timecreated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.tasktitle
```

---

# Requirements

Install all required packages using:

```bash
pip install -r requirements.txt
```

---

# License

This project is intended for educational and portfolio purposes.
