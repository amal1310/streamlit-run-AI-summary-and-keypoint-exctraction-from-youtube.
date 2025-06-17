# 🧠 AI YouTube Summarizer – Amal's Free Version

Summarize YouTube videos by extracting **key bullet points** using **OpenAI Whisper** and **GPT-2** – all running locally with a simple **Streamlit** UI.

## 🔍 Features

- 🎥 Accepts any YouTube video URL
- 🎧 Downloads and transcribes audio using **Whisper**
- ✍️ Summarizes the transcript into bullet points using **GPT-2**
- 💡 Displays the full transcript + generated summary
- 🧪 Runs offline (no OpenAI API needed)

---

## 📦 Tech Stack

| Tool | Purpose |
|------|---------|
| [Streamlit](https://streamlit.io/) | Frontend UI |
| [Whisper](https://github.com/openai/whisper) | Speech-to-text transcription |
| [Hugging Face Transformers](https://huggingface.co/transformers/) | GPT-2 summarizer |
| [Pytube](https://pytube.io/en/latest/) | Download YouTube audio |
| Python Standard Libraries | File handling, temp storage, etc.

---

## 🚀 How It Works

1. **Paste a YouTube URL** into the app.
2. **Audio is downloaded** from the video.
3. **Transcription** is done via Whisper.
4. **Summarization** is done using GPT-2.
5. **Key bullet points** are shown to the user.

---

## 🛠️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/youtube-ai-summarizer.git
cd youtube-ai-summarizer