package net.usermanagment.model;

public class Article {
	private String id;
	private String title;
	private String source_x;
	
	public Article(String title, String source_x) {
		super();
		this.title = title;
		this.source_x = source_x;
	}

	
	public Article(String id, String title, String source_x) {
		super();
		this.id = id;
		this.title = title;
		this.source_x = source_x;
	}
	
	public String getId() {
		return id;
	}
	public void setId(String id) {
		this.id = id;
	}
	public String getTitle() {
		return title;
	}
	public void setTitle(String title) {
		this.title = title;
	}
	public String getSource_x() {
		return source_x;
	}
	public void setEmail(String source_x) {
		this.source_x = source_x;
	}
}
