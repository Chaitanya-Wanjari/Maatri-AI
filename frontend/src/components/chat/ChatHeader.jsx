import { useNavigate } from "react-router-dom";

export default function ChatHeader({ title }) {

    const navigate = useNavigate();

    return (

        <div className="flex justify-between items-center px-4 py-3 border-b border-warm-border bg-warm-bg rounded-t-xl">

            <h1 className="text-2xl font-serif text-warm-primary font-bold">
                {title}
            </h1>

            <button
                onClick={() => navigate("/")}
                className="px-3 py-1 bg-warm-button text-warm-buttonText rounded hover:bg-warm-accent transition"
            >
                Home
            </button>

        </div>

    );

}