CREATE TABLE IF NOT EXISTS resumes (
    id SERIAL PRIMARY KEY,
    original_resume TEXT NOT NULL,
    optimized_resume TEXT NOT NULL,
    ats_score FLOAT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
