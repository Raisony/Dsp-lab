%% 5.Using the filter function and plot the impulse response
clc
clear all
f = 800;
Fs = 8000;
om = 2 * pi * f / Fs;
r = 0.998;

a0 = 1;
a1 = -2 * r * cos(om);
a2 = r^2;
b0 = 1;
b1 = -r * cos(om);
b2 = 0;

a = [a0 a1 a2]
b = [b0 b1 b2]

n = 0:100;
x = ( n==0 );
% make the filter
y = filter(b, a, x);
g = r.^n;

figure(1)
plot(n, y, 'o-', n, g, '--')
legend('impulse response', 'amplitude envelope')
xlabel('n')
ylabel('y(n)')
title('question 5 :')
