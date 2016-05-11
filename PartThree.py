class cars(object):
    def f(self):
        data = {
            'getBrand': 'Nissan',
            'setBrand': lambda x: data.update({'getBrand': x}),
            'getModel': '350z',
            'setModel': lambda x: data.update({'getModel': x})
        }

        def cf (self, d):
            if d in data:
                return data[d]
            else:
                return None
        return cf
    run = f(1)