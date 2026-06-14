import axios from "axios";

const API = axios.create({
    baseURL: "http://127.0.0.1:8000"
});

export const uploadResume = async (file) => {

    const formData = new FormData();

    formData.append("file", file);

    const response = await API.post(
        "/resume/upload",
        formData
    );

    return response.data;
};

export const generateQuestion =
async (
    analysis,
    role,
    interviewType,
    previousQuestions
) => {

    const response =
        await API.post(
            "/interview/question",
            {
                analysis,
                role,
                interview_type: interviewType,
                previous_questions: previousQuestions
            }
        );

    return response.data;
};

export const evaluateAnswer = async (
    questionData,
    userAnswer
) => {

    const response = await API.post(
        "/interview/evaluate",
        {
            question_data: questionData,
            user_answer: userAnswer
        }
    );

    return response.data;
};