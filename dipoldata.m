


%Magnet collibration 
%'D4FL2XTDS'
% information 

Field= getfield('FLASH.MAGNETS/MAGNET.ML/D4FL2XTDS/FIELD.SP', data)
STRENGTH=getfield('FLASH.MAGNETS/MAGNET.ML/D4FL2XTDS/STRENGTH.SP', data)
kick=getfield('FLASH.MAGNETS/MAGNET.ML/D4FL2XTDS/KICK.SP', data)

current=('FLASH.MAGNETS/MAGNET.ML/D4FL2XTDS/CURRENT.SP', data)


% 1/rho=e B/pcolor
% B*rho=E/e; 

%%
% Bending Magnet
%%
% B*rho[T.m]=10/2.998 E[GeV]

theta=3.584*3.14/180;
Leff=0.4444;
rho=Leff/sin(theta)

B=0.634
E=0.2998*B*rho

kick=0.2998*B/E *Leff
