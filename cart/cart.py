from decimal import Decimal
from django.conf import settings
from store.models import Product
import ipdb
class Cart(object):
    """Class to manipulate and to do some operations in the cart, like add product, remove,
    save in memory and retrieve products."""

    def __init__(self, request):
        """ Initialize the cart. """
        self.session = request.session
        # Check if cart is in session. If not, create an empty cart.
        cart = self.session.get(settings.CART_SESSION_ID)
        
        if not cart:
            # save an empty cart in the session
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart


    def add(self, product: Product, quantity=1) -> None:
        """This method should add a product to the cart or update its quantity"""

        try: 
            quantity = int(quantity)
        except ValueError:
            return

        product_id = str(product.id) # Transform to id to search in the cart dictionary.
        
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': quantity, 'price': str(product.price)}
            self.save()

        
        else:
            self.cart[product_id]['quantity'] += quantity
            self.save()


    def update(self, product: Product, quantity: int) -> None:
        """Update the quantity of a product in the cart"""

        try: 
            quantity = int(quantity)
        except ValueError:
            return

        product_id = str(product.id)

        if product_id in self.cart:
            self.cart[product_id]['quantity'] = quantity
            self.save()


    
    def save(self):
        self.session.modified = True


    def remove(self, product: Product) -> None:
        # Remove a product from cart.
        product_id = str(product.id)

        if product_id in self.cart:
            del self.cart[product_id]
        self.save()


    def __iter__(self):
        """Iterate over the items in the cart and get the products from the database."""

        product_ids = self.cart.keys()
        # get the product objects and add them to the cart
        products = Product.objects.filter(id__in=product_ids)
        cart = self.cart.copy()
        
        for product in products:
            cart[str(product.id)]['product'] = product
        
        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item


    def __len__(self):  
        """Count all items in the cart. """
        return sum(item['quantity'] for item in self.cart.values())
    

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())


    def get_total_quantity(self):
        return sum(item['quantity'] for item in self.cart.values())


    def clear(self):
        # remove cart from session
        del self.session[settings.CART_SESSION_ID]
        self.save()


    def __str__(self) -> str:
        return str(self.cart)