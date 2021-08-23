if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', afterDOMLoaded());
} else {
  afterDOMLoaded();
}

function afterDOMLoaded() {
  var url = document.URL;
  var ep = url.substring(url.indexOf('ep-'), url.length);
  alert(ep);
}