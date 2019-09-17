class Register:
    def __init__(self):
        self._register = {}

    def register(self, id, ip, name, userdata):
        self._register[id] = {'ip': ip, 'name': name, 'userdata': userdata}

    def check(self, id):
        if id in self._register:
            return self._register[id]
        return {}

    def list_register(self):
        return sorted(self._register.keys())

    def delete(self, id):
        del self._register[id]

    def update(self, id, ip=None, name=None, userdata=None):
        if id not in self._register:
            raise KeyError(id)
        if ip is not None:
            self._register[id]['ip'] = ip
        if name is not None:
            self._register[id]['name'] = name
        if userdata is not None:
            self._register[id]['userdata'] = userdata
