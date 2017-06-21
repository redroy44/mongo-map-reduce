#!/usr/bin/env python
from nltk.corpus import gutenberg
from utils import connect_db

def main():
    db, coll = connect_db()
    print(coll)

    # Remove existing documents
    coll.remove({})

    for id in gutenberg.fileids():
        print(id)
        result = coll.insert_one({'name': id.split('.')[0], 'content': list(gutenberg.words(id))})

    print('Collection has {} documents'.format(coll.count()))
if __name__ == '__main__':
    main()
