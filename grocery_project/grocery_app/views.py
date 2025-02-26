from django.shortcuts import render

# Grocery items and their prices
grocery_items = [
    {'name': 'Apples', 'price': 2.5},
    {'name': 'Bananas', 'price': 1.2},
    {'name': 'Carrots', 'price': 1.0},
    {'name': 'Milk', 'price': 1.5},
    {'name': 'Eggs', 'price': 3.0},
    {'name': 'Bread', 'price': 1.8},
]

def grocery_list(request):
    selected_items = []
    total_price = 0.0

    # If the form is submitted (POST request)
    if request.method == 'POST':
        # Get the selected items from the form
        for item in grocery_items:
            if item['name'] in request.POST:
                selected_items.append(item)
                total_price += item['price']
    
    return render(request, 'grocery_app/grocery_list.html', {
        'grocery_items': grocery_items,
        'selected_items': selected_items,
        'total_price': total_price
    })
