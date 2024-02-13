$(document).ready(function(){
function fetch_data(){
	const value = $("INPUT#language_code").val();
	$.ajax({
		url: "https://hellosalut.stefanbohacek.dev/?lang="+value,
		type:'GET',
		success: function(data){
			$("DIV#hello").text(data["hello"]);
		}
	})
}

$("INPUT#btn_translate").click(function(){
	fetch_data();
})

$("INPUT#btn_translate").keydown(function(event){
	if (event.which == 13){
		fetch_data();
	}
})
});
