function changeMusic() {
    var audio = document.getElementById('background-music');
    var image = document.getElementById('myImage');
    var xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() {
        if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200) {
            var newMusic = JSON.parse(xhr.responseText).music;
            var newSrc = JSON.parse(xhr.responseText).pic;
            image.src = newSrc;
            audio.src = newMusic;
        } else {
            console.log('Error: ' + xhr.status);
        }
    };

    xhr.open('GET', '/get_new_music', true);
    xhr.send();

}