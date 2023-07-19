
  
    

  create  table "datalake"."staging"."zona_sul__dbt_tmp"
  
  
    as
  
  (
    select names,price * 20 as total from staging.tb_zona_sul
  );
  