// src/api/auth.js
const API_URL = "http://localhost:5000"; // o cambia al dominio de tu backend si ya está desplegado

export const registerUser = async (userData) => {
  const response = await fetch(`${API_URL}/api/register`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(userData),
  });
  return response.json();
};

export const loginUser = async (credentials) => {
  const response = await fetch(`${API_URL}/api/login`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(credentials),
  });
  return response.json();
};
