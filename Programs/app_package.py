# Example using package in Python

import Package.shipping
Package.shipping.calc_shipping()
print("==============================")

from Package.shipping import calc_shipping
calc_shipping()
calc_shipping()
print("===============================")

from Package import shipping
shipping.calc_shipping()
shipping.calc_shipping()
shipping.calc_shipping()
