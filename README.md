# 🧠 Wiki — A Django-Powered Markdown Encyclopedia

A Wikipedia-like online encyclopedia built with **Django**.  
This project was completed as part of **Harvard's CS50W Web Programming with Python and JavaScript** course.  
It demonstrates dynamic content management using Markdown, Django CRUD functionality, and clean backend–frontend integration.

---

## 🚀 Features

### 📝 Entry Pages
- Each encyclopedia entry is written in **Markdown** and stored as a `.md` file.  
- Markdown content is converted to **HTML** dynamically using the `markdown2` library.  
- Visiting `/wiki/<title>` displays the corresponding entry page.  

### 🔍 Search Functionality
- Users can search for entries using a keyword.  
- If an exact match exists → redirects to that entry’s page.  
- Otherwise → displays a **search results** page showing all partial matches.  

### ➕ Create New Page
- Users can add new encyclopedia entries via a simple form.  
- If an entry already exists with the same title, an **error message** is displayed.  
- Successful submissions save a new Markdown file and redirect to the new entry.  

### ✏️ Edit Existing Pages
- Each entry includes an **Edit** option.  
- Opens the entry in a form pre-filled with its current Markdown content.  
- Updates are saved and re-rendered dynamically.  

### 🎲 Random Page
- A “Random Page” option takes users to a randomly selected encyclopedia entry.  

---

## 🧩 Tech Stack

- **Backend:** Django 4.2  
- **Frontend:** HTML, CSS, Django Templates  
- **Data Storage:** Markdown files as entries  
- **Libraries:**  
  - [`markdown2`](https://pypi.org/project/markdown2/) – for Markdown → HTML conversion  

---



###  4️. Run the Django development server
python manage.py runserver

### 5️. Open the app

Visit http://127.0.0.1:8000/ in your browser.

