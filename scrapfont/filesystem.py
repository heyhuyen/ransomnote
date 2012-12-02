import os
import os.path
import errno

def upload_file(dirpath, uid, ext, ufile):
    if not dir_exists(dirpath):
        make_dir(dirpath)
    filepath = dirpath + '/' + uid + '.' + ext
    fout = open(filepath, 'w')
    fout.write(ufile.read())
    fout.close()
    return filepath

def file_exists(path):
    dirchunks = path.split('/')
    dirpath = '/'.join(dirchunks[0:len(dirchunks)-1])
    filename = dirchunks[-1]
    return filename in os.listdir(dirpath)

def open_image(path):
    return open(path, 'rb')

def dir_exists(dirpath):
    return os.path.exists(dirpath)

def make_dir(dirpath):
    try:
        os.makedirs(dirpath)
        return dirpath
    except OSError, exc:
        if exc.errno == errno.EEXIST:
            return dirpath
        else:
            raise

def rm_dir(dirpath):
    if os.path.exists(dirpath):
        try:
            os.rmdirs(dirpath)
        except OSError, exc:
            raise

