import { useEffect, useState } from "react";
import {
    LineChart,
    Line,
    XAxis,
    YAxis,
    Tooltip,
    CartesianGrid,
    ResponsiveContainer
} from "recharts";

import {
    getProgress,
    getHistory
}
from "../services/api";

function Dashboard() {

    const [progress, setProgress] =
        useState(null);

    const [history, setHistory] =
        useState([]);

    useEffect(() => {

    loadDashboard();

}, []);

const loadDashboard = async () => {

    try {

        const userId = 1;

        const progressData =
            await getProgress(userId);

        const historyData =
            await getHistory(userId);

        setProgress(progressData);

        setHistory(historyData);

    }

    catch(error) {

        console.log(error);

    }

};
    const chartData = history.map((item, index) => ({
        interview: index + 1,
        score: item.score
    }));

    
    return (

        <div
            className="dashboard"
        >

            <h1>
                Dashboard
            </h1>

            {progress && (
                <>
                    <div className="stats-grid">

                        <div className="stat-card">

                            <h3>Total Interviews</h3>

                            <p>{progress.total_interviews}</p>

                        </div>

                        <div className="stat-card">

                            <h3>Average Score</h3>

                            <p>{progress.average_score}</p>

                        </div>

                        <div className="stat-card">

                            <h3>Best Score</h3>

                            <p>{progress.best_score}</p>

                        </div>

                        <div className="stat-card">

                            <h3>Latest Score</h3>

                            <p>{progress.latest_score}</p>

                        </div>

                    </div>

                    <div className="chart-card">

                        <h2>Interview Progress</h2>

                        <ResponsiveContainer width="100%" height={300}>

                            <LineChart data={chartData}>

                                <CartesianGrid strokeDasharray="3 3" />

                                <XAxis dataKey="interview" />

                                <YAxis />

                                <Tooltip />

                                <Line
                                    type="monotone"
                                    dataKey="score"
                                    stroke="#8b5cf6"
                                    strokeWidth={3}
                                />

                            </LineChart>

                        </ResponsiveContainer>

                    </div>
                </>
            )}

           
            <h2>
                Interview History
            </h2>

            <table>

                <thead>

                    <tr>

                        <th>
                            Role
                        </th>

                        <th>
                            Type
                        </th>

                        <th>
                            Score
                        </th>

                    </tr>

                </thead>

                <tbody>

                    {
                        history.map(
                            interview => (

                                <tr
                                    key={
                                        interview.id
                                    }
                                >

                                    <td>
                                        {
                                            interview.role
                                        }
                                    </td>

                                    <td>
                                        {
                                            interview.interview_type
                                        }
                                    </td>

                                    <td>
                                        {
                                            interview.score
                                        }
                                    </td>

                                </tr>

                            )
                        )
                    }

                </tbody>

            </table>

        </div>

    );
}

export default Dashboard;