import { useState } from "react";
import { optimizeResume } from "../api";

export default function ResumeForm({ setResult }: any) {
  const [resume, setResume] = useState("");

  const handleSubmit = async () => {
    const result = await optimizeResume(resume);
    setResult(result);
  };

  return (
    <div style={{ padding: "20px" }}>
      <h2>Paste Resume</h2>
      <textarea
        rows={10}
        style={{ width: "100%" }}
        onChange={(e) => setResume(e.target.value)}
      />
      <button onClick={handleSubmit}>
        Optimize Resume
      </button>
    </div>
  );
}
