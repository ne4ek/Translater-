//contex menu
chrome.contextMenus.create({
    id: "translateText",
    title: "Translate Selected Text",
    contexts: ["selection"],
});


chrome.contextMenus.onClicked.addListener(function (info, sender, sendResponse) {
    if (info.menuItemId === "translateText") {
        const selectedText = info.selectionText;
        fetch("http://localhost:5000/sendWordForAdd", {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify({text: [selectedText]}),
        })
    }
})

//connect with popup
chrome.runtime.onMessage.addListener(function (message, sender, sendResponse) {
    if (message[0] === "iconClick") {
        chrome.tabs.query({active: true, currentWindow: true}, function (tabs) {
            if (tabs.length > 0) {
                chrome.scripting.executeScript({
                    target: {tabId: tabs[0].id},
                    function: () => {
                        const selection = window.getSelection().toString();
                        chrome.runtime.sendMessage(["selectionText", selection])

                    }
                });
            }
        });
    } else if (message[0] === "sendWord") {
        fetch("http://localhost:5000/sendWordForAdd", {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify({text: [message[1]]})
        })
    } else if (message[0] === "translateWord") {
        fetch("http://localhost:5000/translateWord?word=" + message[1], {
            method: "GET",
            headers: {"Content-Type": "application/json"},
        })
            .then(response => {
                if (response.ok) {
                    return response.json()
                } else {
                    return null
                }
            }).then(data => {
                chrome.runtime.sendMessage(data)
            }
        )
    } else if (message[0] === "deleteWord") {
        fetch("http://localhost:5000/deleteWord", {
            method: "DELETE",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify({text: [message[1]]})
        })
    } else if (message[0] === "deleteLastWord") {
        fetch("http://localhost:5000/deleteLastWord", {
            method: "DELETE",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify({text: [message[1]]})
        })
    }
});




