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