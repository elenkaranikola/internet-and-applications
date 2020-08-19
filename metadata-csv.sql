USE InterntAndApplications;
CREATE TABLE general(
	cord_uid VARCHAR(20) NOT NULL,
    sha TEXT,
    source_x VARCHAR(20),
    title TEXT,
    doi TEXT,
    pmcid VARCHAR(50),
    pubmed_id INT,
    licence VARCHAR(20),
    abstract TEXT,
    publish_time DATE,
    authors TEXT,
    journal VARCHAR(50),
    pdf_jason_files TEXT,
    pmc_jsaon_files TEXT,
    url TEXT,
    PRIMARY KEY (cord_uid)
);
