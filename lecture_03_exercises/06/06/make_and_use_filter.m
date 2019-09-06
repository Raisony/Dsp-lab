
%% Load wave file

[x, Fs] = audioread('author.wav');
% [x, Fs] = wavread('author.wav');
[x1, Fs1] = audioread('wav_after_filter.wav');
[x2, Fs2] = audioread('wav_canonical.wav');

N = length(x);
n = 1:N;
t = n/Fs;

figure(1)
clf
plot(t, x)
xlabel('Time (sec)')
title('Speech signal')

%%

x_clipped =  min(1, max(-1, x*1000));

figure(1)
clf
plot(t, x_clipped, t, x)
xlabel('Time (sec)')
title('Clipped speech signal')
ylim([-2 2])

%% Make filter
% band-pass filter

[b, a] = butter(2, [500 1000]*2/Fs);

%% Pole-zero diagram

figure(1)
clf
zplane(b, a)
title('Pole-zero diagram')

%% Frequency response

[H, om] = freqz(b, a);
f = om*Fs/(2*pi);
figure(1)
clf
plot(f, abs(H))
xlabel('Frequency (Hz)')
xlim([0 3000])
title('Frequency response')

%% Impulse response

L = 300;
imp = [1 zeros(1, L)];
h = filter(b, a, imp);

figure(1)
clf
stem(0:L, h)
xlabel('Discrete time (n)')
title('Impulse response')

%%

figure(1)
clf
plot((0:L)/Fs, h)
xlabel('Time (sec)')
title('Impulse response')

%% Apply filter to speech signal

y = filter(b, a, x);

figure(1)
clf
% plot(t, x, t, y - 0.5)
plot(t, x, t, y - 0.5, t, x1 - 1, t, x2 - 1.5)
legend('input','matlab','python','canonical')
xlabel('Time (sec)')
title('Speech signal and filtered speech signal')
zoom xon

%% Write output signal to wave file

audiowrite('output_matlab.wav', y, Fs);
% wavwrite(y, Fs, 'output_matlab.wav');

%%

sound(x, Fs)

%%

sound(y, Fs)

%% Filter coefficients
% Copy these coefficients into Python program to implement
% the same filter. Display in long format for higher accuracy.

format long
b'
a'

