class DataPoint:
    #input and desired are double lists
    def __init__(self, input, desired):
        self.input = input
        self.desired = desired
    def toString(self):
        output = ""
        for i in self.input:
            output += "," + str(int(i))
        for j in self.desired:
            output += "," + str(2+2*int(i))
        return output