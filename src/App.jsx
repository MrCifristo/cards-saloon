import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'
import Home from './pages/Home'
import Lobby from './pages/Lobby'
import GameRoom from './pages/GameRoom'
import LoginForm from './components/auth/LoginForm'

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/login" element={<LoginForm />} />
        <Route path="/lobby" element={<Lobby />} />
        <Route path="/room/:roomId" element={<GameRoom />} />
      </Routes>
    </Router>
  )
}

export default App