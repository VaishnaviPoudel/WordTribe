## WordTribe
It is a Django-based web application that allows users to register, log in, and share blog-style posts.

## Features

-  User authentication (login required to create/edit/delete posts)
-  Create, read, update, and delete (CRUD) blog posts
-  Flash messages for user feedback
-  Image upload support (via `request.FILES`)
-  Post ordering by newest first
-  Clean and minimal UI (customizable)

## Tech Stack

-  Python 3
-  Django
-  SQLite (for development)

---

## Getting Started

### Prerequisites

- Python 3.x installed
- Virtual environment tool like `venv` or `virtualenv`

### Installation & Setup

1. **Clone the repository:**

   ```bash
   git clone https://github.com/VaishnaviPoudel/WordTribe.git
   cd WaterTribe
   ```

2. **Create and activate a virtual environment:**
   ```bash
    python -m venv env
    source env/bin/activate      # On Windows: env\Scripts\activate
    ```
3. **Install dependencies:**
   ```bash
    pip install -r requirements.txt
    ```
4. **Apply Migrations**
   ```bash
    python manage.py migrate
    ```
5. **Run the Development Server** 
   ```bash
    python manage.py runserver
    ```
6. **Open your browser and visit:** `http://127.0.0.1:8000/`

## Usage

- Visit the homepage to see all blog posts.
- Register or log in to create, update, or delete posts.
- Admin users can also manage posts via the Django admin panel.
