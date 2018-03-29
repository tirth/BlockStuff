from chain import Chain


def go():
    chain = Chain()

    for i in range(1000):
        print('on', i)
        chain.add_block(f'mined {i}')

    print('valid', chain.verify())


if __name__ == '__main__':
    go()
    print('^')
