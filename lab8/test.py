import wave

# Открываем аудиофайл в формате WAV
with wave.open('output.wav', 'rb') as wav_file:
    # Читаем параметры аудиофайла
    params = wav_file.getparams()
    num_channels, sampwidth, framerate, nframes = params[:4]

    # Читаем все аудиоданные
    audio_data = wav_file.readframes(nframes)

# Выводим информацию о параметрах аудиофайла
print("Количество каналов:", num_channels)
print("Глубина звука (в байтах):", sampwidth)
print("Частота дискретизации (в Гц):", framerate)
print("Общее количество фреймов:", nframes)

# Дальнейшая обработка аудиоданных...
