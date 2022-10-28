import json
from feast import FeatureStore

store = FeatureStore(repo_path="feature_repo")

entities =[
        # {join_key: entity_value}
        {"driver_id": 1004},
        {"driver_id": 1005},
    ]

print(f"Getting features for {entities}")
feature_vector = store.get_online_features(
    features=[
        "driver_hourly_stats:conv_rate",
        "driver_hourly_stats:acc_rate",
        "driver_hourly_stats:avg_daily_trips",
    ],
    entity_rows= entities,
).to_dict()

print(json.dumps(feature_vector, indent=2, default=str))
