import { useState } from "react";

export default function SourceCard({
  source,
  index,
}) {
  const [expanded, setExpanded] =
    useState(false);

  const text =
    source.text || "No content available.";

  const preview =
    text.length > 250
      ? text.slice(0, 250) + "..."
      : text;

  return (
    <div className="rounded-xl border border-gray-200 bg-white shadow-sm">

      {/* Header */}

      <div className="flex justify-between items-center px-4 py-3 border-b bg-gray-50 rounded-t-xl">

        <div>

          <div className="font-semibold text-gray-800">

            📄 Retrieved Document #{index + 1}

          </div>

          <div className="text-xs text-gray-500 mt-1">

            Source: {source.source}

          </div>

        </div>

        {source.rerank_score !== undefined && (
          <div className="px-3 py-1 rounded-full bg-green-100 text-green-700 text-xs font-semibold">

            Score: {source.rerank_score.toFixed(2)}

          </div>
        )}

      </div>

      {/* Evidence */}

      <div className="px-4 py-4">

        <div className="text-sm font-semibold text-gray-700 mb-2">

          Retrieved Evidence

        </div>

        <div className="text-sm whitespace-pre-wrap leading-6 text-gray-700">

          {expanded ? text : preview}

        </div>

        {text.length > 250 && (
          <button
            onClick={() =>
              setExpanded(!expanded)
            }
            className="mt-3 text-blue-600 hover:text-blue-800 text-sm font-medium"
          >
            {expanded
              ? "Show Less ▲"
              : "Show Full Context ▼"}
          </button>
        )}

      </div>

      {/* Footer */}

      <div className="grid grid-cols-2 gap-4 px-4 py-3 border-t bg-gray-50 text-xs">

        <div>

          <div className="font-semibold text-gray-600">

            Dense Score

          </div>

          <div className="text-gray-800">

            {source.dense_score !== undefined
              ? source.dense_score.toFixed(3)
              : "-"}

          </div>

        </div>

        <div>

          <div className="font-semibold text-gray-600">

            Cross Encoder

          </div>

          <div className="text-gray-800">

            {source.rerank_score !== undefined
              ? source.rerank_score.toFixed(3)
              : "-"}

          </div>

        </div>

      </div>

    </div>
  );
}