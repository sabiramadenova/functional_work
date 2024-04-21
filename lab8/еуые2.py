import wave
import struct
import math
import tkinter as tk


def generate_audio_file(num_channels, sampwidth, framerate, duration):
    # Рассчитываем общее количество фреймов
    nframes = int(duration * framerate)

    # Создаем новый объект wave для записи
    with wave.open('output.wav', 'wb') as wav_file:
        # Задаем параметры аудиофайла
        wav_file.setnchannels(num_channels)
        wav_file.setsampwidth(sampwidth)
        wav_file.setframerate(framerate)
        wav_file.setnframes(nframes)

        # Генерируем аудиоданные (например, сумму трех синусоид разных частот)
        for i in range(nframes):
            # Генерируем значения для каждого канала (сумма трех синусоид разных частот)
            value_left = int(32767 * (math.sin(2 * math.pi * 440 * i / framerate) +
                                      math.sin(2 * math.pi * 554.37 * i / framerate) +
                                      math.sin(2 * math.pi * 659.25 * i / framerate))) // 3
            value_right = int(32767 * (math.sin(2 * math.pi * 440 * i / framerate) +
                                       math.sin(2 * math.pi * 554.37 * i / framerate) +
                                       math.sin(2 * math.pi * 659.25 * i / framerate))) // 3

            # Упаковываем значения в двоичный формат и записываем в файл
            data = struct.pack('<hh', value_left, value_right)
            wav_file.writeframesraw(data)

    print("Аудиофайл успешно записан.")


def main():
    def generate_button_clicked():
        num_channels_val = int(num_channels_input.get())
        sampwidth_val = int(sampwidth_input.get())
        framerate_val = int(framerate_input.get())
        duration_val = int(duration_input.get())

        generate_audio_file(num_channels_val, sampwidth_val, framerate_val, duration_val)

    root = tk.Tk()
    root.title("Генератор аудиофайлов")

    num_channels_label = tk.Label(root, text="Количество каналов:")
    num_channels_label.grid(row=0, column=0)
    num_channels_input = tk.Entry(root)
    num_channels_input.grid(row=0, column=1)

    sampwidth_label = tk.Label(root, text="Глубина звука (байт):")
    sampwidth_label.grid(row=1, column=0)
    sampwidth_input = tk.Entry(root)
    sampwidth_input.grid(row=1, column=1)

    framerate_label = tk.Label(root, text="Частота дискретизации (Гц):")
    framerate_label.grid(row=2, column=0)
    framerate_input = tk.Entry(root)
    framerate_input.grid(row=2, column=1)

    duration_label = tk.Label(root, text="Длительность (сек):")
    duration_label.grid(row=3, column=0)
    duration_input = tk.Entry(root)
    duration_input.grid(row=3, column=1)

    generate_button = tk.Button(root, text="Сгенерировать аудиофайл", command=generate_button_clicked)
    generate_button.grid(row=4, column=0, columnspan=2, pady=10)

    root.mainloop()


if __name__ == "__main__":
    main()