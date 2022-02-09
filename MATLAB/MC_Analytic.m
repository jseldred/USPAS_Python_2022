%
% Monte Carlo - analytic method of inversion/integration 
%
close all ;             % erase old plots
clear all;  
help MC_Analytic      % Clear the memory and print header
%
% Initialize  
%
fprintf('Monte Carlo - Analytic Examples \n ')
%
irun = 1;
iloop = 0;
%
while irun > 0
    %
    krun = menu('Another Function?','Yes','No');
    if krun == 2
        irun = -1;
        break
    end
    if krun == 1;
        def = menu('Type','Uniform','Power Law','Exp','Lorentz','Gaussian');
         %
        if def == 1
           for i = 1:1000
               y(i) = rand;
           end
           iloop = iloop + 1;
           figure(iloop)
           hist(y,50)
           title('1000 Uniformly Distributed (0,1) Points') 
        end
        if def == 2
           a = input('Enter Power Law Exponent: ');
           xmi = input('Enter x Minimum: '); 
           xmx = input('Enter x Maximum: '); 
           b = a + 1;
           c = 1/b;
           for i = 1:1000
               y(i) = (xmi .^b + rand .*(xmx .^b - xmi .^b)) .^c;
           end
           iloop = iloop + 1;
           figure(iloop)
           hist(y,50)
           title('1000 Power Law Points') 
        end
         if def == 3
           a = input('Enter Lifetime: ');
           xmi = input('Enter x Minimum: '); 
           xmx = input('Enter x Maximum: '); 
           for i = 1:1000
               y(i) = -a .*log(exp(-xmi ./a) + rand .*(exp(-xmx ./a) - exp(-xmi ./a)));
           end
           iloop = iloop + 1;
           figure(iloop)
           hist(y,50)
           title('1000 Exponential Points') 
         end
         if def == 4
           a = input('Enter Mean: ');
           b = input('Enter Linewidth: ');
           xmi = input('Enter x Minimum: '); 
           xmx = input('Enter x Maximum: '); 
           phmi = (2 .*(xmi - a)) ./b;
           phmx = (2 .*(xmx - a)) ./b;
           for i = 1:1000
               y(i) = a + (b ./2) .*tan(atan(phmi) + rand .*(atan(phmx) - atan(phmi))); 
           end
           iloop = iloop + 1;
           figure(iloop)
           hist(y,50)
           title('1000 Lorentzian Points') 
         end
         if def == 5
           a = input('Enter Mean: ');
           b = input('Enter Standard Deviation: ');
           c = 2.0 .*a .*a;  % pick r^2
           for i = 1:1000
               yy = sqrt(-2.0 .*b .*b .*log(rand));
               ph =  2 .*pi .*rand;
               y(i) = a + yy .*cos(ph);
           end
           iloop = iloop + 1;
           figure(iloop)
           hist(y,50)
           title('1000 Gaussian Points') 
        end
    end
end
%