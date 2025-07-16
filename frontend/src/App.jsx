import React from 'react'
import { Routes, Route } from 'react-router-dom'
import Navbar from './components/Navbar.jsx'
import Login from './views/Login.jsx'
import Register from './views/Register.jsx'
import Upload from './views/Upload.jsx'
import Reports from './views/Reports.jsx'

const App = () => {
  return (
    <>
      <Navbar />
      <div className="container mt-4">
        <Routes>
          <Route path="/" element={<Upload />} />
          <Route path="/login" element={<Login />} />
          <Route path="/register" element={<Register />} />
          <Route path="/reports" element={<Reports />} />
        </Routes>
      </div>
    </>
  )
}

export default App
