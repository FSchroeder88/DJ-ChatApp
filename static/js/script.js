
async function sendMessage() {    // eine asyncrone Funktion
    let fd = new FormData(); // Ein neues Formular wird erstellt
    let token = '{{ csrf_token }}'; // Token an Variable

    fd.append('textmessage', textfield.value); // Mit append kann man etwas anfügen in diesem Fall wollen wir in unser Formular etwas anfügen, den Wert aus der textarea
    fd.append('csrfmiddlewaretoken', token); // Hier fügen wir noch einen Token an um das Ganze zu indentifizieren
    try {
        await fetch('/chat/', {         
            method: 'POST',
            body: fd
        });
        console.log('Success!!')

    } catch (e) {
        console.error('An error occured' , e);
    }

}

 // Bei try und catch wird try ausgeführt wenn der Code funktioniert sollte 
 // ein Fehler kommen dann kommt catch   