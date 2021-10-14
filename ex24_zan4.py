if __name__ == '__main__':
    config = {
        'title':'Text Editor',
        'version':'1.4.2',
        'n_proc': 10,
        'max_mem': 4096,
        'margins':[5,10,5,10]
    }

    for key in config:
        print(f'{key} => {config[key]}')

    print('---')