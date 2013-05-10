clear all
clc
global RMIX Y MdotFuelLbm
LHVBTU=20960;%BTU/lbm
LHV=LHVBTU*1.055*2.2046;%kJ/kg
Y=[0 0 0.21 0.79 0 0];
MdotAir=167.78;%kg/s
RH(1)=0.6;
Rv=15;
Ncomp=.866; Nturb=.885; Ngen=.985;
delPin=4; delPout=4;
for ii=1:1
    %******************************State 0******************************
    To=[59 100];%degrees F
    T0=(To(ii)-32)/1.8;%degrees C
    P0=14.696;%psiA
    HR(1)=.622*RH(1)*SatP(T0)/(101.325-RH(1)*SatP(T0));
    Temp0(1:9)=T0+273;

    %******************************State 1******************************
    P1=(P0-0.036*(delPin))/.14504;%kPa
    T1=T0;
    AIR1=values([T1 P1]);%returns array with values: [h u s k] at given T and P
    Temp1(1:9)=T1+273;

    MdotFuelLbm(1)=50000;
    Load=[1:-0.01:.2];

    %******************************State 2******************************
    P2=P1;%kPa
    evap=0;%Evaporative cooler on(1) or off(0)
    if evap==1
        i=1;
        T2a=0;
        T2b=T1;
        delH=10;
        while(abs(delH(i))>=.00001 & i<100)
            T2=(T2a+T2b)/2;%degrees C
            HR(2)=.622*SatP(T2)/(P2-SatP(T2));
            AIR2=values([T2 P2]);
            delH(i+1)= AIR1(1)+(HR(1)*Hvapor(T1))+((HR(2)-HR(1)) ...
                *Hliq(T2))-(AIR2(1)+HR(2)*Hvapor(T2));
            if (delH(i+1) >= 0)
                T2a=T2;
            elseif (delH(i+1) < 0)
                T2b=T2;
            end
            i=i+1;
        end
    else
        T2=T1;
        HR(2)=HR(1);
        AIR2=AIR1;
    end
    h2=AIR2(1)+HR(2)*Hvapor(T2);
    Y(5)=HR(2)*28.97/18.015;
    Y=Y/sum(Y);
    STATE2=values([T2 P2]);
    Temp2(1:9)=T2+273;
    Y2=Y;
    %-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-[ITERATION]-*-*-*-*-*-*-*-*-*-*-*-*-*-*-
    for k=1:1%length(Load)
        delWcycle(1)=1;
        j=1;
        MFa=0;
        MFb=100000;
        MdotFuelLbm(k)=Load(k)*MdotFuelLbm(1);
        while(abs(delWcycle(j))>=.01) & (j<100)
            Y=Y2;
            if j>98
                display('Error: too many repetitions'); j
            end
            if k==1
                MdotFuelLbm(1)=(MFa+MFb)/2;
            end
            %MdotFuel=2.67711013708057;
            MdotFuel=MdotFuelLbm(k)*.45359/3600;%kg/s
            MDF(k)=MdotFuel;
            %******************************State 3******************************
            P3=Rv*P2;
            HR(3)=HR(2);
            %Iterate to find value of T3
            T3sa=T2;
            T3sb=500;
            i=1;
            deltaS(1)=1;
            while(abs(deltaS(i))>=.00001) & (i<100)
                T3s=(T3sa+T3sb)/2;
                STATE3s=values([T3s P3]);
                deltaS(i+1)=STATE3s(3)-STATE2(3);
                if (deltaS(i+1) >= 0)
                    T3sb=T3s;
                elseif (deltaS(i+1) < 0)
                    T3sa=T3s;
                end
                i=i+1;
            end%Final T3s value is T3 in the isentropic case
            h3s=STATE3s(1);
            %Iterate to find actual T3 with isentropic efficiency
            deltaH(1)=10;
            i=1;
            T3a=T3s;
            T3b=500;
            while(abs(deltaH(i))>=0.00001) & (i<100)
                T3=(T3a+T3b)/2;
                STATE3=values([T3 P3]);
                h3=STATE3(1);
                deltaH(i+1)=Ncomp*(h3-h2)-(h3s-h2);
                if (deltaH(i+1) >= 0)
                    T3b=T3;
                elseif (deltaH(i+1) < 0)
                    T3a=T3;
                end
                i=i+1;
            end
            h3=STATE3(1);
            Temp3(k)=T3+273;
            %******************************State 4******************************
            P4=P3;
            %MdotFuel=2.7055;%kg/s
            %Chemical equation balance
            % (0.961CH4 + 0.025C2H6 + 0.002C3H8 + 0.008CO2 + 0.004N2) + a(O2 + 3.76N2) +
            % bH2O => cH2O + dCO2 + eO2 + fN2
            a=MdotAir/MdotFuel*(16.72/137.328);
            b=HR(2)*a*(137.328/18.015);
            c=2.005+b;
            d=1.025;
            e=(2*.008+2*a+b-c-2*d)/2;
            f=0.004+a*3.76;
            Y=[0 0 e f c d];
            Y=Y/sum(Y);
            MdotTotal=MdotAir*(1+HR(3))+MdotFuel;
            h4in=((MdotAir*(1+HR(3)))*(h3)+MdotFuel*LHV)/MdotTotal;
            i=1;
            T4a=T3;
            T4b=5000;
            while(abs(deltaH(i))>=.00001 & i<100)
                T4=(T4a+T4b)/2;
                STATE4=values([T4 P4]);
                h4=STATE4(1);
                deltaH(i+1)= h4-h4in;
                if (deltaH(i+1) >= 0)
                    T4b=T4;
                elseif (deltaH(i+1) < 0)
                    T4a=T4;
                end
                i=i+1;
            end
            FTK(k)=T4+273;
            %******************************State 5******************************
            P5=(P0+0.036*(delPout))/.14504;
            T5sa=T4;
            T5sb=0;
            i=1;
            deltaS(1)=1;
            while(abs(deltaS(i))>=.001) & (i<100)
                T5s=(T5sa+T5sb)/2;
                STATE5s=values([T5s P5]);
                deltaS(i+1)=STATE5s(3)-STATE4(3);
                if (deltaS(i+1) >= 0)
                    T5sa=T5s;
                elseif (deltaS(i+1) < 0)
                    T5sb=T5s;
                end
                i=i+1;
            end%Final T5s value is T5 in the isentropic case
            h5s=STATE5s(1);

            deltaH(1)=10;
            i=1;
            T5a=T5s;
            T5b=T4;
            while(abs(deltaH(i))>=0.00001) & (i<100)
                T5=(T5a+T5b)/2;
                STATE5=values([T5 P5]);
                h5=STATE5(1);
                deltaH(i+1)=Nturb*(h5s-h4)-(h5-h4);
                if (deltaH(i+1) >= 0)
                    T5a=T5;
                elseif (deltaH(i+1) < 0)
                    T5b=T5;
                end
                i=i+1;
            end
            ETK(k)=T5+273;

            WTurbine=MdotTotal*(h4-h5);
            WCompressor=MdotAir*(1+HR(2))*(h3-h2);
            Wcycle(k)=(WTurbine-WCompressor)*Ngen;
            delWcycle(j+1)=Wcycle(k)-48000;

            if (delWcycle(j+1) >= 0) & (k==1)
                MFb=MdotFuelLbm(k);
            elseif (delWcycle(j+1) < 0) & (k==1)
                MFa=MdotFuelLbm(k);
            else
                delWcycle(j+1)=0;
            end
            j=j+1;
        end
        Nthermal(k)=Wcycle(k)/(MdotFuel*LHV);
        SFC(k)=MdotFuel/Wcycle(k);
        HeatRate(k)=(MdotFuelLbm(k)*LHVBTU)/Wcycle(k);
        FiringTempF(k)=T4*9/5-460;
        FiringTempK(k)=T4;
    end
    if ii>1
        FTF=FTK.*(9/5)-460;
        ETF=ETK.*(9/5)-460;
        figure(1)
        plot(FTF,Wcycle)
        figure(2)
        plot(ETF,Wcycle)
        hold on
    end
