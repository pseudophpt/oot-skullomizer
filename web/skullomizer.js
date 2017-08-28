var used_skulls_map = Array(100).fill(0);
var skull_numbers = [0, 0, 0, 0, 0];
var amount_obtained = [0, 0, 0, 0, 0];
var bonus_obtained = [0, 0, 0, 0, 0];
var race_started = 0;
var seed = 0;
var bonus = 0;
var skull_limit = 0;
var max_panel_skulls = 0;
var total_skulls = 0;
var total_points = 0;
var lock_out = false;
var swap_out = false;
var bonus_enabled = false;
var countdown = false;
var start = 0;
var starting_time = 0;
var ending_time =  0;
var timer;

function get_skull_number () {
	var skull_no = 100;
	var random = gen_random (0, 100);
	while (used_skulls_map[random] == 1) {
		random = gen_random (0, 100);
	}
	skull_no = random;
	used_skulls_map[random] = 1;
	return skull_no;
}

function get_skull_number_swap () {
	var skull_no = 100;
	var random = gen_random (0, 100);
	while (used_skulls_map[random] == 1) {
		random = gen_random (0, 100);
	}
	skull_no = random;
	return skull_no;
}

function gen_random (start, end) {
	return Math.floor((end-start) * Math.random()) + start;
}


function update_values() {
	document.getElementById("text_1").innerHTML = skull_strings[skull_numbers[0]]; 
	document.getElementById("text_2").innerHTML = skull_strings[skull_numbers[1]]; 
	document.getElementById("text_3").innerHTML = skull_strings[skull_numbers[2]]; 
	document.getElementById("text_4").innerHTML = skull_strings[skull_numbers[3]]; 
	document.getElementById("text_5").innerHTML = skull_strings[skull_numbers[4]]; 

	document.getElementById("num_skulls_1").innerHTML = String(amount_obtained[0]); 
	document.getElementById("num_skulls_2").innerHTML = String(amount_obtained[1]); 
	document.getElementById("num_skulls_3").innerHTML = String(amount_obtained[2]); 
	document.getElementById("num_skulls_4").innerHTML = String(amount_obtained[3]); 
	document.getElementById("num_skulls_5").innerHTML = String(amount_obtained[4]); 
	
	document.getElementById("image_1").innerHTML = '<img src="img/'+String(skull_numbers[0])+'.jpg" style="width:100%">';
	document.getElementById("image_2").innerHTML = '<img src="img/'+String(skull_numbers[1])+'.jpg" style="width:100%">';
	document.getElementById("image_3").innerHTML = '<img src="img/'+String(skull_numbers[2])+'.jpg" style="width:100%">';
	document.getElementById("image_4").innerHTML = '<img src="img/'+String(skull_numbers[3])+'.jpg" style="width:100%">';
	document.getElementById("image_5").innerHTML = '<img src="img/'+String(skull_numbers[4])+'.jpg" style="width:100%">';
	
	document.getElementById("total_skulls_amt").innerHTML = String(total_skulls); 
	document.getElementById("total_points_amt").innerHTML = String(total_points); 

}

function init_skull_states () {
	for (var i = 0; i < 5; i++) {
		if (swap_out) {
			skull_numbers[i] = get_skull_number_swap();
		}
		else {
			skull_numbers[i] = get_skull_number();
		}
	}
	amount_obtained = [0, 0, 0, 0, 0];
	bonus_obtained = [0, 0, 0, 0, 0];
}

function toggle_rules () {
	var rules = document.getElementById("rules-text");
	if (rules.style.display == "none") {
		rules.style.display = "block";
	}
	else {
		rules.style.display = "none";	
	}
}

function done_skull (skull_num) {
	if (race_started) {
		amount_obtained[skull_num]++;
		bonus_obtained[skull_num] = 1;
		if (bonus_enabled) {
			show_checkmark(skull_num);
			check_bonuses();
		}
		total_skulls ++;
		total_points ++;
		if (amount_obtained[skull_num] >= max_panel_skulls) {
			hide_panel(skull_num);
		}
		else if (swap_out) {
			used_skulls_map[skull_numbers[skull_num]] = 1;
			for (var i = 0; i < 5; i++) {
				skull_numbers[i] = get_skull_number_swap();
			}
		}
		else {
			skull_numbers[skull_num] = get_skull_number();
		}
		update_values();
		
	}
}

function elim_skull (skull_num) {
	if (race_started & lock_out) {
		if (amount_obtained[skull_num] >= max_panel_skulls) {
			hide_panel(skull_num);
		}
		else if (swap_out) {
			for (var i = 0; i < 5; i++) {
				skull_numbers[i] = get_skull_number_swap();
			}
		}
		else {
			skull_numbers[skull_num] = get_skull_number();
		}
		update_values();
	}
	return false;
}

