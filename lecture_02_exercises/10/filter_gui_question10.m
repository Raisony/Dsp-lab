function filter_gui_question10

Fs = 8000;
N = 1000;
n = 0:N;
imp = [1 zeros(1,N)]

fc = 0.1;
[b, a] = butter(2, 2*fc);       
y = filtfilt(b, a, imp);

f1 = figure(1);
clf

%impluse response
subplot(2,1,1)
line1 = plot(n,y,'color','red','linewidth',2)
legend('impulse response')
xlim([0 N])
ylim([-0.5 1])

%frequency response
subplot(2,1,2)
[H, om] = freqz(b, a);
f_freqz = om*Fs/(2*pi); 
line2 = plot(f_freqz,abs(H),'color','blue','linewidth',2)
legend('frequency response')
title( sprintf('Output of LPF. Cut-off frequency = %.3f (normalized)', fc) )

xlabel('Time')
box off
% xlim([0, N]);
% ylim([-3 3])

drawnow;

slider_handle = uicontrol(f1, ...
    'Style', 'slider', ...
    'Min', 0, 'Max', 0.2, ...
    'Value', fc, ...
    'SliderStep', [0.02 0.05], ...
    'units', 'normalized', ...
    'Position', [0.2 0.0 0.6 0.2], ...
    'Callback',  {@fun1, line1, line2 });

end


% callback function fun1

function fun1(hObject, eventdata, line1, line2)


fc = get(hObject, 'Value');     % cut-off frequency

fc = max(0.01, fc);             % minimum value
fc = min(1.0, fc);             % maximum value

N = 1000;
n = 0:N;
imp = [1 zeros(1,N)] ;% Input signal

Fs = 8000;
[b, a] = butter(2, 2*fc);       
y = filtfilt(b, a, imp);
% y = filter(b, a, x);

[H, om] = freqz(b, a);
f_freqz = om*Fs/(2*pi); %?Fs

set(line1, 'ydata',  y);
set(line2, 'ydata',  abs(H), 'xdata',  f_freqz);

title( sprintf('Output of LPF. Cut-off frequency = %.3f (normalized)', fc) )

end

