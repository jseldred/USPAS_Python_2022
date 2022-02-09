%
 function[x] = PowerLaw(xmi,xmx,a)
%
% picks x from xmi to xmx our of 1/x^a power law
%
  p = rand .*((1.0 ./xmx) .^(a-1) - (1.0 ./xmi) .^(a-1)) +(1.0 ./xmi) .^(a-1);
  x = (1.0 ./p) .^(1.0 ./(a-1));
%
end
% 