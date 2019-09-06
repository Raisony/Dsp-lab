%% read_wavefile_01.m
% View parameters, plot waveform, compute and display spectrum

%% Start

clear

help wavread

%% Load .wav file 

[x, Fs, nbits, opts] = wavread('cat01.wav');   % or use audioread

whos

%%

Fs
nbits
opts.fmt

%%

soundsc(x, Fs)

%% Plot waveform

figure(1)
clf
plot(x)
xlabel('Time (sample)')
title('Signal')

%% Time axis in seconds

N = length(x);
t = (1:N)/Fs;

figure(1)
clf
plot(t, x)
xlabel('Time (sec)')
title('Signal')

%% Zoom in to 50 msec

xlim(0.4 + [0 0.050])

%% Distribution of samples

xs = sort(x);

figure(1)
clf
plot(xs)
title('Sorted signal values')

%% See quantization

ylim([-0.0002 0.0002])
grid

%% What is the quantization increment ?

% smallest positive value (SPV)

SPV = min(x(x > 0))

%%

% The smallest positive value is 1/2^15
1/SPV
2^15

%%
% All values x(n) are integer multiples of 1/2^15
% Why?

%% Frequency spectrum
% Use Fast Fourier Transform (FFT)

% Use power of 2 for FFT efficiency
N = length(x)
Nfft = 2^ceil(log2(N))  % smallest power of 2 greater than signal length

%% Compute Fourier transform 

X = fft(x, Nfft);   
k = 0:Nfft-1;      % FFT index

figure(1)
clf
plot(k, abs(X))
xlabel('FFT index')
title('Spectrum')

%% Center dc

X2 = fftshift(X);
k2 = -Nfft/2 : Nfft/2-1;

figure(1)
clf
plot(k2, abs(X2))
xlabel('FFT index')
title('Spectrum')

%% Normalized frequency
% Normalized frequency is in units of [cycles per sample]

fn = ( -Nfft/2 : Nfft/2-1 ) / Nfft;

figure(1)
clf
plot(fn, abs(X2))
xlabel('Frequency (cycles/sample)')
title('Spectrum')

%% Frequency in Hz

f = fn * Fs;

figure(1)
clf
plot(f, abs(X2))
xlabel('Frequency (cycles/second, i.e. Hz)')
title('Spectrum')


