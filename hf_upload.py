from huggingface_hub import HfApi
import os

api = HfApi(token=os.getenv(""))

api = HfApi()
api.upload_folder(
    repo_id="philippe-miranthis/testing-submit",
    folder_path="exp/lact/lact-swa2048-rope-fw02-id-rank32-init0.5-gain0.5-nh4-momentum-140M-8K-B"
)