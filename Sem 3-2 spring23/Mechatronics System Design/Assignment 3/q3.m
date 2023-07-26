%% 3.a

% points
p2x = -2;
p2y = -1;
p3x = -3;
p3y = -2;

% angles
a2 = 5;
a3 = 10;
b2 = 20;
b3 = 40;
g2 = 10;
g3 = 20;


A = [
    cos(b2)-1 -sin(b2) -cos(a2)+1 sin(a2);
    sin(b2) cos(b2)-1 -sin(a2) -cos(a2)+1;
    cos(b3)-1 -sin(b3) -cos(a3)+1 sin(a3);
    sin(b3) cos(b3)-1 -sin(a3) -cos(a3)+1
    ];
B = [
    p2x;
    p2y;
    p3x;
    p3y
    ];
left = A\B;
a = left(1);
b = left(2);
c = left(3);
d = left(4);
w1 = sqrt(a^2 + b^2);
z1 = sqrt(c^2 + d^2);

C = [
    cos(g2)-1 -sin(g2) -cos(a2)+1 sin(a2);
    sin(g2) cos(g2)-1 -sin(a2) -cos(a2)+1;
    cos(g3)-1 -sin(g3) -cos(a3)+1 sin(a3);
    sin(g3) cos(g3)-1 -sin(a3) -cos(a3)+1
    ];
D = [
    p2x;
    p2y;
    p3x;
    p3y
    ];
right = C\D;
p = right(1);
q = right(2);
r = right(3);
s = right(4);
u1 = sqrt(p^2 + q^2);
s1 = sqrt(r^2 + s^2);
v1 = sqrt((c-r)^2 + (d-s)^2);
g1 = sqrt((a+c-r-p)^2 + (b+d-s-q)^2);

disp("w1: " + w1);
disp("z1: " + z1);
disp("u1: " + u1);
disp("s1: " + s1);
disp("v1 (coupler link): " + v1);
disp("g1 (ground link): " + g1);

% Please find 3.b in q2.m
