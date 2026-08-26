from datasets import load_dataset


def fetch_hf_dataset(
    dataset_name: str,
    split: str = "train",
):
    return load_dataset(
        dataset_name,
        split=split,
    )
