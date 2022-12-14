import { BrowserRouter as Router, Routes, Route } from "react-router-dom"
import { Container } from 'react-bootstrap'
import Signup from './Signup'
import Login from './Login'
import { AuthProvider } from "../Context/AuthContext";

function App() {
  return (
    <Container>
      <Router>
        <AuthProvider>
          <Routes>
            <Route path="/signup" element={<Signup />} />
            <Route path="/login" element={<Login />} />
          </Routes>
        </AuthProvider>
      </Router>
    </Container>
  );
}

export default App;
