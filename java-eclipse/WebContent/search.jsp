<%@ page language="java" contentType="text/html; charset=UTF-8"
	pageEncoding="UTF-8"%>
<html>
<head>
<title>User Management Application</title>
<link rel="stylesheet"
	href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css"
	crossorigin="anonymous">
</head>
<body>

	<header>
		<nav class="navbar navbar-expand-md navbar-dark"
			style="background-color: #5600bf">
			<ul class="navbar-nav">
				<li><a href="<%=request.getContextPath()%>/article"
					class="nav-link">Articles</a></li>
			</ul>
		</nav>
	</header>
	<br>

	<div class="row">
		<!-- <div class="alert alert-success" *ngIf='message'>{{message}}</div> -->

		<div class="container">
			<h3 class="text-center">List of Articles</h3>
			<hr>
			<br>
        	<div>
           		<input placeholder="search by organization" id="search-input">
          		 <button id="search-btn">Search</button>
        	</div>
			<br>
			<hr>
			<table class="table table-bordered">
				<thead>
					<tr>
						<th>Title</th>
					</tr>
				</thead>
				<tbody>
					<!--   for (Todo todo: todos) {  -->
					<c:forEach var="article" items="${listArticle}">

						<tr>
							<td><c:out value="${article.id}" /></td>
							<td><c:out value="${article.title}" /></td>
							<td><a href="show?source_x=<c:out value='${article.source_x}' />">Edit</a>
								&nbsp;&nbsp;&nbsp; </td>
						</tr>
					</c:forEach>
					<!-- } -->
				</tbody>

			</table>
		</div>
	</div>
</body>
</html>