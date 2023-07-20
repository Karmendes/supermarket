
  
    

  create  table "datalake"."staging_raw"."_prix__prices__dbt_tmp"
  
  
    as
  
  (
    with

source as (

    select * from "datalake"."staging"."tb_prix"

),
renamed as (
    select names as products,
    REPLACE(REPLACE(prices, 'R$ ', ''),',','.')::numeric as price,
    source as supermarket,
    DATE(dh_extraction) as dt_extraction
    from source
)

select * from renamed
  );
  