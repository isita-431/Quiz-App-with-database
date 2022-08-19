import streamlit as st 
import pandas as pd 
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report
import sys
import os
import streamlit.components.v1 as stc
import matplotlib.pyplot as plt
import sqlite3
import csv
conn = sqlite3.connect('data.db',check_same_thread=False)
cur = conn.cursor()
st.set_page_config(page_title='Quiz',layout='wide')

st.title('QUIZ APP')


def addData(name,a,b,c,d,e):
	cur.execute("""create table if not exists clg_form(name text(10),q1 text(10),q2 text(10),q3 text(10),q4 text(10),q5 text(10));""")
	# st.write("""create table if not exists clg_form(name text(10),q1 text(10),q2 text(10),q3 text(10),q4 text(10),q5 text(10));""")
	# st.write("INSERT INTO clg_form values"+str((name,a[0],b[0],c[0],d[0],e[0])))
	cur.execute("INSERT INTO clg_form values"+str((name,a[0],b[0],c[0],d[0],e[0]))+';')
	conn.commit()
	conn.close()
	st.success('Successfully submitted')
    
# def create_csv():
#     with open('output.csv', 'a+',  newline = '') as file_output:
#         headers = ["name","q1","q2","q3","q4","q5"]
#         writer = csv.DictWriter(file_output, delimiter=',', lineterminator='\n',fieldnames=headers)
#         writer.writeheader()

def update_csv(name,a,b,c,d,e):
    with open('output.csv', 'a+',  newline = '') as file_output:
        # csv_writer.writerows(rows) 
        csv_writer = csv.writer(file_output)
        # Add contents of list as last row in the csv file
        csv_writer.writerow([name,a[0],b[0],c[0],d[0],e[0]])
        
with st.form(key='quiz form'):
    name = st.text_input(label='Enter your name : ')
    st.markdown('You are given a  csv file  “student_records.csv” , dataframe “student_records” , “Student name” and “marks” are two columns in the dataframe.')
    l1 =("pandas.read_csv(‘student_records.csv’)", "pandas.read.csv(‘student_records.csv’)", "pandas.readcsv(‘student_records.csv’)","pandas.csv(‘student_records.csv’)")
    q1 = st.radio("1.What is the right syntax to load the dataframe  in pandas?",l1)
    # a='wrong'
    # if q1==l1[0]:
	#     a= 'right'
    a = ['right' if q1==l1[0] else 'wrong']

    l2 = ("student_records.inspect_data()","student_records.inspect()","student_records.info()",
	"student_records.describe()")
    q2 = st.radio("2.How do we check the rows and their information and type in the data frame?" ,
     l2)
    b = ['right' if q2==l2[2] else 'wrong']

    l3 =("print(student_records.shape)","print(student_records.shape[0])","print(student_records.rows)","print(student_records.n_rows)")
    q3 = st.radio( "3. How to find the number of rows in a dataframe:",
     l3)
    c = ['right' if q3==l3[1] else 'wrong']

    l4_1 =["student_records[‘marks’]","student_records.[‘Student name’]","student_records[‘marks’’]]","student_records.marks"]
    l4_2 =["student_records[‘marks’’]]"]
    q4 = st.multiselect('4.Right syntax to Select the column  “marks” from “student_records” .(multi choice)',
    l4_1,l4_2)

    d = ['right' if (q4[0]==l4_1[0]) and (q4[1]==l4_1[3]) else 'wrong']

    l5 =("student_records.Student name","student_records.[‘Student name’]","student_records[“Student name”]","student_records[Student name]")
    q5 = st.radio("5.Select the right way to select “Student name” from student_records dataframe." ,l5)
    e = ['right' if q5==l5[2] else 'wrong']
    submission = st.form_submit_button(label='Submit')
    # create_csv()
    if submission == True:
#         addData(name,a,b,c,d,e)
        update_csv(name,a,b,c,d,e)

# def display(col_name):
#     cur.execute("""select """+col_name+' from clg_form;')
b = st.button('click here for result summary : ')
if b:
    df = pd.read_csv('output.csv')
    st.write('First Question :')
    arr = df['q1']
    fig, ax = plt.subplots()
    ax.bar(arr.value_counts().index,arr.value_counts())
    plt.figure(figsize=(6,8))
    st.pyplot(fig)  
    st.write('Second Question :')
    arr2 = df['q2']
    fig, ax = plt.subplots()
    ax.bar(arr2.value_counts().index,arr2.value_counts())
    plt.figure(figsize=(6,8))
    st.pyplot(fig)  
    st.write('Third Question :')
    arr3 = df['q3']
    fig, ax = plt.subplots()
    ax.bar(arr3.value_counts().index,arr3.value_counts())
    plt.figure(figsize=(6,8))
    st.pyplot(fig)  
    st.write('Fourth Question :')
    arr4 = df['q4']
    fig, ax = plt.subplots()
    ax.bar(arr4.value_counts().index,arr4.value_counts())
    plt.figure(figsize=(6,8))
    st.pyplot(fig)  
    st.write('Fifth Question :')
    arr5 = df['q5']
    fig, ax = plt.subplots()
    ax.bar(arr5.value_counts().index,arr5.value_counts())
    plt.figure(figsize=(2,2))
    st.pyplot(fig)  
