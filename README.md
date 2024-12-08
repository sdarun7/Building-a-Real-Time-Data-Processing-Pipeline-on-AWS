Real-Time Data Processing Pipeline on AWS 

This repository shows how real-time data analytics is possible with AWS services such as Kinesis, Lambda, S3, Glue, Athena, and QuickSight. The streaming data is processed, and in real-time, transformations are applied, along with the visualization of insights through dashboards. 

 
Project Overview
 
1. Data Streaming 
Simulated data sent to AWS Kinesis from a data producer. 
 
2. Real-Time Data Transformation
- AWS Lambda processes incoming data by filtering, parsing, and enriching it.  

3. Data Storage and Querying  
- Transformed data is stored in S3.  
- AWS Glue catalogs the data for querying with Athena.  

4. Data Visualization
- QuickSight dashboards display key metrics, trends, and time-series data.


Setup Instructions  

1. Clone the Repository: Download the project files.
2. Deploy AWS Resources: Create Kinesis streams, Lambda functions, S3 buckets, and Glue crawlers.  
3. Run the Data Producer: Simulate and stream real-time data.  
4. Query and Visualize: Use Athena for queries and build QuickSight dashboards.  


Deliverables  

- Data producer for real-time streaming.  
- Lambda function for real-time data processing.  
- Athena SQL queries for analytics.  
- QuickSight dashboards for visualization.

![Screenshot (144)](https://github.com/user-attachments/assets/29cf7185-addc-4b83-9c14-7a162c170ecd)
![Screenshot (143)](https://github.com/user-attachments/assets/ef70ad44-a593-4e04-924f-97e3ce9b13e9)
![Screenshot (149)](https://github.com/user-attachments/assets/20dc20c6-93c5-43ca-b960-48641af5de34)
![Screenshot (150)](https://github.com/user-attachments/assets/e83f049e-7677-45ba-9eda-713b00532315)
![Screenshot (147)](https://github.com/user-attachments/assets/05936e91-6d6f-4a83-ad6b-329285a36235)
![Screenshot (145)](https://github.com/user-attachments/assets/0ae96a18-4968-4331-829a-04e9ec840e87)
![Screenshot (146)](https://github.com/user-attachments/assets/a0e0c9c8-34b4-441b-8e75-0b2c9831fa73)
