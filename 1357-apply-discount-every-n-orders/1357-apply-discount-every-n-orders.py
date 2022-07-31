class Cashier:

    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.customers = 0
        self.n = n
        self.discount = (100 - discount) / 100
        self.products = products
        self.prices = prices
        self.prodMap = defaultdict(int)
        for product, price in zip(products, prices):
            self.prodMap[product] = price

    def getBill(self, product: List[int], amount: List[int]) -> float:
        self.customers += 1
        bill = 0
        for p, a in zip(product, amount):
            bill += self.prodMap[p] * a
        return bill * self.discount if self.customers % self.n == 0 else bill


# Your Cashier object will be instantiated and called as such:
# obj = Cashier(n, discount, products, prices)
# param_1 = obj.getBill(product,amount)