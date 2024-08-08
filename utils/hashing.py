import hashlib

def hash_file(file):
    hasher = hashlib.sha256()
    buf = file.read()
    hasher.update(buf)
    file.seek(0)
    return hasher.hexdigest()