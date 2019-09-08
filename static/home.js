function slide() {
    console.log('slide')
    themes = ["rocketry-splash", "cubesat-splash", "tarc-splash"];
    var index = (parseInt(document.getElementById('index').innerHTML) + 1) % 3;
    document.getElementById('index').innerHTML = index;
    for (i = 0; i < themes.length; i++) {
        if (i == index) {
            document.getElementById(themes[i]).style.cssText = "display: -webkit-flex; display: -ms-flexbox; display: flex;";
        } else {
            document.getElementById(themes[i]).style.display = "none";
        }
    }
}
var interval= window.setInterval(slide, 15000);
