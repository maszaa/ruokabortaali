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
	
	$.getJSON('https://ruokabortaali.herokuapp.com/api/2016/12/12', function (data) {
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