function filter_gui11

N = 50;
n = 0:N;
%imp  = [1 zeros(1, N)]
imp = ( n==0 )
Fs=8000;
% fc = 0.78
fc = 0.1;
[b, a] = butter(2, 2*fc); 
% [b, a] = butter(2, fc);
y = filter(b, a, imp);
[H, om] = freqz(b, a);
f_freqz = om*Fs/(2*pi);% Input signal

figure(1)
clf
subplot(2,1,1)
line_handle = plot( y);
xlim([0, N]);
ylim([-1 1])
subplot(2,1,2)
line_handle1= plot(f_freqz, abs(H));
title('input ' ,'fontsize', 12 )
xlabel('Time')
box off
xlim([0, 4000]);
ylim([-1 1])
drawnow;
slider_handle = uicontrol('Style', 'slider', ...
    'Min', 0, 'Max', 1,...
    'Value', 1, ...
    'SliderStep', [0.02 0.05], ...
    'Position', [5 5 200 20], ...           % [left, bottom, width, height]
    'Callback',  {@fun1, line_handle,line_handle1 }    );

end


function fun1(hObject, eventdata, line_handle,line_handle1)

fc = get(hObject, 'Value');  % fc : cut-off frequency

fc = max(0.10, fc);         % minimum value
fc = min(0.99, fc);         % maximum value
N = 50;
n = 0:N;
% imp  = [1 zeros(1, N)]
imp = ( n==0 )
[b, a] = butter(2, fc);     % Order-2 Butterworth filter
y = filter(b, a, imp);
Fs=8000;

        % Input signal

[H, om] = freqz(b, a);

f_freqz = om*Fs/(2*pi);

set(line_handle, 'ydata',  y);    
set(line_handle1,'ydata', abs(H));% Update data in figure

title( sprintf('Output of LPF. Cut-off frequency = %.3f', fc), 'fontsize', 12 )

end

