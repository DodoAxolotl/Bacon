import { useState } from "react";
import "./App.css";

function App() {
  const [actor, setActor] = useState("");
  const [baconDistance, setBaconDistance] = useState("");

  const calculateBaconDistance = async () => {
    const response = await fetch(`http://localhost:5173/${actor}`);
    const result = await response.text();
    setBaconDistance(result);
  }

  return (
    <div>
      <input type="text" onChange={e => setActor(e.target.value)}></input>
      <button onClick={calculateBaconDistance}>Calculate Bacon Distance</button>
      <p>{baconDistance}</p>
    </div>
  )
}

export default App;
