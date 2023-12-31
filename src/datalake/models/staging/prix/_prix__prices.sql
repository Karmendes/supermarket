with

source as (

    select * from {{source('supermarkets','tb_prix')}}

),
renamed as (
    select names as products,
    REPLACE(REPLACE(prices, 'R$ ', ''),',','.')::numeric as price,
    source as supermarket,
    DATE(dh_extraction) as dt_extraction
    from source
)

select * from renamed