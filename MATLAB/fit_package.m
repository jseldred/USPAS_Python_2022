%
function[nxi,erxi,xibin,afit,erra,diag,chs,dof] = fit_package(xo,xmi,xmx,nb,ao)
%
% generic fit function specified in function fit_fun
% declare X Y Wt Yfit Itype as global
%
global  X Y Wt Yfit Itype
%
% assume a set of events with a 1-d variable xo
% now make histo of xo from xmi to xmx in nb bins, hist nxi, error errxi
% bin center xbini - fit to histo points
% or it could be a series of data points with errors
%
[nxi,erxi,xibin] = fit_hst(xo,xmi,xmx,nb);
figure
errorbar(xibin,nxi,erxi,'ob')
title('Fit to Hist of the Data or Data Points')
xlabel('x'); ylabel('n(x)')
%
% input starting values of fit variables a are in ao
% the chisq function to be minimized is defined in fit_fun
%
Y = nxi;
X = xibin;
Wt = 1.0 ./(erxi .^2);
%
% type of fit stored in fit_fun, Itype global variable
%
options = optimset('TolFun',0.1,'TolX',0.1); % set convergence criteria
afit = fminsearch(@fit_fun,ao) ; % starting values ao
chs = fit_fun(afit); % minimum chisq at best fit
dof = length(Y) - length(afit); 
%
% then find err martix on fit values - need explicit deriv vector of chi
% wrt a. diagonal approximation diag
%
[erra,diag] = fit_err(ao,afit);
% 
% -------------------------------------------------------------------
%
function[nxi,erxi,xibin] = fit_hst(xo,xmi,xmx,nb)
%
% find histo for fit package
% xo is the vector to be histogranned from (xmi,xmx) - nb bins
% nxi in bin i with error erxi, bin center xibin
%
for k = 1: nb+1
    edg(k) = xmi + ((xmx - xmi) .* (k - 1)) ./nb; 
    % edges of hist are xmi and xmx
end
for k = 1: nb
    xibin(k) = edg(k) + (xmx - xmi) ./(2.0 .*nb);
    % bin centers
end
%
nnxi = histc(xo,edg);
for i = 1:nb
    nxi(i) = nnxi(i);
end
erxi = sqrt(nxi);
%
% -----------------------------------------------------------------------
%
% general fit function for least sq fit to measures Y with weight Wt at 
% points X fit parameters a, Yfit a specified function. 
%
function[chi] = fit_fun(a)
global X Y Wt Yfit Itype % X Y Yfit Wt Itype are global.
%
% Itype = 1 pure gaussian 
% Ityp2 = 2, simple exponential
% Itype = 3, exponential times 3th order polynomial
% Itype = 4, 1/(aX^b) - power law
%
if Itype == 1
 % a(1) norm, a(2) mean, a(3) sigma = r.m.s.
 Yfit = a(1) ./ (sqrt(2.0 .*pi) .*a(3));
 Yfit = Yfit .*(exp(-(X-a(2)).^2./(2 .*a(3) .*a(3))));
 %   
end
if Itype == 2
 Yfit = a(1) .*exp(-X ./a(2)); % simple exponential y = a1e(-x/a2)
end
%
if Itype == 3
 Yfit = a(1) .*exp(-X ./a(2)) + a(3) + a(4) .*X  +a(5) .*X .*X; 
 % simple exponential a1exp(-x/a2) + quardartic polynomiaial, a3, a4, a5
end
if Itype == 4
 Yfit = a(1) ./((X - a(3)) .^a(2)); % power law a1/(x-a3)^a2
end
%
ch = ((Y-Yfit) .^2) .*Wt;
chi = sum(ch);
%
% ----------------------------------------------------------------------
%
% calculates the error matrix on fit variables a in least sq fit
% companion to fit_fun, get gradient numerically 
%
function[erra,diag] = fit_err(ao,a)
%
% X Y Wt Yfit Itype are assumed global variables, used in fminsearch, fit_fun
%
global  X Y Wt Yfit Itype
%
% a are best fit params - ao are starting values
%
 npt = length(X); 
 na = length(a);
%
% get deriv of the npt Yfit wrt the na parameters, step 1% of distance to ao
%
  dyda = zeros(na,npt);
  da = abs((a-ao) ./100.0);
  ymin  = Yfit;
%
for i = 1:na
      b = a;
      b(i) = a(i) + da(i); % change 1 at a time 
   for j = 1:npt
      dummy = fit_fun(b); % change fron ymin best fit
      dyda(i,j) = (Yfit(j) - ymin(j)) ./da(i);  
   end  
end
%
% now propagate errors from meas points YY to param a
% assume that the starting errors on YY are uncorrelated - but easy generalize
%
 covyi = zeros(npt,npt);
 for i = 1:npt
   covyi(i,i) = covyi(i,i) + Wt(i); % diagonal
 end
 covai = dyda * covyi * (dyda'); % off diagonal
 ii = eye(na); 
 erra = ii / covai;
 
% estimator using diagonal elements
%
 for i=1:na
  diag(i) = sqrt(abs(erra(i,i)));
 end
%
