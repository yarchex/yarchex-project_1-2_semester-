import logging

logging.basicConfig(filename='../logs/data_collection.log', level=logging.INFO)

def main():
    logging.info("Starting data collection")
    # ... весь код из data_collection.ipynb
    logging.info("Data collection completed successfully")

if __name__ == "__main__":
    main()
