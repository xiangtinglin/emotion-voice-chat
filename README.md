# Emotion Voice Chatbot (Streamlit)

## 📌 專案簡介
這是一個使用 Azure API + Streamlit 打造的英文語音情緒互動 demo。
功能：
- 語音辨識（Speech to Text）
- 文字情緒分析（Text Analytics）
- 固定回應邏輯（非 GPT）
- 語音合成回應（Text to Speech）

## 🚀 使用教學

1. 建立 `.env` 檔案，填入你的 Azure 金鑰：

```
SPEECH_KEY=your_azure_speech_key
SPEECH_REGION=your_azure_speech_region
TEXT_KEY=your_text_analytics_key
TEXT_ENDPOINT=https://your_text_analytics_endpoint/
```

2. 安裝依賴：

```bash
pip install -r requirements.txt
```

3. 執行 app：

```bash
streamlit run app.py
```

---

如需自動部署至 Streamlit Cloud，請將 `.env` 中內容設為環境變數。
