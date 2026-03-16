import { useState } from "react";
import "./App.css";

function App() {
  const [actor, setActor] = useState("");
  const [baconDistance, setBaconDistance] = useState("");
  const [errorMessage, setErrorMessage] = useState("");

  const calculateBaconDistance = async () => {
    const response = await fetch(`http://localhost:5000/calc/${actor}`);
    if (response.ok) {
      const result = await response.text();
      setBaconDistance(result);
      setErrorMessage("");
    }
    else {
      const result = await response.json();
      setBaconDistance("");
      setErrorMessage(result["error"]);
    }
  }

  return (
    <div>
      <input type="text" onChange={e => setActor(e.target.value)}></input>
      <button onClick={() => {if (actor.length > 0) {calculateBaconDistance()}}}>Calculate Bacon Distance</button>
      <p>{errorMessage ? errorMessage : baconDistance}</p>
    </div>
  )
}

export default App;
