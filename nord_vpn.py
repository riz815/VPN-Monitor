import subprocess
import smtplib
import time
from email.mime.text import MIMEText

# === CONFIGURATION ===
YOUR_EMAIL = "email1"
YOUR_PASSWORD = "pjynlwbddhycvgxn"  # App Password
TO_EMAIL = "email2"
CHECK_INTERVAL_SECONDS = 5  # 5 minutes

def is_nordlayer_connected():
    try:
        result = subprocess.run(["ipconfig"], capture_output=True, text=True)
        output = result.stdout
        # Customize this if your adapter shows a different name
        if "NordLayer" in output or "Ethernet adapter NordLayer" in output:
            return True
        return False
    except Exception as e:
        print(f"Error checking VPN status: {e}")
        return False

def send_email():
    msg = MIMEText("🚨 NordLayer VPN is DISCONNECTED on your PC!")
    msg["Subject"] = "NordVPN Alert"
    msg["From"] = YOUR_EMAIL
    msg["To"] = TO_EMAIL

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(YOUR_EMAIL, YOUR_PASSWORD)
            server.sendmail(YOUR_EMAIL, TO_EMAIL, msg.as_string())
        print("Email sent successfully.")
    except Exception as e:
        print(f"Failed to send email: {e}")

# === LOOP ===
alert_sent = False  # Tracks if alert has already been sent

while True:
    vpn_connected = is_nordlayer_connected()

    if not vpn_connected:
        print("VPN is DISCONNECTED.")
        if not alert_sent:
            send_email()
            alert_sent = True  # Prevent multiple emails
    else:
        print("VPN is connected.")
        alert_sent = False  # Reset alert if reconnected

    time.sleep(CHECK_INTERVAL_SECONDS)
