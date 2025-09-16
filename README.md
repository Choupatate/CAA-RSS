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
- If new entries are found, notifications are sent based on the configuration.

### **4. Notifications**
- Notifications can be sent via **email** or **Slack**, configured in `config.json`.
- The script prints new updates to the console and sends them according to the configuration.

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

### **3. Configure Notifications**
- Copy `config.json.example` to `config.json`:
  ```bash
  cp config.json.example config.json
  ```
- Edit `config.json` to enable and configure email/Slack notifications.

### **4. Run Locally (Optional)**
```bash
python scraper.py
```
- This will fetch the latest entries, compare them with previous runs, and send notifications if configured.

### **5. GitHub Actions Setup**
- The workflow (`.github/workflows/daily_check.yml`) runs automatically every day.
- No additional setup is required—just push the code to GitHub.

---

## 🔄 How It Works

1. **First Run:**
   - Fetches the latest entries and saves them to `previous_entries.json`.

2. **Subsequent Runs:**
   - Fetches the latest entries again.
   - Compares them with `previous_entries.json`.
   - If new entries are found, notifications are sent.

---

## 📂 Files

| File | Purpose |
|------|---------|
| `scraper.py` | Main script to fetch and compare news entries. |
| `config.json.example` | Example configuration file for notifications. |
| `config.json` | Your actual configuration file (ignored by Git). |
| `requirements.txt` | Python dependencies. |
| `previous_entries.json` | Stores the last fetched entries (ignored by Git). |
| `.github/workflows/daily_check.yml` | GitHub Actions workflow for daily execution. |
| `.gitignore` | Specifies files to ignore (e.g., sensitive data). |

---

## 📧 Notification Configuration

### **Email Notification**
- Set `enabled` to `true` in `config.json`.
- Configure SMTP server, port, sender email, password, and recipient email.

### **Slack Notification**
- Set `enabled` to `true` in `config.json`.
- Add your Slack webhook URL.

---

## 📅 Schedule
- The script runs **daily at 8 AM UTC** (adjustable in `daily_check.yml`).

---

## 🔧 Customization
- **Change the schedule:** Edit the `cron` expression in `daily_check.yml`.
- **Add more features:** Extend the script to generate an RSS feed or integrate with other tools.

---

## 📝 Notes
- This project does **not** generate an RSS feed. It only checks for updates and sends notifications.
- If you want an RSS feed, consider using a third-party tool like [RSS.app](https://rss.app/) on the "Actualités" page.