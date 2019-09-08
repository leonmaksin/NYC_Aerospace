document.getElementById('trigger').onclick = function() {
  if (document.getElementById('trigger').classList.contains('is-active')) {
    console.log('called to close')
    document.getElementById('trigger').classList.remove('is-active');
    document.getElementById('mobile-header').style.display = "none"
  } else {
    console.log('called to open')
    document.getElementById('trigger').classList.add('is-active');
    document.getElementById('mobile-header').style.display = "flex"
  }
}
