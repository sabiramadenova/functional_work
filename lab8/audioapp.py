import wave
import struct
import math
import tkinter as tk

NOTES = {
    "До мажор": 261.63,
    "До# мажор": 277.18,
    "Ре мажор": 293.66,
    "Ре# мажор": 311.13,
    "Ми мажор": 329.63,
    "Фа мажор": 349.23,
    "Фа# мажор": 369.99,
    "Соль мажор": 392.00,
    "Соль# мажор": 415.30,
    "Ля мажор": 440,
    "Ля# мажор": 466.16,
    "Си мажор": 493.88,
}


def generate_audio_file(note1_freq, note2_freq, num_channels, sampwidth, framerate, duration):

    nframes = int(duration * framerate)

    with wave.open('output.wav', 'wb') as wav_file:

        wav_file.setnchannels(num_channels)
        wav_file.setsampwidth(sampwidth)
        wav_file.setframerate(framerate)
        wav_file.setnframes(nframes)

        for i in range(nframes):
            value1 = math.sin(2 * math.pi * note1_freq * i / framerate)
            value2 = math.sin(2 * math.pi * note2_freq * i / framerate)

            value = (value1 + value2) / 2

            scaled_value = int(value * 32767)

            data = struct.pack('<h', scaled_value)
            if num_channels == 2:
                data *= 2
            wav_file.writeframesraw(data)

    print("Audio file successfully written.")


def main():
    def generate_button_clicked():
        note1_freq_val = NOTES[note1_var.get()]
        note2_freq_val = NOTES[note2_var.get()]
        num_channels_val = int(num_channels_input.get())
        sampwidth_val = int(sampwidth_input.get())
        framerate_val = int(framerate_input.get())
        duration_val = int(duration_input.get())

        generate_audio_file(note1_freq_val, note2_freq_val, num_channels_val, sampwidth_val, framerate_val,
                            duration_val)

    root = tk.Tk()
    root.title("Audio File Generator")

    note1_var = tk.StringVar()
    note2_var = tk.StringVar()

    note1_label = tk.Label(root, text="Select note 1:")
    note1_label.grid(row=0, column=0)
    note1_dropdown = tk.OptionMenu(root, note1_var, *NOTES.keys())
    note1_dropdown.grid(row=0, column=1)

    note2_label = tk.Label(root, text="Select note 2:")
    note2_label.grid(row=1, column=0)
    note2_dropdown = tk.OptionMenu(root, note2_var, *NOTES.keys())
    note2_dropdown.grid(row=1, column=1)

    num_channels_label = tk.Label(root, text="Number of channels:")
    num_channels_label.grid(row=2, column=0)
    num_channels_input = tk.Entry(root)
    num_channels_input.grid(row=2, column=1)

    sampwidth_label = tk.Label(root, text="Sample width (bytes):")
    sampwidth_label.grid(row=3, column=0)
    sampwidth_input = tk.Entry(root)
    sampwidth_input.grid(row=3, column=1)

    framerate_label = tk.Label(root, text="Sampling rate (Hz):")
    framerate_label.grid(row=4, column=0)
    framerate_input = tk.Entry(root)
    framerate_input.grid(row=4, column=1)

    duration_label = tk.Label(root, text="Duration (sec):")
    duration_label.grid(row=5, column=0)
    duration_input = tk.Entry(root)
    duration_input.grid(row=5, column=1)

    generate_button = tk.Button(root, text="Generate Audio File", command=generate_button_clicked)
    generate_button.grid(row=6, column=0, columnspan=2, pady=10)

    root.mainloop()


if __name__ == "__main__":
    main()
