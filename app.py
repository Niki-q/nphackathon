import os
import time
import streamlit as st
import sounddevice as sd
import soundfile as sf
import numpy as np
import requests

# Streamlit App
st.title("Voice Recording and Backend Communication")

# Initialize log messages from a file if it exists
log_messages = []
log_file_path = "log.txt"
if os.path.exists(log_file_path):
    with open(log_file_path, "r") as log_file:
        log_messages = log_file.readlines()

# Log Input
with st.expander("Log", expanded=True):
    log_container = st.empty()
    log_content = "\n".join(log_messages)
    log_container.markdown(log_content, unsafe_allow_html=True)

def set_log(message):
    if message.startswith("["):
        log_message = message
    else:
        timestamp = time.strftime("[%Y-%m-%d %H:%M:%S] ", time.localtime())
        log_message = f"{timestamp}{message}"

    log_messages.append(log_message)
    log_content = "\n".join(log_messages)
    log_container.markdown(log_content, unsafe_allow_html=True)

    # Save log messages to a file
    with open(log_file_path, "w") as log_file:
        log_file.writelines(log_messages)

def record_audio(file_path):
    set_log("Recording started.")

    fs = 44100  # Sample rate
    duration = 10  # Recording duration in seconds (increased to 10 seconds)

    audio_frames = []

    def audio_callback(indata, frames, time, status):
        audio_frames.append(indata.copy())

    with sd.InputStream(samplerate=fs, channels=1, dtype='int16', callback=audio_callback):
        sd.sleep(int(duration * 1000))

    audio_data = np.concatenate(audio_frames, axis=0)
    sf.write(file_path, audio_data, fs)

    set_log("Recording stopped.")
    send_to_backend(file_path)

def send_to_backend(file_path):
    backend_url = "http://127.0.0.1:8000/upload"  # Замените на свой URL
    set_log("Sending recording to backend...")

    with open(file_path, "rb") as f:
        files = {"files": (file_path, f)}
        response = requests.post(backend_url, files=files)

    if response.status_code == 200:
        set_log("Recording sent successfully to backend.")
        os.remove(file_path)
    else:
        set_log(f"Failed to send recording. Backend response: {response.status_code}")

# Button to start/stop recording
recording = st.button("Record Voice")

# Button to clear logs
clear_logs = st.button("Clear Logs")

if recording:
    file_path = "recorded_voice.wav"
    record_audio(file_path)

if clear_logs:
    log_messages = []
    log_container.markdown("", unsafe_allow_html=True)  # Clear the log container visually
    with open(log_file_path, "w") as log_file:
        log_file.writelines(log_messages)  # Clear the log file
