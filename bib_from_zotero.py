from pyzotero import zotero



if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='Generate publications markdown from Zotero collection')
    parser.add_argument('userID', type=str,
                        help='Zotero user id. You can find your userid by going in:'
                             ' https://www.zotero.org/settings/keys. There it is written: '
                             '`Your userID for use in API calls is [USERID]`. Use this id')
    parser.add_argument('key', type=str,
                        help='Private key to access zotero. You can manage '
                             'your keys at: https://www.zotero.org/settings/keys')


    zot = zotero.Zotero('4218406', 'user', 'a4mpCw5jVzcMC5UMqzMlwxPT')

zot.add_parameters(content=None)
zot.publications()
zot.collection_items('ZKPAFLT9')