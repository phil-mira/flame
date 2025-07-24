from datasets import load_dataset

# load fineweb-edu with parallel processing
dataset = load_dataset("Salesforce/wikitext", "wikitext-2-v1", cache_dir="/home/uceeppm/Data")
