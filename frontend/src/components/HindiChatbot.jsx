import Chatbot from "./Chatbot";

const welcome =
  "नमस्ते! 👋 मैं मातृ हूँ — आपकी मातृत्व स्वास्थ्य सहायक। कृपया बताएं, मैं आपकी कैसे मदद कर सकती हूँ?";

export default function HindiChatbot() {
  return (
    <Chatbot
      title="मातृ — मातृत्व स्वास्थ्य सहायक"
      welcome={welcome}
      placeholder="अपना प्रश्न यहाँ लिखें..."
      sendLabel="भेजें"
      language="hi"
    />
  );
}