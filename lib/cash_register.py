#!/usr/bin/env python3


class CashRegister:
    def __init__(self, discount=0):
        # Validate discount input via property setter
        self._discount = 0
        self.discount = discount

        self.total = 0
        self.items = []
        self.previous_transactions = []

    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, value):
        if isinstance(value, int) and 0 <= value <= 100:
            self._discount = value
        else:
            print("Not valid discount")

    def add_item(self, item, price, quantity=1):
        """Add item to register."""
        self.total += price * quantity
        self.items.extend([item] * quantity)
        self.previous_transactions.append({
            "item": item,
            "price": price,
            "quantity": quantity
        })

    def apply_discount(self):
        """Apply discount to total."""
        if not self.previous_transactions:
            print("There is no discount to apply.")
            return

        discount_amount = self.total * (self.discount / 100)
        self.total -= discount_amount
        # Remove last transaction
        last_transaction = self.previous_transactions.pop()
        for _ in range(last_transaction["quantity"]):
            if last_transaction["item"] in self.items:
                self.items.remove(last_transaction["item"])

    def void_last_transaction(self):
        """Remove last transaction without discount logic."""
        if not self.previous_transactions:
            return
        last_transaction = self.previous_transactions.pop()
        self.total -= last_transaction["price"] * last_transaction["quantity"]
        for _ in range(last_transaction["quantity"]):
            if last_transaction["item"] in self.items:
                self.items.remove(last_transaction["item"])
