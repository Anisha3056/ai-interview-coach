import { useState } from "react";
import "./App.css";

import ResumeUpload from "./components/ResumeUpload";
import InterviewPage from "./components/InterviewPage";
import EvaluationPage from "./components/EvaluationPage";

function App() {

    const [analysis, setAnalysis] =
        useState(null);

    const [evaluation, setEvaluation] =
        useState(null);

    const [question, setQuestion] =
        useState(null);

    const [previousQuestions, setPreviousQuestions] =
        useState([]);

    return (

        <div className="app-container">

            {/* Hero Section */}

            <div className="hero">

    <h1>
        AI Interview Coach 
    </h1>

    <p>
        Practice smarter.
        Improve faster.
        Get interview ready.
    </p>

    <div className="steps">

        <div className="step">
            📄 Resume
        </div>

        <div className="step">
            🎯 Questions
        </div>

        <div className="step">
            📝 Evaluation
        </div>

        <div className="step">
            🚀 Improvement
        </div>

    </div>

</div>

            {/* Resume Upload */}
<div >
{
    !analysis && (

        <div className="section-card">

            <ResumeUpload
                setAnalysis={setAnalysis}
            />

        </div>

    )
}
</div>

            {/* Resume Analysis */}



            {
    analysis && (

        <div className="section-card">

            <h2>Candidate</h2>

            <div className="candidate-name">
                {analysis.candidate_name}
            </div>

            <h2>
                Recommended Roles
            </h2>

            <div className="role-cards">

                {
                    analysis.recommended_roles.map(
                        (role, index) => (

                            <div
                                key={index}
                                className="role-card"
                            >
                                {role}
                            </div>

                        )
                    )
                }

            </div>

        </div>

    )
}
            {/* Interview */}

            {
                analysis &&
                !evaluation && (

                    <div className="question-card">

                        <InterviewPage
                            analysis={analysis}
                            question={question}
                            setQuestion={setQuestion}
                            evaluation={evaluation}
                            setEvaluation={setEvaluation}
                            previousQuestions={previousQuestions}
                            setPreviousQuestions={setPreviousQuestions}
                        />

  

                    </div>

                    

                )
            }
          

            {/* Evaluation */}



            {
                evaluation && (

                    <div className="section-card">

                        <EvaluationPage
                            evaluation={evaluation}
                            setEvaluation={setEvaluation}
                            setQuestion={setQuestion}
                        />


                    </div>

                )
            }
            </div>

        

    );
}

export default App;