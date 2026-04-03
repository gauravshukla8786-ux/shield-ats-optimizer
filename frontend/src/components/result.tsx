export default function Result({ result }: any) {
  if (!result) return null;

  return (
    <div style={{ padding: "20px" }}>
      <h3>ATS Score: {result.ats_score}</h3>
      <pre>{result.optimized_resume}</pre>
    </div>
  );
}
