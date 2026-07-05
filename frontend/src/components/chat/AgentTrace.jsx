export default function AgentTrace({
  message,
}) {

  if (!message.metadata)
    return null;

  const m = message.metadata;

  return (

    <div className="mt-4 rounded-lg border border-warm-border bg-warm-bg p-3">

      <div className="font-semibold mb-2">

        ⚙ Agent Execution

      </div>

      <div className="space-y-1 text-sm">

        <div>🟢 Planner Agent</div>

        <div>↓</div>

        <div>🟣 {message.agent}</div>

        <div>↓</div>

        <div>🔵 {m.knowledge_engine}</div>

        <div>↓</div>

        <div>🟠 {m.retriever}</div>

        <div>↓</div>

        <div>🟡 {m.reranker}</div>

        <div>↓</div>

        <div>⭐ {m.llm}</div>

        <hr className="my-2"/>

        <div>

          📚 Documents:
          {" "}
          {m.documents_used}

        </div>

        <div>

          ⚡ Latency:
          {" "}
          {m.latency_ms} ms

        </div>

      </div>

    </div>

  );

}