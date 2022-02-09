%
% Monte Carlo - numerical method of inversion/integration 
%
close all ;             % erase old plots
clear all;  
help MC_Numeric      % Clear the memory and print header
%
% Initialize  
%
fprintf('Monte Carlo - Numerical Compton Scattering Example \n ')
%
irun = 1;
iloop = 0;
%
while irun > 0
    %
    krun = menu('Another Photon Energy?','Yes','No');
    if krun == 2
        irun = -1;
        break
    end
    if krun == 1;
        iloop = 0;
        w = input('Enter Photon Energy Divided by Electron Mass: ');
        %
        ctmi = -1;  % Compton scattering angle
        ctmx = 1;
        pmx = 2;
        pmi = 0;
        ipass = 0;
        for i = 1:10000
            ct = ctmi + rand .*(ctmx - ctmi);
            yc = 1.0 ./(1 + w .*(1-ct));
            pc = yc .*yc .*(yc + 1 ./yc - (1 - ct .*ct)); % Compton dsigma/domega 
            if rand < pc ./pmx;
                ipass = ipass + 1;
                Compt(ipass) = ct;
            end
        end
        iloop = iloop + 1;
        figure(iloop)
        hist(Compt,50);
        title('Compton Scattering Angular Distribution')
        xlabel('cos(\theta)')
        ylabel('d\sigma/d\Omega')
    end
end
%