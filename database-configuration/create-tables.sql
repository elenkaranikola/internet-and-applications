USE InterntAndApplications;
CREATE TABLE general(
	cord_uid VARCHAR(20) NOT NULL,
    sha TEXT,
    source_x VARCHAR(20),
    title TEXT,
    doi TEXT,
    pmcid VARCHAR(50),
    pubmed_id INT,
    license VARCHAR(20),
    abstract LONGTEXT,
    publish_time DATE,
    authors TEXT,
    journal TEXT,
    mag_id CHAR,
    who_covidence_id CHAR,
    arxiv_id CHAR,
    pdf_json_files TEXT,
    pmc_json_files TEXT,
    url TEXT,
    s2_id TEXT,
    PRIMARY KEY (cord_uid)
);

CREATE TABLE first_json(
    paper_id VARCHAR(50) NOT NULL,
    title TEXT,
    PRIMARY KEY (paper_id)
);

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

CREATE TABLE abstract(
    paper_id VARCHAR(50) NOT NULL,
    spot INT,
    body LONGTEXT,
    section VARCHAR(50),
    PRIMARY KEY (paper_id,spot),
    FOREIGN KEY (paper_id) REFERENCES first_json(paper_id)
);

CREATE TABLE cite_span_abstract(
    paper_id VARCHAR(50) NOT NULL,
    paragraph_number INT,
    start_text INT,
    end_text INT,
    text_span VARCHAR(50),
    ref_id VARCHAR(50),
    PRIMARY KEY (paper_id,paragraph_number,ref_id),
    FOREIGN KEY (paper_id,paragraph_number) REFERENCES abstract(paper_id,spot)
    ON DELETE CASCADE
);

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

CREATE TABLE body_text(
    paper_id VARCHAR(50) NOT NULL,
    spot INT,
    body LONGTEXT,
    section VARCHAR(50),
    PRIMARY KEY (paper_id,spot),
    FOREIGN KEY (paper_id) REFERENCES first_json(paper_id)
);

CREATE TABLE cite_span(
    paper_id VARCHAR(50) NOT NULL,
    paragraph_number INT,
    start_text INT,
    end_text INT,
    text_span VARCHAR(50),
    ref_id VARCHAR(50),
    PRIMARY KEY (paper_id,paragraph_number,ref_id),
    FOREIGN KEY (paper_id,paragraph_number) REFERENCES body_text(paper_id,spot)
);

CREATE TABLE ref_span(
    paper_id VARCHAR(50) NOT NULL,
    paragraph_number INT,
    start_text INT,
    end_text INT,
    text_ref VARCHAR(50),
    ref_id VARCHAR(50),
    PRIMARY KEY (paper_id,paragraph_number,ref_id),
    FOREIGN KEY (paper_id,paragraph_number) REFERENCES body_text(paper_id,spot)
);

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

CREATE TABLE back_matter(
    paper_id VARCHAR(50) NOT NULL,
    spot INT,
    body LONGTEXT,
    section VARCHAR(50),
    PRIMARY KEY (paper_id,spot),
    FOREIGN KEY (paper_id) REFERENCES first_json(paper_id)
);

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

CREATE TABLE ref_span_back_matter(
    paper_id VARCHAR(50) NOT NULL,
    paragraph_number INT,
    start_text INT,
    end_text INT,
    text_ref VARCHAR(50),
    ref_id VARCHAR(50),
    PRIMARY KEY (paper_id,paragraph_number,ref_id),
    FOREIGN KEY (paper_id,paragraph_number) REFERENCES back_matter(paper_id,spot)
    ON DELETE CASCADE
);
