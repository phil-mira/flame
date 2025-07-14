from datasets import load_dataset, Value



# or load a subset with roughly 100B tokens, suitable for small- or medium-sized experiments
"""
dataset = load_dataset(
    "HuggingFaceFW/fineweb-edu",
    name="sample-10BT",
    cache_dir=r"D:\Data",
    streaming=True  # enables loading small amounts at a time
)
# Load only the first few data points (e.g., first 5) using streaming (does not load entire dataset)
first_few = [item for _, item in zip(range(5), dataset['train'])]
print(first_few[0])
"""


ds = load_dataset("Salesforce/wikitext", "wikitext-2-raw-v1", cache_dir=r"D:\Data")

#d = load_dataset("karpathy/tiny_shakespeare", cache_dir=r"D:\Data", trust_remote_code=True)



