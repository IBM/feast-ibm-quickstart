# Copyright 2022 Abhay Ratnaparkhi, Michal Siedlaczek
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# This is an example feature definition file

from datetime import timedelta

import pandas as pd

from feast import (
    Entity,
    FeatureService,
    FeatureView,
    Field,
    FileSource,
    PushSource,
    RequestSource,
)
from feast.on_demand_feature_view import on_demand_feature_view
from feast.types import Float32, Float64, Int64

from ibm_data_engine import DataEngineDataSource

# Define an entity for the driver. You can think of an entity as a primary key used to
# fetch features.
driver = Entity(name="driver", join_keys=["driver_id"])

# Read data from IBM Cloud Data Engine Tables backed by Object store. The Data Engine stores data in IBM Cloud Object
# Store and Table Definitions are stored in Data Engine
# for more info. https://cloud.ibm.com/docs/sql-query/sql-query.htm


driver_stats_source = DataEngineDataSource(
    name="driver_hourly_stats_source",
    table="driver_stats_demo",
    timestamp_field="event_timestamp",
)
# Our  IBM Cloud Data Engine Table contain sample data that includes a driver_id column, timestamps and
# three feature column. Here we define a Feature View that will allow us to serve this
# data to our model online.
driver_stats_fv = FeatureView(
    # The unique name of this feature view. Two feature views in a single
    # project cannot have the same name
    name="driver_hourly_stats",
    entities=[driver],
    ttl=timedelta(days=1),
    # The list of features defined below act as a schema to both define features
    # for both materialization of features into a store, and are used as references
    # during retrieval for building a training dataset or serving features
    schema=[
        Field(name="conv_rate", dtype=Float32),
        Field(name="acc_rate", dtype=Float32),
        Field(name="avg_daily_trips", dtype=Int64),
    ],
    online=True,
    source=driver_stats_source,
    # Tags are user defined key/value pairs that are attached to each
    # feature view
    tags={"team": "driver_performance"},
)
