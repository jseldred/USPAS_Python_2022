%
close all
clear all
%
% drive the fit_package to check out errors etc.
%
global  X Y Wt Yfit Itype
%
ntot = 10000; % events
nb = 50; % bins of histo to fit
%
Itype = 1;
for i = 1:ntot
     %
     % choice of exp, Gaussian, 
     if Itype == 1
        xmi = 0.0; xmx = 8.0; [xo(i),dum] = Gaus(4, 4, 2); %Itype = 1
        ao = [ntot .*0.9 4.5 2.5 ]; % starting values for Gaussian
     end
     if(Itype == 2)
        xmi = 0.0; xmx = 5.0; xo(i) = expMC(1,xmi,xmx); % Itype = 2
        ao = [0.1 4.5]; % starting values for exp
     end
     %
end
%
[nxi,erxi,xibin,afit,erra,diag,chs,dof] = fit_package(xo,xmi,xmx,nb,ao);
hold on % first data with errors plotting then add fit
xplot = linspace(xmi, xmx);
if Itype == 1
    yplot = afit(1) ./ (sqrt(2.0 .*pi) .*afit(3));% Itype 1 Gaussian
    yplot = yplot .*(exp(-(xplot-afit(2)).^2./(2 .*afit(3) .*afit(3))));
end
if Itype == 2
    yplot = afit(1) .*exp(-xplot ./afit(2)); %Itype = 2 exp
end
%
plot(xplot,yplot,'-r');
hold off
%
fprintf(' afit =%g\n',afit);
fprintf(' chi^2 = %g\n',chs);
fprintf(' DOF = %g\n', dof) ;
fprintf(' dafit = %g\n',diag)
%
figure
errorbar(xibin,nxi,erxi,'ob')
title('Hist of the Data')
xlabel('x'); ylabel('n(x)')
%

