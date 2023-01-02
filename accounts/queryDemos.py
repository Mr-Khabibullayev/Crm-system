from .models import *
#*** (1) Return all customers from customer table
customers = Customer.objects.all()

#(2) Return last customer in table
firstCustomer = Customer.objects.first()

#(3) Return last customer in table
lastCustomer = Customer.objects.last()

#(4) Return single customer by name
customerByName = Customer.objects.get(name='axrorbek')

#***(5)  Return single customer by name
customerById = Customer.objects.get(id=4)

#***(6) Return all orders to customer (firstCustomer variable set above)
firstCustomer.order_set.all()

#***(7) Return orders customer name: (Query parent model values)
order = Order.objects.first()
parentName = order.customer.name

#***(8) Return products from products table with value of "Out Door" in category attribute
products = Product.objects.filter(category="Out Door")

#***(9) Order/Sort Objects by id
leastToGreatest = Product.objects.all().order_by('id')
greatestToLeast = Product.objects.all().order_by('-id')


#(10) return all products with tag of "Sports" : (Query Many to many Fields)
productsFilter = Product.objects.filter(tag__name='Sports')



##  Return the total count for number of time  a 'Ball' was ordered by the first customer 
ballOrders = firstCustomer.order_set().filter(product__name='Ball').count()

allOrders ={}

for order in firstCustomer.order_set.all():
    if order.product.name in allOrders:
        allOrders[order.product.name] += 1
    else:
        allOrders[order.product.name] = 1
        
#Return : allOrders: {'Ball': 2,'BBG Grill': 1}

# RELATED SET EXAMPLE
class ParentModel(models.Model):
    name = models.CharField(max_length=200, null=True)

class ChildModel(models.Model):
    parent = models.ForeignKey(ParentModel)
    name = models.CharField(max_length=200, null=True)
    
    
parent = ParentModel.objects.first()
# Return all child models related  to parent 
parent.childmodel_set.all()