function check_bonuses () {
	if (bonus_obtained[0] + bonus_obtained[1] + bonus_obtained[2] + bonus_obtained[3] + bonus_obtained[4] == 5) {
		hide_all_checkmarks();
		for (var i = 0; i < 5; i++) {
			bonus_obtained[i] = 0;
		}
		total_points += bonus;
	} 
}

function hide_panel (skull_num) {
	switch (skull_num) {
		case 0:
			document.getElementById("panel_1").style.visibility = "hidden";
			break;
		case 1:
			document.getElementById("panel_2").style.visibility = "hidden";
			break;
		case 2:
			document.getElementById("panel_3").style.visibility = "hidden";
			break;
		case 3:
			document.getElementById("panel_4").style.visibility = "hidden";
			break;
		case 4:
			document.getElementById("panel_5").style.visibility = "hidden";
	}
}

function show_checkmark (skull_num) {
	switch (skull_num) {
		case 0:
			document.getElementById("bonus_icon_1").style.visibility = "visible";
			break;
		case 1:
			document.getElementById("bonus_icon_2").style.visibility = "visible";
			break;
		case 2:
			document.getElementById("bonus_icon_3").style.visibility = "visible";
			break;
		case 3:
			document.getElementById("bonus_icon_4").style.visibility = "visible";
			break;
		case 4:
			document.getElementById("bonus_icon_5").style.visibility = "visible";
	}
}

function show_all_panels () {
	document.getElementById("panel_1").style.visibility = "visible";
	document.getElementById("panel_2").style.visibility = "visible";
	document.getElementById("panel_3").style.visibility = "visible";
	document.getElementById("panel_4").style.visibility = "visible";
	document.getElementById("panel_5").style.visibility = "visible";
}

function hide_all_checkmarks () {
	document.getElementById("bonus_icon_1").style.visibility = "hidden";
	document.getElementById("bonus_icon_2").style.visibility = "hidden";
	document.getElementById("bonus_icon_3").style.visibility = "hidden";
	document.getElementById("bonus_icon_4").style.visibility = "hidden";
	document.getElementById("bonus_icon_5").style.visibility = "hidden";
}

function start_timer () {
	starting_time = new Date().getTime();
	window.clearInterval(timer);
	if (countdown_enabled) {
		timer = window.setInterval(update_countdown, 250);
		ending_time = starting_time + (countdown * 60000);
	}
	else {
		timer = window.setInterval(update_race, 250);
	}
}

function start_race () {
	race_started = 1;
	seed = document.getElementById("seed").value;
	Math.seedrandom(seed);
	bonus = Number(document.getElementById("bonus").value);
	skull_limit = Number(document.getElementById("skulls").value);
	countdown = Number(document.getElementById("countdown").value);
	max_panel_skulls = Math.ceil(skull_limit / 5);
	bonus_enabled = document.getElementById("bonus_enabled").checked;
	countdown_enabled = document.getElementById("countdown_enabled").checked;
	lock_out = document.getElementById("lockout").checked;
	swap_out = document.getElementById("swap").checked;
	used_skulls_map = Array(100).fill(0);
	total_skulls = 0;
	total_points = 0;
	show_all_panels();
	init_skull_states();
	hide_all_checkmarks();
	update_values();
	start_timer();
}


function update_countdown () {	
	current_time = ending_time - new Date().getTime();
	if (current_time <= 0) {
		window.clearInterval(timer);
		alert("Countdown complete! You finished with "+total_skulls+" skulltulas and "+total_points+" points in "+countdown+" minutes!");
		race_started = 0;
	}
	else {
		var countdown_sec = Math.floor(current_time / 1000) % 60;
		var countdown_min = Math.floor(current_time / 60000) % 60;
		var countdown_hr = Math.floor(current_time / 3600000) % 24;
		document.getElementById("timer").innerHTML = String(countdown_hr) + "h" + String(countdown_min) + "m" + String(countdown_sec) + "s";
	}
	
}
function update_race () {
	var current_time = new Date().getTime() - starting_time;
	var countdown_sec = Math.floor(current_time / 1000) % 60;
	var countdown_min = Math.floor(current_time / 60000) % 60;
	var countdown_hr = Math.floor(current_time / 3600000) % 24;
	document.getElementById("timer").innerHTML = String(countdown_hr) + "h" + String(countdown_min) + "m" + String(countdown_sec) + "s";
	if (total_skulls >= skull_limit) {
		window.clearInterval(timer);
		race_started = 0;
		alert("Race complete! You finished a race of "+skull_limit+" skulltulas with "+total_points+" points in "+String(countdown_hr) + "h" + String(countdown_min) + "m" + String(countdown_sec) + "s!");
	}
}
