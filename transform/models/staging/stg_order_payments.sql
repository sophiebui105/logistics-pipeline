select
    order_id,
    payment_sequential,
    payment_type,
    cast(payment_installments as integer) as installments,
    cast(payment_value as decimal(10, 2)) as value
from {{ source('raw', 'order_payments') }}