function y = values(x)%input parameter = [temp(C) pressure(kPa)]
global RMIX X Y MMIX;
%get values of mixture pressure and temperature
press=x(2);
T=x(1);
tempK=T+273;%Temperature C to K;
%Stored reference values
M=[4.003 39.948 31.999 28.013 18.015 44.010]; %[He Ar O2 N2 H2O CO2]
R=[2.077 .208 .26 .297 .462 .189];
Sref=[31.5375 3.876 6.6999 6.8045 10.423 4.8585];
Uref=[928.419 92.976 194.2 221.44 412.05 156.57];
Href=[1547.365 154.96 271.72 309.99 549.75 212.93];
%Calculate other mixture values
MMIX=M*Y';
X=Y.*M./MMIX;
RMIX=8.3145/MMIX;
%Coefficients of Cp equations
COEFF=[0 0 0 0;
        0 0 0 0;
        0.7963 4.7501e-004 -2.2360e-007 4.1001e-011;
        1.0317 -5.6081e-005 2.8847e-007 -1.0256e-010;
        1.7896 1.0674e-004 5.8562e-007 -1.9956e-010;
        0.5058 0.00136 -7.9550e-007 1.6971e-010];
%Coefficients of Cv equations where Cv=Cp-R
CvCOEFF=COEFF;
CvCOEFF(3,1)=COEFF(3,1)-R(3);
CvCOEFF(4,1)=COEFF(4,1)-R(4);
CvCOEFF(5,1)=COEFF(5,1)-R(5);
CvCOEFF(6,1)=COEFF(6,1)-R(6);
%Divide each coefficient by its respective power for integration to find entropy
sintCOEFF(:,1)=COEFF(:,1);
sintCOEFF(:,2)=COEFF(:,2);
sintCOEFF(:,3)=COEFF(:,3)/2; 
sintCOEFF(:,4)=COEFF(:,4)/3;
%Divide each coefficient by its respective power for integration to find h
intCOEFF(:,1)=COEFF(:,1);
intCOEFF(:,2)=COEFF(:,2)/2;
intCOEFF(:,3)=COEFF(:,3)/3;
intCOEFF(:,4)=COEFF(:,4)/4;
%Divide each coefficient by its respective power for integration to find u
intCvCOEFF(:,1)=CvCOEFF(:,1);
intCvCOEFF(:,2)=CvCOEFF(:,2)/2;
intCvCOEFF(:,3)=CvCOEFF(:,3)/3;
intCvCOEFF(:,4)=CvCOEFF(:,4)/4;
%Calculate reference values for mixture
hrefMIX=Href*X';
urefMIX=Uref*X';
srefMIX=Sref*X';
%Set tempratures over which to integrate
TEMPz=[tempK 298];
Pref=101.325;%in kPa
Tref=298;%in Kelvin
%calculate values of Cp and Cv, integrals of Cp and Cv, h, u and s
for i=1:2
    temp=TEMPz(i);
    TEMP=[1 temp temp^2 temp^3];
    sTEMP=[log(temp) temp temp^2 temp^3];
    Cp=COEFF*TEMP';
    Cp(1)=5/2*R(1);
    Cp(2)=5/2*R(2);
    Cp=COEFF*TEMP';
    s=sintCOEFF*sTEMP';
    s(1)=5/2*R(1)*log(temp);
    s(2)=5/2*R(2)*log(temp);
    %Perform calculations
    intTEMP=temp*TEMP;%Add a power to each temp
    intCp=intCOEFF*intTEMP';%Calculate integral values for 4 polynomial functions
    intCp(1)=5/2*R(1)*temp;%Assign integrated values of constant 5/2*R values = 5/2*R*temp
    intCp(2)=5/2*R(2)*temp;
    intCv=intCvCOEFF*intTEMP';
    intCv(1)=3/2*R(1)*temp;
    intCv(2)=3/2*R(2)*temp;
    %Multiply matrices to calculate values
    CpMIXA=X*Cp;
    intCpMIXA(i)=X*intCp;
    intCvMIXA(i)=X*intCv;
    CvMIXA=CpMIXA-RMIX;
    sMIX(i)=X*s;
    i=i+1;
end
h=intCpMIXA(1)-intCpMIXA(2)+hrefMIX;
u=intCvMIXA(1)-intCvMIXA(2)+urefMIX;
S=sMIX(1)-sMIX(2)+srefMIX-RMIX*log(press/Pref);
%Calculate other values
CpMIX=X*Cp;
CvMIX=CpMIX-RMIX;
K=CpMIX/CvMIX;
y=[h u S K];