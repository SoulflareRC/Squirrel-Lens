
function main(){
  const localhost = "http://127.0.0.1:8000";
  const imgs = $("img");
  // alert("Found "+imgs.length+" images");
  if (imgs.length>0){
    var imgLinks = [];
    imgs.each(function(index,a){
      // $(this).hover(function(){
      // $(this).css("visibility","hidden");
      imgLinks.push( $(this).attr("src") );
      $(this).append($("<p>test</p>"));
    });
    // alert(imgLinks);
    chrome.runtime.sendMessage(
      {"links": imgLinks},
      (response) =>{
          console.log("Received user data"+response);
          var result = response
          // alert("Got response:"+ result);
          console.log(result);
          var replace_links = result.replace_links
          for(var i = 0;i<replace_links.length;i++){
            var replace_link = replace_links[i];
            if(replace_link.length>1){
              var newLink = localhost+replace_link;
              console.log("Replacing image at index "+i+" to "+newLink);
              $(imgs[i]).attr("src",newLink);
              $(imgs[i]).after("<h2><em>!!!Chonky squirrel spotted!!!</em></h2>");
            }
          }
      });
  }

}
window.onload = function(){
  main();
};