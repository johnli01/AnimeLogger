// Waits for website to complete load before continuing
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', afterDOMLoaded());
} else {
  afterDOMLoaded();
}

function afterDOMLoaded() {
  if (document.URL.includes("ANIME URL")) {
    // Uses URL to collect the current ep information on anime site
    var url = document.URL;
    var ep;
    var epInfo;
    if (url.indexOf('?ep=') != -1) {
      ep = url.substring(url.indexOf('?ep='), url.length);
      epInfo = ep.split('=');
    } else {
      ep = url.substring(url.indexOf('/ep-'), url.length);
      epInfo = ep.split('-');
    }

    // Searches for the closest id then directly accessing its children for title info
    var section = document.getElementById('info');
    var div = section.children[1];
    var title = div.children[1].textContent;
    var jtitle = div.children[1].getAttribute("data-jtitle");

    // Sends the collected information from anime site to background. js
    chrome.runtime.sendMessage({"title": title, "jtitle": jtitle, "ep": epInfo[1]},
      function(response) {
        console.log(response);
    });
  }
}