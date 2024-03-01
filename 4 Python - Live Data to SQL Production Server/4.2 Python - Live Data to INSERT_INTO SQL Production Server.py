#!/usr/bin/env python
# coding: utf-8

# In[13]:


import pypyodbc as odbc #!pip install pypyodbc
import pandas as pd
import time
import os

print(odbc.drivers())


# In[14]:


driverName = "SQL Server" 
serverName = "DESKTOP-UVMKETP\SQLEXPRESS"
TEMP_dataBaseName = "SQL_PowerBI_Test"
FIN_dataBaseName = "SQL_PowerBI_Production"
username = "jvenncpe"
pwd = "#Juv1994*"
tableName = "productDetails"


# In[15]:


def updateSQL():
    try:
        conn.commit()
        return print("SQL Updated Successfully!")
        
    except Exception as e:
        return print(f"Error occurred: {e}")

def SQL_dropTable_query(SQLDatabase,SQLTableName):
    SQL_dropTable_query = f"\
        DROP TABLE IF EXISTS {SQLDatabase}.dbo.{SQLTableName}".strip()
    return SQL_dropTable_query

def SQL_Production_query():
    SQL_InsertTable_To_Production_query = f"""
    WITH
        distinct_Test as
        (
        SELECT DISTINCT * FROM SQL_PowerBI_Test.dbo.productDetails
        ),

		distinct_timestamp as
		(
		SELECT DISTINCT [ASIN], [TIMESTAMP] FROM distinct_Test
		),

		distinct_tables as
        (
        SELECT 
            Table1.[TIMESTAMP]
            ,Table1.[ASIN]
            ,[CATEGORY]
            ,[TITLE]
            ,[PRICE]
            ,[RATING]
            ,[NO_OF_REVIEWS]
            ,[NO_OF_SOLD_PRODUCTS]
            ,[LINK]
        FROM distinct_timestamp as Table1
    
        LEFT JOIN distinct_Test ON 
            Table1.[TIMESTAMP] = distinct_Test.[TIMESTAMP] AND Table1.[ASIN] = distinct_Test.[ASIN]
        ),

        CLEAN_NO_OF_SOLD_PRODUCT as
        (
        SELECT DISTINCT
            [ASIN]
			,[TIMESTAMP]
            ,CAST
            (
                COALESCE
                (
                    CASE 
                        WHEN TRY_CAST(NO_OF_SOLD_PRODUCTS AS INT) IS NULL THEN 0
                        ELSE CAST(NO_OF_SOLD_PRODUCTS AS INT)
                    END, 0
                ) 
            AS INT
            ) AS NO_OF_SOLD_PRODUCTS
            
                FROM
                (
                    SELECT
                        [ASIN],
                        SUBSTRING([NO_OF_SOLD_PRODUCTS], 1, CHARINDEX(' ', NO_OF_REVIEWS) - 1) AS NO_OF_SOLD_PRODUCTS
						,[TIMESTAMP]
                    FROM distinct_tables
                ) AS sub
        ),
            
        CLEAN_PRICE as
        (
        SELECT DISTINCT
            [ASIN]
            ,CAST(REPLACE(REPLACE(REPLACE(PRICE, '$', ''),'S',''),',','') AS FLOAT) as PRICE
			,[TIMESTAMP]
        FROM distinct_tables
        ),
            
        CleanedTable as
        (
        SELECT DISTINCT
            CAST(COALESCE(Table1.[TIMESTAMP], '0') AS DATETIME) AS [TIMESTAMP],
            CAST(COALESCE(Table1.[TIMESTAMP], '0') AS DATE) AS [DATE],
            COALESCE(Table1.[ASIN], '0') AS [ASIN],
            COALESCE(CATEGORY, 'Unknown') AS [CATEGORY],
            COALESCE(TITLE, 'Unknown') AS [TITLE],
            COALESCE(CLEAN_PRICE.PRICE, '0.00') AS [PRICE],
            CAST(REPLACE(COALESCE(SUBSTRING(RATING, 1, CHARINDEX(' ', RATING) - 1), '0.00'),',','') AS FLOAT) AS [RATING],
            CAST(REPLACE(COALESCE(SUBSTRING(NO_OF_REVIEWS, 1, CHARINDEX(' ', NO_OF_REVIEWS) - 1), '0'),',','') AS INT)  AS [NO_OF_REVIEWS],
            COALESCE(CLEAN_NO_OF_SOLD_PRODUCT.NO_OF_SOLD_PRODUCTS,'0') AS [NO_OF_SOLD_PRODUCTS],
            COALESCE(LINK, '0') AS [LINK]
            
        FROM distinct_tables as Table1
            
        INNER JOIN CLEAN_NO_OF_SOLD_PRODUCT ON Table1.[ASIN] = CLEAN_NO_OF_SOLD_PRODUCT.[ASIN] AND Table1.[TIMESTAMP] = CLEAN_NO_OF_SOLD_PRODUCT.[TIMESTAMP]
        INNER JOIN CLEAN_PRICE ON Table1.[ASIN] = CLEAN_PRICE.[ASIN] AND Table1.[TIMESTAMP] = CLEAN_PRICE.[TIMESTAMP]
        )

        INSERT INTO SQL_PowerBI_Production.dbo.productDetails
        SELECT *
        FROM CleanedTable;
    """.strip()
    return SQL_InsertTable_To_Production_query


# #### Adhoc SQL Configuration

# In[16]:


def TEMP_dataBaseName_connect():
    connection_string = f"""
        DRIVER={{{driverName}}};
        SERVER={serverName};
        DATABASE={TEMP_dataBaseName};
        Trust_Connection=yes;
        UID={username};
        PWD={pwd};
    """
    try:
        conn = odbc.connect(connection_string)
        cursor = conn.cursor()
        a = print(f"Connection successful! for {TEMP_dataBaseName}")
    
    except Exception as e:
        a = print(f"Error: {e}")
    return a, conn, cursor


# In[17]:


def FIN_dataBaseName_connect():
    connection_string = f"""
        DRIVER={{{driverName}}};
        SERVER={serverName};
        DATABASE={FIN_dataBaseName};
        Trust_Connection=yes;
        UID={username};
        PWD={pwd};
    """
    try:
        conn = odbc.connect(connection_string)
        cursor = conn.cursor()
        a = print(f"Connection successful! for {FIN_dataBaseName}")
    
    except Exception as e:
        a = print(f"Error: {e}")
        
    return a, conn, cursor


# #### Main Function

# In[18]:


if __name__ == '__main__':
    a, conn, cursor = TEMP_dataBaseName_connect()
    try:
        with cursor:
            cursor.execute(SQL_Production_query())
            updateSQL()
    except Exception as e:
        print(e)
        conn.rollback()
        print('Transaction rollback')

