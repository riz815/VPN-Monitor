# NordLayer VPN Monitor & Email Alert

This Python script continuously monitors the connection status of **NordLayer VPN** on a Windows machine.  
If the VPN disconnects, it automatically sends an **email alert** using Gmail SMTP.

---

## 🚀 Features
- Detects whether **NordLayer VPN** is connected.
- Sends an **email alert** if the VPN disconnects.
- Prevents **duplicate alerts** (only sends one email until VPN reconnects).
- Simple and lightweight — runs in the background.

---

## ⚙️ Requirements
- Python 3.7+
- A Gmail account with an **App Password** (not your regular password).
- Windows (uses `ipconfig` command).

---

## 📦 Installation
1. Clone or download this repository.
2. Install dependencies (only standard library is used, no extra packages required).
3. Set up a **Gmail App Password**:  
   - Go to [Google App Passwords](https://myaccount.google.com/apppasswords).  
   - Generate a password for "Mail".  
   - Copy it into the script.

---

## 🔧 Configuration
Edit these values in the script:

```python
YOUR_EMAIL = "your_email@gmail.com"
YOUR_PASSWORD = "your_app_password"  # App Password
TO_EMAIL = "recipient_email@gmail.com"
CHECK_INTERVAL_SECONDS = 300  # check every 5 minutes
