if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', afterDOMLoaded());
} else {
  afterDOMLoaded();
}

function afterDOMLoaded() {
  // Uses URL to collect the current ep information on anime site
  var url = document.URL;
  var ep = url.substring(url.indexOf('ep-'), url.length);
  var epInfo = ep.split("-");

  // Searches for the closest id then directly accessing its children for title info
  var section = document.getElementById('info');
  var div = section.children[1];
  var title = div.children[1].textContent;
  var jtitle = div.children[1].getAttribute("data-jtitle");
  alert(jtitle);

  // Sends the collected information from anime site to background.js
  chrome.runtime.sendMessage({"title": title, "jtitle": jtitle, "ep": epInfo[1]},
    function(response) {
      console.log(response);
  });

}