import requests
from bs4 import BeautifulSoup
import os

def download_pdf(url, keyword):
  # Get the HTML content of the web page
  response = requests.get(url)
  # Parse the HTML content using BeautifulSoup
  soup = BeautifulSoup(response.content, "html.parser")
  # Find all the links that have the keyword in their text
  links = soup.find_all("a", text=lambda t: keyword in t)
  # Loop through the links
  for link in links:
    # Get the href attribute of the link
    href = link["href"]
    # Check if the href ends with ".pdf"
    if href.endswith(".pdf"):
      # Get the file name from the href
      file_name = href.split("/")[-1]
      # Create the full URL of the PDF file
      pdf_url = url + href
      # Get the PDF content from the URL
      pdf_response = requests.get(pdf_url)
      # Save the PDF content to a file
      with open(file_name, "wb") as f:
        f.write(pdf_response.content)
      # Print a message
      print(f"Downloaded {file_name} from {pdf_url}")

import requests
from selenium import webdriver
import os

def download_pdf(url, keyword):
  # Create a webdriver object
  driver = webdriver.Chrome()
  # Get the web page using the driver
  driver.get(url)
  # Find all the links that have the keyword in their text
  links = driver.find_elements_by_partial_link_text(keyword)
  # Loop through the links
  for link in links:
    # Get the href attribute of the link
    href = link.get_attribute("href")
    # Check if the href ends with ".pdf"
    if href.endswith(".pdf"):
      # Get the file name from the href
      file_name = href.split("/")[-1]
      # Get the PDF content from the URL
      pdf_response = requests.get(href)
      # Save the PDF content to a file
      with open(file_name, "wb") as f:
        f.write(pdf_response.content)
      # Print a message
      print(f"Downloaded {file_name} from {href}")
  # Close the driver
  driver.close()

import tabula

def extract_table(pdf_file):
  # Use tabula to read the PDF file and extract the table
  table = tabula.read_pdf(pdf_file, pages="all")
  # Return the table as a pandas dataframe
  return table


# create a function to insert a dataframe into a database table 
def insert_table(table, table_name, conn):
  # Loop through the rows of the dataframe
  for row in table.itertuples():
    # Create a SQL query to insert the row into the table
    query = f"INSERT INTO {table_name} VALUES ("
    # Loop through the columns of the row
    for i in range(1, len(row)):
      # Get the value of the column
      value = row[i]
      # Check if the value is a string
      if isinstance(value, str):
        # Add quotes around the value
        value = f"'{value}'"
      # Add the value to the query
      query += f"{value},"
    # Remove the last comma
    query = query[:-1]
    # Add the closing bracket
    query += ")"
    # Execute the query
    conn.execute(query)
  # Commit the changes to the database
  conn.commit()

  #create a function to check if a row entry exists in the database table\
def check_row_exists(table_name, conn, **kwargs):
  # Create a SQL query to check if the row exists
  query = f"SELECT * FROM {table_name} WHERE "
  # Loop through the keyword arguments
  for key, value in kwargs.items():
    # Add the column name and value to the query
    query += f"{key} = '{value}' AND "
  # Remove the last "AND"
  query = query[:-5]
  # Execute the query
  results = conn.execute(query)
  # Return True if the row exists, False otherwise
  return len(results.fetchall()) > 0