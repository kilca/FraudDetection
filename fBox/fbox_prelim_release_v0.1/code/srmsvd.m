function [] = srmsvd(datapath,neigs)

A = load(datapath)
A = A.M
disp 'data loaded'
disp(['neigs set to ' num2str(neigs)])
opts.issym = 0;
opts.isreal = 1;
opts.disp = 0;
[u,s,v,flag] = svds(A,neigs,'L',opts);
disp 'svd complete'
indegs = sum(A,1);
outdegs = sum(A,2);
rec_indegs = sum((v*s).^2,2);
rec_outdegs = sum((u*s).^2,2);
[~,fn,~] = fileparts(datapath)

save(strcat(fn,'svd.mat'),'u','s','v','indegs','outdegs','rec_indegs','rec_outdegs','-v7.3');
disp(['data saved to ' strcat(fn,'svd.mat')])

end
