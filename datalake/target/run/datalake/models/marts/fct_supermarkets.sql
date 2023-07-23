
  
    

  create  table "datalake"."staging_marts"."fct_supermarkets__dbt_tmp"
  
  
    as
  
  (
    select * from "datalake"."staging_raw"."_prix__prices"
union
select * from "datalake"."staging_raw"."_zona_sul__prices"
  );
  