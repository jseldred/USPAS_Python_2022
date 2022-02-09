function [t] = expMC(b, tmin,tmax)
%
% function to give exp dist in Monte Carlo 
%
t = log(exp(-b .*tmin)-rand .*(exp(-b .*tmin)-exp(-b .*tmax)));
t=(-1.0 .*t) ./b;
end

