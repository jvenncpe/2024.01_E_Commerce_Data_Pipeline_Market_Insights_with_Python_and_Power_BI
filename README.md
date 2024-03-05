#### *Personal Project: February 2024*

<p align="center">
<img src="https://github.com/jvenncpe/2024.01_E_Commerce_Data_Pipeline_Market_Insights_with_Python_and_Power_BI/assets/35190918/169ba480-54ea-4d7e-93e0-218e01ca6054"/>
</p>

#### [Power BI Report View - Output Link Here](https://app.powerbi.com/view?r=eyJrIjoiMjkxZWRmMDEtNDJhMC00ZGY3LWEwMWItZDE2OTcxODU5OTRkIiwidCI6IjQwNWNhNjU3LThiNjQtNDAwMy04ZDMyLTkyYWYyZjU5Y2UwNCIsImMiOjEwfQ%3D%3D)

# E-Commerce Data Pipeline and Market Insights with Python and Power BI
Imported historical dataset into SQL Server using Python and developed a Python script to web scrape market competition that were then initially stored in a SQL staging table for data cleaning before importing to SQL production table to be used for Power BI dashboard and machine learning.

## Dataset Context
<p align="center">
<img src="https://github.com/jvenncpe/2024.01_E_Commerce_Data_Pipeline_Market_Insights_with_Python_and_Power_BI/assets/35190918/9568d8d5-ca88-4bed-b4d2-f17cbbce630f"/>
</p>

These datasets were generously provided by Olist, the largest department store in Brazilian marketplaces. Olist connects small businesses from all over Brazil to channels without hassle and with a single contract. Those merchants are able to sell their products through the Olist Store and ship them directly to the customers using Olist logistics partners. See more at: www.olist.com

After a customer purchases the product from Olist Store a seller gets notified to fulfill that order. Once the customer receives the product, or the estimated delivery date is due, the customer gets a satisfaction survey by email where he can give a note for the purchase experience and write down some comments.

## Methodology:
Data Collection and Analysis:
</br>• Utilized historical data from an e-commerce store on Amazon for analysis and visualization.
</br>• These historical data were cleaned and imported to the SQL Server using Python.
</br></br>Web Scraping and Data Management:
</br>• Developed a Python script to scrape current amazon market competition and initially stored the web-scraped data in a staging table to do final data cleaning before moving it to the SQL production table.
</br></br>Data Visualization and Analysis:
</br>• The data from SQL Server was connected to Microsoft Power BI  (Microsoft Fabric) Service through on-premise gateway for scalability, online access and Power BI web publishing.
</br>• Power BI means of access to SQL Server: historical data via import and the cleaned web-scraped data in the production table was accessed via direct query.
</br>• Developed a Power BI dashboard with three (3) modules or pagination wherein:

  <table align="center" width="100%">
      <tr>
        <td width="33.33%" valign="top">
          <strong>First Page:</br></strong> The dashboard summarizes overall sales revenue, successful deliveries, and customer metrics, including its key performance indicators (KPIs).
        </td>
        <td width="33.33%" valign="top">
          <strong>Second Page:</br></strong> Historical pricing analysis by product category, highlighting popular and least popular items, including pricing performance such as the most popular, lowest sold, and highest sold product prices.
        </td>
        <td width="33.33%" valign="top">
          <strong>Third Page:</br></strong> Live data showcasing current competitor price analysis on Amazon, featuring the most popular product category and its corresponding pricing metrics, including the most popular, lowest sold, and highest sold product prices.
        </td>
      </tr>
    </table>

Predictive Modeling:
</br>• Developed a machine learning model to predict freight costs, evaluated its performance using MSE, MAE, R2, and Explained Variance metrics, and identified the most influential factors through feature importance analysis.

## Outputs, Results and Discussion:
1. [Power BI Dashboard](https://app.powerbi.com/view?r=eyJrIjoiMjkxZWRmMDEtNDJhMC00ZGY3LWEwMWItZDE2OTcxODU5OTRkIiwidCI6IjQwNWNhNjU3LThiNjQtNDAwMy04ZDMyLTkyYWYyZjU5Y2UwNCIsImMiOjEwfQ%3D%3D):
     <p align="center">
      <img src="https://github.com/jvenncpe/2024.01_E_Commerce_Data_Pipeline_Market_Insights_with_Python_and_Power_BI/assets/35190918/169ba480-54ea-4d7e-93e0-218e01ca6054"/>
      <img src="https://github.com/jvenncpe/2024.01_E_Commerce_Data_Pipeline_Market_Insights_with_Python_and_Power_BI/assets/35190918/4705dd46-2da3-4a2c-8523-497224ff00e5"/>
      <img src="https://github.com/jvenncpe/2024.01_E_Commerce_Data_Pipeline_Market_Insights_with_Python_and_Power_BI/assets/35190918/2c027e9c-5f4b-4677-a8fc-1cc98ef3dbfb"/>
    </p>

2. Freight Pricing Model Evaluation Metrics:
   
     | Metric                   | XGBoost (XGB) | Gradient Boosting (GB) | Random Forest (RF) |
      |--------------------------|---------------|-------------------------|--------------------|
      | Mean Squared Error (MSE) | 71.15         | 72.74                   | 86.95              |
      | Mean Absolute Error (MAE)| 4.28          | 4.34                    | 4.97               |
      | R2 Score                  | 0.71          | 0.72                    | 0.66               |
      | Explained Variance        | 0.71          | 0.72                    | 0.66               |

     Upon comprehensive analysis of the evaluation metrics, it is evident that both the XGBoost and Gradient Boosting algorithms have demonstrated superior performance compared to the Random Forest model across multiple criteria.

   <p>Overall, based on the MSE and MAE (lower the better), R2 score, and Explained Variance (higher the better) -- XGBoost and Gradient Boosting models perform better compared to Random Forest. </p>
   
 3. Feature Importance:
    <p align="center">
      <img src="https://github.com/jvenncpe/2024.01_E_Commerce_Data_Pipeline_Market_Insights_with_Python_and_Power_BI/assets/35190918/b98d45f7-2e3c-445c-b94b-97d63b27e95e"/>
      <img src="https://github.com/jvenncpe/2024.01_E_Commerce_Data_Pipeline_Market_Insights_with_Python_and_Power_BI/assets/35190918/09e16bea-596d-428b-ac13-ec2b7d508a49"/>
      <img src="https://github.com/jvenncpe/2024.01_E_Commerce_Data_Pipeline_Market_Insights_with_Python_and_Power_BI/assets/35190918/1955e93e-f5c7-4f03-afe4-477d5ce12dc2"/>
    </p>
    
    "Product Weight (g)" and "Customer Zip Code Prefix" are among the features with the highest importance scores across the models. 

    This means that "Product Weight (g)" and "Customer Zip Code Prefix" are among the most influential factors in determining the outcomes of the models, indicating that these features are crucial for the generalization of the models. 

    Their importance suggests that the models are highly sensitive to variations in these features, which could lead to different outcomes based on the specific characteristics of the products and the geographical locations of the customers.
  
---
# Thank you!
