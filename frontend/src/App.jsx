import "./App.css";
import { Routes, Route } from "react-router-dom";
import Dashboard from "./pages/Dashboard";
import HomePage from "./pages/HomePage";

function App() {

    return (

        <Routes>

            <Route
                path="/"
                element={
                    <HomePage />
                }
            />

            <Route
                path="/dashboard"
                element={
                    <Dashboard />
                }
            />

        </Routes>

    );
}

export default App;