# data_engineering_assignment
Take home assignment for data engineering candidates at SpotOn

# Assignment
Your task is to download data https://www.kaggle.com/olistbr/brazilian-ecommerce load it to object storage, ingest data to a database, and perform some light modeling on top of the raw data.

1) Retrieve Brazilian eCommerce data from Kaggle place json document in object storage 
(can use provided Docker container with MinIO or cloud storage provider of your choice)

https://www.kaggle.com/olistbr/brazilian-ecommerce
- customers: https://www.kaggle.com/olistbr/brazilian-ecommerce?select=olist_customers_dataset.csv
- order_items: https://www.kaggle.com/olistbr/brazilian-ecommerce?select=olist_order_items_dataset.csv
- orders: https://www.kaggle.com/olistbr/brazilian-ecommerce?select=olist_orders_dataset.csv
- products: https://www.kaggle.com/olistbr/brazilian-ecommerce?select=olist_products_dataset.csv

2) Ingest files from object store into a database using a custom python script or Singer. 
(can use provided Postgres container, other options include MySQL or SQLite)

(can use provide docker image)
CSV Singer tap: https://github.com/singer-io/tap-s3-csv
Postgres Singer target: https://github.com/datamill-co/target-postgres
SQLite Singer target: https://gitlab.com/meltano/target-sqlite


3) Create transformation job using python or dbt to materialize an order to create two aggregate tables 
agg_customer_order
customer_cohort (based on first order month, order volume by month)


# Acceptance Criteria
