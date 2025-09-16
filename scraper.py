#!/usr/bin/env python3
"""
Script to scrape the CAA Luxembourg website for new updates in the "Actualités" section.
Saves the latest entries and compares them with previous runs to detect new updates.
"""

import requests
from bs4 import BeautifulSoup
import json
import os
from datetime import datetime

# URL of the "Actualités" section
URL = "https://www.caa.lu/fr/actualites"

# File to store previous entries
PREVIOUS_ENTRIES_FILE = "previous_entries.json"


def fetch_news_entries():
    """Fetch the latest news entries from the CAA Luxembourg website."""
    try:
        response = requests.get(URL)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract news entries from the table
        news_entries = []
        for row in soup.select("table tr"):
            cells = row.find_all("td")
            if len(cells) >= 2:
                date = cells[0].get_text(strip=True)
                title = cells[1].get_text(strip=True)
                link = cells[1].find("a")["href"] if cells[1].find("a") else ""
                news_entries.append({"date": date, "title": title, "link": link})
        
        return news_entries
    except Exception as e:
        print(f"Error fetching news entries: {e}")
        return []


def load_previous_entries():
    """Load previous news entries from a JSON file."""
    if os.path.exists(PREVIOUS_ENTRIES_FILE):
        with open(PREVIOUS_ENTRIES_FILE, "r") as f:
            return json.load(f)
    return []


def save_entries(entries):
    """Save the current news entries to a JSON file."""
    with open(PREVIOUS_ENTRIES_FILE, "w") as f:
        json.dump(entries, f, indent=2)


def detect_new_entries(current_entries, previous_entries):
    """Detect new entries by comparing current and previous entries."""
    new_entries = []
    for entry in current_entries:
        if entry not in previous_entries:
            new_entries.append(entry)
    return new_entries


def notify_new_entries(new_entries):
    """Print new entries (replace with email/Slack notification if needed)."""
    if new_entries:
        print(f"🔔 {len(new_entries)} new update(s) detected:")
        for entry in new_entries:
            print(f"- {entry['date']}: {entry['title']} ({entry['link']})")
    else:
        print("No new updates.")


def main():
    print(f"🔍 Checking for updates at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    current_entries = fetch_news_entries()
    previous_entries = load_previous_entries()
    
    new_entries = detect_new_entries(current_entries, previous_entries)
    notify_new_entries(new_entries)
    
    save_entries(current_entries)


if __name__ == "__main__":
    main()