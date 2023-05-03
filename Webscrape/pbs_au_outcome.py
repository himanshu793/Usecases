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
