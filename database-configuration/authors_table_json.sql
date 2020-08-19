USE InterntAndApplications;
CREATE TABLE authors(
    paper_id VARCHAR(50) NOT NULL,
    first_name VARCHAR(50),
    middle VARCHAR(50),
    last_name VARCHAR(50),
    suffix VARCHAR(50),
    laboratory VARCHAR(50),
    institutions VARCHAR(50),
    postCode VARCHAR(50),
    settlement VARCHAR(50),
    region VARCHAR(50),
    country VARCHAR(50),
    email VARCHAR(50),
    PRIMARY KEY (paper_id,last_name),
    FOREIGN KEY (paper_id) REFERENCES first_json(paper_id)
);