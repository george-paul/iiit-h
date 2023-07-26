% inputs
zeta1 = 0.5;
zeta2 = 0.9;
omega1 = 4;
omega2 = 2;
Ua = @(s) ( 1 ) / ( s );
Ub = @(s) ( 1 ) / ( s^2+4 );

G = @(s) ( 2 ) / ( s+2 );
S1 = @(s) ( omega1^2 ) / ( s^2+2*zeta1*omega1*s+omega1^2 );
S2 = @(s) ( omega2^2 ) / ( s^2+2*zeta2*omega2*s+omega2^2 );

Ya = @(s) G(s) * Ua(s);
Yb = @(s) G(s) * Ub(s);
Yma1 = @(s) S1(s) * Ya(s);
Yma2 = @(s) S2(s) * Ya(s);
Ymb1 = @(s) S1(s) * Yb(s);
Ymb2 = @(s) S2(s) * Yb(s); 

fplot(Yma1);
fplot(Yma2);
fplot(Ymb1, [-10 10]);
fplot(Ymb2, [-10 10]);