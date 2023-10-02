import { useAuth } from "./contexts/AuthContext";

function App() {
  const {currentUser, register, login, logout} = useAuth()

  return (
    <div className="App">
      {currentUser}
      <button onClick={(e) => {
        e.preventDefault()
        register("cc@c.com", "ccc")
      }}>register</button>
      <button onClick={(e) => {
        e.preventDefault()
        login("cc@c.com", "ccc")
      }}>login</button>
      <button onClick={(e) => {
        e.preventDefault()
        logout()
      }}>logout</button>
    </div>
  );
}

export default App;
