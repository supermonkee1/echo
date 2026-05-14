import sounddevice as sd
from scipy.io.wavfile import write
from faster_whisper import WhisperModel

# Record settings
duration = 5
sample_rate = 16000

print("Recording...")

audio = sd.rec(
    int(duration * sample_rate),
    samplerate=sample_rate,
    channels=1
)

sd.wait()

write("recording.wav", sample_rate, audio)

print("Transcribing...")

model = WhisperModel("base", compute_type="float32")

segments, info = model.transcribe(
    "recording.wav",
    language="en"
)

for segment in segments:
    print(segment.text)