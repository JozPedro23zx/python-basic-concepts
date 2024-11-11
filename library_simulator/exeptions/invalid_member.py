class InvalidMemberError(Exception):
    def __init__(self, member):
        self.message = f"Not find any member with name: {member}"
        super().__init__(self.message)