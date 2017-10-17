
from calendar import timegm
from datetime import datetime
import pytz

from ethereum.utils import zpad
from web3 import Web3, HTTPProvider, IPCProvider

# first start geth:
# $ geth --rinkeby


web3 = Web3(IPCProvider('/home/ggruszczynski/.ethereum/rinkeby/geth.ipc'))
web3.eth.getBlock('latest')
syncing = web3.eth.syncing

my_address_pad = '0x000000000000000000000000aa4abfaaa535087386e9c5bc82b7c858224988bf'
my_address = '0xaa4abfaaa535087386e9c5bc82b7c858224988bf'

LOG_ID = '0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef'  # noqa

block_num = 753335
block_hash = '0xa435eda52586183f1362dcebb42b3ccf15ee4e033d2420543fa5be1130644f27'

from time import sleep
def is_syncing():
    def get_timestamp_utc():
        now = datetime.now(pytz.utc)
        return datetime_to_timestamp(now)

    def datetime_to_timestamp(then):
        return timegm(then.utctimetuple()) + then.microsecond / 1000000.0

    """
    :return: Returns either False if the node is not syncing, True otherwise
    """
    syncing = web3.eth.syncing
    if syncing:
        return syncing['currentBlock'] < syncing['highestBlock']

    # node may not have started syncing yet
    try:
        last_block = web3.eth.getBlock('latest')
    except Exception as ex:
        return False
    if isinstance(last_block, dict):
        timestamp = int(last_block['timestamp'])
    else:
        timestamp = last_block.timestamp
    return get_timestamp_utc() - timestamp > 120

#
# syncing = True
# while syncing:
#     try:
#         syncing = is_syncing()
#         print('syncing...')
#     except Exception as e:
#         syncing = False
#     else:
#         sleep(0.5)

print('--------------- synced ----------------')

def new_filter(from_block="latest", to_block="latest", address=None, topics=None):
    """
    Creates a filter object, based on filter options, to notify when the state changes (logs)
    :param from_block: Integer block number, or "latest" for the last mined block
    or "pending", "earliest" for not yet mined transactions
    :param to_block: Integer block number, or "latest" for the last mined block
    or "pending", "earliest" for not yet mined transactions
    :param address: Contract address or a list of addresses from which logs should originate
    :param topics: Array of 32 Bytes DATA topics. Topics are order-dependent.
    Each topic can also be an array of DATA with "or" options
    :return: filter id
    """
    if topics is not None:
        for i in range(len(topics)):
            topics[i] = add_padding(topics[i])
    obj = {
        'fromBlock': from_block,
        'toBlock': to_block,
        'address': add_padding(address),
        'topics': topics
    }
    return web3.eth.filter(obj).filter_id

def get_filter_changes(self, filer_id):
    """
    Polling method for a filter, which returns an array of logs which occurred since last poll
    :param filer_id: the filter id
    :return: Returns all new entries which occurred since the last call to this method for the given filter_id
    """
    return web3.eth.getFilterChanges(add_padding(filer_id))

def get_logs(from_block=None, to_block=None, address=None, topics=None):
    """
    Retrieves logs based on filter options
    :param from_block: Integer block number, or "latest" for the last mined block
    or "pending", "earliest" for not yet mined transactions
    :param to_block: Integer block number, or "latest" for the last mined block
    or "pending", "earliest" for not yet mined transactions
    :param address: Contract address or a list of addresses from which logs should originate
    :param topics: Array of 32 Bytes DATA topics. Topics are order-dependent.
    Each topic can also be an array of DATA with "or" options
    topic[hash, from, to]
    The first topic is the hash of the signature of the event (e.g. Deposit(address,bytes32,uint256)), except you declared the event with the anonymous specifier.)
    :return: Returns log entries described by filter options
    """
    for i in range(len(topics)):
        topics[i] = add_padding(topics[i])
    filter_id = new_filter(from_block, to_block, add_padding(address), topics)
    return web3.eth.getFilterLogs(filter_id)


def add_padding(address):
    """
    Provide proper length of address and add 0x to it
    :param address: Address to validation
    :return: Padded address
    """
    if address is None:
        return address
    elif isinstance(address, str):
        address = address.encode()
    if isinstance(address, bytes):
        if address.startswith(b'0x'):
            return address
        return b'0x' + zpad(address, 32)
        raise TypeError('Address must be a string or a byte string')



block_info = web3.eth.getBlock(block_hash)
print(block_info)

logs = get_logs(from_block=block_num,
                        to_block=block_num,
                        topics=[LOG_ID, None, my_address_pad])

print('----------logs----------------')

block_num = 760513
income_log = get_logs(from_block=block_num,
                        to_block=block_num,
                        topics=[LOG_ID, None, my_address_pad])

sender = income_log[0]['topics'][1][-40:]
receiver = income_log[0]['topics'][2][-40:]
log_value = int(income_log[0]['data'], 16)

print(logs)

# value = 0.000416578782929315