end
if k==1
    val=[HeatRate(1) MdotTotal*3600 MdotFuelLbm T5];
    val2=[10600 622170 24280 523];
    error=abs((val2-val)./val2*100)
end
SpecVol=RMIX*(T5+273)/P5;
DEAD=values([25 101.325]);
EXERGY=MdotTotal*((STATE5(2)-DEAD(2))+101.325*(SpecVol-0.844076)-298*(STATE5(3)-DEAD(3)));

if k>9
    figure(1);
    plot(Load,Nthermal);
    xlabel('Load(%)')
    ylabel('Thermal Efficiency(%)')
    figure(2);
    plot(Load,MdotFuelLbm);
    xlabel('Load(%)')
    ylabel('Fuel Flow Rate(Lbm/Hr)')
    figure(3);
    plot(Load,SFC);
    xlabel('Load(%)')
    ylabel('Specific Fuel Consumption(Lbm/kW-Hr)')
    figure(4);
    plot(Load,HeatRate);
    xlabel('Load(%)')
    ylabel('Heat Rate(BTU/Lbm-Hr)')
    figure(5);
    plot(Load,FiringTempF);
    xlabel('Load(%)')
    ylabel('Firing Temperature(F)')
    figure(6);
    plot(Load,FiringTempK);
    xlabel('Load(%)')
    ylabel('Firing Temperature(K)')
end
if k>1
P0=P0/.14504;
TEMPS=[Temp0;Temp1;Temp2;Temp3;FTK;ETK];
end
PRESS=[P0;P1;P2;P3;P4;P5;P0];