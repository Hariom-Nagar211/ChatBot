# ChatBot - AI-Powered Conversational Assistant

A modern conversational AI chatbot built with Google's Gemini 1.5 Flash model, featuring a clean Streamlit web interface and robust conversation management using LangGraph.

## 🚀 Features

- **Advanced AI Conversations**: Powered by Google's Gemini 1.5 Flash model for intelligent responses
- **Persistent Chat History**: Maintains conversation context throughout the session
- **Modern Web Interface**: Clean and intuitive Streamlit-based UI
- **State Management**: Built with LangGraph for robust conversation flow control
- **Memory Management**: In-memory conversation checkpointing for seamless interactions
- **Environment Configuration**: Secure API key management with dotenv

## 🏗️ Architecture

The application follows a modular architecture:

- **Frontend** (`streamlit_frontend.py`): Streamlit-based web interface handling user interactions
- **Backend** (`langgraph_backend.py`): LangGraph-powered conversation engine with Gemini integration
- **State Management**: TypedDict-based conversation state with message history
- **Memory**: In-memory checkpointing for conversation persistence

## 📋 Prerequisites

- Python 3.8 or higher
- Google AI Studio API key (Gemini API access)
- Internet connection for API calls

## 🛠️ Installation

1. **Clone the repository**:
   ```bash
   git clone <your-repo-url>
   cd ChatBot
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**:
   Create a `.env` file in the project root:
   ```env
   GEMINI_API_KEY=your_gemini_api_key_here
   ```

   To get your API key:
   - Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
   - Create a new API key
   - Copy and paste it into your `.env` file

## 🚀 Usage

1. **Start the application**:
   ```bash
   streamlit run streamlit_frontend.py
   ```

2. **Access the chatbot**:
   - Open your browser and navigate to `http://localhost:8501`
   - Start chatting with the AI assistant!

3. **Features**:
   - Type your message in the chat input
   - View conversation history
   - Enjoy persistent conversations within the session

## 📁 Project Structure

```
ChatBot/
├── .env                    # Environment variables (API keys)
├── .gitignore             # Git ignore rules
├── README.md              # Project documentation
├── requirements.txt       # Python dependencies
├── langgraph_backend.py   # Backend logic with LangGraph
└── streamlit_frontend.py  # Frontend Streamlit interface
```

## 🔧 Configuration

### Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `GEMINI_API_KEY` | Google AI Studio API key for Gemini access | Yes |

### Model Configuration

The chatbot uses Google's Gemini 1.5 Flash model by default. You can modify the model in `langgraph_backend.py`:

```python
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",  # Change model here
    api_key=os.getenv("GEMINI_API_KEY"),
)
```

## 🛡️ Security

- API keys are stored in environment variables
- `.env` file is gitignored to prevent accidental commits
- No sensitive data is logged or exposed

## 🔍 Troubleshooting

### Common Issues

1. **Import Error**: `cannot import name 'Gemini' from 'langchain_gemini'`
   - **Solution**: Use `ChatGoogleGenerativeAI` from `langchain_google_genai` instead

2. **Credentials Error**: `DefaultCredentialsError`
   - **Solution**: Ensure `GEMINI_API_KEY` is set in your `.env` file

3. **Module Not Found**: Missing dependencies
   - **Solution**: Run `pip install -r requirements.txt`

### Debug Mode

To enable debug logging, add this to your backend:
```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Google AI for the Gemini API
- LangChain team for the excellent framework
- Streamlit for the intuitive web framework
- LangGraph for conversation state management

## 📞 Support

If you encounter any issues or have questions:
1. Check the troubleshooting section above
2. Create an issue in the repository
3. Ensure your API key is valid and has sufficient quota

---

**Happy Chatting! 🤖💬**
