function [x,y] = Gaus(xo,yo,sig)
    % Monte Carlo - Gaussian
    r = sqrt(-2.0 .*sig .*sig .*log(rand));
    phi = 2.0 .*pi .*rand;
    x = xo + r .*cos(phi);
    y = yo + r .*sin(phi);
    %
end