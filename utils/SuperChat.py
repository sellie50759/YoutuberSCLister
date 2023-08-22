class SuperChat:

    def __init__(self, display_name, created_at, currency, amount_micros, comment_text):
        self.funder_name = display_name
        self.createdAt = created_at
        self.currency = currency
        self.amount = int(amount_micros)//1000000
        self.comment = comment_text

    def getTuple(self):
        return (self.funder_name,
                self.createdAt,
                self.currency,
                self.amount,
                self.comment
                )
