from crypto_utils import CryptoWallet

wallet = CryptoWallet("Alice")
wallet.deposit("BTC", 0.5)
print(wallet.view_balance())  # Output: {'BTC': 0.5}