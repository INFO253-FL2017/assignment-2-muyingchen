function addAlertToTop() {
    var form = document.querySelectorAll("#contact-form")[0];
    var alert = document.querySelectorAll("#alert")[0];
    var name = form.elements.namedItem("name").value;
    var subject = form.elements.namedItem("subject").value;
    var message = form.elements.namedItem("message").value;
    alert.innerHTML = "";

    if (name == "") {
        alert.innerHTML += "You must fill out your name!";
        alert.innerHTML += "\n";
    }
    if (subject == "") {
        alert.innerHTML += "You must fill out the subject!";
        alert.innerHTML += "\n";
    }
    if (message == "") {
        alert.innerHTML += "You must fill out the message!";
        alert.innerHTML += "\n";
    }
    if (name && subject && message) {
        alert.innerHTML = "Hi " + name + ", your message has been sent.";
    }
    event.preventDefault();
    return false;
}
