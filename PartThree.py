class cars(object):
    def f(self):
        data = {
            'brand': 'Nissan',
            '$brand': lambda x: data.update({'name': x}),
            'model': '350z',
            '$model': lambda x: data.update({'model': x})
        }

        def cf (self, d):
            if d in data:
                return data[d]
            else:
                return None
        return cf
    run = f(1)