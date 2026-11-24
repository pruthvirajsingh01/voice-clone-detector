
import asyncio
import os
import librosa
import soundfile as sf
import edge_tts

OUTPUT_DIR = "data/test/fake"
os.makedirs(OUTPUT_DIR, exist_ok=True)

samples = [
    "Hello, my name is Alex. Today I am testing a voice detection system.",
    "Artificial intelligence is changing the way people communicate.",
    "Machine learning helps computers identify patterns in data.",
    "Good morning everyone. Welcome to our technology presentation.",
    "Voice cloning technology can generate realistic human-like speech."
]

async def generate_audio():
    for i, text in enumerate(samples, start=1):
        mp3_path = f"{OUTPUT_DIR}/ai_{i:02d}.mp3"
        wav_path = f"{OUTPUT_DIR}/ai_{i:02d}.wav"

        communicate = edge_tts.Communicate(
            text,
            "en-US-AriaNeural"
        )

        await communicate.save(mp3_path)

        audio, sr = librosa.load(mp3_path, sr=None)
        sf.write(wav_path, audio, sr)

        os.remove(mp3_path)

        print(f"Created: {wav_path}")

asyncio.run(generate_audio())
