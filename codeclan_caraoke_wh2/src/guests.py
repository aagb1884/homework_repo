class Guests:
    def __init__(self, name, wallet, fave_song):
        self.name = name
        self.wallet = wallet
        self.fave_song = fave_song

    def pay_entry(self, entry_fee):
        self.wallet -= entry_fee