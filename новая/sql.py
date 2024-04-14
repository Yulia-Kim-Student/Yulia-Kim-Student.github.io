name = input()
limit = float(input())
sql_template = f'''SELECT
  id,
  SUM(product_price) AS revenue_by_user
FROM
  dataset.data_table
WHERE
  ab_test = '{name}'
GROUP BY
  id
HAVING
  revenue_by_user < {limit:.2f}'''
print(sql_template)
