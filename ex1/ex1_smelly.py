class OrderProcessor:
    def process_order(self, order):
        # Step 1: Validate order details
        self.validateDetails(order)

        # Step 2: Calculate total price
        total_price = self.getTotalPrice(order)

        total_price_discounted = self.getdiscount(order) * total_price

        updated = self.updateInventory(order)

        receipt = self.generateReceipt(order, total_price_discounted)

        email = self.sendEmail(order, receipt)

        return receipt
    
    def validateDetails(self, order):
        if not order.get("customer_id"):
            raise ValueError("Customer ID is required.")
        if not order.get("items"):
            raise ValueError("Order must contain items.")
    
    def getTotalPrice(self, order):
        total_price = 0
        for item in order["items"]:
            total_price += item["price"] * item["quantity"]
        return total_price

    def getdiscount(self, order):
        if order.get("discount_code") == "SUMMER20":
            return 0.8
        elif order.get("discount_code") == "WELCOME10":
            return 0.9
        else:
            return 1
    def updateInventory(self, order):
        for item in order["items"]:
            item_id = item["id"]
            quantity = item["quantity"]
            # Code to update inventory for each item
            # (for simplicity, let's assume a simple print statement here)
            print(f"Updating inventory for item {item_id}, reducing stock by {quantity}.")
    
    def generateReceipt(self, order, total_price):
        receipt = f"Customer ID: {order['customer_id']}\n"
        receipt += "Items:\n"
        for item in order["items"]:
            receipt += f"- {item['name']}: {item['quantity']} x ${item['price']}\n"
        receipt += f"Total: ${total_price:.2f}\n"
        return receipt
    
    def sendEmail(self, order, receipt):
        print(f"Sending email to customer {order['customer_id']} with receipt:\n{receipt}")

