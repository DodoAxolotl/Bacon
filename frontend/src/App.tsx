import { useState } from "react";
import "./App.css";

function App() {
  const [actor, setActor] = useState("");
  const [baconDistance, setBaconDistance] = useState("");
  const [errorMessage, setErrorMessage] = useState("");

  const calculateBaconDistance = async () => {
    try {  
      const response = await fetch(`http://localhost:5000/calc/${actor}`);
      const result = await response.text();
      setBaconDistance(response.ok ? result : "");
      setErrorMessage(response.ok ? "" : result);
    } catch (_) {
      setBaconDistance("");
      setErrorMessage("Could not fetch the required data");
    }
  }

  return (
    <div>
      <input type="text" onChange={e => setActor(e.target.value)}></input>
      <button disabled={actor.length === 0} onClick={calculateBaconDistance}>Calculate Bacon Distance</button>
      <p>{errorMessage ? errorMessage : baconDistance}</p>
    </div>
  )
}

export default App;
