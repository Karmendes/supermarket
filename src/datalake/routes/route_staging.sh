#!/bin/bash

# Execute o comando dbt run com a opção --select
# para especificar apenas o modelo "models/staging"
cd datalake && dbt run --select models/staging
