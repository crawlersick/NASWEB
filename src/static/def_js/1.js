$.getJSON(
"/toplist",
function(json){
var cList = $('div.list-group')
$.each(json, function(i)
{
    var aaa = $('<a/>')
        .addClass('list-group-item list-group-item-action')
    //   .attr('href',"l2/"+json[i])
        .attr('href',"#")
    //    .attr('data-toggle',"dropdown")
        .text(json[i])
        .appendTo(cList);
    aaa.click(function(){
        /*
        alert(json[i]);

        aaa.append(
        $('<a>')
        .addClass('list-group-item list-group-item-action')
        .attr('href',"/ll").text('~~~~')
        )


        aaa.append(
        $('<a>')
        .addClass('list-group-item list-group-item-action')
        .attr('href',"#").text('~~~~')
        )
        */
        $.getJSON(
        "/l2/"+json[i],
        function(eplist){
            $.each(
            eplist,
                function(i){
                
                    var tmp=$('<a>')
                    .addClass('list-group-item list-group-item-action')
                    .attr('href',"#").text(eplist[i])
                    aaa.append(tmp)
                
                }
            ) 
                        }
        )


        aaa.unbind("click")
                        });
});
}
)
