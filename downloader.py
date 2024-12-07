# download the full dataset
import os

os.environ["HF_HUB_ENABLE_HF_TRANSFER"] = "1"
from huggingface_hub import snapshot_download

print("downloading ....")
snapshot_download(
    repo_id="osv5m/osv5m",
    local_dir="data/osv5m_streetview_cropped/",
    repo_type="dataset",
)
