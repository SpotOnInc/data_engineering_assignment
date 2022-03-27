class Spoton:
    """Ingestion constant variables"""

    target_data_sets = [
        "olist_customers_dataset.csv",
        "olist_order_items_dataset.csv",
        "olist_orders_dataset.csv",
        "olist_products_dataset.csv",
    ]

    kaggle_target_data = "./spoton/kaggle_data"
    unzipped_target_data = f"{kaggle_target_data}/unzipped/"
