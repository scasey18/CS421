
function showForm(){
	document.getElementById("UpdateForm").hidden = false;
}

function closeForm() {
	document.getElementById("UpdateForm").hidden = true;
}

function updateStudent(row){
	document.getElementsByName("id")[0].value = document.getElementById("id"+row).textContent;
	document.getElementsByName("name")[0].value = document.getElementById("name"+row).textContent;
	document.getElementsByName("grade")[0].value = document.getElementById("grade"+row).textContent;
	showForm();
}

