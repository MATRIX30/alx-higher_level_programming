$(document).ready(function(){
	$("INPUT#btn_translate").click(function(){
		const lang_code = $("INPUT#language_code").val();
		const url = "https://hellosalut.stefanbohacek.dev/?lang="+lang_code
		$.ajax({
			url:url,
			type: 'GET',
			dataType:"json",
			success:function(data){
				$("DIV#hello").text(data["hello"]);
			}
		})
	})
})

