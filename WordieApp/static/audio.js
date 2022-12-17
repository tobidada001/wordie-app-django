function checkMediaPlaying(){
    var audiofile =  document.getElementById('audio');
    
    if (!audiofile.ended && !audiofile.paused) {
        
        audiofile.pause();
        audiofile.src = audiofile.src
    }else{
     audiofile.play();
    }
 }