Web Scraping Project

Objective

The objective of this project is to scrape book details from a public website and create a custom dataset using Python web scraping techniques.

Website Used

https://books.toscrape.com/

Technologies Used

- Python
- Requests
- BeautifulSoup
- Pandas

Project Description

This project extracts book information from the "Books to Scrape" website using Python libraries. The scraped data is cleaned and stored in a CSV file for further analysis.

Data Collected

The following details are collected:

- Book Title
- Price
- Rating

Project Files

CodeAlpha_WebScraping
│
├── README.md
├── scraper.py
├── books.csv
└── requirements.txt

How It Works

1. Sends a request to the website using the Requests library.
2. Parses HTML content using BeautifulSoup.
3. Extracts book details like title, price, and rating.
4. Stores the collected data into a CSV file using Pandas.

How to Run

Install required libraries:

pip install -r requirements.txt

Run the scraper:

python scraper.py

Output

The extracted dataset is saved as:

books.csv

The CSV file contains:

- Title
- Price
- Rating

Result

Successfully created a custom dataset by scraping book information from a public website using Python.
