import json
import math 

class EL1:
    def __init__(self, arg):
        self.arg = arg

    def Triac(self):
        argument = self.arg[0:]
        FV = float(argument[23])
        RV = float(argument[43])
        print(json.dumps({"answer":[{"Result":"Thus the V-I characteristics of TRIAC was obtained and graph was drawn.","Break over voltage in forward direction of TRIAC (VBO)":str(FV),"Break over voltage in reverse direction of TRIAC (VBO)":str(RV)}]}))

    def CRO(self):
        argument = self.arg[0:]
        #Peak voltag
        PV1 = float(argument[1])*float(argument[2])
        PV2 = float(argument[3])*float(argument[4])
        PV3 = float(argument[5])*float(argument[6])
        PV4 = float(argument[7])*float(argument[8])
        PV=(PV1+PV2+PV3+PV4)/4
        #Time period
        TP1 = float(argument[9])*float(argument[10])
        TP2 = float(argument[11])*float(argument[12])
        TP3 = float(argument[13])*float(argument[14])
        TP4 = float(argument[15])*float(argument[16])
        #Frequency
        F1 = 1/TP1
        F2 = 1/TP2
        F3 = 1/TP3
        F4 = 1/TP4
        F=(F1+F2+F3+F4)/4
        print(json.dumps({"answer":[{"Result":"Thus the Amplitude and frequency Measurement for different waveforms is obtained","Amplitude":str(PV),"Frequency":str(F)}]}))

    def PN_Juction(self):
        argument = self.arg[0:]
        def SFR(x,y):return(x/(y*0.001))
        def DFR(a,b,c,d):return((a-b)/((c-d)*0.001))
        SFR1=round((SFR(float(argument[1]),float(argument[2]))),2)
        SFR2=round((SFR(float(argument[3]),float(argument[4]))),2)
        SFR3=round((SFR(float(argument[5]),float(argument[6]))),2)
        SFR4=round((SFR(float(argument[7]),float(argument[8]))),2)
        SFR5=round((SFR(float(argument[9]),float(argument[10]))),2)
        SFR6=round((SFR(float(argument[11]),float(argument[12]))),2)
        SFR7=round((SFR(float(argument[13]),float(argument[14]))),2)
        SFR8=round((SFR(float(argument[15]),float(argument[16]))),2)
        SFR9=round((SFR(float(argument[17]),float(argument[18]))),2)

        DFR1=round((DFR(float(argument[3]),float(argument[1]),float(argument[4]),float(argument[2]))),2)
        DFR2=round((DFR(float(argument[5]),float(argument[3]),float(argument[6]),float(argument[4]))),2)
        DFR3=round((DFR(float(argument[7]),float(argument[5]),float(argument[8]),float(argument[6]))),2)
        DFR4=round((DFR(float(argument[9]),float(argument[7]),float(argument[10]),float(argument[8]))),2)
        DFR5=round((DFR(float(argument[11]),float(argument[9]),float(argument[12]),float(argument[10]))),2)
        DFR6=round((DFR(float(argument[13]),float(argument[11]),float(argument[14]),float(argument[12]))),2)
        DFR7=round((DFR(float(argument[15]),float(argument[13]),float(argument[16]),float(argument[14]))),2)
        DFR8=round((DFR(float(argument[17]),float(argument[15]),float(argument[18]),float(argument[16]))),2)

        SRR1=SFR(float(argument[19]),float(argument[20]))
        SRR2=SFR(float(argument[21]),float(argument[22]))
        SRR3=SFR(float(argument[23]),float(argument[24]))
        SRR4=round(SFR(float(argument[25]),float(argument[26])),2)
        SRR5=SFR(float(argument[27]),float(argument[28]))
        SRR6=round(SFR(float(argument[29]),float(argument[30]))/100,2)
        SRR7=round(SFR(float(argument[31]),float(argument[32]))/100,2)
        SRR8=SFR(float(argument[33]),float(argument[34]))/100
        SRR9=round(SFR(float(argument[35]),float(argument[36]))/100,2)

        DRR1=DFR(float(argument[21]),float(argument[19]),float(argument[22]),float(argument[20]))
        DRR2=round(DFR(float(argument[23]),float(argument[21]),float(argument[24]),float(argument[22])))
        DRR3=round(DFR(float(argument[25]),float(argument[23]),float(argument[26]),float(argument[24])))
        DRR4=round(DFR(float(argument[27]),float(argument[25]),float(argument[28]),float(argument[26])),2)
        DRR5=DFR(float(argument[29]),float(argument[27]),float(argument[30]),float(argument[28]))
        DRR6=DFR(float(argument[31]),float(argument[29]),float(argument[32]),float(argument[30]))
        DRR7=DFR(float(argument[33]),float(argument[31]),float(argument[34]),float(argument[32]))
        DRR8=DFR(float(argument[35]),float(argument[33]),float(argument[36]),float(argument[34]))
        print(json.dumps({"answer":[{"Result":"The static and dynamic resistances of the PN Junction Diode are calculated from the forward and reverse bias Characteristics.","Static forward resistance":str(SFR1)+"Ω, "+str(SFR2)+"Ω, "+str(SFR3)+"Ω, "+str(SFR4)+"Ω, "+str(SFR5)+"Ω, "+str(SFR6)+"Ω, "+str(SFR7)+"Ω, "+str(SFR8)+"Ω, "+str(SFR9)+"Ω","Dynamic forward resistance":
        str(DFR1)+"Ω, "+str(DFR2)+"Ω, "+str(DFR3)+"Ω, "+str(DFR4)+"Ω, "+str(DFR5)+"Ω, "+str(DFR6)+"Ω, "+str(DFR7)+"Ω, "+str(DFR8)+"Ω","Static reverse Characteristics":str(SRR1)+"Ω, "+str(SRR2)+"Ω, "+str(SRR3)+"Ω, "+str(SRR4)+"Ω, "+str(SRR5)+"Ω, "+str(SRR6)+"Ω, "+str(SRR7)+"Ω, "+str(SRR8)+"Ω, "+str(SRR9)+"Ω","Dynamic reverse Characteristics":str(DRR1)+"Ω, "+str(DRR2)+"Ω, "+str(DRR3)+"Ω, "+str(DRR4)+"Ω, "+str(DRR5)+"Ω, "+str(DRR6)+"Ω, "+str(DRR7)+"Ω, "+str(DRR8)+"Ω"}]}))

    def Clipper(self):
        argument = self.arg[0:]
        def M(x,y):return(x*y)
        A1=M(float(argument[1]),float(argument[5]))
        A2=M(float(argument[1]),float(argument[9]))
        T1=round(M(float(argument[2]),float(argument[6])),2)
        T2=round(M(float(argument[2]),float(argument[10])),2)
        A3=M(float(argument[3]),float(argument[7]))
        A4=M(float(argument[3]),float(argument[11]))
        T3=round(M(float(argument[4]),float(argument[8])),2)
        T4=round(M(float(argument[4]),float(argument[12])),2)

        A5=M(float(argument[13]),float(argument[17]))
        A6=M(float(argument[13]),float(argument[21]))
        T5=round(M(float(argument[14]),float(argument[18])),2)
        T6=round(M(float(argument[14]),float(argument[22])),2)
        A7=M(float(argument[15]),float(argument[19]))
        A8=M(float(argument[15]),float(argument[23]))
        T7=round(M(float(argument[16]),float(argument[20])),2)
        T8=round(M(float(argument[16]),float(argument[24])),2)
        # print(json.dumps({"d":[{"r":"r","S":str(A1)+str(A2)+str(A3)+str(A4)
        # +str(T1)+str(T2)+str(T3)+str(T4)}]}))
        print(json.dumps({"answer":[{"Result":"Thus the output performance for the clippers and clampers circuit is verified.",
        "Input waveform":str(),"Positive Clipper":str(A1)+"V, "+str(T1)+"ms","Positive Clamper":str(A5)+"V, "+str(T5)+"ms",
        "Negative clipper":str(A2)+"V, "+str(T2)+"ms","Negative clamper":str(A6)+"V, "+str(T6)+"ms","Output waveform":str(),"positive clipper":str(A3)+"V, "+str(T3)+"ms","positive clamper":str(A7)+"V, "+str(T7)+"ms","negative clipper":str(A4)+"V, "+str(T4)+"ms","negative clamper":str(A8)+"V, "+str(T8)+"ms"}]}))        
    
    def zener(self):
        argument = self.arg[0:]
        def SFR(x,y):return(x/(y*0.001))
        def DFR(a,b,c,d):return((a-b)/((c-d)*0.001))
        SFR1=round((SFR(float(argument[1]),float(argument[2]))),2)
        SFR2=round((SFR(float(argument[3]),float(argument[4]))),2)
        SFR3=round((SFR(float(argument[5]),float(argument[6]))),2)
        SFR4=round((SFR(float(argument[7]),float(argument[8]))),2)
        SFR5=round((SFR(float(argument[9]),float(argument[10]))),2)
        SFR6=round((SFR(float(argument[11]),float(argument[12]))),2)
        SFR7=round((SFR(float(argument[13]),float(argument[14]))),2)
        SFR8=round((SFR(float(argument[15]),float(argument[16]))),2)
        SFR9=round((SFR(float(argument[17]),float(argument[18]))),2)
        SFR10=round((SFR(float(argument[19]),float(argument[20]))),2)

        DFR1=round((DFR(float(argument[3]),float(argument[1]),float(argument[4]),float(argument[2]))),2)
        DFR2=round((DFR(float(argument[5]),float(argument[3]),float(argument[6]),float(argument[4]))),2)
        DFR3=round((DFR(float(argument[7]),float(argument[5]),float(argument[8]),float(argument[6]))),2)
        DFR4=round((DFR(float(argument[9]),float(argument[7]),float(argument[10]),float(argument[8]))),2)
        DFR5=round((DFR(float(argument[11]),float(argument[9]),float(argument[12]),float(argument[10]))),2)
        DFR6=round((DFR(float(argument[13]),float(argument[11]),float(argument[14]),float(argument[12]))),2)
        DFR7=round((DFR(float(argument[15]),float(argument[13]),float(argument[16]),float(argument[14]))),2)
        DFR8=round((DFR(float(argument[17]),float(argument[15]),float(argument[18]),float(argument[16]))),2)
        DFR9=round((DFR(float(argument[19]),float(argument[17]),float(argument[20]),float(argument[18]))),2)


        SRR2=SFR(float(argument[21]),float(argument[22]))
        SRR3=round(SFR(float(argument[23]),float(argument[24])),2)
        SRR4=round(SFR(float(argument[25]),float(argument[26])),2)
        SRR5=round(SFR(float(argument[27]),float(argument[28])),2)
        SRR6=round(SFR(float(argument[29]),float(argument[30])),2)
        SRR7=round(SFR(float(argument[31]),float(argument[32])),2)
        SRR8=round(SFR(float(argument[33]),float(argument[34])),2)
        SRR9=round(SFR(float(argument[35]),float(argument[36])),2)
        SRR10=round(SFR(float(argument[37]),float(argument[38])))
        SRR11=round(SFR(float(argument[39]),float(argument[40])))

        DRR2=round(DFR(float(argument[23]),float(argument[21]),float(argument[24]),float(argument[22])))
        DRR3=round(DFR(float(argument[25]),float(argument[23]),float(argument[26]),float(argument[24])))
        DRR4=round(DFR(float(argument[27]),float(argument[25]),float(argument[28]),float(argument[26])),2)
        DRR5=round(DFR(float(argument[29]),float(argument[27]),float(argument[30]),float(argument[28])))
        DRR6=round(DFR(float(argument[31]),float(argument[29]),float(argument[32]),float(argument[30])))
        DRR7=round(DFR(float(argument[33]),float(argument[31]),float(argument[34]),float(argument[32])))
        DRR8=round(DFR(float(argument[35]),float(argument[33]),float(argument[36]),float(argument[34])))
        DRR9=round(DFR(float(argument[37]),float(argument[35]),float(argument[38]),float(argument[36])))
        DRR10=round(DFR(float(argument[39]),float(argument[37]),float(argument[40]),float(argument[38])))

        print(json.dumps({"answer":[{"Result":"The VI characteristics of the zener diode is plotted and following parameters are calculated","Static forward resistance":str(SFR1)+"Ω, "+str(SFR2)+"Ω, "+str(SFR3)+"Ω, "+str(SFR4)+"Ω, "+str(SFR5)+"Ω, "+str(SFR6)+"Ω, "+str(SFR7)+"Ω, "+str(SFR8)+"Ω, "+str(SFR9)+"Ω, "+str(SFR10)+"Ω","Dynamic forward resistance":
        str(DFR1)+"Ω, "+str(DFR2)+"Ω, "+str(DFR3)+"Ω, "+str(DFR4)+"Ω, "+str(DFR5)+"Ω, "+str(DFR6)+"Ω, "+str(DFR7)+"Ω, "+str(DFR8)+"Ω, "+str(DFR9)+"Ω","Static reverse Characteristics":str(SRR2)+"Ω, "+str(SRR3)+"Ω, "+str(SRR4)+"Ω, "+str(SRR5)+"Ω, "+str(SRR6)+"Ω, "+str(SRR7)+"Ω, "+str(SRR8)+"Ω, "+str(SRR9)+"Ω, "+str(SRR10)+"Ω, "+str(SRR11)+"Ω ","Dynamic reverse Characteristics":str(DRR2)+"Ω, "+str(DRR3)+"Ω, "+str(DRR4)+"Ω, "+str(DRR5)+"Ω, "+str(DRR6)+"Ω, "+str(DRR7)+"Ω, "+str(DRR8)+"Ω, "+str(DRR9)+"Ω, "+str(DRR10)+"Ω"}]}))

    
    def Bias(self):
        print(json.dumps({"answer":[{"Result":"Thus the various biasing circuits has been designed and tested successfully."}]})) 
    
    def SCR(self):
        print(json.dumps({"answer":[{"Result":"The Characteristics of SCR was studied and the graphs were plotted."}]})) 
    def Half(self):
        argument = self.arg[0:]
        Vrms1= float(argument[3])/2 
        Vdc= round(float(argument[3])/3.14,2)
        r1=round(math.sqrt(((Vrms1/Vdc)**2)-1),3)
        e1=round(((Vdc/Vrms1)**2)*100,3)
        Vrms2=round(math.sqrt((Vrms1**2)+(Vdc**2)),2)
        RP=round((Vrms2/Vdc),2)
        e2=round(((Vdc/Vrms2)**2)*100,2)
        print(json.dumps({"answer":[{"Result":"The input and output waveforms of the half-wave Rectifier and also calculate its load regulation and ripple factor.","With Filter":str(),"Vrms":str(Vrms1)+"V" ,"Vdc": str(Vdc)+"V ","Ripple factor,r":str(r1),"Efficiency(η)":str(e1)+" %","Without filter":str(),"Vrms1":str(Vrms2)+"V","Ripple Factor(r)":str(RP),"Efficiency η":str(e2)+" %"}]})) 

    def Full(self):
        argument = self.arg[0:]
        Vrms1= round(float(argument[3])/(math.sqrt(2)) ,2)                                                                                                                                                                                                                                                              
        Vdc1= round(((2*float(argument[3]))/3.14),2)
        r1=round((math.sqrt(((Vrms1/Vdc1)**2)-1))*100)
        e1=round(((Vdc1/Vrms1)**2)*100,3)
        Vrms2=round(float(argument[6])/(math.sqrt(2)),2)
        Vdc2=round(((2*float(argument[6]))/3.14),2)
        RP=round((math.sqrt((Vrms2**2)+(Vdc2**2))),2)
        e2=round(((Vdc2/Vrms2)**2)*100,2)
        print(json.dumps({"answer":[{"Result":"The input and output waveforms of the full-wave Rectifier and also calculate its load regulation and ripple factor.","With Filter":str(),"Vrms":str(Vrms2)+"V" ,"Vdc": str(Vdc2)+"V ","Ripple factor,r":str(RP),"Efficiency(η)":str(e2)+" %","Without filter":str(),"Vrms1":str(Vrms1)+"V","Vdc":str(Vdc2)+"V","Ripple Factor(r)":str(r1),"Efficiency η":str(e1)+" %"}]})) 



    def CB(self):
        argument = self.arg[0:]
        I= round((float(argument[27])/float(argument[28])) *1000 ,2)
        O= round((float(argument[29])/float(argument[30])) *100,2)
        F= (float(argument[69])/float(argument[70]))
        R= (float(argument[71])/float(argument[72]))
        
        print(json.dumps ({"answer":[{"Result":"The input and output characteristics of the bipolar junction transistor in common base confirguration is obtained.","Input Impedance":str(I)+" Ω","Output Impedance":str(O)+" mv ","Forward current gain":str(F)+" mv ","Reverse current gain":str(R)+" mv"}]}))
    def CE(self):
        argument = self.arg[0:]
        def D(x,y):return(x/y)
        IM=round(D(float(argument[15]),float(argument[16])),2)
        OA=round(D(float(argument[33]),float(argument[34])),2)
        FCG=round(D(float(argument[33]),float(argument[35])),2)
        RVG=round(D(float(argument[17]),float(argument[34])),2)
        print(json.dumps({"answer":[{"Result":"Thus the input and output characteristics of the bipolar junction transistor in  Common Emitter configuration is obtained.","Input Impedance":str(IM)+" Ω",
        "Output Impedance":str(OA)+" mv ","Forward current gain":str(FCG)+" mv ","Reverse current gain":str(RVG)+" mv"}]}))

    def JFET(self):
        print(json.dumps({"answer":[{"Result":"Thus the  Drain  & Transfer  characteristics  of given  FET is Plotted. "}]}))         
    
    def UJT(self):
        argument = self.arg[0:]
        n1=round(( float(argument[35])+ float(argument[36]))/2)
        print(json.dumps({"answer":[{"Result":"The characteristics of UJT is obtained and the intrensic stand - off ratio(η) is determined","Ratio(η)":str(n1)}]}))         
