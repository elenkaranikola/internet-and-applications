USE InterntAndApplications;
CREATE TABLE authors_bib(
    paper_id VARCHAR(50) NOT NULL,
    bib_name VARCHAR(50),
    first_name VARCHAR(50),
    middle VARCHAR(50),
    last_name VARCHAR(50),
    suffix VARCHAR(50),
    PRIMARY KEY (paper_id,bib_name,last_name),
    FOREIGN KEY (paper_id,bib_name) REFERENCES bib_entries(paper_id,bib_name)
    ON DELETE CASCADE
);
