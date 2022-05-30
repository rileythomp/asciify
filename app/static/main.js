function uploadImage(input) {
	asciiart = document.getElementById('asciiart');
	asciiart.style.fontFamily = 'Courier';
    let file = input.files[0];
    if (file == undefined || file == null) {
		asciiart.style.fontSize = '1em';
		asciiart.style.color = 'Black';
		asciiart.style.backgroundColor = 'White';
        asciiart.innerText = 'File not found';
    }
    const formData = new FormData();
    formData.append('image', file);
    fetch('https://asciiart.herokuapp.com/', {
        method: 'POST',
        body: formData
	})
	.then(response => response.text())
	.then(text => {
		if (text == 'Error converting image to ascii') {
			asciiart.style.fontSize = '1em';
			asciiart.style.color = 'Black';
			asciiart.style.backgroundColor = 'White';
		} else {
			asciiart.style.width = 'max-content';
			asciiart.style.fontSize = '0.3em';
			asciiart.style.color = 'White';
			asciiart.style.backgroundColor = 'Black';
		}
		asciiart.innerText = text;
	})
}