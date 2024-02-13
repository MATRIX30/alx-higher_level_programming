$.get("https://swapi-api.alx-tools.com/api/people/5/?format=json", function(data, statusCode, xhr){
	$("DIV#character").text(data["name"]);
});
