$(function() {
	//规则库
	var rule_list = [];

	$.get("/date",function(data){
		result = data.split(",");
		for (var i = 0;i < result.length;i++){
			result[i] = result[i].replace("[","");
			result[i] = result[i].replace("'","");
			result[i] = result[i].replace("'","");
			result[i] = result[i].replace(" ","");
			result[i] = result[i].replace("]","");
			result[i] = result[i].split("、");

			rule_list[i] = result[i];
		}
	});

	//判断输入，根据输入再输出结果
	$('#submit-btn').on('click',function() {
		$('#result').html('');
		//获取当前已知的动物特征
		var cur_true = [];
		for (var i = 0;i < 24;i++) {
			var checkbox = $('.checkbox'+i);
			if (checkbox.is(':checked')) {
				cur_true.push(checkbox.val());
			}


		//待测试规则表
		var wait_list = [];
		var if_first_period = true;
		reasoningPeriod(cur_true,rule_list,[]);
		 
		function reasoningPeriod(cur_true,rule_list,wait_list) {
			var par_cur_true = cur_true,
				par_cur_true_length = par_cur_true.length;
			var rule_list_length = rule_list.length;
			for (var i = 0;i < rule_list_length;i++) {
				var cur_rule = rule_list[i],
					length = cur_rule.length;

				var fix_count = 0;
				var if_confilct = false;
				for (var j = 0;j < length - 1;j++) {
					for (var k = 0;k < par_cur_true_length;k++) {
						if (cur_rule[j] == cur_true[k]) {
							fix_count++;
						}
					}
				}
				if (fix_count === length-1) {
					cur_true.push(cur_rule[length - 1]);
				} else {
					wait_list.push(cur_rule);
				}
			}

			var child_cur_true_lenght = cur_true.length;
			console.log(cur_true);
				
			if((child_cur_true_lenght == par_cur_true_length) || !wait_list.length) {
				if (cur_true[child_cur_true_lenght-1] != ""){
				// if (cur_true[child_cur_true_lenght-1] == '金钱豹' || cur_true[child_cur_true_lenght-1] == '虎' || cur_true[child_cur_true_lenght-1] == '长颈鹿' || cur_true[child_cur_true_lenght-1] == '斑马' || cur_true[child_cur_true_lenght-1] == '鸵鸟' || cur_true[child_cur_true_lenght-1] == '企鹅' || cur_true[child_cur_true_lenght-1] == '信天翁') {
					$('#result').html(cur_true[child_cur_true_lenght-1]);
				} else {
					$('#result').html('请输入再详细点的信息');
				}
				return false;
			} else {
				reasoningPeriod(cur_true,wait_list,[]);
			}
		}
	}

		$("#flip").click(function(){
	    	$("#panel").slideToggle("slow");
	  	})
	})
})