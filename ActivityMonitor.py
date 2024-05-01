```python
# ActivityMonitor.py

import requests
import time

class ActivityMonitor:
    def __init__(self, target_url):
        self.target_url = target_url
        self.session = requests.Session()

    def monitor_suspicious_activity(self):
        """
        Monitor for any suspicious activity that might indicate a security breach.
        This function pretends to check for unusual network traffic or unauthorized access attempts.
        """
        print("Monitoring for suspicious activities...")
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
        }
        response = self.session.get(self.target_url, headers=headers)
        if response.status_code == 200:
            print("No suspicious activities detected.")
            return False
        else:
            print("Suspicious activities detected!")
            return True

    def log_activity(self, activity_details):
        """
        Log the detected activities for further analysis.
        This function pretends to write activity details to a log file.
        """
        print("Logging activity...")
        with open("activity_log.txt", "a") as log_file:
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
            log_file.write(f"{timestamp} - {activity_details}\n")
            print("Activity logged.")

if __name__ == "__main__":
    target_url = "http://example.com/security"
    activity_monitor = ActivityMonitor(target_url)
    if activity_monitor.monitor_suspicious_activity():
        activity_monitor.log_activity("Detected unauthorized access attempts.")
    else:
        activity_monitor.log_activity("No unusual activities detected.")
```
