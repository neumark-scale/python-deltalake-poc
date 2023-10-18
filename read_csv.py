import pandas as pd
from deltalake import DeltaTable
import os

storage_options = {
    "AWS_DEFAULT_REGION": os.environ.get("AWS_DEFAULT_REGION"),
    "AWS_ACCESS_KEY_ID": os.environ.get("AWS_ACCESS_KEY_ID"),
    "AWS_SECRET_ACCESS_KEY": os.environ.get("AWS_SECRET_ACCESS_KEY"),
    "AWS_S3_ALLOW_UNSAFE_RENAME": "true",
}

# based on: https://github.com/delta-io/delta-rs/blob/main/docs/usage/loading-table.md
dt = DeltaTable("s3a://scale-dev/neumark/python-deltalake-poc/lookup_area_8277", storage_options=storage_options)
print(dt.to_pyarrow_table().to_pydict())
