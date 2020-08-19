USE InterntAndApplications;
CREATE TABLE back_matter(
    paper_id VARCHAR(50) NOT NULL,
    spot INT,
    body LONGTEXT,
    section VARCHAR(50),
    PRIMARY KEY (paper_id,spot),
    FOREIGN KEY (paper_id) REFERENCES first_json(paper_id)
);