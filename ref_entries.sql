USE InterntAndApplications;
CREATE TABLE ref_entries(
    paper_id VARCHAR(50) NOT NULL,
    ref_name VARCHAR(50),
    ref_text TEXT,
    latex TEXT,
    ref_type VARCHAR(50),
    PRIMARY KEY (paper_id,ref_name),
    FOREIGN KEY (paper_id) REFERENCES first_json(paper_id)
    ON DELETE CASCADE
);