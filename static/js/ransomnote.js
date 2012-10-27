function echo()
{
var note = document.getElementById("note");
document.getElementById("output").innerHTML = note.value;
}

$(document).ready(function(){
    var ransomform= $('#ransomform');
    var ransomnote = ransomform.children(".input");
    var letters = $("#output");
    ransomnote.on("keyup", function(e)  {
        if (e.keyCode ==  46 || e.keyCode == 8) {
           $('img').last().remove();
        } else {
            
            var lastchar = this.value[this.value.length -1]
            $.ajax({
                url: "/ransom",
                type: "POST",
                data: {
                    inputchar: lastchar
                },
                success: function(data) {
                    var img = JSON.parse(data);
                    letters.append(
                        $("<img/>").attr("src", img)
                    );
                }
            });
        }
    });
});
