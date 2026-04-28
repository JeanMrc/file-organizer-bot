# File Organizer Bot
**Automated Directory Management Pipeline**

A high-performance Python-based utility designed to eliminate digital clutter by organizing directories in real-time. This tool leverages event-driven programming to monitor, categorize, and archive files based on their MIME types and extensions.

---

## Features
* **Recursive Initial Indexing:** Automatically sorts existing files upon the first execution.
* **Real-Time Monitoring:** Utilizes the \`watchdog\` API to detect and process new file arrivals instantly.
* **Intelligent Categorization:** Pre-configured support for Documents, Media, and Developer Assets.
* **Automated Logging:** Maintains a detailed \`activity.log\` with timestamps for transparency.

---

## Built With
* **Python**
* **Watchdog:** Cross-platform file system event monitoring.

---

## Installation & Setup

### 1. Clone the Repository
\`\`\`bash
git clone https://github.com/JeanMrc/file-organizer-bot.git
cd file-organizer-bot
\`\`\`

### 2. Configure Environment
\`\`\`bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
\`\`\`

### 3. Execution
\`\`\`bash
python organizer.py
\`\`\`

---
