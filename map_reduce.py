#!/usr/bin/env python
import pymongo

from utils import connect_db

def main():
    db, coll = connect_db()
    print(coll)
    print('Collection has {} documents'.format(coll.count()))

    map = """
    function() {
        var words = this.content;
        words.forEach(function(word){
            if(word.length > 3) {
                emit(word, 1);
            }
        });
    }
    """
    reduce = """
        function(key,values) {
            return Array.sum(values);
            }
    """

    # word count for all documents
    query = {}
    # filter documents
    #query = { '$or': [{'name': 'shakespeare-hamlet'}, {'name': 'shakespeare-macbeth'}]}

    coll.map_reduce(map, reduce, 'word_count', query=query)
    # Results stored in collection "word_count"
    result = db['word_count']
    cursor = result.find().sort('value', pymongo.DESCENDING)
    print('Word count for {} words'.format(cursor.count()))
    for elem in cursor.limit(25):
        print(elem)


if __name__ == '__main__':
    main()
