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

  return (
    <div className="p-5 space-y-5">

      {/* Title */}

      <div>
        <h2 className="text-xl font-bold">
          Explainability
        </h2>

        <p className="text-xs text-gray-500 mt-1">
          Every response is grounded using retrieved medical evidence.
        </p>
      </div>

      {/* Agent */}

      <div className="rounded-xl border shadow-sm p-4 bg-white">

        <div className="text-xs uppercase text-gray-500">
          Active Agent
        </div>

        <div className="mt-2 font-semibold text-lg">
          🤖 {message.agent}
        </div>

      </div>

      {/* Language */}

      <div className="rounded-xl border shadow-sm p-4 bg-white">

        <div className="text-xs uppercase text-gray-500">
          Language
        </div>

        <div className="mt-2 font-semibold">

          🌍 {meta.language}

        </div>

      </div>

      {/* Query Rewrite */}

      <div className="rounded-xl border shadow-sm p-4 bg-white">

        <div className="font-semibold mb-3">

          🔁 Query Rewriting

        </div>

        <div className="text-xs text-gray-500">

          Original Question

        </div>

        <div className="mt-1 text-sm bg-gray-100 rounded-lg p-2">

          {trace.original_query}

        </div>

        <div className="text-xs text-gray-500 mt-4">

          Retrieval Query

        </div>

        <div className="mt-1 text-sm bg-green-50 border border-green-200 rounded-lg p-2">

          {trace.rewritten_query}

        </div>

      </div>

      {/* Statistics */}

      <div className="grid grid-cols-2 gap-3">

        <div className="rounded-xl border p-4 text-center bg-white">

          <div className="text-2xl font-bold">

            {trace.retrieved_documents}

          </div>

          <div className="text-xs text-gray-500 mt-1">

            Documents Retrieved

          </div>

        </div>

        <div className="rounded-xl border p-4 text-center bg-white">

          <div className="text-2xl font-bold">

            {meta.latency_ms}

          </div>

          <div className="text-xs text-gray-500 mt-1">

            Latency (ms)

          </div>

        </div>

      </div>

      {/* Technology */}

      <div className="rounded-xl border shadow-sm p-4 bg-white">

        <div className="font-semibold mb-3">

          ⚙️ Technology Stack

        </div>

        <div className="flex flex-wrap gap-2">

          <span className="px-3 py-1 rounded-full bg-blue-100 text-blue-700 text-xs">
            Gemini
          </span>

          <span className="px-3 py-1 rounded-full bg-purple-100 text-purple-700 text-xs">
            FAISS
          </span>

          <span className="px-3 py-1 rounded-full bg-orange-100 text-orange-700 text-xs">
            Cross Encoder
          </span>

          <span className="px-3 py-1 rounded-full bg-green-100 text-green-700 text-xs">
            RAG
          </span>

          <span className="px-3 py-1 rounded-full bg-pink-100 text-pink-700 text-xs">
            ADK
          </span>

        </div>

      </div>

      {/* Pipeline */}

      <div className="rounded-xl border shadow-sm p-4 bg-white">

        <div className="font-semibold mb-4">

          🧠 Execution Pipeline

        </div>

        <div className="space-y-3">

          <div className="flex items-center gap-3">
            <span>🌍</span>
            <span>Language Detection</span>
          </div>

          <div className="ml-4 text-gray-400">↓</div>

          <div className="flex items-center gap-3">
            <span>🗂️</span>
            <span>Planner Agent</span>
          </div>

          <div className="ml-4 text-gray-400">↓</div>

          <div className="flex items-center gap-3">
            <span>🤖</span>
            <span>{message.agent}</span>
          </div>

          <div className="ml-4 text-gray-400">↓</div>

          <div className="flex items-center gap-3">
            <span>🔍</span>
            <span>FAISS Retrieval</span>
          </div>

          <div className="ml-4 text-gray-400">↓</div>

          <div className="flex items-center gap-3">
            <span>🎯</span>
            <span>Cross Encoder Re-ranking</span>
          </div>

          <div className="ml-4 text-gray-400">↓</div>

          <div className="flex items-center gap-3">
            <span>✨</span>
            <span>Gemini Response Generation</span>
          </div>

        </div>

      </div>

    </div>
  );
}