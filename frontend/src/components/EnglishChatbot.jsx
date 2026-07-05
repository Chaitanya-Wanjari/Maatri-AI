import Chatbot from "./Chatbot";

const welcome =
  "Hello! 👋 I'm Maatri, your maternal health assistant. How are you feeling today? You can ask me about pregnancy, diet, symptoms, medicines, exercises and much more.";

export default function EnglishChatbot() {
  return (
    <Chatbot
      title="Maatri - Maternal Healthcare Assistant"
      welcome={welcome}
      placeholder="Type your question..."
      sendLabel="Send"
      language="en"
    />
  );
}