import web
from random import randint

def add_letter(db, letter, ext):
    """ Adds entry into db and returns rowid."""
    return db.insert('letters', letter=letter.lower(), ext=ext)

def rm_letter(db, letter, filename):
    """ Removes entry from db if it exists.

    Returns 1 if deleted successfully, 0 otherwise.

    """
    id_num = int(filename.split('.')[0])
    ext = filename.split('.')[-1]
    if get_letter(db, id_num, letter, ext):
        where_dict = {
            'id' : id_num,
            'letter' : letter.lower(),
            'ext' : ext
        }
        db.delete('letters', where=web.db.sqlwhere(where_dict), vars=locals())
        return 1
    return 0

def get_letter(db, id_num, letter, ext):
    """ Retrieves entry from db if it exists.

    Returns None if it doesn't exist.

    """
    where_dict = {
        'id' : id_num,
        'letter' : letter.lower(),
        'ext' : ext
    }
    try:
        existing = db.select('letters', where = web.db.sqlwhere(where_dict), vars = locals())
        return existing[0]
    except:
        return None

def get_random_letter_file(db, letter):
    query = db.query("SELECT COUNT(*) AS total FROM letters WHERE letter=$letter", vars = locals())
    count = query[0].total
    if count > 0:
        matches = db.select('letters', where="letter=$letter", vars = locals())
        row = matches[randint(0, count - 1)]
        path = 'img/' + letter + '/' + str(row.id) + '.' + row.ext
        return path
    else:
        return 'img/default.png'
