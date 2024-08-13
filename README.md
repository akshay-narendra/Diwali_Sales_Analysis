# Diwali_Sales_Analysis

### Overview
The goal of this project was to analyze and visualize retail sales data from a Diwali festival period in India. The dataset, sourced from Kaggle, includes detailed information on product sales, including categories, sales channels, dates, times, sale prices, and quantities sold.

![image](https://github.com/user-attachments/assets/836e477b-c28b-4971-b56f-4726145f8246)
The purple bars represent total sales in each sector, while the green line shows the number of orders

### Data Pipeline: Kaggle to Power BI
![image](https://github.com/user-attachments/assets/d5ab0bbe-857b-4bec-bb98-9a63dba06c49)

This project involved loading data from Kaggle using the API, performing transformations with Pandas, and storing the cleaned data in SQL(refer to python script). The SQL database was then connected to Power BI for visualization.

## Key Insights:

- The IT sector and central region dominate in sales and orders.
- Unmarried females significantly outspend other demographic groups.
- Uttar Pradesh leads in state-wise sales, with substantial contributions from Maharashtra and Karnataka.
- Food is the most popular product category, followed by clothing, electronics, and footwear.

### Data set

https://www.kaggle.com/datasets/prajwal6362venom/diwali-sales/data

### Overview:

- **Total Sales:** 106 M
- **Total Orders:** 28 K

### Sector-wise Sales & Orders:

- **Top Sectors:**
    - **IT Sector:** Leading with sales close to 15 million and 4 k orders.
    - **Healthcare:** Second with over 12 million in sales and 3.5 k orders.
    - **Aviation:** Approximately 10 million in sales and 3.2 k orders.
- **Lowest Performing Sectors:**
    - **Lawyer, Chemical, Automobile:** Each around 1.3 million in sales and 1,300 orders.

### Sales Split Across Gender & Marital Status:

Unmarried females lead with 40 million in sales and 11,400 orders, followed by married females (30 million, 8.2 k orders), unmarried males (20 million, 4,900 orders), and married males (16 million, 3.6 k orders).

### State-wise Sales and Orders (Top 10):

- **Top States:**
    - **Uttar Pradesh:** Leading with sales nearly 20 million and 4.8 K orders.
    - **Maharashtra:** Close second with 15 million in sales and 3.8 K orders.
    - **Karnataka:** Over 12 million in sales and 3.3 k orders.
- **Lower Performing States:**
    - **Gujarat, Bihar, Haryana:** Each with sales around 5 million and approximately 1.1 k orders.

### Sales Across Product Categories (Top 5):

Food has the highest sales at 34 million, while Furniture has the lowest at 5 million.

### Region-wise Sales:

The Central Region leads with 42 million in sales, while the Eastern Region has the lowest at 7 million.

### Tools and Technologies

- **Data Cleaning and Transformation**: Pandas
- **Data Storage and Analysis**: SQL (via SQLAlchemy)
- **Visualization**: Power BI
