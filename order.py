class Order:
  """Stock transactions placed by clients. """

  num_orders = 0
  def __init__(self, client_id, quantity, price, symbol):
    Order.num_orders += 1
    self.order_id = Order.num_orders
    self.client_id = client_id
    self.quantity = quantity
    self.price = price
    self.symbol = symbol

    # Status: accepted = 1; pending = 0; decline = -1;
    self.status = 0
