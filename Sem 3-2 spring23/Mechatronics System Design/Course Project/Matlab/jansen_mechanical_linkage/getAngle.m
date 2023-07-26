function [X1,X2] = getAngle(a,b,x1,x2,c1,c2)
%[x1,y1] = getAngle(a,b,x1,x2,c1,c2):
%Calculates the two unknown angles from a ststem of linear equations using
%Newton-Raphson.
%Inputs a,b = length of segments.
%Inputs x1, x2 = initial guess for angles.
%Inputs c1, c2 = constant values for 
%Outputs X1,X2 = values for the angles that Newton-Raphson Converges
%onto.

%Version 1: Created 03/03/17. Author: D. Gormley
%This MATLAB function m-file can be used find the two unknown angles of the
%system 

% ------------------------------------------------------------------------%
%Internal Parameters
iterationLimit = 10;   %maximum number of iterations before function terminates
tolerance = 10^-8;      %minimum modulus of f

%-------------------------------------------------------------------------%

%Error Checking: To ensure the correct values were inputted into function.
if (nargin ~= 6), error('Incorrect number of input arguments.'); end

% initialise vector of unknowns
v = [x1;x2];
f1 = (a*cos(v(1)))+(b*cos(v(2)))+c1;
f2 = (a*sin(v(1)))+(b*sin(v(2)))+c2;

% create function matrix
f = [f1;f2];

%Finding the Jacobian
f1_x1 = -a*sin(v(1));
f1_x2 = -b*sin(v(2));
f2_x1 = a*cos(v(1));
f2_x2 = b*cos(v(2));

Df = [f1_x1 f1_x2;f2_x1 f2_x2];

for count = 1:iterationLimit+1
    
    if count == iterationLimit+1
        error('The Iteration limit has been reached and did not converge')
        break
    end
    
    if abs(f) < tolerance
        break
    else
        v = v - (inv(Df)*f);
        
        % update values of f and Df based on new values of v vector
        f1 = (a*cos(v(1)))+(b*cos(v(2)))+c1;
        f2 = (a*sin(v(1)))+(b*sin(v(2)))+c2;
        f = [f1;f2];
        
        f1_x1 = -a*sin(v(1));
        f1_x2 = -b*sin(v(2));
        f2_x1 = a*cos(v(1));
        f2_x2 = b*cos(v(2));

        Df = [f1_x1 f1_x2;f2_x1 f2_x2];
        
    end

end

%Assigning the angles that Newton Raphson converged onto as output.
X1 = v(1);
X2 = v(2);

%Error Checking: To ensure corrent number of values being outputted
if (nargout ~= 2), error('An incorrect number of elements are being returned'); end

end