
var data = [
    {
        "Item": "Corn Flakes",
        "Manufacturer": "kellogg's",
        "Size": "18 oz",
        "UnitPrice": "2.50",
        "Quantity": "1",
        "TotalPrice": "2.50"
    },
        {
        "Item": "Solid White Tuna",
        "Manufacturer": "Starkist",
        "Size": "5 oz",
        "UnitPrice": "2.79",
        "Quantity": "2",
        "TotalPrice": "5.58"
    },
        {
        "Item": "Cream of Mushroom Soup",
        "Manufacturer": "Campbell's",
        "Size": "10.75 oz",
        "UnitPrice": "1.00",
        "Quantity": "2",
        "TotalPrice": "2.00"
    },
        {
        "Item": "2% Lowfat Milk",
        "Manufacturer": "Safeway",
        "Size": "0.5 gal",
        "UnitPrice": "1.99",
        "Quantity": "1",
        "TotalPrice": "1.99"
    },
        {
        "Item": "Extra-Wide Egg Noodles",
        "Manufacturer": "Golden Grain",
        "Size": "12 oz",
        "UnitPrice": "0.87",
        "Quantity": "3",
        "TotalPrice": "2.61"
    }
]

var display = function(pagecount) {
    // check everypage
    var everypage = $("input#everypage").val();
    if(!everypage)
        everypage = 5;
    else if(everypage <= 0){
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
    var titlestring = new String();
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
        string += "<tr>";
        for(x in newdata[i])
            string += "<td>"+newdata[i][x]+"</td>";
        string += "</tr>";
    }
    string += "<tr><th></th><th></th><th></th><th></th><th></th><th></th></tr>"
    string += "<tr><th>Total</th><th></th><th></th><th></th><th>9</th><th>14.68</th></tr>";
    for(x in newdata[0])
        titlestring += "<th>"+x+"</th>";
    $("tbody").html(string);
    $("thead tr").html(titlestring);
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
            $("link#theme").attr("href", "css/p1.css");
            break;
        case 2:
            $("link#theme").attr("href", "css/p2.css");
            break;
        default:
            break;
    }
}