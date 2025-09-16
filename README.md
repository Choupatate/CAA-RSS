# CAA-RSS: Automated Daily Check for CAA Luxembourg Updates

This project automates the process of checking for new updates on the [CAA Luxembourg website](https://www.caa.lu/fr/actualites) and notifies you of any changes.

---

## 📌 Logic of the Script

### **1. Scraping the Website**
- The script (`scraper.py`) fetches the "Actualités" section of the CAA Luxembourg website.
- It extracts the **date**, **title**, and **link** of each news entry from the HTML table.

### **2. Storing Previous Entries**
- The script saves the latest entries in a file called `previous_entries.json`.
- This file is **not an RSS feed**, but a simple JSON file that stores the last fetched entries for comparison.

### **3. Detecting New Updates**
- On each run, the script compares the current entries with the previous ones stored in `previous_entries.json`.
- If new entries are found, they are printed in the console (or can be sent as notifications).

### **4. Notifications**
- Currently, notifications are printed in the **GitHub Actions workflow logs**.
- You can extend the `notify_new_entries` function to send emails, Slack messages, or create GitHub issues.

### **5. Automation**
- The script runs **daily at 8 AM UTC** via GitHub Actions.
- You can also trigger it manually from the **Actions** tab.

---

## 🛠 Installation & Setup

### **1. Clone the Repository**
```bash
git clone https://github.com/Choupatate/CAA-RSS.git
cd CAA-RSS
```

### **2. Install Dependencies**
```bash
pip install -r requirements.txt
```

### **3. Run Locally (Optional)**
```bash
python scraper.py
```
- This will fetch the latest entries, compare them with previous runs, and print new updates.

### **4. GitHub Actions Setup**
- The workflow (`.github/workflows/daily_check.yml`) runs automatically every day.
- No additional setup is required—just push the code to GitHub.

---

## 🔄 How It Works

1. **First Run:**
   - Fetches the latest entries and saves them to `previous_entries.json`.

2. **Subsequent Runs:**
   - Fetches the latest entries again.
   - Compares them with `previous_entries.json`.
   - If new entries are found, they are logged in the workflow output.

---

## 📂 Files

| File | Purpose |
|------|---------|
| `scraper.py` | Main script to fetch and compare news entries. |
| `requirements.txt` | Python dependencies. |
| `previous_entries.json` | Stores the last fetched entries (auto-generated). |
| `.github/workflows/daily_check.yml` | GitHub Actions workflow for daily execution. |

---

## 🚀 Extending Notifications

To receive **email/Slack alerts**, modify the `notify_new_entries` function in `scraper.py`.

### **Example: Email Notification (Python)**
```python
import smtplib
from email.mime.text import MIMEText

def notify_new_entries(new_entries):
    if new_entries:
        message = "New updates on CAA Luxembourg:\n\n" + "\n".join(
            f"{entry['date']}: {entry['title']} - {entry['link']}" for entry in new_entries
        )
        
        msg = MIMEText(message)
        msg['Subject'] = 'New Updates on CAA Luxembourg'
        msg['From'] = 'your_email@example.com'
        msg['To'] = 'recipient@example.com'
        
        with smtplib.SMTP('smtp.example.com', 587) as server:
            server.starttls()
            server.login('your_email@example.com', 'your_password')
            server.send_message(msg)
```

---

## 📅 Schedule
- The script runs **daily at 8 AM UTC** (adjustable in `daily_check.yml`).

---

## 🔧 Customization
- **Change the schedule:** Edit the `cron` expression in `daily_check.yml`.
- **Add more features:** Extend the script to generate an RSS feed or integrate with other tools.

---

## 📝 Notes
- This project does **not** generate an RSS feed. It only checks for updates and logs them.
- If you want an RSS feed, consider using a third-party tool like [RSS.app](https://rss.app/) on the "Actualités" page.