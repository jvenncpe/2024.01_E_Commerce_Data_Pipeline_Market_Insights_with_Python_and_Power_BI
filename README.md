#### *Personal Project: February 2024*

<p align="center">
<img src="https://github.com/jvenncpe/2024.01_E_Commerce_Data_Pipeline_Market_Insights_with_Python_and_Power_BI/assets/35190918/169ba480-54ea-4d7e-93e0-218e01ca6054"/>
</p>

#### [Power BI Report View - Output Link Here](https://app.powerbi.com/view?r=eyJrIjoiMjkxZWRmMDEtNDJhMC00ZGY3LWEwMWItZDE2OTcxODU5OTRkIiwidCI6IjQwNWNhNjU3LThiNjQtNDAwMy04ZDMyLTkyYWYyZjU5Y2UwNCIsImMiOjEwfQ%3D%3D)

# E-Commerce Data Pipeline and Competitive Insights with Python and Power BI
Analyzed Amazon e-commerce data, cleaned, and imported to SQL Server with Python. Developed a Python script for web scraping market competition, storing the data in a staging table before cleaning and moving to production. Created a Power BI dashboard and a machine learning model to predict freight costs.

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
  
# CONCLUSION
### Findings:

<p>Upon comprehensive analysis of the evaluation metrics, it is evident that both the XGBoost and Gradient Boosting algorithms have demonstrated superior performance compared to the Random Forest model across multiple criteria.</p>
<p align="center">
  
| Metric                   | XGBoost (XGB) | Gradient Boosting (GB) | Random Forest (RF) |
|--------------------------|---------------|-------------------------|--------------------|
| Mean Squared Error (MSE) | 71.26         | 72.74                   | 87.33              |
| Mean Absolute Error (MAE)| 4.27          | 4.34                    | 4.97               |
| R2 Score                  | 0.71          | 0.71                    | 0.72               |
| Explained Variance        | 0.71          | 0.71                    | 0.72               |

</p>

<p>Overall, based on the lower MSE and MAE, higher R2 score, and Explained Variance --- XGBoost and Gradient Boosting models perform better compared to Random Forest. </p>
