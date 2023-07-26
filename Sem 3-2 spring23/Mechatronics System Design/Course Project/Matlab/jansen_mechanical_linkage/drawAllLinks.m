function [handleLinks] = drawAllLinks(S,A,count,N,L)
%[handleLinks] = drawAllLinks(S,A,count,N):
%Draws all the links and node of the Jansen Linkage model
%Input S = matrix of all the coordinates
%Input A = matrix of all of the crank angles
%Input count = counter that keeps track of the column of the matrices 
%Input N = number of crank angles
%Output handleLink = matrix of the handles to the links and nodes created

%Version 1: Created 08/03/17. Author: D. Gormley
%This MATLAB function m-file can be used to draw the links and nodes of the
%Jansen Linkage model

%=========================================================================%
%Internal Parameters
radius_Link = 3;
radius_Node = 4;
X_offset = 0;

%=========================================================================%

%Error Checking: To ensure the correct values were inputted into function.
if (nargin ~= 5), error('Incorrect number of input arguments.'); end

%The following are function calls to create all of the links
h_0i = drawLink(S(count,1),S(count,2),N,L(1),A(count,1),X_offset-20,radius_Link);
h_ij = drawLink(S(count,5),S(count,6),N,L(2),A(count,2),X_offset,radius_Link);
h_1j = drawLink(S(count,3),S(count,4),N,L(3),A(count,3),X_offset,radius_Link);
h_1k = drawLink(S(count,3),S(count,4),N,L(4),A(count,4),X_offset,radius_Link);
h_kj = drawLink(S(count,9),S(count,10),N,L(5),A(count,5),X_offset,radius_Link);
h_lk = drawLink(S(count,11),S(count,12),N,L(8),A(count,8),X_offset,radius_Link);
h_ml = drawLink(S(count,13),S(count,14),N,L(9),A(count,9),X_offset,radius_Link);
h_m1 = drawLink(S(count,13),S(count,14),N,L(6),A(count,6),X_offset,radius_Link);
h_mi = drawLink(S(count,13),S(count,14),N,L(7),A(count,7),X_offset,radius_Link);
h_nl = drawLink(S(count,15),S(count,16),N,L(10),A(count,10),X_offset,radius_Link);
h_nm = drawLink(S(count,15),S(count,16),N,L(11),A(count,11),X_offset,radius_Link);

%Function calls to create all of the nodes and static links
%The last three inputs to theis function can be used to change its colour.
h_crankShaft = drawStaticLink(S(count,5),S(count,6),20,radius_Link,-20,N,128/255,0/255,128/255);
h_0 = drawStaticLink(S(count,1),S(count,2),8,radius_Node,-24,N);
h_i_Back = drawStaticLink(S(count,5),S(count,6),8,radius_Node,-24,N);
h_i_Front = drawStaticLink(S(count,5),S(count,6),8,radius_Node,-4,N);
h_j = drawStaticLink(S(count,7),S(count,8),8,radius_Node,-4,N);
h_k = drawStaticLink(S(count,9),S(count,10),8,radius_Node,-4,N);
h_1 = drawStaticLink(S(count,3),S(count,4),8,radius_Node,-4,N);
h_l = drawStaticLink(S(count,11),S(count,12),8,radius_Node,-4,N);
h_m = drawStaticLink(S(count,13),S(count,14),8,radius_Node,-4,N);
h_n = drawStaticLink(S(count,15),S(count,16),8,radius_Node,-4,N);

%Function call to create the trace
h_trace = drawTrace(S(count,15),S(count,16),3,2,N,-7);

%Create a matrix to store all the handles
handleLinks = [h_0i;h_ij;h_1j;h_1k;h_kj;h_m1;h_mi;h_lk;h_ml;h_nl;h_nm;h_crankShaft;h_0;h_i_Back;h_i_Front;h_j;h_k;h_1;h_l;h_m;h_n];

%Error Checking: To ensure corrent number of values being outputted
if (nargout ~= 1), error('An incorrect number of elements are being returned'); end

end

