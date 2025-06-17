import streamlit as st
import whisper
from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM
from pytube import YouTube
import os
from tempfile import NamedTemporaryFile

# 🌟 Streamlit UI
st.set_page_config(page_title="🎧 YouTube Summary Tool", layout="centered")
st.title("🧠 AI YouTube Summarizer (Amal's Free Version)")
st.markdown("Summarize videos by extracting key points using Whisper + GPT2")

yt_url = st.text_input("📺 Paste YouTube Video URL")

max_len = st.slider("📝 Max Tokens for Summary", 100, 300, 150)

@st.cache_resource
def load_whisper_model():
    return whisper.load_model("base") # Choose "tiny", "base", "small", etc.

# Load GPT-2 summarizer (offline)
@st.cache_resource
def load_summarizer():
    model_id = "gpt2"
    tokenizer = AutoTokenizer.from_pretrained(model_id)
    model = AutoModelForCausalLM.from_pretrained(model_id)
    return pipeline("text-generation", model=model, tokenizer=tokenizer)

transcriber = load_whisper_model()
summarizer = load_summarizer()

# Start Processing
if st.button("🚀 Generate Summary"):
    if not yt_url:
        st.warning("Please paste a valid YouTube link.")
        st.stop()

    # --- Error handling for YouTube download ---
    try:
        with st.spinner("📥 Downloading audio..."):
            yt = YouTube(yt_url)
            audio_stream = yt.streams.filter(only_audio=True).first()
            if audio_stream is None:
                st.error("No audio stream found. The video may be restricted or unavailable.")
                st.stop()
            temp_audio = NamedTemporaryFile(delete=False, suffix=".mp4")
            audio_stream.download(filename=temp_audio.name)
    except Exception as e:
        st.error(f"Failed to download audio: {e}")
        st.stop()

    with st.spinner("🔊 Transcribing audio using Whisper..."):
        transcript = transcriber.transcribe(temp_audio.name)["text"]

    with st.expander("📝 Full Transcript"):
        st.write(transcript)

    os.remove(temp_audio.name)

    with st.spinner("🧠 Summarizing using GPT-2..."):
        prompt = f"Summarize the following transcript into key bullet points:\n\n{transcript}"
        output = summarizer(prompt, max_new_tokens=max_len, do_sample=True, temperature=0.7)[0]["generated_text"]

    st.success("✅ Summary Ready!")
    st.markdown("### 🔑 Key Points:")
    st.markdown(output.replace(prompt, "").strip())