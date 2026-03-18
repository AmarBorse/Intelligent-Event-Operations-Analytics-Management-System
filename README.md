# Intelligent Event Operations & Analytics Management System

A full-stack web-based event management platform built using **Python** and **Streamlit** 
as an MCA Major Project at Pimpri Chinchwad University.

## 🔍 About the Project
This system goes beyond basic event management by integrating data analytics, 
NLP sentiment analysis, and intelligent performance scoring to help institutions 
manage and evaluate events effectively.

## ✨ Key Features
- 🔐 **Role-Based Access** — Admin and Organizer roles with secure login and session management
- 📅 **Venue Conflict Detection** — Automatically prevents double-booking of venues
- 🎯 **Event Success Index (ESI)** — Custom algorithm scoring events out of 100
- 🧠 **NLP Sentiment Analysis** — TextBlob analyzes participant feedback automatically
- 💰 **Budget Tracking** — Real-time planned vs actual expense monitoring with alerts
- 👥 **Attendance Analytics** — Register participants, mark attendance, track ratios
- 📊 **Analytics Dashboard** — Plotly charts with best/worst event insights
- ⚙️ **Resource Management** — Request and approval workflow with auto staff assignment
- 🤖 **AI Chatbot** — Floating assistant for event queries on every page

## 🛠️ Tech Stack
| Layer | Technology |
|-------|-----------|
| UI Framework | Streamlit |
| Backend | Python |
| Database | MySQL |
| Analytics | Pandas, NumPy |
| Visualization | Plotly |
| NLP | TextBlob / NLTK |
| Security | SHA-256 Encryption |

## 📐 ESI Formula
```
ESI = (Attendance % × 0.3) + (Budget Efficiency % × 0.3) + (Feedback Score % × 0.4)
```
| Score | Category |
|-------|----------|
| 80+ | Excellent |
| 60–79 | Good |
| 40–59 | Average |
| Below 40 | Poor |

## 🚀 How to Run
1. Install dependencies:
   pip install streamlit mysql-connector-python pandas plotly textblob
2. Set your MySQL password in database.py
3. Create database:
   CREATE DATABASE event_system;
4. Create Admin account in MySQL:
   INSERT INTO users (username, password, role) VALUES ('admin', SHA2('admin123', 256), 'Admin');
5. Run the project:
   streamlit run app.py
