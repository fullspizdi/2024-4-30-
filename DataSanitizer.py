```python
# DataSanitizer.py

import re

class DataSanitizer:
    def __init__(self, data):
        """
        Initialize the DataSanitizer with data to be sanitized.
        """
        self.data = data

    def sanitize_financial_data(self):
        """
        Sanitize financial data by removing sensitive numerical values.
        """
        print("Sanitizing financial data...")
        sanitized_data = re.sub(r'\d{2,}', '[REDACTED]', self.data)
        print("Financial data sanitized.")
        return sanitized_data

    def sanitize_customer_data(self):
        """
        Sanitize customer data by anonymizing names and email addresses.
        """
        print("Sanitizing customer data...")
        sanitized_data = re.sub(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', '[EMAIL REDACTED]', self.data)
        sanitized_data = re.sub(r'\b[A-Z][a-z]+ [A-Z][a-z]+\b', '[NAME REDACTED]', sanitized_data)
        print("Customer data sanitized.")
        return sanitized_data

    def sanitize_project_data(self):
        """
        Sanitize project data by removing specific project identifiers and keywords.
        """
        print("Sanitizing project data...")
        sanitized_data = re.sub(r'\bProject\s+ID\s+\d+\b', '[PROJECT ID REDACTED]', self.data)
        sanitized_data = re.sub(r'\b(confidential|secret|classified)\b', '[CLASSIFIED]', sanitized_data, flags=re.IGNORECASE)
        print("Project data sanitized.")
        return sanitized_data

if __name__ == "__main__":
    # Example usage
    example_financial_data = "The total revenue in 2024 was 50000 dollars."
    example_customer_data = "Customer John Doe can be reached at john.doe@example.com."
    example_project_data = "Project ID 12345 is classified and involves confidential data."

    sanitizer = DataSanitizer(example_financial_data)
    sanitized_financial_data = sanitizer.sanitize_financial_data()
    print(sanitized_financial_data)

    sanitizer = DataSanitizer(example_customer_data)
    sanitized_customer_data = sanitizer.sanitize_customer_data()
    print(sanitized_customer_data)

    sanitizer = DataSanitizer(example_project_data)
    sanitized_project_data = sanitizer.sanitize_project_data()
    print(sanitized_project_data)
```
