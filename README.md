#Automated-Batch-Data-Pipeline-Glue-S3-Athena-
Use AWS Glue to extract, transform, and load large datasets.  Store in S3.  Query with Athena.

📊 AWS Batch Data Pipeline (S3 + Glue + Athena)
This project demonstrates a fully serverless batch data processing pipeline on AWS using the following components:

Amazon S3 for data storage (raw and processed zones)

AWS Glue for data transformation and ETL (Extract, Transform, Load)

AWS Lambda to trigger Glue jobs automatically when new files are uploaded

Amazon Athena for querying the processed data using SQL

🔧 What This Pipeline Does
Ingests Data
A CSV file containing sample course analytics data (e.g., student performance, enrollment, completion rates) is uploaded to the S3 bucket's raw/ folder.

Triggers an ETL Job Automatically
When a new file is uploaded, an S3 event triggers an AWS Lambda function, which in turn starts an AWS Glue job.

Processes Data Using Glue
The Glue job reads the raw data from S3, performs necessary transformations (e.g., cleaning, casting types, computing metrics), and stores the cleaned data in the processed/ folder on S3.

Queries Data Using Athena
Athena is used to run SQL queries on the transformed dataset stored in S3 via the AWS Glue Data Catalog. Tables for both raw and processed datasets are created automatically.

⚙️ Architecture Overview
[CSV Upload to S3 (raw/)]
            ↓
      [S3 Event Trigger]
            ↓
     [AWS Lambda Function]
            ↓
       [AWS Glue ETL Job]
            ↓
 [Processed Data in S3 (processed/)]
            ↓
        [Athena Queries]
