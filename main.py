from bip_utils import CardanoByronLegacy, CardanoByronLegacyBip32, CardanoByronLegacySeedGenerator

class Cardano():
    def __init__(self, mnemonic : str = ''):
        self.mnemonic = mnemonic
    
    def get_address(self, count : int = 0):
        seed_bytes = CardanoByronLegacySeedGenerator(mnemonic).Generate()
        byron_legacy = CardanoByronLegacy.FromSeed(seed_bytes)
        byron_legacy = CardanoByronLegacy(
            CardanoByronLegacyBip32.FromSeed(seed_bytes)
        )
        
        return {"mnemonic" : self.mnemonic,
                "address" : byron_legacy.GetAddress(0, count),
                "private" : byron_legacy.GetPrivateKey(0, count).Raw().ToHex()}

with open("mnemonics.txt",'r',encoding='utf-8') as file:
    mnemonics = [mnemo.strip() for mnemo in file.readlines()]
    
for mnemonic in mnemonics:
    COUNT_DERIVATION_PATH = 1
    for count in range(COUNT_DERIVATION_PATH):
        try:
            keys = Cardano(mnemonic=mnemonic)
            info = keys.get_address(count)
            with open("address.txt",'a') as file:
                file.write(info["address"]+'\n')
            with open("private.txt",'a') as file:
                file.write(info["private"]+'\n')
            with open("alldata.txt",'a') as file:
                file.write(info["mnemonic"]+' '+info["private"]+' '+info["address"]+'\n')
        except:
            continue
