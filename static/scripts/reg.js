$(document).ready(function(){
	$("#mobileReg").click(function(){
		$(this).siblings().removeAttr("class");
		$(this).toggleClass("active");
		$("#phoneWrap").css({"display":"block"});
		//$("#email").val("");
		$("#emailWrap").css({"display":"none"});
	});
	$("#emailReg").click(function(){
		$(this).siblings().removeAttr("class");
		$(this).toggleClass("active");
		$("#phoneWrap").css({"display":"none"});
		//$("#phone").val("");
		$("#emailWrap").css({"display":"block"});
	});

	<!--用户名验证 -->
	$("#username").focus(function(){
		$("#username_Tip").removeAttr("class");
		$("#username_Tip").toggleClass("action");
		$("#username_Tip").children().html("1-20位,注册成功后用户名不能修改");
	});

	$("#username").blur(function(){
		vfname();
	});

	<!--手机号验证 -->
	$("#phone").focus(function(){
		$("#phone_Tip").removeAttr("class");
		$("#phone_Tip").toggleClass("action");
		$("#phone_Tip").children().html("请输入您的手机号码");
	});

	$("#phone").blur(function(){
		vfphone();
	});

	<!--邮箱验证 -->
	$("#email").focus(function(){
		$("#email_Tip").removeAttr("class");
		$("#email_Tip").toggleClass("action");
		$("#email_Tip").children().html("请输入您的邮箱");
	});

	$("#email").blur(function(){
		vfemail();
	});

	<!--密码验证 -->
	$("#password").focus(function(){
		$("#password_Tip").removeAttr("class");
		$("#password_Tip").toggleClass("action");
		$("#password_Tip").children().html("密码长度6-16位");
	});

	$("#password").blur(function(){
		vfpassword();
	});

	$("#cpassword").focus(function(){
		$("#cpassword_Tip").removeAttr("class");
		$("#cpassword_Tip").toggleClass("action");
		$("#cpassword_Tip").children().html("请再次输入您的密码");
	});

	$("#cpassword").blur(function(){
		vfcpassword();
	});

	$("#btnNext").click(function(){
		if($("#mobileReg").hasClass("active")){
			$("#email").val("");
			$("#reg-form").submit();
		}else if($("#emailReg").hasClass("active")){
			$("#phone").val("");
			$("#reg-form").submit();
		}	
	});

	$("#info-btn").click(function(){
		$("#reg-user-info-form").submit();
	});
});

function vfname(){
	var text = $("#username").val();

	//检查用户名长度
	if(!(text.length>=1 && text.length<=20)){
		change_username({'result':false,'wrong_msg':"用户名无效"});
		return false;
	}

	$.ajax({
		url:"/check-user",
		type:"post",
		dataType:"json",
		data:JSON.stringify({
			'username':text
		}),
		contentType:'application/json;charset=UTF-8',
		success:function (data) {
			//alert(JSON.stringify(data));
			if(data['msg']){
				change_username({'result':true});
			}else{
				change_username({'result':false,'wrong_msg':"用户名已存在"});
			}
		},
		error:function (data) {
			//alert(JSON.stringify(data));
			change_username({'result':false,'wrong_msg':"用户名无效"});
		},
	});
	return true;
}

function change_username(data){
	if(data["result"]){
		$("#username_Tip").removeAttr("class");
		$("#username_Tip").toggleClass("success");
		$("#username_Tip").children().html("");
	}else{
		$("#username_Tip").removeAttr("class");
		$("#username_Tip").toggleClass("wrong");
		$("#username_Tip").children().html(data['wrong_msg']);
	}
}

function vfphone(){
	var text = $("#phone").val();
	var result = true;
	
	if(text.length!=11){
		result = false;
	} else if(text.search(/^[0-9]+$/)==-1){
		result = false;
	} 

	if(!result){
		change_phone({'result':false,'wrong_msg':"请输入正确的手机号码"});
		return result;
	}

	$.ajax({
		url:"/check-user",
		type:"post",
		dataType:"json",
		data:JSON.stringify({
			'phone':text
		}),
		contentType:'application/json;charset=UTF-8',
		success:function (data) {
			//alert(JSON.stringify(data));
			if(data['msg']){
				change_phone({'result':true});
			}else{
				change_phone({'result':false,'wrong_msg':"该手机号码已注册"});
			}
		},
		error:function (data) {
			alert(JSON.stringify(data));
			change_phone({'result':false,'wrong_msg':"请输入正确的手机号码"});
		},
	});
	return true;
}

function change_phone(data){
	if(data["result"]){
		$("#phone_Tip").removeAttr("class");
		$("#phone_Tip").toggleClass("success");
		$("#phone_Tip").children().html("");
	}else{
		$("#phone_Tip").removeAttr("class");
		$("#phone_Tip").toggleClass("wrong");
		$("#phone_Tip").children().html(data['wrong_msg']);
	}
}

function vfemail(){
	var text = $("#email").val();
	if (text.search(/^[_/.a-z0-9]+@[a-z0-9]+[/.][a-z0-9]{2,}$/i)==-1) {
		change_email({'result':false,'wrong_msg':"邮箱输入有误"});
		return false;
	} 

	$.ajax({
		url:"/check-user",
		type:"post",
		dataType:"json",
		data:JSON.stringify({
			'email':text
		}),
		contentType:'application/json;charset=UTF-8',
		success:function (data) {
			//alert(JSON.stringify(data));
			if(data['msg']){
				change_email({'result':true});
			}else{
				change_email({'result':false,'wrong_msg':"该邮箱已注册"});
			}
		},
		error:function (data) {
			//alert(JSON.stringify(data));
			change_email({'result':false,'wrong_msg':"邮箱输入有误"});
		},
	});
	return true;
}

function change_email(data){
	if(data["result"]){
		$("#email_Tip").removeAttr("class");
		$("#email_Tip").toggleClass("success");
		$("#email_Tip").children().html("");
	}else{
		$("#email_Tip").removeAttr("class");
		$("#email_Tip").toggleClass("wrong");
		$("#email_Tip").children().html(data['wrong_msg']);
	}
}

function vfpassword(){
	var text = $("#password").val();
	var result = false;
	if(text.length>=6 && text.length<=16)
		result=true;
	else
		result=false;
	if (result) {
		$("#password_Tip").removeAttr("class");
		$("#password_Tip").toggleClass("success");
		$("#password_Tip").children().html("");
	}else{
		$("#password_Tip").removeAttr("class");
		$("#password_Tip").toggleClass("wrong");
		$("#password_Tip").children().html("您输入的密码有误");
	};
	return result;
}

function vfcpassword(){
	var text = $("#cpassword").val();
	var passtext = $("#password").val();
	var result = false;
	if(text==passtext)
		result=true;
	else
		result=false;
	if (result) {
		$("#cpassword_Tip").removeAttr("class");
		$("#cpassword_Tip").toggleClass("success");
		$("#cpassword_Tip").children().html("");
	}else{
		$("#cpassword_Tip").removeAttr("class");
		$("#cpassword_Tip").toggleClass("wrong");
		$("#cpassword_Tip").children().html("两次输入的密码不一致");
	};
	return result;
}