$("body").on("click",".items ul>li>.quantity>a,.ct .quantity>a",function(){
	var q = ''
	var iid = $(this).parent().parent().attr("data");
	if ($(this).attr('class') == 'plus'){
		$(this).prev("input").val(parseInt($(this).prev("input").val())+1);
		q = $(this).prev("input").val()
		$.get("/cart/update/",{ id : iid, quantity:q }, function(data){
			$(".total").text('¥ '+parseFloat(data.total).toFixed(2));
			$("tr[data="+data.id+"] .price").text('¥ '+parseFloat(data.price).toFixed(2));
			$(".cart>.items>ul>li[data="+data.id+"] .price").text('¥ '+parseFloat(data.price).toFixed(2));
	});
	}
	else{
		if (parseInt($(this).next("input").val())>1){
			$(this).next("input").val(parseInt($(this).next("input").val())-1);
			q = $(this).next("input").val()
			$.get("/cart/update/",{ id : iid, quantity:q }, function(data){
				$(".total").text('¥ '+parseFloat(data.total).toFixed(2));
				$("tr[data="+data.id+"] .price").text('¥ '+parseFloat(data.price).toFixed(2));
				$(".cart>.items>ul>li[data="+data.id+"] .price").text('¥ '+parseFloat(data.price).toFixed(2));
			});
		}
	}
});

$(".thumb>.btn>a,.rank>ul>li>a").click(function(){
	var a = $(this)
	$.getJSON("/cart/add/",{ iid: a.attr("data"), cid: $(".cart").attr("id") }, function(data){
		if (data.status == '0'){
			$(".cart>.items>ul>label").remove();

			var li = "<li data="+data.id+">"
			li+="<div class='name'>"+data.name+"</div>";
			li+="<div class='quantity'>";
			li+="<a href='javascript:void(0)' class='minus'>-</a>";
			li+="<input type='text' value="+data.quantity+" readonly='readonly' />";
			li+="<a href='javascript:void(0)' class='plus'>+</a>";
			li+="</div>";
			li+="<div class='price'>¥ "+parseFloat(data.price).toFixed(2)+"</div>";
			li+="</li>"
			$(".cart>.items>ul").append(li);
		}
		else{

			$('.cart>.items>ul>li[data='+data.id+']>.quantity>input').val(data.quantity);
		}
		$(".count").text(data.count);
		$(".total").text("¥ "+parseFloat(data.total).toFixed(2));
	});
});

$(".items ul>li>span>input").attr("readonly","readonly");



$(".ct .delete").click(function(){
	$.get("/cart/delete/",{ id:$(this).attr("data") },function(data){
		$('.ct tr[data='+data.id+']').fadeOut("normal",function(){
			$(this).remove()
		});
		$(".count").text(data.count);
		$(".total").text("￥"+parseFloat(data.total).toFixed(2));
	});
});

$(".submit").click(function(){
	if(confirm("请确认您的订单，为了不打扰您的游戏时间，请提前准备好餐费，谢谢~"))
	$("form").submit();
});