import { motion } from "framer-motion";

import BotLogo from "../../assets/logo.jpeg";
import UserImage from "../../assets/heroimage.jpg";

import SourceCard from "./SourceCard";
import AgentTrace from "./AgentTrace";

export default function MessageBubble({
  message,
  index,
  toggleSources,
}) {
  const isUser = message.sender === "user";

  return (
    <div
      className={`flex items-start ${
        isUser ? "justify-end" : "justify-start"
      }`}
    >
      {!isUser && (
        <img
          src={BotLogo}
          alt="Bot"
          className="w-10 h-10 rounded-full mr-3 border border-warm-border shadow-sm"
        />
      )}

      <motion.div
        initial={{ opacity: 0, y: 8 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.2 }}
        className={`max-w-[82%] rounded-2xl shadow-md px-5 py-4 whitespace-pre-line ${
          isUser
            ? "bg-warm-primary text-warm-buttonText"
            : "bg-white text-gray-800 border border-gray-200"
        }`}
      >
        {/* Message */}

        <div className="leading-7 text-[15px]">
          {message.text}
        </div>

        {/* Disclaimer */}

        {message.disclaimer && (
          <div className="mt-4 text-xs text-gray-500 border-t pt-3">
            {message.disclaimer}
          </div>
        )}

        {/* Agent Trace */}

        {message.metadata && (
          <div className="mt-4">
            <AgentTrace
              message={message}
            />
          </div>
        )}

        {/* Sources */}

        {message.sources &&
          message.sources.length > 0 && (
            <div className="mt-5">

              <button
                onClick={() =>
                  toggleSources(index)
                }
                className="px-4 py-2 rounded-lg bg-blue-50 border border-blue-200 text-blue-700 text-sm font-medium hover:bg-blue-100 transition"
              >
                {message.showSources
                  ? "Hide Retrieved Evidence"
                  : `Show Retrieved Evidence (${message.sources.length})`}
              </button>

              {message.showSources && (
                <div className="mt-4 space-y-4">

                  {message.sources.map(
                    (source, i) => (
                      <SourceCard
                        key={i}
                        source={source}
                        index={i}
                      />
                    )
                  )}

                </div>
              )}

            </div>
          )}

      </motion.div>

      {isUser && (
        <img
          src={UserImage}
          alt="User"
          className="w-10 h-10 rounded-full ml-3 border border-warm-border shadow-sm"
        />
      )}
    </div>
  );
}