import logging

# Set up logging configuration
logging.basicConfig(filename="error_log.txt", level=logging.ERROR,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def log_error(message):
    """Log errors to a log file."""
    logging.error(message)
