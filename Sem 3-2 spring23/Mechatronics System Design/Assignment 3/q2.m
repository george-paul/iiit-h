%% 2.b and 3.b

% ---links---
r1 = 18;
r2 = 10;
r3 = 20;
r4 = 25;

% link lengths for q3.b
% r1 = 3.8033;
% r2 = 1.316;
% r3 = 1.9168;
% r4 = 1.1702;


k1 = r1/r2;
k2 = r1/r4;
k3 = (r2^2 + r1^2 - r3^2 + r4^2)/(2*r2*r4); 

for angle2=0:0.5:5*pi

    a = ( k2*cos(angle2) ) - k3 - cos(angle2) + k1;
    b = ( 2*sin(angle2) );
    c = ( k2*cos(angle2))  - k3 + cos(angle2) - k1;

    determinant = b^2 - (4*a*c);
    
    t1 = (-b + sqrt(determinant))/(2*a);
    t2 = (-b - sqrt(determinant))/(2*a);

    angle4_1 =2*atan(t1);
    angle4_2 = 2*atan(t2);

    angle3_1 = acos( ((r4*cos(angle4_1) + r1 - r2*cos(angle2))/r3) );
    angle3_2 = acos( (r4*cos(angle4_2) + r1 - r2*cos(angle2))/r3 );
%     q3.b
%     x1_1 = 10;
    x1_1 = 40;
    y1_1 = 0;
    
    x1_2 = 0;
    y1_2 = 0;
        
    x2_1 = x1_1 + (r2*cos(angle2));
    y2_1 = y1_1 + (r2*sin(angle2));

    x2_2 = x1_2 + (r2*cos(angle2));
    y2_2 = y1_2 + (r2*sin(angle2));
    
    x3_1 = x2_1 + (r3*cos(angle3_1));
    y3_1 = y2_1 + (r3*sin(angle3_1));
    
    x3_2 = x1_2 + r1 + (r4*cos(angle4_2));
    y3_2 = y1_2 + r4*sin(angle4_2);

    x4_1 = x1_1 + r1;
    y4_1 = y1_1;
    
    x4_2 = x1_2 +r1;
    y4_2 = y1_2;

    drawnow
        clf
%         q3.b
%         axis([-10 20 -10 20]);
        axis([-30 60 -30 60]);
        line([x1_1 x4_1], [y1_1 y4_1], 'Color', 'black', 'LineWidth', 3);
        line([x1_1 x2_1], [y1_1 y2_1], 'Color', 'blue', 'LineWidth', 3);
        line([x2_1 x3_1], [y2_1 y3_1], 'Color', 'green', 'LineWidth', 3);
        line([x3_1 x4_1], [y3_1 y4_1], 'Color', 'red', 'LineWidth', 3);
        
        line([x1_2 x4_2], [y1_2 y4_2], 'Color', 'black', 'LineWidth', 3);
        line([x1_2 x2_2], [y1_2 y2_2], 'Color', 'blue', 'LineWidth', 3);
        line([x2_2 x3_2], [y2_2 y3_2], 'Color', 'green', 'LineWidth', 3);
        line([x3_2 x4_2], [y3_2 y4_2], 'Color', 'red', 'LineWidth', 3);
    
end