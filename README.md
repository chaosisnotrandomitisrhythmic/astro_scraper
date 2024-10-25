# Astro.com Horoscope Scraper

## Description
This Python script uses Selenium WebDriver to automate the process of logging into Astro.com and retrieving daily horoscopes. 

## Prerequisites
- Python 3.x
- Selenium WebDriver
- ChromeDriver

## Installation
1. Clone this repository or download the script.
2. Create and activate a virtual environment:
   ```
   python -m venv .venv
   source .venv/bin/activate  # On Windows, use `.venv\Scripts\activate`
   ```
3. Install the required Python packages:
   ```
   pip install -r requirements.txt
   ```
4. Download and install ChromeDriver, ensuring it's in your system PATH or update the path in the script.

## Configuration
Set the following environment variables:
- ASTRO_EMAIL: Your Astro.com account email
- ASTRO_PASSWORD: Your Astro.com account password

## Usage
Run the script using Python:
```
python src/app.py
```
