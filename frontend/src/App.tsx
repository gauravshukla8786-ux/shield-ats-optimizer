import { useState } from "react";
import ResumeForm from "./components/ResumeForm";
import Result from "./components/Result";

function App() {
  const [result, setResult] = useState(null);

  return (
    <>
      <ResumeForm setResult={setResult} />
      <Result result={result} />
    </>
  );
}

export default App;
