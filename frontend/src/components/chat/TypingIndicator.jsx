import BotLogo from "../../assets/logo.jpeg";

export default function TypingIndicator() {

    return (

        <div className="flex items-start gap-2">

            <img
                src={BotLogo}
                alt="Bot"
                className="w-10 h-10 rounded-full border border-warm-border"
            />

            <div className="max-w-[70%] p-3 rounded-xl bg-warm-soft flex space-x-1">

                <span className="w-2.5 h-2.5 bg-warm-primary rounded-full animate-bounce"></span>

                <span className="w-2.5 h-2.5 bg-warm-primary rounded-full animate-bounce delay-150"></span>

                <span className="w-2.5 h-2.5 bg-warm-primary rounded-full animate-bounce delay-300"></span>

            </div>

        </div>

    );

}