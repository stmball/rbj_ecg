// Handle data uploading
upload_button = document.querySelector('#upload_button');
input_data = document.querySelector('#input_data');
analyse_button = document.querySelector('#analyse_button');

// Handle data downloading
download_button = document.querySelector('#download_data');

Sample_Interval = document.querySelector('#Sample_Interval');
Species = document.querySelector('#Species');
filename = document.querySelector('#filename');
var processing = document.getElementById("processing");

// Add an event listener to the "analyse_button"
//analyse_button.addEventListener("click", function() {
//	Species = document.querySelector('#Species');
    // When the "analyse_button" is clicked, remove the 'hidden' attribute from the "processing" button
 //   processing.hidden = false
//	console.log("processing button should now show");
//	console.log(processing.hidden);
//});


upload_button.addEventListener('change', function(e) {
	download_button.hidden = true
    // Load a new FileReader
    const reader = new FileReader()
    reader.readAsText(e.target.files[0])
	filename.value = e.target.files[0].name
	console.log(filename.value);
	Species = document.querySelector('#Species');
	console.log(Species.value);
	Sample_Interval = document.querySelector('#Sample_Interval');
	console.log(Sample_Interval.value);
	document.getElementById('mpl').innerHTML = '';
	document.getElementById('signals').innerHTML = '';
	
    // On load, store the data as text on the page
    // There's probably a better way to do this!
    reader.onload = function() {
        input_data.textContent = reader.result.replace(/\n/g, ',')
        upload_button.hidden = true
        analyse_button.hidden = false
    }
    reader.onerror = function() {
        console.error(reader.error)
    }
})

download_button.addEventListener('click', function(e) {
    text = document.querySelector("#signals").innerText

    if (text != ""){
        var element = document.createElement('a');
        element.setAttribute('href', 'data:text/plain;charset=utf-8,' + encodeURIComponent(text));
        element.setAttribute('download', "output.csv");

        element.style.display = 'none';
        document.body.appendChild(element);

        element.click();

        document.body.removeChild(element);
    }
        upload_button.hidden = false
        analyse_button.hidden = true 	
})

