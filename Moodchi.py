# import packages
import pandas as pd
import streamlit as st
import datetime as dt
import gspread
from google.oauth2.service_account import Credentials
import matplotlib
import matplotlib.pyplot as plt

# operation on a specific spread sheet
scopes = ["https://www.googleapis.com/auth/spreadsheets"]

# getting the generated json credentials and authorizing usage
creds = Credentials.from_service_account_file("gcpcred.json", scopes = scopes)
client = gspread.authorize(creds)

# open the workbook by the id portion of url 
sheet_id = "1RCdBCszGyQmV-G5uSiy_FCxNRX6LhgRIcPrSf_O2fWM"
workbook = client.open_by_key(sheet_id)

# specifying sheet name on the workbook
sheet = workbook.worksheet('Sheet1') # specifying which sheet to work on


# the initial sessions-state df if it's empty
if "all_data" not in st.session_state:
    st.session_state['all_data'] = pd.DataFrame(columns=['Timestamp', 'Mood', 'Note'])

with st.form("mood_form"):
    # get now date and time
    today = dt.datetime.today().strftime("%Y-%m-%d %H:%M")
    # Title of this app
    st.write(
        f"""
        # Mood of the Queue 
        {today}
        ###### - Tracking patient ticket one mochi🍡 at a time
        """)
    
    # A dropdown box with emojis 
    moodchi = st.selectbox("What's the moodchi of the last customer?",
                            ('Angry😡','Happy😀', 'Curious🧐'),
                            index=None,
                            placeholder = "Select a Mood-chi")
    st.write("This patient's Moodchi: ", moodchi)

    # A customizable note section
    note = st.selectbox("Add a note?",
                        ('The customer needs immediate consultation',
                        'The customer is very satisfied with our service',
                        'The customer wants to spend more on our services'),
                        index = None,
                        placeholder = "Select or add a note",
                        accept_new_options = True)
    st.write("This patient's note: ")
    
    # create a submit button
    submitted = st.form_submit_button('Submit Moodchi')


# if form is submitted, we append the data to session state
if submitted:
    new_data =  pd.DataFrame([{'Timestamp':today, 'Mood': moodchi, 'Note':note}])
    st.session_state['all_data'] = pd.concat([st.session_state['all_data'], new_data], ignore_index=True)

# display all the entries so far for non-initial states
if not st.session_state['all_data'].empty:
    st.write('### ALL Moodchi Entries So Far:')
    all_data = st.dataframe(st.session_state['all_data'])
    
    # update the google sheet as new entries come in
    gs_data = [st.session_state['all_data'].columns.values.tolist()] + st.session_state['all_data'].values.tolist()
    sheet.update('A1',gs_data)  
    
    # create a barplot for all the entries for today
    st.pyplot(  # slice the df to today's date which was created previously
        st.session_state['all_data'][pd.to_datetime(st.session_state['all_data']['Timestamp'])
        .dt.date.eq(pd.to_datetime(today).date())]['Mood'].value_counts()
        .plot(kind='bar', title = "Moodchi Distribution").get_figure())
        #if st.checkbox("Auto-refresh chart every time"):
        # st.experimental_rerun()
