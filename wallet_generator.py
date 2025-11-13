from algosdk import account, mnemonic

private_key, address = account.generate_account()
print("✅ New Algorand Account Created Successfully!")
print("Address:", address)

mnemo = mnemonic.from_private_key(private_key)
print("\nMnemonic Passphrase (Save this safely):")
print(mnemo)
