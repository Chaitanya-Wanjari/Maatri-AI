export default function ExplainabilityPanel({ message }) {
  if (!message || !message.metadata) {
    return (
      <div className="h-full flex items-center justify-center p-6 text-center text-gray-500">
        <div>
          <div className="text-5xl mb-4">🧠</div>
          <h2 className="text-lg font-semibold mb-2">
            Explainability Panel
          </h2>
          <p className="text-sm">
            Ask a question to inspect how Maatri reasons,
            retrieves knowledge, and generates answers.
          </p>
        </div>
      </div>
    );
  }

  const meta = message.metadata;
  const trace = message.trace || {};
  const risk = meta.risk || {};

  return (
    <div className="p-5 space-y-5">

    <div>
        <h2 className="text-xl font-bold">
            🧠 Explainability
        </h2>

        <p className="text-xs text-gray-500 mt-1">
            Every response is grounded using retrieved medical evidence and routed through multiple AI agents.
        </p>
    </div>

    {/* Active Agent */}

    <div className="rounded-xl border bg-white shadow-sm p-4">

        <div className="text-xs uppercase text-gray-500">
            Active Agent
        </div>

        <div className="mt-2 font-semibold text-lg">
            🤖 {message.agent}
        </div>

    </div>

    {/* Language */}

    <div className="rounded-xl border bg-white shadow-sm p-4">

        <div className="text-xs uppercase text-gray-500">
            Language
        </div>

        <div className="mt-2 font-semibold">
            🌍 {meta.language}
        </div>

    </div>

    {/* Risk */}

    <div className="rounded-xl border bg-white shadow-sm p-4">

        <div className="font-semibold mb-3">
            🩺 Risk Assessment
        </div>

        <div className="space-y-3">

            <div>

                <div className="text-xs text-gray-500">
                    Agent
                </div>

                <div className="font-medium">
                    {risk.agent || "Risk Assessment Agent"}
                </div>

            </div>

            <div>

                <div className="text-xs text-gray-500">
                    Risk Level
                </div>

                <div
                    className={`inline-block mt-1 px-3 py-1 rounded-full text-sm font-semibold ${
                        risk.level === "high"
                            ? "bg-red-100 text-red-700"
                            : risk.level === "medium"
                            ? "bg-yellow-100 text-yellow-700"
                            : "bg-green-100 text-green-700"
                    }`}
                >
                    {(risk.level || "low").toUpperCase()}
                </div>

            </div>

            {risk.reason && (

                <div>

                    <div className="text-xs text-gray-500">
                        Why?
                    </div>

                    <div className="mt-2 rounded-lg bg-red-50 border border-red-200 p-3 text-sm">
                        Detected because the query contains
                        <div className="font-semibold mt-2">
                            "{risk.reason}"
                        </div>
                    </div>

                </div>

            )}

        </div>

    </div>

    {/* Query Rewrite */}

    <div className="rounded-xl border bg-white shadow-sm p-4">

        <div className="font-semibold mb-3">
            🔁 Query Rewrite
        </div>

        <div className="text-xs text-gray-500">
            Original Question
        </div>

        <div className="bg-gray-100 rounded-lg mt-1 p-2 text-sm">
            {trace.original_query}
        </div>

        <div className="text-xs text-gray-500 mt-4">
            Retrieval Query
        </div>

        <div className="bg-green-50 border border-green-200 rounded-lg mt-1 p-2 text-sm">
            {trace.rewritten_query}
        </div>

    </div>

    {/* Retrieval Stats */}

    <div className="grid grid-cols-2 gap-3">

        <div className="rounded-xl border bg-white p-4 text-center">

            <div className="text-3xl font-bold">
                {trace.retrieved_documents}
            </div>

            <div className="text-xs text-gray-500 mt-2">
                Documents Retrieved
            </div>

        </div>

        <div className="rounded-xl border bg-white p-4 text-center">

            <div className="text-3xl font-bold">
                {meta.latency_ms}
            </div>

            <div className="text-xs text-gray-500 mt-2">
                Latency (ms)
            </div>

        </div>

    </div>

    {/* Technology */}

    <div className="rounded-xl border bg-white shadow-sm p-4">

        <div className="font-semibold mb-3">
            ⚙️ Technology Stack
        </div>

        <div className="flex flex-wrap gap-2">

            {[
                "Google ADK",
                "Gemini",
                "FAISS",
                "Cross Encoder",
                "RAG",
                "MCP",
            ].map((item) => (

                <span
                    key={item}
                    className="px-3 py-1 rounded-full bg-blue-100 text-blue-700 text-xs"
                >
                    {item}
                </span>

            ))}

        </div>

    </div>

    {/* Execution Timeline */}

    <div className="rounded-xl border bg-white shadow-sm p-4">

        <div className="font-semibold mb-4">
            🚀 Execution Timeline
        </div>

        {[
            "Language Detection",
            "Risk Assessment Agent",
            "Planner Agent",
            message.agent,
            "FAISS Retrieval",
            "Cross Encoder",
            "Gemini Response",
        ].map((step, index) => (

            <div
                key={index}
                className="flex items-center gap-3 mb-3"
            >

                <span className="text-green-600">
                    ✅
                </span>

                <span className="text-sm">
                    {step}
                </span>

            </div>

        ))}

    </div>

    {/* Conversation Memory */}

    <div className="rounded-xl border bg-white shadow-sm p-4">

        <div className="font-semibold mb-3">
            💬 Conversation Memory
        </div>

        {trace.conversation_memory &&
        trace.conversation_memory.length > 0 ? (

            <div className="space-y-3">

                {trace.conversation_memory.map((msg, index) => (

                    <div
                        key={index}
                        className={`rounded-lg p-3 text-sm ${
                            msg.role === "user"
                                ? "bg-blue-50 border border-blue-200"
                                : "bg-green-50 border border-green-200"
                        }`}
                    >

                        <div className="font-semibold mb-1">

                            {msg.role === "user"
                                ? "👤 User"
                                : "🤖 Assistant"}

                        </div>

                        <div>
                            {msg.content}
                        </div>

                    </div>

                ))}

            </div>

        ) : (

            <div className="text-sm text-gray-500">
                No previous conversation.
            </div>

        )}

    </div>

</div>
    
  );
}