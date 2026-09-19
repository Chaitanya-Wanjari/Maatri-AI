export default function AgentTrace({ message }) {
  if (!message.metadata) return null;

  const m = message.metadata;

  return (
    <div className="mt-4 rounded-lg border border-warm-border bg-warm-bg p-3">
      <div className="font-semibold mb-2">📚 Supporting Sources</div>

      <div className="text-sm text-gray-700">
        Retrieved from {m.documents_used} trusted reference
        {m.documents_used !== 1 ? "s" : ""}.
      </div>
    </div>
  );
}