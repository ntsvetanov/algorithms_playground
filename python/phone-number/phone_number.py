class Phone(object):
    def __init__(self, phone_number):
        number =  ''.join(i for i in phone_number if i.isdigit())

        if number[0] == "1":
            if len(number) != 11:
                raise ValueError("wrong number")
            number = number[1:]
        else:
            if len(number) != 10:
                raise ValueError("wrong number")

        if number[0] == '0' or number[0] == '1':
                raise ValueError("wrong number")
        if number[3] == '0' or number[3] =='1':
            raise ValueError("wrong number")

        self.number = number
        self.area_code = self.number[:3]
        
    def pretty(self):
        return "({}) {}-{}".format(self.number[:3],  self.number[3:6],  self.number[6:])