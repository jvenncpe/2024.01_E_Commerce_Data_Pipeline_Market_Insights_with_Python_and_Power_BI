#### *Personal Project: February 2024*

<p align="center">
<img src="https://github.com/jvenncpe/2024.01_E_Commerce_Data_Pipeline_Market_Insights_with_Python_and_Power_BI/assets/35190918/169ba480-54ea-4d7e-93e0-218e01ca6054"/>
</p>

#### [Power BI Report View - Output Link Here](https://app.powerbi.com/view?r=eyJrIjoiMjkxZWRmMDEtNDJhMC00ZGY3LWEwMWItZDE2OTcxODU5OTRkIiwidCI6IjQwNWNhNjU3LThiNjQtNDAwMy04ZDMyLTkyYWYyZjU5Y2UwNCIsImMiOjEwfQ%3D%3D)

# E-Commerce Data Pipeline and Competitive Insights with Python and Power BI
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
</br>• Cleaned and imported this data into SQL Server using Python.
</br></br>Web Scraping and Data Management:
</br>• Developed a Python script to scrape current market competition.
</br>• Initially stored the web-scraped data in a staging table, then cleaned it and moved it to a production table.
</br></br>Data Visualization and Analysis:
</br>• Connected data from SQL Server to Microsoft Power BI Service for publishing and online access.
</br>• Power BI accessed SQL Server: historical data via import and cleaned web-scraped data in the production table via direct query.
</br>• Developed a Power BI dashboard to visualize both historical and web-scraped data.
</br></br>Predictive Modeling:
</br>• Created a machine learning model to predict freight costs.

## Outputs:
1. [Power BI Dashboard](https://app.powerbi.com/view?r=eyJrIjoiMjkxZWRmMDEtNDJhMC00ZGY3LWEwMWItZDE2OTcxODU5OTRkIiwidCI6IjQwNWNhNjU3LThiNjQtNDAwMy04ZDMyLTkyYWYyZjU5Y2UwNCIsImMiOjEwfQ%3D%3D): </br></br>
  <p align="center"><img src="https://github.com/jvenncpe/2024.01_E_Commerce_Data_Pipeline_Market_Insights_with_Python_and_Power_BI/assets/35190918/169ba480-54ea-4d7e-93e0-218e01ca6054"/></p>
  <p align="center"><img src="https://github.com/jvenncpe/2024.01_E_Commerce_Data_Pipeline_Market_Insights_with_Python_and_Power_BI/assets/35190918/4705dd46-2da3-4a2c-8523-497224ff00e5"/></p>
  <p align="center"><img src="https://github.com/jvenncpe/2024.01_E_Commerce_Data_Pipeline_Market_Insights_with_Python_and_Power_BI/assets/35190918/2c027e9c-5f4b-4677-a8fc-1cc98ef3dbfb"/></p>

2. Freight Pricing Model Evaluation Metrics:
  <p align="center"><img src="https://github.com/jvenncpe/2024.01_E_Commerce_Data_Pipeline_Market_Insights_with_Python_and_Power_BI/assets/35190918/e2b3948c-4665-480d-81eb-fba4267bcde9"/></p>
  <p align="center"><img src="https://github.com/jvenncpe/2024.01_E_Commerce_Data_Pipeline_Market_Insights_with_Python_and_Power_BI/assets/35190918/375f20b8-f39d-4570-b077-3f3e088b948c"/></p>
  <p align="center"><img src="https://github.com/jvenncpe/2024.01_E_Commerce_Data_Pipeline_Market_Insights_with_Python_and_Power_BI/assets/35190918/66617338-19ef-4af0-8e69-52ad05aaa893"/></p>
  
  Upon comprehensive analysis of the evaluation metrics, it is evident that both the XGBoost and Gradient Boosting algorithms have demonstrated superior performance compared to the Random Forest model across multiple criteria.</p>
  
  | Metric                   | XGBoost (XGB) | Gradient Boosting (GB) | Random Forest (RF) |
  |--------------------------|---------------|-------------------------|--------------------|
  | Mean Squared Error (MSE) | 71.15         | 72.74                   | 86.95              |
  | Mean Absolute Error (MAE)| 4.28          | 4.34                    | 4.97               |
  | R2 Score                  | 0.71          | 0.72                    | 0.66               |
  | Explained Variance        | 0.71          | 0.72                    | 0.66               |
  
  <p>Overall, based on the MSE and MAE (lower the better), R2 score, and Explained Variance (higher the better) -- XGBoost and Gradient Boosting models perform better compared to Random Forest. </p>

  
  Feature Importance:
  <p align="center"><img src="https://github.com/jvenncpe/2024.01_E_Commerce_Data_Pipeline_Market_Insights_with_Python_and_Power_BI/assets/35190918/b98d45f7-2e3c-445c-b94b-97d63b27e95e"/></p>
  <p align="center"><img src="https://github.com/jvenncpe/2024.01_E_Commerce_Data_Pipeline_Market_Insights_with_Python_and_Power_BI/assets/35190918/09e16bea-596d-428b-ac13-ec2b7d508a49"/></p>
  <p align="center"><img src="https://github.com/jvenncpe/2024.01_E_Commerce_Data_Pipeline_Market_Insights_with_Python_and_Power_BI/assets/35190918/1955e93e-f5c7-4f03-afe4-477d5ce12dc2"/></p>

  "Product Weight (g)" and "Customer Zip Code Prefix" are among the features with the highest importance scores across the models.
