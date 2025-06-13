# Moodchi
🧪 Mood of the Queue
Challenge: Build a quick internal tool to track the “mood” of support tickets
Tech: Python, Streamlit, Google Sheets, matplotlib

💡 Overview
Support agents handle hundreds of patient tickets a day — each with its own vibe. Some are delightful, others frustrating, and some just plain weird.

This tool helps capture that mood in real time and visualize the emotional pulse of the queue.

🎯 Features
✅ Log customer mood via dropdown (with emojis!)
✅ Add quick context via note
✅ Automatically logs timestamp
✅ Saves all data to Google Sheets
✅ Displays a bar chart of today’s moods
✅ Updates chart and data on every submission
✅ Built with clean, readable Python in ~30 mins

👉 [Google Sheet Link https://docs.google.com/spreadsheets/d/1RCdBCszGyQmV-G5uSiy_FCxNRX6LhgRIcPrSf_O2fWM/edit?gid=0#gid=0]

👉 Run locally with:
bash
Copy
Edit
streamlit run mood_st.py
🔧 Tech Stack
Frontend: Streamlit

Backend: Python

Storage: Google Sheets via gspread + Google Cloud service account

Charts: matplotlib

📂 File Structure
bash
Copy
Edit
📁 mood-of-the-queue/
│
├── gcpcred.json               # Google Cloud credentials (not included)
├── mood_st.py                 # Main Streamlit app
└── README.md                  # This file
🚀 To Run It Yourself
Set up a Google Cloud project

Enable Google Sheets API

Download the JSON credentials and name it gcpcred.json

Share the target Google Sheet with the service account email

Run:

bash
Copy
Edit
streamlit run mood_st.py

🔔 Mood streaks / alerts	“3 Angry tickets in a row!” → triggers a red alert banner.

🔍 Filtering by mood / agent

🎨 UI polish (custom themes, mochi icons?)

📊 Add summary stats (avg mood score, etc.)

🙌 Why This Matters
This is the kind of quick, pragmatic tool you build for your ops team on a Friday afternoon — fast, useful, clear.

No over-engineering, just vibes. 🍡

👋 About Me
Tony Fang
Cornell M.Eng | Data + Ops nerd | LA native
LinkedIn | tf277@cornell.edu
