# myBot for discord

srcフォルダに.envファイルを作成
```
GEMINI_PROMPT = 'ここに簡単なプロンプト(語尾や口調)を記載'
DISCORD_TOKEN = 'YOUR_DISCORDBOT_TOKEN'
GEMINI_API_KEY = 'YOUR_GEMINI_API_KEY'
```
※本格的なプロンプト設定はAISTUDIOを推奨します。
https://aistudio.google.com/app/prompts/new_chat

# Google Gemini用のChatBot機能
チュートリアル: Gemini API のスタートガイド
https://ai.google.dev/gemini-api/docs/get-started/tutorial?lang=python&hl=ja

# コマンド一覧
* `/chat [message]` 'gemini-1.5-flash'でのonetimeチャット
* `/chatbot [model] [message]` モデル選択ができるonetimeチャット
* `/getGeminiModel` geminiの使用可能モデルを参照
