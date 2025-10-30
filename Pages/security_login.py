import pymysql
import streamlit as st

def initialize_database():
    try:
        mysql_config = st.secrets["mysql"]
        host = mysql_config["host"]
        user = mysql_config["user"]
        password = mysql_config["password"]
        port = mysql_config["port"]
        db = "Docx"

        # Connect to MySQL server (no database selected initially)
        mydb = pymysql.connect(host=host, user=user, password=password, port=port, ssl={"ssl_disabled": True})
        mycursor = mydb.cursor()

        # Create the database if it does not exist
        mycursor.execute(f"CREATE DATABASE IF NOT EXISTS {db}")
        mydb.commit()

        # Now select the created database
        mycursor.execute(f"USE {db}")

        # Create the Visitor table if it does not exist
        query4 = """
        CREATE TABLE IF NOT EXISTS Visitor (
            Visitor_number INT AUTO_INCREMENT PRIMARY KEY,
            Timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """
        mycursor.execute(query4)

        # Create pdf_count table
        query_pdf_count = """
        CREATE TABLE IF NOT EXISTS pdf_count (
            S_No INT AUTO_INCREMENT PRIMARY KEY,
            pdf_file_name VARCHAR(255),
            Timestamp TIMESTAMP DEFAULT NOW()
        )
        """
        mycursor.execute(query_pdf_count)

        mydb.commit()
        st.success(f"Database '{db}' and tables created successfully.")
        return mydb, mycursor

    except pymysql.Error as e:
        st.error(f"Error: {e}")
        return None, None

# Function to connect to the database (after it has been initialized)
def connect_to_db():
    mysql_config = st.secrets["mysql"]
    return pymysql.connect(host=mysql_config["host"], user=mysql_config["user"], password=mysql_config["password"],
                            port=mysql_config["port"], database="Docx", ssl={"ssl_disabled": True})

def update_visitor_count():
    conn4 = connect_to_db()
    cursor4 = conn4.cursor()
    
    # Only add a new visitor if it's the first access on a non-home page
    if st.session_state.get("first_access", False):
        if st.session_state.current_page != "Home":
            query = "INSERT INTO Visitor (Timestamp) VALUES (NOW())"
            cursor4.execute(query)
            conn4.commit()
            st.session_state.first_access = False

    # Count the number of visitors
    query = "SELECT COUNT(*) FROM Visitor"
    cursor4.execute(query)
    result = cursor4.fetchone()
    cursor4.execute("SELECT COUNT(*) FROM pdf_count")
    result2 = cursor4.fetchone()
    conn4.close()
    return result[0],result2[0]

def insert_pdf_record(pdf_filename):
    try:
        conn = connect_to_db()
        cursor = conn.cursor()
        # Insert PDF filename into pdf_count table
        query = "INSERT INTO pdf_count (pdf_file_name) VALUES (%s)"
        cursor.execute(query, (pdf_filename,))
        conn.commit()
        conn.close()
    except pymysql.Error as e:
        st.error(f"Database insert error: {e}")

import pandas as pd

def show_database_entries():
    try:
        conn = connect_to_db()
        cursor = conn.cursor()

        # Fetch all entries from Visitor table
        cursor.execute("SELECT * FROM Visitor")
        visitor_data = cursor.fetchall()
        visitor_columns = [desc[0] for desc in cursor.description]

        # Fetch all entries from pdf_count table
        cursor.execute("SELECT * FROM pdf_count")
        pdf_data = cursor.fetchall()
        pdf_columns = [desc[0] for desc in cursor.description]

        conn.close()

        # Convert fetched data into DataFrames
        visitor_df = pd.DataFrame(visitor_data, columns=visitor_columns)
        pdf_df = pd.DataFrame(pdf_data, columns=pdf_columns)

        # Display in Streamlit
        st.subheader("📋 Visitor Table")
        if not visitor_df.empty:
            st.dataframe(visitor_df)
        else:
            st.info("No visitor data found.")

        st.subheader("📂 PDF Count Table")
        if not pdf_df.empty:
            st.dataframe(pdf_df)
        else:
            st.info("No PDF records found.")

    except pymysql.Error as e:
        st.error(f"Error fetching data: {e}")

# Initialize the database when the script is run
if __name__ == "__main__":
    # Call initialize_database only if you haven't initialized it already
    if 'db_initialized' not in st.session_state:
        mydb, mycursor = initialize_database()
        st.session_state.db_initialized = True
    update_visitor_count()
    if st.button("📑 Show Database Records"):
        show_database_entries()