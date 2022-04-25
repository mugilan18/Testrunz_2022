import json

class MP1:
    def __init__(self, arg):
        self.arg = arg
    def Lathe(self):
        print(json.dumps({"answer":[{"Result":"Thus the working principle of the lathe machine and its parts are studied thoroughly."}]}))        #Thus the given specimen was annealed and its hardness was studied.

    def V_Shaping(self):
        print(json.dumps({"answer":[{"Result":"Thus a V- shape is made in the given workpiece to the dimensions as shown in  the figure using a shaper machine."}]}))        #Thus the given specimen was annealed and its hardness was studied.
    
    def Cube(self):
        print(json.dumps({"answer":[{"Result":"The cube milling was performed on the given workpiece to the required dimensions."}]})) 
    def Cube_Shaping(self):
        print(json.dumps({"answer":[{"Result":"Thus a cube is made in the given workpiece to the dimensions as shown in the figure using shaper machine."}]}))

    def Facing(self):
        print(json.dumps({"answer":[{"Result":"Thus the required size and shape of the given work piece is obtained"}]}))         
    def Step(self):
        print(json.dumps({"answer":[{"Result":"Thus step milling was performed on the given work piece to the required dimensions."}]}))         
    def Turning(self):
        print(json.dumps({"answer":[{"Result":"Thus the required size and shape of the given work piece is obtained. "}]}))         
    def Compound(self):
        print(json.dumps({"answer":[{"Result":"Thus the required size and shape of the given work piece is obtained."}]}))         

    def V_Thread(self):
        print(json.dumps({"answer":[{"Result":"Thus, thread cutting operation is performed in the given workpiece."}]}))         
