
import json

from ethereum import abi

from my_stuff.my_packages.Contracts_ABI import GNT_Deposit, get_raw_string


# x = gntw_Faucet._GNTW_Faucet__ABI
# string = x.replace('\n', "").replace('\r', "").replace('\t', "").replace(' ', "")


ex_dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

kontrakty = {}
__GNT_Deposit_Contract = abi.ContractTranslator(
    json.loads(get_raw_string(GNT_Deposit.ABI)))


tuple = ('cat', 'dog', 'mouse')

print (tuple[0])