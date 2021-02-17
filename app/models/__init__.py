
class City_data:

    def __init__(self, name, temperature, condition):
        self.name = name
        self.temperature = temperature
        self.condition = condition

    def data_dict(self):
        return {'City_name': self.name,
                'City_temp': self.temperature,
                'City_condition': self.condition}
