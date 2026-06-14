import { useState, useEffect } from "react";

function EvaluationPage({
    evaluation,
    setEvaluation,
    setQuestion
}) {

    const [notes, setNotes] =
        useState("");

    useEffect(() => {

        const savedNotes =
            localStorage.getItem(
                "interviewNotes"
            );

        if (savedNotes) {

            setNotes(savedNotes);

        }

    }, []);

    const saveNotes = () => {

        localStorage.setItem(
            "interviewNotes",
            notes
        );

        alert(
            "Notes Saved!"
        );

    };

    const downloadNotes = () => {

        const blob =
            new Blob(
                [notes],
                {
                    type: "text/plain"
                }
            );

        const url =
            window.URL.createObjectURL(
                blob
            );

        const a =
            document.createElement("a");

        a.href = url;

        a.download =
            "interview-notes.txt";

        a.click();

        window.URL.revokeObjectURL(
            url
        );

    };

    const addMissingPoints = () => {

        const generatedNotes =

            evaluation
                .missing_points

                .map(
                    point =>
                        `- Learn ${point}`
                )

                .join("\n");

        setNotes(
            prev =>
                prev +
                "\n" +
                generatedNotes
        );

    };

    const scoreColor =
        evaluation.score >= 8
            ? "#22c55e"
            : evaluation.score >= 5
            ? "#f59e0b"
            : "#ef4444";

    return (

        <div>

            <h2>
                Score:
                {" "}
                {evaluation.score}/10
            </h2>

            <div className="score-bar">

                <div
                    className="score-fill"
                    style={{
                        width:
                            `${evaluation.score * 10}%`,
                        backgroundColor:
                            scoreColor
                    }}
                />

            </div>

            <h3>
                Strengths
            </h3>

            <ul>

                {
                    evaluation.strengths.map(
                        (
                            item,
                            index
                        ) => (

                            <li key={index}>
                                {item}
                            </li>

                        )
                    )
                }

            </ul>

            <h3>
                Missing Points
            </h3>

            <ul>

                {
                    evaluation.missing_points.map(
                        (
                            item,
                            index
                        ) => (

                            <li key={index}>
                                {item}
                            </li>

                        )
                    )
                }

            </ul>

            <div className="feedback-card">

    <h3>💡 Feedback</h3>

    <p>{evaluation.feedback}</p>

</div>

            <br />

            <button

                onClick={() => {

                    setEvaluation(
                        null
                    );

                    setQuestion(
                        null
                    );

                }}

            >
                Next Question
            </button>

            <hr />

            <h3>
                📝 Learning Notes
            </h3>

            <textarea

                rows="8"

                cols="80"

                value={notes}

                placeholder={`Write interview learnings...

- Revise ROC-AUC
- Learn ADASYN
- Review threshold tuning`}

                onChange={(e) =>

                    setNotes(
                        e.target.value
                    )

                }

            />

            <br />
            <br />

            <button
                onClick={saveNotes}
            >
                Save Notes
            </button>

            {" "}

            <button
                onClick={addMissingPoints}
            >
                Add Missing Points
            </button>

            {" "}

            <button
                onClick={downloadNotes}
            >
                Download Notes
            </button>

        </div>

    );

}

export default EvaluationPage;