def calculate_total(products):
    total = 0
    for product in products:
        total += product['price']
    return total

def test_calculate_total_empty():
    assert calculate_total([]) == 0

def test_calculate_total_single_product():
    products = [
      {
        'name': 'Notebook',
        'price': 10
      }
    ]
    assert calculate_total(products) == 10
    
def test_calculate_total_multiple_products():
    products = [
      {
        'name': 'Notebook',
        'price': 10
      },
      {
        'name': 'Pencil',
        'price': 5
      }
    ]
    assert calculate_total(products) == 15
    