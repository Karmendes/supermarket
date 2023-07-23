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