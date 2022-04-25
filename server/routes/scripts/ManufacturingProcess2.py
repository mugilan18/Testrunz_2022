import json
import math
class MP2:
    def __init__(self, arg):
        self.arg = arg
    def Drilling(self):
        print(json.dumps({"answer":[{"Result":"Thus the drilling and boring operations has been done on the given work piece as per dimensions."}]}))        #Thus the given specimen was annealed and its hardness was studied.

    def Turning(self):
        print(json.dumps({"answer":[{"Result":"Thus the turning between the center's operation is done on the given workpiece as per the dimensions."}]}))        #Thus the given specimen was annealed and its hardness was studied.
    
    def Multi(self):
        print(json.dumps({"answer":[{"Result":"Thus, the square and multi-start thread cutting operation is performed in the given workpiece as per dimensions."}]})) 
    def Eccentric(self):
        print(json.dumps({"answer":[{"Result":" Thus the eccentric operation has been performed in the given work piece as per dimensions by using center lathe."}]}))

    def Study(self):
        print(json.dumps({"answer":[{"Result":" Thus the various parts and working principle of radial drilling machine has been studied."}]}))         
    def Drilling(self):
        print(json.dumps({"answer":[{"Result":"  Drilling and Tapping operations are performed on the given work piece as per given dimensions."}]}))         
    def Shaping(self):
        print(json.dumps({"answer":[{"Result":" Thus, a V- slot grooving is made in the given work piece to the dimensions using shaping machine."}]}))         
    def Spline(self):
        print(json.dumps({"answer":[{"Result":"Thus the spline has been made as per the dimensions on the given work piece by using milling machine."}]}))         

    def Keyway(self):
        print(json.dumps({"answer":[{"Result":"Thus the external keyway is made as per the dimensions on the given work piece using milling machine."}]}))         
    def grinding(self):
        print(json.dumps({"answer":[{"Result":"Thus the cylindrical grinding machine and its working has been studied."}]}))         
    def Cylindrical(self):
        print(json.dumps({"answer":[{"Result":"Thus the cylindrical grinding operation has been performed on the given works piece as per the dimensions using cylindrical grinding machine."}]}))         
