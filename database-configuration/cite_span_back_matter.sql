USE InterntAndApplications;
CREATE TABLE cite_span_back_matter(
    paper_id VARCHAR(50) NOT NULL,
    paragraph_number INT,
    start_text INT,
    end_text INT,
    text_span VARCHAR(50),
    ref_id VARCHAR(50),
    PRIMARY KEY (paper_id,paragraph_number,ref_id),
    FOREIGN KEY (paper_id,paragraph_number) REFERENCES back_matter(paper_id,spot)
    ON DELETE CASCADE
);