import unittest
from client3 import getDataPoint
from client3 import getRatio

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    dataPoint = ('ABC', 120.48, 121.2, 120.48)  # Expected data point
    self.assertEqual(getDataPoint(quotes[0]), dataPoint)  # Assert equality of computed data point and expected data point

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    dataPoint = ('ABC', 120.48, 119.2, 120.48)  # Expected data point where bid price is greater than ask price
    self.assertEqual(getDataPoint(quotes[0]), dataPoint)  # Assert equality of computed data point and expected data point


  """ ------------ Add more unit tests ------------ """
  def test_getRatio_when_price_b_not_zero(self):
    """ Test when price_b is not zero """
    price_a = 20
    price_b = 10
    expected_ratio = 2
    self.assertEqual(getRatio(price_a, price_b), expected_ratio)
    
  def test_getRatio_when_price_b_zero(self):
    """ Test when price_b is zero """
    price_a = 10
    price_b = 0
    self.assertIsNone(getRatio(price_a, price_b))


if __name__ == '__main__':
    unittest.main()
