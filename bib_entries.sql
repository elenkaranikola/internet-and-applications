USE InterntAndApplications;
CREATE TABLE bib_entries(
    paper_id VARCHAR(50) NOT NULL,
    bib_name VARCHAR(50),
    ref_id VARCHAR(50),
    title TEXT,
    ref_year TEXT,
    venue VARCHAR(50),
    volume VARCHAR(50),
    issn VARCHAR(50),
    pages VARCHAR(50),
    other_ids VARCHAR(50),
    PRIMARY KEY (paper_id,bib_name),
    FOREIGN KEY (paper_id) REFERENCES first_json(paper_id)
    ON DELETE CASCADE
);
