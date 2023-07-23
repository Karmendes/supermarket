
  
    

  create  table "datalake"."staging_raw"."_zona_sul__prices__dbt_tmp"
  
  
    as
  
  (
    with

source as (

    select * from "datalake"."staging"."tb_zona_sul"

),
renamed as (
    select "names" as products,
    "price",
    "source" as supermarket,
    DATE(dh_extraction) as dt_extraction
    from source
)

select * from renamed
  );
  