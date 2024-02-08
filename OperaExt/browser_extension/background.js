chrome.contextMenus.create({
    id: "translateText",
    title: "Translate Selected Text",
    contexts: ["selection"],
});

// chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
//     if (message === "run") {
//         chrome.tabs.query({active: true, currentWindow: true}, function (tabs) {
//             if (tabs.length > 0) {
//                 chrome.scripting.executeScript({
//                     target: {tabId: tabs[0].id},
//                     function: () => {
//                         const selection = window.getSelection().toString();
//                         fetch("http://localhost:5000/convert", {
//                             method: "POST",
//                             headers: {"Content-Type": "application/json"},
//                             body: JSON.stringify({text: [selection]}),
//                         });
//                     }
//                 });
//             }
//         });
//     }
// });

chrome.contextMenus.onClicked.addEventListener(function (info, tab) {
    if (info.menuItemId === "translateText") {
        const selectedText = info.selectionText;
        fetch("http://localhost:5000/sendWordForAdd", {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify({text: [selectedText]}),
        })
    }
});