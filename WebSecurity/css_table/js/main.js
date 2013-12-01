
var data = [
    {
        "name": "Andos",
        "age": "23",
        "school": "ustc",
        "email": "h.chujieandos@gmail.com"
    },
    {
        "name": "tiny",
        "age": "22",
        "school": "hit",
        "email": "tiny@gmail.com"
    },
    {
        "name": "cindy",
        "age": "21",
        "school": "pku",
        "email": "cindy@gmail.com"
    },
    {
        "name": "Andrew",
        "age": "25",
        "school": "tsu",
        "email": "Andrew@qq.com"
    },
    {
        "name": "Jobs",
        "age": "24",
        "school": "cau",
        "email": "Jobs@hotmail.com"
    },
    {
        "name": "Larry",
        "age": "21",
        "school": "google",
        "email": "Larry@gmail.com"
    },
    {
        "name": "Bill",
        "age": "33",
        "school": "ms",
        "email": "Bill@yahoo.com"
    },

]

var display = function(pagecount) {
    // check everypage
    var everypage = $("input#everypage").val();
    if(!everypage)
        everypage = 5;
    if(everypage <= 0){
        alert("每页显示条目数设置非法,应为大于0的整数");
        return;
    }
    // get valid data
    var searchinfo = $("input#searchinfo").val();
    var pattern = new RegExp(searchinfo);
    var newdata = new Array();
    for (var i = 0; i < data.length; i++) {
        for(x in data[i]){
            if(pattern.test(data[i][x])){
                newdata.push(data[i]);
                break;
            }
        }
    }
    // set button
    var lastpage = pagecount - 1;
    var nextpage = pagecount + 1;
    var button;
    var string = new String();
    if(pagecount == 1)
        button = "&nbsp&nbsp&nbsp&nbsp&nbsp<button class=\"btn btn-info\" onclick=\"display("+nextpage+")\">nextpage</button>";
    else if(pagecount*everypage>newdata.length)
        button = "&nbsp&nbsp&nbsp&nbsp&nbsp<button class=\"btn btn-info\" onclick=\"display("+lastpage+")\">lastpage</button>";
    else
        button = "<button class=\"btn btn-info\" onclick=\"display("+lastpage+")\">lastpage</button>&nbsp&nbsp&nbsp&nbsp&nbsp<button class=\"btn btn-info\" onclick=\"display("+nextpage+")\">nextpage</button>";
    $('div#button').html(button);
    var i = pagecount==1?0:newdata.length<everypage?0:(pagecount-1)*everypage;
    var number = (newdata.length-i<everypage?newdata.length:(pagecount)*everypage);
    for(; i < number; i++){
        string += "<tr><th>"+newdata[i].name+"</th><th>"+newdata[i].age+"</th><th>"+newdata[i].school+"</th><th>"+newdata[i].email+"</th></tr>";
    }
    $("tbody#userinfo").html(string);
    $("#pagecount").html(pagecount);
}

var setting = function(tableclass, inputhead, tbodycolor, theadcolor){
    $("table").attr("class", tableclass);
    $("div#inputhead").attr("style", inputhead);
    $("tbody").attr("style", tbodycolor);
    $("thead").attr("style", theadcolor);
}

var themesetting = function(theme){
    switch(theme){
        case 1:
            setting("table", "", "", "");
            break;
        case 2:
            setting("table table-striped", "", "", "")
            break;
        case 3:
            setting("table", "height: 50px;background-color: #99CCFF;border-radius: 25px;padding: 15px 5px 5px 5px;", "background-color: #FFFFCC", "background-color: #66CCFF")
            break;
        case 4:
            setting("table table-striped", "height: 50px;background-color: #99CCFF;border-radius: 25px;padding: 15px 5px 5px 5px;", "background-color: #FFFFCC", "background-color: #6666FF")
            break;
        default:
            break;
    }
}