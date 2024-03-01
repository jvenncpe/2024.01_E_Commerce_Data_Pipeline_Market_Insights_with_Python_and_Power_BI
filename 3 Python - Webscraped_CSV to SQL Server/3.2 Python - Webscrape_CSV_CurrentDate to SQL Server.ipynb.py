#!/usr/bin/env python
# coding: utf-8

# In[32]:


import pypyodbc as odbc #!pip install pypyodbc
import pandas as pd
import time
import datetime
import os

print(odbc.drivers())


# #### Needed Inputs:

# In[33]:


driverName = "SQL Server" 
serverName = "DESKTOP-UVMKETP\SQLEXPRESS"
dataBaseName = "SQL_PowerBI_Test"
username = "jvenncpe"
pwd = "#Juv1994*"
tableName = "productDetails"

csv_FilePaTH = r"G:\00 Work Files\02 Work Trainings & Apps\00 Project Portfolio\Ecommerce_Amazon (Python, SQL, PowerBI)"
csv_FolderName = r"CSV Files"
csv_FileName = r"product_details_updateSQL.csv" #To be used for column name reference in SQL Table


# ### Custom Functions

# In[34]:


def updateSQL():
    try:
        conn.commit()
        return print("SQL Updated Successfully!")
        
    except Exception as e:
        return print(f"Error occurred: {e}")

def SQL_createTable_columnName(column):
    column_names = []
    for x in column:
        x = f'[{x}] VARCHAR(MAX)'
        column_names.append(x)
    return ', '.join(column_names)  # Join the column names with commas

def SQL_createTable_query(tableName,tableColumns):
    createTable_query = f"\
    IF NOT EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = '{tableName}')\
    BEGIN\
        CREATE TABLE {dataBaseName}.dbo.{tableName}({tableColumns})\
    END".strip()
    return createTable_query

def SQL_dropTable_query(SQLDatabase,SQLTableName):
    SQL_dropTable_query = f"\
        DROP TABLE IF EXISTS {SQLDatabase}.dbo.{SQLTableName}".strip()
    return SQL_dropTable_query

def bulk_insert(datapath_file, SQL_Table):
    insertBulk_query = f"""
        BULK INSERT {SQL_Table}
        FROM '{datapath_file}'
        WITH
        (   
            FORMAT='CSV',
            FIRSTROW = 2, 
            FIELDTERMINATOR = ',',
            ROWTERMINATOR = '\\n'
        )    
    """.strip()
    return insertBulk_query


# #### Adhoc SQL Configuration

# In[35]:


connection_string = f"""
    DRIVER={{{driverName}}};
    SERVER={serverName};
    DATABASE={dataBaseName};
    Trust_Connection=yes;
    UID={username};
    PWD={pwd};
"""
try:
    conn = odbc.connect(connection_string)
    cursor = conn.cursor()
    print("Connection successful!")

except Exception as e:
    print(f"Error: {e}")


# #### Main Function

# In[36]:


if __name__ == '__main__':
    
    csv_filePaTH_REF = os.path.join(csv_FilePaTH,csv_FolderName,csv_FileName)   
    csv_FoldderPath = os.path.join(csv_FilePaTH, csv_FolderName)
    
    df_productDetails = pd.read_csv(csv_filePaTH_REF, encoding='latin1', na_values=[""])
    
    for columnName in df_productDetails.columns:
        columnName_After = columnName.replace(".","")
        columnName_After = columnName_After.replace(" ","_")
        df_productDetails.rename(columns={columnName: columnName_After}, inplace=True)

    cursor = conn.cursor()
    try:
        with cursor:
            cursor.execute(SQL_dropTable_query(dataBaseName,tableName))
            updateSQL()
    except Exception as e:
        print(e)
        conn.rollback()
        print('Transaction rollback')
    
    cursor = conn.cursor()
    tableColumns = SQL_createTable_columnName(df_productDetails.columns)
    try:
        with cursor:
            cursor.execute(SQL_createTable_query(tableName,tableColumns))
            updateSQL()
    except Exception as e:
        print(e)
        conn.rollback()
        print('Transaction rollback')
    
    data_files = os.listdir(csv_FoldderPath)
    SQL_Table = f'{dataBaseName}.dbo.{tableName}'
    
    cursor = conn.cursor()
    try:
        with cursor:
            print(f"Target SQL Table: {SQL_Table}")
            print(f"---------------------------")
            print(f"Files to Upload:")
            
            current_time = datetime.datetime.now()
            current_date = current_time.strftime("%Y-%m-%d")
            
            for data_file in data_files:
                if data_file.endswith(f'_{current_date}.csv'):
                    cursor.execute(bulk_insert(os.path.join(csv_FoldderPath, data_file), SQL_Table))
                    print(data_file)
                    
            print(f"---------------------------")
            updateSQL()
            
    except Exception as e:
        print(e)
        conn.rollback()
        print('Transaction rollback')

