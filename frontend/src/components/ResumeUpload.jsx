import { useState } from "react";
import { uploadResume } from "../services/api";

function ResumeUpload({ setAnalysis }) {

    const [file, setFile] = useState(null);

    const [loading, setLoading] = useState(false);

    const [status, setStatus] = useState("");

    const handleUpload = async () => {

    if (!file) {

        alert("Please select a resume");

        return;
    }

    try {

        setLoading(true);

        setStatus(
            "📄 Parsing resume..."
        );

        setTimeout(() => {

            setStatus(
                "🧠 Analyzing skills and projects..."
            );

        }, 1500);

        const result =
            await uploadResume(file);

        setStatus(
            "✅ Resume analysis complete!"
        );

        setAnalysis(
            result.analysis
        );

    }
    catch (error) {

        console.error(error);

        alert(
            "Resume upload failed"
        );

    }
    finally {

        setLoading(false);

    }
};

    return (

        <div>

            <h2>
                Upload Resume
            </h2>

            <input
                type="file"
                accept=".pdf"
                onChange={(e) =>
                    setFile(
                        e.target.files[0]
                    )
                }
            />

            <br />
            <br />

            <button
                onClick={handleUpload}
            >
                {
                    loading
                        ? "Analyzing..."
                        : "Analyze Resume"
                }
            </button>

            {
    loading && (

        <div className="loading-box">

            <div className="spinner"></div>

            <p>{status}</p>

        </div>

    )
}

        </div>
    );
}



export default ResumeUpload;