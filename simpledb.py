#!/usr/bin/pyhon

__dbSeq = None

def read(topic):
    global __dbSeq
    import os
    from cPickle import load
    from settings import general
    try: db = load(open(os.path.expanduser(general['dbpath']), 'rb'))
    except: db = {'__seq': 0}
    if __dbSeq is not None and db['__seq'] != __dbSeq:
        raise "DB changed while reading"
    __dbSeq = db['__seq']
    return db.get(topic, None)

def write(topic, data):
    global __dbSeq
    import os
    from cPickle import load, dump
    from settings import general
    try: db = load(open(os.path.expanduser(general['dbpath']), 'rb'))
    except: db = {'__seq': 0}
    if __dbSeq is not None and db['__seq'] != __dbSeq:
        raise "DB changed before reading"
    db['__dbSeq'] = __dbSeq + 1
    db[topic] = data
    dump(db, open(os.path.expanduser(general['dbpath']), 'wb'))

