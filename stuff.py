from chain_db import ChainDb

db = ChainDb()


def go():
    chain = db.get_chain()

    for i in range(100):
        print('on', i)
        chain.add_data(f'mining {i}')

    db.sync(chain)


def stuff():
    nonces = [block.nonce for block in db.get_blocks()]
    print(f'avg nonce: {sum(nonces)/len(nonces)}, max: {max(nonces)}, min: {min(nonces)}')


if __name__ == '__main__':
    go()
    stuff()
    print('^')
