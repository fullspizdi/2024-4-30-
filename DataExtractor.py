```python
# DataExtractor.py

import requests
from bs4 import BeautifulSoup

class DataExtractor:
    def __init__(self, session, base_url):
        self.session = session
        self.base_url = base_url

    def extract_financial_data(self):
        """
        Simulate extraction of financial data from the target's internal network.
        This function pretends to scrape financial reports from the internal network.
        """
        print("Extracting financial data...")
        financial_url = f"{self.base_url}/financial_reports"
        response = self.session.get(financial_url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            financial_data = soup.find(id="financial-data")
            if financial_data:
                print("Financial data extracted successfully.")
                return financial_data.text
            else:
                print("No financial data found.")
                return None
        else:
            print("Failed to access financial data.")
            return None

    def extract_customer_data(self):
        """
        Simulate extraction of customer data from the target's internal network.
        This function pretends to scrape customer information from the internal network.
        """
        print("Extracting customer data...")
        customer_url = f"{self.base_url}/customer_info"
        response = self.session.get(customer_url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            customer_data = soup.find(id="customer-data")
            if customer_data:
                print("Customer data extracted successfully.")
                return customer_data.text
            else:
                print("No customer data found.")
                return None
        else:
            print("Failed to access customer data.")
            return None

    def extract_project_data(self):
        """
        Simulate extraction of confidential project data from the target's internal network.
        This function pretends to scrape details of confidential projects from the internal network.
        """
        print("Extracting project data...")
        project_url = f"{self.base_url}/confidential_projects"
        response = self.session.get(project_url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            project_data = soup.find(id="project-data")
            if project_data:
                print("Project data extracted successfully.")
                return project_data.text
            else:
                print("No project data found.")
                return None
        else:
            print("Failed to access project data.")
            return None

if __name__ == "__main__":
    from InternalNetworkNavigator import InternalNetworkNavigator
    base_url = "http://example.com/internal"
    navigator = InternalNetworkNavigator(base_url)
    session = navigator.session
    data_extractor = DataExtractor(session, base_url)
    financial_data = data_extractor.extract_financial_data()
    customer_data = data_extractor.extract_customer_data()
    project_data = data_extractor.extract_project_data()
```
