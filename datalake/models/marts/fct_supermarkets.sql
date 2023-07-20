

select * from {{ ref('_prix__prices') }}
union
select * from {{ ref('_zona_sul__prices') }}


