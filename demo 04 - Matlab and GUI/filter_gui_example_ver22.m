function filter_gui_example_ver2

N = 500;
n = 1:N;
%x = sin(5*pi*n/N) + 0.5*randn(1, N);        % Input signal
x = zeros(N,1);
x(1) = 1;
fc = 0.1;
[b, a] = butter(2, 2*fc);       
% y = filtfilt(b, a, x);
y = filter(b, a, x);

f1=figure(1);
clf
ax1 = subplot(2,1,1)
line(n, x, 'marker', '.', 'linestyle', 'none', 'markersize', 10, 'color', [1 1 1]*0.5)
line_handle1 = line(n, y, 'linewidth', 2, 'color', 'black');
legend('Noisy data', 'Filtered data')
title( sprintf('Output of LPF. Cut-off frequency = %.3f (normalized)', fc) )
xlabel('Time')
box off
xlim([0, 100]);
ylim([-3 3])
f2 = figure(2)
clf
ax2 = subplot(2,1,2)
[H,om] = freqz(b,a);
line_handle2 = plot(om,abs(H))
drawnow;

slider_handle = uicontrol(f1 ...
    'Style', 'slider', ...
    'Min', 0.005, 'Max', 0.2, ...
    'Value', fc, ...
    'SliderStep', [0.02 0.05], ...
    'units', 'normalized', ...
    'Position', [0.2 0.0 0.6 0.2], ...
    'Callback',  {@fun1, ax1,ax2, line_handle1, line_handle2, x}  );

end


% callback function fun1

function fun1(hObject, eventdata,ax1,ax2, line_handle1, line_handle2, x)


fc = get(hObject, 'Value');     % cut-off frequency

[b, a] = butter(2, 2*fc);       % Order-2 Butterworth filter (multiply fc by 2 due to non-conventional Matlab convention)
y = filtfilt(b, a, x);

set(line_handle1, 'ydata',  y);
[H,om] = freqz(b,a);
set(line_handle2, 'ydata',  abs(H));
title( sprintf('Output of LPF. Cut-off frequency = %.3f (normalized)', fc) )

end