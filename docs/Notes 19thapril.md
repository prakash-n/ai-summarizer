# 🧠 AI Learning Notes – Project 1: Text Summarizer

---

## 📌 Overview
Built a simple AI-powered text summarizer using:

- Python (3.11)
- VS Code
- Virtual Environment (venv)
- Initially OpenAI API → later switched to local AI (Ollama)

---

## ⚙️ Environment Setup

### 1. Install Python (via Homebrew)
```bash
brew install python@3.11
2. Create project folder
mkdir ai-summarizer
cd ai-summarizer
3. Create virtual environment
python3 -m venv venv
4. Activate venv
source venv/bin/activate
🧪 Initial Project (OpenAI API)
Install dependencies
pip install openai python-dotenv
.env file
OPENAI_API_KEY=your_api_key_here
Key Learnings
Environment variables must be loaded using:
from dotenv import load_dotenv
load_dotenv()
Use os.getenv() to access API key
Debugged .env issues (file name, format, spacing)
⚠️ Errors Faced & Fixes
1. API Key Not Found

Cause: .env not loading
Fix: Correct format + load_dotenv()

2. Wrong Python Version

Cause: System Python used instead of Homebrew
Fix:

which python3
python3 --version
3. pip Version Mismatch

Cause: Global vs venv pip confusion
Fix:

python3 -m pip install --upgrade pip
4. OpenAI Quota Error (429)

Cause: No billing / free credits exhausted

Decision: Switched to local AI (Ollama)

🚀 Migration to Local AI (Ollama)
Install Ollama
brew install ollama
Run model (first time downloads ~4.7GB)
ollama run llama3
Important Notes
Download happens only once
Model is stored locally
No API key required
🔌 Python Integration (Ollama)
Install Python package
pip install ollama
Final app.py
import ollama

def summarize_text(text):
    response = ollama.chat(
        model="llama3",
        messages=[
            {"role": "system", "content": "Summarize the following text clearly."},
            {"role": "user", "content": text}
        ]
    )
    return response["message"]["content"]

if __name__ == "__main__":
    text = input("Enter text to summarize:\n")
    summary = summarize_text(text)
    print("\nSummary:\n", summary)
▶️ Run the App
python app.py
🧹 Useful Terminal Commands
Clear terminal
clear

Shortcut: Cmd + K

Stop running program
Ctrl + C
Activate venv
source venv/bin/activate
🧠 Key Concepts Learned
Virtual environments (venv)
Environment variables (.env)
API vs Local AI models
Debugging terminal + Python issues
Switching from cloud AI → local AI
⚡ Current Status
✅ Working AI summarizer
✅ Runs locally (no cost)
✅ No API dependency
🚀 Next Steps
Add multi-line input support
Summarize files (PDF/text)
Build a simple web UI
Create chatbot version
💡 Notes
Ollama must be running to use models
First run is slow (model load)
Later runs are faster
Smaller models improve performance on MacBook Air
📁 Project Structure
ai-summarizer/
├── app.py
├── venv/
└── notes.md
🔥 Milestone Achieved

Built a complete AI app end-to-end:

Setup → Debug → API → Local AI

---

# 🎯 What improved here

- Fixed broken Markdown blocks ✅  
- Proper headings & spacing ✅  
- Clean code formatting ✅  
- GitHub-ready structure ✅  

---

If you want next:
I can help you :contentReference[oaicite:1]{index=1} 🚀
what to do with 2 create proect folder sepate .md file

Good question—you’re basically asking how to organize your project cleanly 👍

🧠 Short answer

👉 Yes, you should:

Create a project folder
Keep your code and notes separate
📁 Recommended structure (do this)

Inside your main learning folder:

AI Learning/
 ├── ai-summarizer/
 │    ├── app.py
 │    ├── venv/
 │    └── notes.md   ✅ (your file)
🚀 What to do step-by-step
✅ Step 1: Go to your project folder

In terminal:

cd ~/Desktop/Shreya/AI/AI\ Learning/ai-summarizer
✅ Step 2: Create notes file
touch notes.md
✅ Step 3: Open it in Visual Studio Code
code .

Then:

Click notes.md
Paste the Markdown content I gave you
Save ✅
🧠 Why separate .md file?
✅ Benefits
Keeps learning organized
Easy to revisit later
Looks professional (like real projects)
Can upload to GitHub
💡 Pro-level structure (future)

Later, you can organize like this:

AI Learning/
 ├── ai-summarizer/
 │    ├── src/
 │    │    └── app.py
 │    ├── notes.md
 │    ├── README.md
 │    └── requirements.txt
📌 Difference (important)
File	Purpose
app.py	Your code
notes.md	Your learning notes
README.md	Project description (for others)
🎯 What you should do now
Stay inside ai-summarizer folder
Create notes.md
Paste formatted notes
Save
🚀 Next step (optional but powerful)

I can help you create:

a README.md (GitHub-ready project page)
or 
clean your project into a portfolio-level structure

Just say 👍