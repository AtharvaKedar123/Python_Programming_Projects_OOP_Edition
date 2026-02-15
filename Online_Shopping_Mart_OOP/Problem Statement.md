## Problem Statement

Design an Online Mart Management System to manage users, products, and orders.

The system should allow users to register, products to be added to the platform, and users to place orders. The system must validate stock availability, apply discounts when applicable, and generate order totals.

---

# Class Diagram

                           +---------------------------+
                           |     ECommercePlatform     |
                           +---------------------------+
                           | - users_list : list       |
                           | - products_list : list    |
                           | - orders_list : list      |
                           +---------------------------+
                           | + register_user()         |
                           | + add_product()           |
                           | + create_order()          |
                           +---------------------------+
                                     |
       ----------------------------------------------------------------
       |                              |                              |
       | Composition                  | Composition                  | Composition
       v                              v                              v

 +----------------+            +----------------+            +----------------+
 |      User      |            |    Product     |            |      Order     |
 +----------------+            +----------------+            +----------------+
 | - user_id      |            | - product_id   |            | - order_id     |
 | - name         |            | - product_name |            | - user         |
 | - email        |            | - price        |            | - cart_items   |
 +----------------+            | - stock_quantity|           | - total_amount |
                               +----------------+            +----------------+
                               | + reduce_stock()|           | + calculate_   |
                               +----------------+            |   order_total()|
                                                             +----------------+
                                                                     |
                                                                     | Composition
                                                                     v
                                                            +----------------+
                                                            |    CartItem    |
                                                            +----------------+
                                                            | - product      |
                                                            | - quantity     |
                                                            +----------------+
                                                            | + calculate_   |
                                                            |   total()      |
                                                            +----------------+


# Class description

## User class:

1. Initialize static variable `counter` to 2000  
2. Include the following attributes:  
   - `user_id`  
   - `name`  
   - `email`  
3. Auto-generate `user_id` starting from 2001 whenever a new user object is created  

---

## Product class:

1. Initialize static variable `counter` to 5000  
2. Include the following attributes:  
   - `product_id`  
   - `product_name`  
   - `price`  
   - `stock_quantity`  
3. Auto-generate `product_id` starting from 5001 whenever a new product object is created  

4. Include method `reduce_stock(quantity)`:
   1. If `quantity` ≤ `stock_quantity`,  
      - Reduce the stock by the given quantity  
      - Return True  
   2. Else, return False  

---

## CartItem class:

1. Include the following attributes:  
   - `product` (reference to Product object)  
   - `quantity`  

2. Include method `calculate_total()`:
   1. Calculate total as `product.price × quantity`  
   2. Return the calculated total  

---

## Order class:

1. Initialize static variable `counter` to 800  
2. Include the following attributes:  
   - `order_id`  
   - `user` (reference to User object)  
   - `cart_items` (list of CartItem objects)  
   - `total_amount` (initialize to 0)  
3. Auto-generate `order_id` starting from 801 whenever a new order object is created  

4. Include method `calculate_order_total()`:
   1. Calculate total amount by summing all cart item totals  
   2. If total amount ≥ 5000,  
      - Provide 10% discount on total amount  
   3. Update `total_amount`  
   4. Return final total amount  

---

## ECommercePlatform class:

1. `users_list`: List of User objects  
2. `products_list`: List of Product objects  
3. `orders_list`: List of Order objects  

4. `register_user(name, email)`:
   1. Create a new User object  
   2. Add the user object to `users_list`  
   3. Return the created user object  

5. `add_product(product_name, price, stock_quantity)`:
   1. Create a new Product object  
   2. Add the product object to `products_list`  
   3. Return the created product object  

6. `create_order(user_id, product_id, quantity)`:
   1. Check whether the user exists in `users_list`  
   2. Check whether the product exists in `products_list`  
   3. If both exist,  
      - Check whether sufficient stock is available  
      - If stock is available,  
         - Reduce product stock  
         - Create a CartItem object  
         - Create an Order object  
         - Add CartItem to order  
         - Calculate order total  
         - Add order to `orders_list`  
         - Return final order amount  
      - Else, return False  
   4. Else, return False  

---

# Functional Requirements

1. A user cannot place an order if:
   - The user does not exist  
   - The product does not exist  
   - Requested quantity exceeds stock  

2. Discount Rule:
   - If total order amount ≥ 5000, apply 10% discount  

3. Stock must be updated immediately after successful order creation  

4. Multiple users can place orders  

---

# Constraints

1. All comparisons must be case-sensitive  
2. No duplicate ID generation  
3. IDs must be auto-generated only  
4. Lists must store object references  

---

# Expected Output Behavior

1. If order is successful → return final payable amount  
2. If order fails → return False  
3. Stock must reflect updated quantity after order  

---