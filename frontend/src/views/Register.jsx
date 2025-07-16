import React, { useState } from "react";
import { registerUser } from "../api/auth";
import { useNavigate } from "react-router-dom";

const Register = () => {
  const [formData, setFormData] = useState({ email: "", password: "" });
  const navigate = useNavigate();

  const handleChange = e => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async e => {
    e.preventDefault();
    const result = await registerUser(formData);
    if (result.message === "User registered successfully") {
      navigate("/login");
    } else {
      alert(result.message || "Register failed");
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <h2>Register</h2>
      <input type="email" name="email" placeholder="Email" onChange={handleChange} required />
      <input type="password" name="password" placeholder="Password" onChange={handleChange} required />
      <button type="submit">Create Account</button>
    </form>
  );
};

export default Register;

