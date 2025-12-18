imple Project - n8n + Python Feedback Analysis

A full feedback automation and analysis project combining n8n workflow automation and Python data analysis. This project collects customer feedback via a webhook, analyzes sentiment using OpenAI, stores results in Google Sheets, and provides detailed statistics and visualizations.

🚀 Features

Collects customer feedback through a webhook form

Analyzes sentiment (Positive / Negative) using OpenAI

Stores feedback data (name, email, country, rating, sentiment) in Google Sheets

Sends personalized email responses:

😊 Positive → "Thank you for your kind feedback!"

😞 Negative → "We’re sorry and will work to improve."

Performs Python-based analysis to:

Show sentiment distribution

Calculate ratings statistics (average, min, max, standard deviation)

Generate PDF charts for reporting

🧠 Workflow Structure

Webhook Node — Receives feedback submission

OpenAI Node — Determines sentiment (Positive / Negative)

Google Sheets Node — Saves feedback and sentiment

Gmail Node (optional) — Sends automated emails

Python Analysis — Pulls Google Sheet data and generates statistics & visualizations

🛠 Tools Used

n8n — Workflow automation

OpenAI — Sentiment analysis

Google Sheets — Feedback storage

Gmail API — Email notifications

Python (Pandas + Matplotlib) — Data analysis & visualization

🗂️ How to Use

Import the workflow JSON (sentiment-feedback.json) into n8n

Configure credentials for Google Sheets, OpenAI, and Gmail (optional)

Deploy the workflow

Submit feedback via the webhook URL

Run the Python analysis script to view statistics and generate charts
