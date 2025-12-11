import React, { useEffect, useState } from "react";
import useGlobalReducer from "../hooks/useGlobalReducer.jsx";
import "../index.css";
// Components
import { LoadingSpinner } from "../components/LoadingSpinner.jsx";
// Services
import { registerUser } from "../services/user.js";


export const Register = () => {
    const { store, dispatch } = useGlobalReducer();
    const [formData, setFormData] = useState({
        email: "",
        password: "",
        confirmPassword: ""
    });

    const [loading, setLoading] = useState(false);
    const [messageState, setMessageState] = useState("");

    const handleSubmit = async (e) => {
        e.preventDefault();
        setLoading(true);

        if (formData.password !== formData.confirmPassword) {
            setMessageState("Los passwords no coinciden.");
            setLoading(false);

            return;
        }

        try {
            const response = await registerUser(formData.email, formData.password, "customer");
            setLoading(false);
            setMessageState("Registro realizado con éxito.");
            // Optionally, redirect to login or home page
        } catch (error) {
            setMessageState(`Error en el registro: ${error.message}`);
            setLoading(false);
        }
    };

    return (
        <div className="text-center">
            <div className="col-span-12">
                <h1 className="text-4xl font-bold mb-3">Register Page</h1>
            </div>
            <form className="max-w-md mx-auto bg-white p-8 rounded shadow-md">
                <div className="mb-4 text-left">
                    <label className="block text-gray-700 mb-2" htmlFor="email">Email:</label>
                    <input
                        type="email"
                        id="email"
                        className="w-full px-3 py-2 border rounded"
                        value={formData.email}
                        onChange={(e) => setFormData({ ...formData, email: e.target.value })}
                    />
                </div>
                <div className="mb-4 text-left">
                    <label className="block text-gray-700 mb-2" htmlFor="password">Password:</label>
                    <input
                        type="password"
                        id="password"
                        className="w-full px-3 py-2 border rounded"
                        value={formData.password}
                        onChange={(e) => setFormData({ ...formData, password: e.target.value })}
                    />
                </div>
                <div className="mb-4 text-left">
                    <label className="block text-gray-700 mb-2" htmlFor="confirmPassword">Confirm Password:</label>
                    <input
                        type="password"
                        id="confirmPassword"
                        className="w-full px-3 py-2 border rounded"
                        value={formData.confirmPassword}
                        onChange={(e) => setFormData({ ...formData, confirmPassword: e.target.value })}
                    />
                </div>
                <button
                    type="submit"
                    className="w-full bg-blue-500 text-white py-2 px-4 rounded hover:bg-blue-600"
                    onClick={handleSubmit}
                >
                    {loading ?
                        <div className="flex justify-center">
                            <LoadingSpinner />
                        </div>
                        : "Regístrate"}
                </button>
                {messageState && <p className="mt-4 text-red-500">{messageState}</p>}
            </form>
        </div>
    );
}