# 💬 Simple Project - n8n Sentiment Analysis Workflow

An **n8n workflow** that collects customer feedback via **Webhook**, analyzes the **sentiment** (Positive or Negative) using **OpenAI**, saves the results to **Google Sheets**, and automatically sends emails based on the analysis.

---

## 🚀 Features

- Collects customer feedback through a webhook form  
- Analyzes how the customer feels using **OpenAI sentiment analysis**  
- Saves results (name, email, country, rating, sentiment) to **Google Sheets**  
- Sends a personalized email:
  - 😊 Positive → “Thank you for your kind feedback!”
  - 😞 Negative → “We’re sorry and will work to improve.”

---

## 🧠 Workflow Structure

1. **Webhook** — Receives the feedback form submission  
2. **OpenAI Node** — Determines the sentiment (Positive / Negative)  
3. **Google Sheets** — Saves the feedback and sentiment  
4. **Gmail Node (optional)** — Sends automatic response emails  

---

## 🧩 Tools Used

- [n8n](https://n8n.io/) — Automation platform  
- [OpenAI](https://platform.openai.com/) — Sentiment analysis  
- [Google Sheets](https://www.google.com/sheets/about/) — Data storage  
- [Gmail API](https://developers.google.com/gmail/api) — Email sending  

---

## 📸 Example Workflow (screenshot)

![n8n workflow](./workflow-example.png)

*(Optional — Add an exported image of your workflow here)*

---

## 🗂️ How to Use

1. Import the file `sentiment-feedback.json` into your n8n instance  
2. Set up your credentials for:
   - Google Sheets  
   - OpenAI  
   - Gmail (optional)
3. Deploy the workflow  
4. Send feedback through your webhook URL  
5. Check the results in your Google Sheet  

---

## 👤 Author

**Bassam Bourourou**  
🌐 [LinkedIn](https://www.linkedin.com/in/bessam-bourourou-9291b3295/)  
💻 [GitHub](https://github.com/bassambour)

---

## 🏷️ License
This project is open-source under the **MIT License**.
