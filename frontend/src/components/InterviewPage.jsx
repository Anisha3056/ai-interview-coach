import { useState } from "react";
import {
    generateQuestion,
    evaluateAnswer
} from "../services/api";

function InterviewPage({
    analysis,
    evaluation,
    setEvaluation,
    previousQuestions,
    setPreviousQuestions
}) {

    const [role, setRole] =
        useState("Machine Learning Engineer");

    const [question, setQuestion] =
        useState(null);

    const [answer, setAnswer] =
        useState("");

    const [interviewType, setInterviewType] =
    useState("Project Based");

    const [loading, setLoading] = 
    useState(false);
    
    const [status, setStatus] =
    useState("");

    const handleGenerateQuestion =
async () => {

    try {

        setLoading(true);

        setStatus(
            "🎯 Generating interview question..."
        );

        const result =
            await generateQuestion(
                analysis,
                role,
                interviewType,
                previousQuestions
            );

        setQuestion(result);

        setPreviousQuestions([
            ...previousQuestions,
            {
                question:
                    result.question,
                topic:
                    result.topic,
                interview_type:
                    interviewType
            }
        ]);

        setStatus(
            "✅ Question generated!"
        );

    }
    catch (error) {

        console.error(error);

        alert(
            "Question generation failed"
        );

    }
    finally {

        setLoading(false);

    }
};

    const handleEvaluateAnswer =
async () => {

    try {

        setLoading(true);

        setStatus(
            "📝 Evaluating answer..."
        );

        setTimeout(() => {

            setStatus(
                "📊 Calculating score..."
            );

        }, 1200);

        setTimeout(() => {

            setStatus(
                "💡 Generating feedback..."
            );

        }, 2500);

        const result =
            await evaluateAnswer(
                question,
                answer
            );

        setEvaluation(
            result
        );

        setStatus(
            "✅ Evaluation complete!"
        );

    }
    catch (error) {

        console.error(error);

        alert(
            "Evaluation failed"
        );

    }
    finally {

        setLoading(false);

    }
};
    return (

        <div>

            <h2>
                Interview
            </h2>

            <label>
                Select Role:
            </label>

            <select
                value={role}
                onChange={(e) =>
                    setRole(
                        e.target.value
                    )
                }
            >

                <option>
                    Machine Learning Engineer
                </option>

                <option>
                    Data Scientist
                </option>

                <option>
                    AI Engineer
                </option>

                <option>
                    Software Engineer
                </option>

                <option>
                    Business Analyst
                </option>

                <option>
                    Data Analyst
                </option>

                <option>
                    Cybersecurity Analyst
                </option>

                <option>
                    Product Manager
                </option>

                <option>
                    DevOps Engineer
                </option>

            </select>

            <select
    value={interviewType}
    onChange={(e) =>
        setInterviewType(e.target.value)
    }
>

    <option>
        Project Based
    </option>

    <option>
        Behavioral
    </option>

    <option>
        Tech Stack
    </option>

    <option>
        System Design
    </option>

    <option>
        Machine Learning Fundamentals
    </option>

    <option>
        DSA
    </option>

</select>

            <br />
            <br />

            <button
                onClick={
                    handleGenerateQuestion
                }
            >
                Generate Question
            </button>

            {
    loading && (

        <p className="status-text">
            {status}
        </p>

    )
}

            {
                question && (

                    <div>

                        <div className="question-card">

    <h3>
        🎯 Interview Question
    </h3>

    <p className="question-text">
        {question.question}
    </p>

    <div className="question-meta">

        <span className="badge medium">
            {question.difficulty}
        </span>

        <span className="badge">
            {question.topic}
        </span>

    </div>

</div>

                        <textarea

                            rows="10"

                            cols="80"

                            placeholder="Type your answer here..."

                            value={answer}

                            onChange={(e) =>
                                setAnswer(
                                    e.target.value
                                )
                            }

                        />

                        <br />
                        <br />

                        <button
                            onClick={
                                handleEvaluateAnswer
                            }
                        >
                            Submit Answer
                        </button>

                    </div>

                )
            }

        </div>
    );
}

export default InterviewPage;