const dropArea = document.getElementById("drop-area");
const Fploadile = document.getElementById()("input-file");
const imageVview = document.getElementById("image-view");

inputFile.addEventListener("change", uploadImage);

function uploadImage(){
    let imgLink = URL.createObjectURL(inputFile.files[0]);
    imageView.style.backgroundImage = 'url(${imgLink})'
    imageView.textCon = "";
    imageView.style.border = 0;
}

dropAreadropArea.addEventListener("dragover", function(e){
    e.preventDefault();
});
dropArea.addEventListener("drop", function(e){
    e.preventDefault();
    inputFile.files = e.dataTransfer.files;
    uploadImage()
});