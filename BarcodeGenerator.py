import sys
import os
import re

class BarcodeGenerator:
    

    def __init__(self, codedef, lastBarcode, numOfBarcodes):
        self.codedef = self.prepareCodedef(codedef)
        print(self.codedef)
        self.snRegex = re.compile(self.codedef)
        print(self.snRegex.match(lastBarcode))
        self.lastBarcode = lastBarcode
        self.numOfBarcodes = numOfBarcodes
    
    def prepareCodedef(self, codedef):
        newCodedef = []
        newCD = codedef[0]
        for i in range(1, len(codedef), 1):
            if ((codedef[i] == "?") and (codedef[i-1] == "(")):
                newCodedef.append("P")
                newCodedef.append(codedef[i])
                newCD += codedef[i]
                newCD += "P"
            else:
                newCodedef.append(codedef[i])
                newCD += codedef[i]

        return newCD

generator = BarcodeGenerator("(?<test>[0-9]{8})", "12345678", 10)

print(generator.codedef)