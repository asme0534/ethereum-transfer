from web3 import Web3

# Ganache Testnet
ganache_mode = True

ganache_url = "HTTP://127.0.0.1:8545"

# infura apikey
infura_apikey = "e4db0eb0005b4129bc5f79095657cb51" 
infura_url= f"https://mainnet.infura.io/v3/e4db0eb0005b4129bc5f79095657cb51{infura_apikey}"


# Public key & Private key accounts
victim_address = "0x7Be6Ec941331450641337fEBE7c0d5D6Ec71d57d" # The victim's ETH address
victim_key = "b8741eb5839da02a26a0ca6aa984719be88522f526495a07f9f1b52e578653ad" # The victim's private key


recipient_address = "0x5f946e326042f1745e0dC6544E50F807198FC8b9" # An account you want to send ETH to
