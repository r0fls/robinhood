import hashlib
# this isn't to spec, just demonstrates the concept
hashes = [hashlib.md5,
          hashlib.sha256,
          hashlib.sha224,
          hashlib.sha1,
          hashlib.sha384,
          hashlib.sha512,
          hashlib.sha512,
          ]

class node:
    def __init__(self, string, probe_length, method):
        self.string = string
        self.probe_length = probe_length
        self.method = method

    def __repr__(self):
        return self.string

    def __eq__(self, string):
        return self.string == string

class robinhood(dict):
    def __init__(self, length):
        self.length = length

    def insert(self, string, probe_length=0):
        for h in hashes[probe_length:]:
            if not self.get(h(string).hexdigest()[:self.length], None):
                self[h(string).hexdigest()[:self.length]] = node(string, probe_length, h)
                return
            else:
                if self[h(string).hexdigest()[:self.length]] == string:
                    return
                current_probe_length = self[h(string).hexdigest()[:self.length]].probe_length
                if current_probe_length >= probe_length:
                    probe_length += 1
                    continue
                else:
                    new_string = self[h(string).hexdigest()[:self.length]].string
                    self[h(string).hexdigest()[:self.length]] = node(string, probe_length, h)
                    self.insert(new_string, current_probe_length)
                    return
