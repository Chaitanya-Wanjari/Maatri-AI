import React, { useState, useEffect, useRef } from "react";

import MessageBubble from "./chat/MessageBubble";
import ChatHeader from "./chat/ChatHeader";
import TypingIndicator from "./chat/TypingIndicator";
import ExplainabilityPanel from "./chat/ExplainabilityPanel";

import API_BASE_URL from "../config";

export default function Chatbot({
  title,
  welcome,
  placeholder,
  sendLabel,
  language,
}) {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");
  const [loading, setLoading] = useState(false);

  const chatEndRef = useRef(null);

  //--------------------------------------------------
  // Session ID
  //--------------------------------------------------

  const [sessionId] = useState(() => {
    const existing = localStorage.getItem("maatri-session");

    if (existing) return existing;

    const id = crypto.randomUUID();

    localStorage.setItem(
      "maatri-session",
      id
    );

    return id;
  });

  //--------------------------------------------------
  // Latest Bot Message
  //--------------------------------------------------

  const latestBotMessage = [...messages]
    .reverse()
    .find((m) => m.sender === "bot");

  //--------------------------------------------------
  // Auto Scroll
  //--------------------------------------------------

  useEffect(() => {
    chatEndRef.current?.scrollIntoView({
      behavior: "smooth",
      block: "end",
    });
  }, [messages, loading]);

  //--------------------------------------------------
  // Welcome Animation
  //--------------------------------------------------

  useEffect(() => {
    let i = 0;

    const timer = setInterval(() => {
      i++;

      setMessages([
        {
          sender: "bot",
          text: welcome.slice(0, i),
          showSources: false,
        },
      ]);

      if (i >= welcome.length) {
        clearInterval(timer);
      }
    }, 20);

    return () => clearInterval(timer);
  }, [welcome]);

  //--------------------------------------------------
  // Send Message
  //--------------------------------------------------

  const sendMessage = async () => {
    if (!input.trim()) return;

    const question = input;

    setMessages((prev) => [
      ...prev,
      {
        sender: "user",
        text: question,
      },
    ]);

    setInput("");

    setLoading(true);

    try {
      const res = await fetch(
        `${API_BASE_URL}/ask`,
        {
          method: "POST",

          headers: {
            "Content-Type":
              "application/json",
          },

          body: JSON.stringify({
            question,
            session_id: sessionId,
          }),
        }
      );

      if (!res.ok)
        throw new Error("Request failed");

      const data = await res.json();

      setMessages((prev) => [
        ...prev,
        {
          sender: "bot",

          text: data.answer,

          disclaimer:
            data.disclaimer,

          sources:
            data.sources,

          metadata:
            data.metadata,

          agent:
            data.agent,

          trace:
            data.trace,

          showSources: false,
        },
      ]);
    } catch (err) {
      console.error(err);

      setMessages((prev) => [
        ...prev,
        {
          sender: "bot",

          text:
            language === "hi"
              ? "⚠️ सर्वर से कनेक्ट नहीं हो पाया।"
              : "⚠️ Unable to connect to server.",
        },
      ]);
    } finally {
      setLoading(false);
    }
  };

  //--------------------------------------------------
  // Enter Key
  //--------------------------------------------------

  const handleKeyDown = (e) => {
    if (e.key === "Enter") {
      sendMessage();
    }
  };

  //--------------------------------------------------
  // Toggle Sources
  //--------------------------------------------------

  const toggleSources = (index) => {
    setMessages((prev) =>
      prev.map((msg, i) =>
        i === index
          ? {
              ...msg,
              showSources:
                !msg.showSources,
            }
          : msg
      )
    );
  };

  //--------------------------------------------------
  // UI
  //--------------------------------------------------

  return (
    <div className="h-screen bg-warm-bg p-5">

      <div className="h-full max-w-7xl mx-auto flex gap-5">

        {/* ================= CHAT ================= */}

        <div className="flex-[2] flex flex-col border border-warm-border rounded-xl shadow-lg bg-warm-cardbg overflow-hidden">

          <ChatHeader title={title} />

          {/* Messages */}

          <div className="flex-1 overflow-y-auto p-4 flex flex-col space-y-4">

            {messages.map((message, index) => (
              <MessageBubble
                key={index}
                message={message}
                index={index}
                toggleSources={toggleSources}
              />
            ))}

            {loading && (
              <TypingIndicator />
            )}

            <div ref={chatEndRef} />

          </div>

          {/* Input */}

          <div className="border-t border-warm-border bg-warm-bg p-3 flex">

            <input
              className="flex-1 rounded-xl border border-warm-border px-4 py-2 outline-none"

              placeholder={placeholder}

              value={input}

              onChange={(e) =>
                setInput(e.target.value)
              }

              onKeyDown={handleKeyDown}
            />

            <button
              onClick={sendMessage}
              className="ml-2 px-5 py-2 rounded-xl bg-warm-button text-warm-buttonText hover:bg-warm-accent"
            >
              {sendLabel}
            </button>

          </div>

        </div>

        {/* ================= EXPLAINABILITY ================= */}

        <div className="w-[340px] border border-warm-border rounded-xl bg-white shadow-lg overflow-y-auto">

          <ExplainabilityPanel
            message={latestBotMessage}
          />

        </div>

      </div>

    </div>
  );
}