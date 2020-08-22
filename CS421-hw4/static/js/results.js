
function showForm(){
	document.getElementById("UpdateForm").hidden = false;
}

function closeForm() {
	document.getElementById("UpdateForm").hidden = true;
}

function updateRecord(row){
	document.getElementsByName("id")[0].value = document.getElementById("id"+row).textContent;
	document.getElementsByName("name")[0].value = document.getElementById("name"+row).textContent;
	document.getElementsByName("email")[0].value = document.getElementById("email"+row).textContent;
	document.getElementsByName("phonenum")[0].value = document.getElementById("phonenum"+row).textContent;
	document.getElementsByName("address")[0].value = document.getElementById("address"+row).textContent;
	showForm();
}

