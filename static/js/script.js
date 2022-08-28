async function sendMessage() {
    let fd = new FormData(); // Ein neues Formular wird erstellt
    //let token = "{{ csrf_token }}"; // Token an Variable übergeben
    let token = document.querySelector('[name=csrfmiddlewaretoken]').value;

    let today = new Date();
    let date = today.getFullYear() + "-" + (today.getMonth() + 1) + "-" + today.getDate();
    let time = today.getHours();
    let dateTime = date + " " + time;

    fd.append("textmessage", textfield.value); // Mit append kann man etwas anfügen in diesem Fall wollen wir in unser Formular etwas anfügen, den Wert aus der textarea
    fd.append("csrfmiddlewaretoken", token); // Hier fügen wir noch einen Token an um das Ganze zu indentifizieren

    try {
        messageContainer.innerHTML += `
            <div id="deleteMessage">
                <span class="color-gray">${date}</span> {{ request.user.username }}: <i class="color-gray">${textfield.value} </i>
            </div>`;

        let response = await fetch("/chat/", {
            method: "POST",
            body: fd,
        });
        let json = await response.json();
        let js = JSON.parse(json);

        console.log("Json is", js);

        document.getElementById("deleteMessage").remove();
        messageContainer.innerHTML += `
        <div id="deleteMessage" >
            <span class="color-gray">${date}</span> {{ request.user.username }}: <i>${textfield.value} </i>
        </div>
        `;

        scrollToBottom();

        renderMessage(js);
        document.getElementById("deleteMessage").remove();

        textfield.value = "";
    } catch (e) {
        console.error("An error occured", e);
    }
}

function scrollToBottom() {
    let objDiv = document.getElementById("text-content-scroll");
    objDiv.scrollTop = objDiv.scrollHeight;
}

async function renderMessage(js, user) {
    //let created_at = js['fields']['created_at'];
    let time = js["fields"]["time"];
    let author = js["fields"]["author"];
    let text = js["fields"]["text"];

    messageContainer.innerHTML += `
    <div class="own-message-bubble ">
            <div class="created_at"> ${time}</div>
            <img class="user-picture-chat" id="show-dialog" src="{{ user.profile.image.url }}">{{ user.username }}: ${text}
    </div>`;
    scrollToBottom();
    console.log("Success!!");
}

/*
// Function websocket für den weiteren Verlauf

let url = `ws://${window.location.host}/ws/socket-server/`
const chatSocket = new WebSocket(url)

chatSocket.onmessage = function(e) {
    let data = JSON.parse(e.data)
    console.log('Data:', data)

    if (data.type === 'chat') {
        let messages = document.getElementById('messageContainer')

        messages.insertAdjacentHTML('beforeend', `
                <div class="own-message-bubble "><p>${data.message}</p></div> `)
    }
}

let form = document.getElementById('textfield')
if (form) {
    form.addEventListener('submit', (e) => {
        e.preventDefault()
        let message = e.target.message.value
        chatSocket.send(JSON.stringify({
            'message': message
        }))
        console.log('Message is', message)
        form.reset()
    })
}
*/