select
    product_id,
    product_category_name,
    product_name_lenght,
    product_description_lenght,
    product_photos_qty,
    cast(product_weight_g as decimal(10, 2)) as weight,
    cast(product_length_cm as decimal(10, 2)) as length,
    cast(product_height_cm as decimal(10, 2)) as height,
    cast(product_width_cm as decimal(10, 2)) as width
from {{ source('raw', 'products') }}
