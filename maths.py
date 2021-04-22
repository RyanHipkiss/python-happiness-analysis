from math import log10, floor

class Maths:
    @staticmethod
    def mean(values):
        return Maths.sigfig(sum(values) / len(values))

    @staticmethod
    def sigfig(number, sf=3):
        return round(number, sf-int(floor(log10(abs(number))))-1)

    @staticmethod
    def float(number):
        return Maths.sigfig(float(number))