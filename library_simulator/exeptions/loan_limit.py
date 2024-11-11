class LoanLimitError(Exception):
    def __init__(self, member):
        self.message = f"The member {member} cannot take another book"
        super().__init__(self.message)