from datasets import load_dataset

def fetch_hf_dataset(
    dataset_name: str,
    config: str = None,
    split: str = "train",
):
    """
    Load a dataset from Hugging Face Hub.
    
    Parameters:
    dataset_name : str
        Name of the dataset on Hugging Face.
    config : str, optional
        Dataset configuration, such as "en", "zh", "en_mix", or "zh_mix".
    split : str, default="train"
        Dataset split to load, such as "train", "test", or "validation".
    """
            
    return load_dataset(
        dataset_name,
        config,
        split=split,
    )
