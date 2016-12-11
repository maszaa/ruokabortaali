$(document).ready(function () {
	function makeUL(array) {
			var list = document.createElement('ul');
			for(var i = 0; i < array.length; i++) {
					var item = document.createElement('li');
					item.appendChild(document.createTextNode(array[i]));
					list.appendChild(item);
			}
			return list;
	}
	
	var d = new Date();
	var date = d.getDate();
	var month = d.getMonth();
	month = month + 1;
	var year = d.getFullYear();
	var paiva = year + '/' + month + '/' + date;
	var url = 'https://ruokabortaali.herokuapp.com/api/' + paiva;
	$.getJSON(url, function (data) {
		console.log(data);
		var menu = {"linjastot" : {}, }
		var items = data.ravintolat[0].linjastot;
		var items2 = data.ravintolat[1].linjastot;
		
		for (var key in items) {
			var array1 = [];
			var obj = items[key];
			document.getElementById('show-data').append(key);
			for (var prop in obj) {
				var content = prop + ": " + obj[prop];
				array1.push(content);
			}
			document.getElementById('show-data').appendChild(makeUL(array1));
		}
		
		for (var key in items2) {
			var array1 = [];
			var obj = items2[key];
			document.getElementById('show-data2').append(key);
			for (var prop in obj) {
				var content = prop + ": " + obj[prop];
				array1.push(content);
			}
			document.getElementById('show-data2').appendChild(makeUL(array1));
		}
	});
});