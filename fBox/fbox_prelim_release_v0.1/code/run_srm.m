datapath = 'data_amz.mat'; %path to matlab file with sparse data matrix
neigs = 50; %number of eigenvectors

srmsvd(datapath,neigs);
[~,fn,~] = fileparts(datapath);
svdfile = strcat(fn,'svd.mat');
srmculprits(svdfile);
disp 'processing complete'
