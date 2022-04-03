# import re
# pattern = r"(@#+)([A-Z][A-Za-z\d]{5,})\1"
# check = int(input())
# words = []
#
#
# for i in range(check):
#     word = input()
#     words = re.findall(pattern, word)
#     if words:
#         product_group = "".join([x for x in words[0][1] if x.isdigit()])
#         if not product_group:
#             product_group = '00'
#         print(f'Product group: {product_group}')
#     else:
#         print('Invalid barcode')

import re

count_of_barcodes = int(input())

for value in range(count_of_barcodes):
    barcode = input()
    barcode_pattern = r'\@\#+([A-Z][A-Za-z0-9]{4,}[A-Z])\@\#+'
    is_valid = re.findall(barcode_pattern, barcode)

    if is_valid:
        barcode = ''.join(is_valid)
        product_group = ''.join([x for x in barcode if x.isdigit()])
        if not product_group:
            product_group = '00'
        print(f'Product group: {product_group}')
    else:
        print('Invalid barcode')
