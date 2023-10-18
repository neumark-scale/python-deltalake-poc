import pandas as pd
from deltalake.writer import write_deltalake
import os

# read CSV file to Pandas DataFrame
df = pd.read_csv('data/DimenLookupArea8277.csv')

# write Pandas dataframe to delta lake on S3
# based on https://stackoverflow.com/a/76238756

storage_options = {
    "AWS_DEFAULT_REGION": os.environ.get("AWS_DEFAULT_REGION"),
    "AWS_ACCESS_KEY_ID": os.environ.get("AWS_ACCESS_KEY_ID"),
    "AWS_SECRET_ACCESS_KEY": os.environ.get("AWS_SECRET_ACCESS_KEY"),
    "AWS_S3_ALLOW_UNSAFE_RENAME": "true",
}

write_deltalake(
    "s3a://scale-dev/neumark/python-deltalake-poc/lookup_area_8277",
    df,
    mode="append",
    storage_options=storage_options,
)
print("done writing file")
