from datasets import load_dataset

# Load a Hugging Face dataset

def fetch_hf_dataset(
    dataset_name: str,
    split: str = "train",
):
    return load_dataset(
        dataset_name,
        split=split,
    )
