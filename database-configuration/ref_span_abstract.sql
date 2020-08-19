USE InterntAndApplications;
CREATE TABLE ref_span_abstract(
    paper_id VARCHAR(50) NOT NULL,
    paragraph_number INT,
    start_text INT,
    end_text INT,
    text_ref VARCHAR(50),
    ref_id VARCHAR(50),
    PRIMARY KEY (paper_id,paragraph_number,ref_id),
    FOREIGN KEY (paper_id,paragraph_number) REFERENCES abstract(paper_id,spot)
    ON DELETE CASCADE
);