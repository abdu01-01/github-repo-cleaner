# 🧹 GitHub Repository Cleaner

A simple Python script to automatically delete all your GitHub repositories using the GitHub API.

---

## 🚀 Features

- Delete all repositories you own
- Works with GitHub API
- Handles errors and retries
- Supports many repositories (pagination)
- Safe (skips repositories without access)

---

## 📦 Requirements

Make sure you have:

- Python 3.x  
- requests library  

Install requests:

pip install requests

---

## 🔑 Create GitHub Token

To use this script, you need a GitHub token.

### Step 1: Open this link

https://github.com/settings/personal-access-tokens

---

### Step 2: Create token

- Click **Generate new token**
- Choose **Fine-grained token**

---

### Step 3: Set permissions

- Repository access → **All repositories**

- Permissions →  
  - Repository permissions →  
    - **Administration → Read and write**

---

### Step 4: Copy token

Paste your token into the script:

TOKEN = "your-token-here"

---

## ⚙️ Setup

Edit the script:

USERNAME = "your-username"  
TOKEN = "your-token"

---

## ▶️ Run

python delete.py

---

## ⚠️ WARNING

This script will permanently delete your repositories.  
There is NO undo.  

Use carefully.

---

## 📌 Example Output

Deleting: my-repo  
Status: 204  
Deleted ✅  

---

## 👨‍💻 Author

Created for learning GitHub API and automation.
