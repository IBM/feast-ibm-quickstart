# Feast Quickstart (with IBM Cloud)
If you haven't already, check out the quickstart guide on Feast's website (http://docs.feast.dev/quickstart), which 
uses this repo. A quick view of what's in this repository's `feature_repo/` directory:

* `data/` contains raw demo parquet data
* `feature_repo/example_repo.py` contains demo feature definitions
* `feature_repo/feature_store.yaml` contains a demo setup configuring where data sources are IBM Cloud redis service for online store and IBM Cloud Data Engine for offline store.
* `feature_repo/test_workflow.py` showcases how to run all key Feast commands, including defining, retrieving, and pushing features. 

You can run the overall workflow with `python test_workflow.py`.

## To run a demo with IBM Cloud services:

1. Procure [IBM Cloud Redis](https://www.ibm.com/cloud/databases-for-redis) and [IBM Cloud Data Engine](https://www.ibm.com/cloud/data-engine) services
2. Set below environment variables
   ```
   export DATA_ENGINE_API_KEY=<DATA_ENGINE_API_KEY>
   export REDIS_PASSWORD=<REDIS_PASSWORD>
   export REDIS_CERT_PATH=<REDIS_CERT_PATH>
   ```
3. Download [ibm-cloud-data-engine plugin](https://github.ibm.com/CIO-Hackathon-2022/spectacular) project and configure path in [pyproject.toml](https://github.ibm.com/Abhay-Ratnaparkhi1/hackathon-demo/blob/main/pyproject.toml)
4. Install dependencies
   
   ```
   poetry install
   ```
4. Run [feast apply](https://docs.feast.dev/reference/feast-cli-commands#apply) to create/update feature store deployment.
   ```
   poetry run feast -c ./feature_repo apply
   ```
5. Run training by retriving historical feature information from feature store
   ```
   poetry run python training.py
   ```
6. [Materialize](https://docs.feast.dev/reference/feast-cli-commands#materialize) features from offline to online store
   ```
   poetry run feast -c ./ materialize '<START_TIMESTAMP>'  '<END_TIMESTAMP>'
   ```
7. Run inference during production to retrieve features from online store.
   ```
   poetry run python inference.py
   ```