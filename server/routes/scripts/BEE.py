# import json
# import math as m

# class BEE:
#     def __init__(self, arg):
#         self.arg = arg

#     def CRO(self):
#         argument = self.arg[0:]
#         p1=(float(argument[2])* float(argument[3]))
#         p2=(float(argument[5])* float(argument[6]))
#         p3=(float(argument[8])* float(argument[9]))
#         p4=(float(argument[11])* float(argument[12]))
#         p5=(float(argument[14])* float(argument[13]))
#         p = (p1+p2+p3+p4+p5)/5
#         TP1 =(float(argument[17])* float(argument[18]))
#         TP2=(float(argument[20])* float(argument[21]))
#         TP3 =(float(argument[23])* float(argument[24]))
#         TP4 =(float(argument[26])* float(argument[27]))
#         TP5 =(float(argument[29])* float(argument[30]))
#         TP = (TP1+TP2+TP3+TP4+TP5)/5
#         F =((1/TP1)+(1/TP2)+(1/TP3)+(1/TP4)+(1/TP4))/5
#         print(json.dumps({"length":[{"Peak voltage is " : str(p),"Time period is " : str(TP)}], "breadth":[{"Frequency mesurement for different waveform " : str(F)}] }))

