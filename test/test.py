import pandas as pd

df = pd.read_csv("data/MachineLearningRating_v3.txt", delimiter="|", low_memory=False)

# Check column name
print("\n📋 Column Names:\n", df.columns.tolist())

# Look at the values in TrackingDevice
if "TrackingDevice" in df.columns:
    print("\n🔍 TrackingDevice Unique Values:\n", df["TrackingDevice"].value_counts(dropna=False))
else:
    print("\n❌ 'TrackingDevice' column not found!")
